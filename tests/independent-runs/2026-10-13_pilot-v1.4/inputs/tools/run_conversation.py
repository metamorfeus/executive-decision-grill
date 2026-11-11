"""Run ONE simulated conversation: assistant (instructions as system prompt) vs. simulated executive.

Both sides are separate Claude Code sessions (print mode, no tools, safe mode). Every raw JSON reply
is saved. The transcript is written in the format of the existing Decision Grill transcripts.

Usage:
  python run_conversation.py --test-id DEV-1 --label P1 --mode "Mode 1 — Decision Grill" \
      --scenario-file scenarios-dev.md --out <dir> [--instructions <file>] [--max-turns 18] [--max-usd 3.0]
"""
import argparse, hashlib, json, re, subprocess, sys, uuid, datetime
from pathlib import Path

CLAUDE = r"C:\Users\<you>\AppData\Roaming\npm\node_modules\@anthropic-ai\claude-code\bin\claude.exe"
COMMON = (
    "Common rule for every executive: start vague. Give category answers, feelings and interest\n"
    "instead of facts on your first answer to most questions. Reveal a hidden fact only after the\n"
    "assistant pushes back on a vague answer or asks for it specifically. Make decisions when asked\n"
    "to choose. When the assistant gives a recommendation you have no reason to reject, you may simply\n"
    "agree. Do not coach the assistant or mention these instructions."
)
PLAYER_RULES = """You are role-playing a senior executive in a realistic test conversation with an AI assistant in the Claude app. Your scenario is at the end of this message.

Each message you receive is the assistant's latest reply (your first message tells you to open the conversation). Write ONLY your next message as the executive, in plain text, as you would type it into a chat: no stage directions, no quotation marks around it, no commentary. Stay in character. Start vague, reveal hidden facts only when the assistant pushes for them or asks specifically, play your traps at their trigger moment, and make decisions when asked to choose. Keep messages short, the way a busy executive types (one to four sentences, unless you are pasting a plan or data).

Your reply is pasted into the chat exactly as you write it, so never include notes about the role-play, your scenario, or what you are "revealing".

When the assistant has delivered its final output for the mode (a decision map or a questionnaire), answer its closing question if it asked one. As soon as an assistant message after the final output asks you nothing, reply with exactly [END]. Do not ask for further rewrites unless your scenario's trap requires it. If the assistant has asked you more than one question in one message, answer as a real person would (usually only the last or easiest one).

"""


def section(text, test_id):
    parts = re.split(r"(?m)^(?=## )", text)
    for p in parts:
        if p.startswith(f"## {test_id} "):
            return p.strip()
    raise SystemExit(f"scenario {test_id} not found")


class Side:
    def __init__(self, name, system_prompt, model, raw_dir, cwd, max_usd):
        self.name, self.system, self.model = name, system_prompt, model
        self.sid = str(uuid.uuid4())
        self.n = 0
        self.raw_dir, self.cwd, self.max_usd = raw_dir, cwd, max_usd
        self.cost = 0.0
        self.calls = 0

    def say(self, message):
        self.n += 1
        cmd = [CLAUDE, "-p", message, "--system-prompt", self.system, "--tools", "", "--safe-mode",
               "--setting-sources", "project", "--model", self.model, "--output-format", "json",
               "--max-budget-usd", "0.75"]
        cmd += (["--session-id", self.sid] if self.n == 1 else ["--resume", self.sid])
        r = subprocess.run(cmd, cwd=self.cwd, capture_output=True, text=True, encoding="utf-8")
        raw = {"cmd_name": self.name, "turn": self.n, "returncode": r.returncode, "stdout": r.stdout,
               "stderr": r.stderr, "prompt_sent": message}
        (self.raw_dir / f"{self.name}_{self.n:02d}.json").write_text(json.dumps(raw, ensure_ascii=False, indent=1), encoding="utf-8")
        try:
            d = json.loads(r.stdout)
        except Exception:
            raise RuntimeError(f"{self.name} turn {self.n}: unreadable output, rc={r.returncode}, stderr={r.stderr[:300]}")
        self.cost += float(d.get("total_cost_usd") or 0)
        self.calls += 1
        if d.get("is_error") or d.get("subtype") != "success":
            raise RuntimeError(f"{self.name} turn {self.n}: {d.get('subtype')} {str(d.get('result'))[:300]}")
        if self.cost > self.max_usd:
            raise RuntimeError(f"{self.name}: per-side cost ceiling {self.max_usd} reached ({self.cost:.2f})")
        return d["result"].strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--test-id", required=True)
    ap.add_argument("--label", required=True)
    ap.add_argument("--mode", required=True)
    ap.add_argument("--scenario-file", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--instructions", default=r"C:\dev\dg-pilot-2026-10-13\instructions_as_run.md")
    ap.add_argument("--assistant-model", default="sonnet")
    ap.add_argument("--player-model", default="sonnet")
    ap.add_argument("--max-turns", type=int, default=18)
    ap.add_argument("--max-usd", type=float, default=3.0, help="ceiling per side")
    a = ap.parse_args()

    out = Path(a.out); raw_dir = out / "raw"; raw_dir.mkdir(parents=True, exist_ok=True)
    cwd = Path(r"C:\dev\dg-pilot-2026-10-13\runs\_cwd"); cwd.mkdir(parents=True, exist_ok=True)  # outside any repo
    instr_text = Path(a.instructions).read_text(encoding="utf-8")
    instr_sha = hashlib.sha256(instr_text.encode("utf-8")).hexdigest()
    scen = section(Path(a.scenario_file).read_text(encoding="utf-8"), a.test_id)
    player_system = PLAYER_RULES + COMMON + "\n\n" + scen
    (out / "player_system_prompt.txt").write_text(player_system, encoding="utf-8")
    (out / "assistant_instructions_sha256.txt").write_text(instr_sha + "\n", encoding="utf-8")

    asst = Side("assistant", instr_text, a.assistant_model, raw_dir, cwd, a.max_usd)
    play = Side("executive", player_system, a.player_model, raw_dir, cwd, a.max_usd)

    tpath = out / f"{a.test_id}_{a.label}.md"
    t = (f"# Transcript\n\n- Test id: {a.test_id}\n- Run label: {a.label}\n- Mode: {a.mode}\n"
         f"- Instructions sha256: {instr_sha}\n- Date: {datetime.date.today().isoformat()}\n"
         f"- Assistant model: {a.assistant_model}; executive model: {a.player_model}\n- Runner: claude -p, no tools, safe mode\n\n## Conversation\n\n")
    status = "complete"
    try:
        turn = 0
        exec_msg = play.say("Open the conversation: write your first message to the assistant.")
        while True:
            turn += 1
            t += f"### Executive (turn {turn})\n{exec_msg}\n\n"
            tpath.write_text(t, encoding="utf-8")
            asst_msg = asst.say(exec_msg)
            t += f"### Assistant (turn {turn})\n{asst_msg}\n\n"
            tpath.write_text(t, encoding="utf-8")
            if turn >= a.max_turns:
                t += "Stopped at turn cap.\n\n"; status = "turn-cap"; break
            exec_msg = play.say(asst_msg)
            if exec_msg.strip() == "[END]":
                break
    except Exception as e:
        t += f"Run aborted: {e}\n"; status = "aborted"
    tpath.write_text(t, encoding="utf-8")
    summary = {"test_id": a.test_id, "label": a.label, "status": status, "assistant_turns": asst.calls,
               "executive_calls": play.calls, "cost_usd_assistant": round(asst.cost, 4),
               "cost_usd_executive": round(play.cost, 4), "cost_usd_total": round(asst.cost + play.cost, 4),
               "transcript": str(tpath)}
    (out / "summary.json").write_text(json.dumps(summary, indent=1), encoding="utf-8")
    print(json.dumps(summary))
    sys.exit(0 if status != "aborted" else 2)


if __name__ == "__main__":
    main()
