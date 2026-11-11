"""Build the two blind reader folders.

Each reader folder gets: task_prompt.md, sheet.md (transcripts under neutral letters, each with its
watch-for list and its program-check output), rules.md (the instructions text, no version line),
rubric.md (the six checks), validate_scores.py (counts only). A separate key file maps letters back
to scenarios; it is written OUTSIDE the reader folders and nobody opens it before scoring.

Usage: python build_sheets.py <run_root> <out_root>
  run_root/<ID>/<ID>_P1.md           the transcripts (ID in DEV-1..DEV-4 and M1-B)
  run_root/<ID>/checks.md|.json      program-check output
"""
import json, random, re, shutil, sys
from pathlib import Path

RUN = Path(sys.argv[1]); OUT = Path(sys.argv[2])
ROOT = Path(r"C:\dev\dg-pilot-2026-10-13")
IDS = ["DEV-1", "DEV-2", "DEV-3", "DEV-4", "M1-B"]
KEYFILES = {"DEV": ROOT / "keywriter" / "watch-for-dev.md", "M1": ROOT / "keywriter" / "watch-for-replay.md"}
LEAK = re.compile(r"sonnet|opus|haiku|v1\.\d|sha256|DEV-\d|SEAL-|M1-[AB]|M2-[AB]|replay|pilot|changelog|\bR[1-9]\b", re.I)


def key_section(sid):
    f = KEYFILES["DEV" if sid.startswith("DEV") else "M1"]
    t = f.read_text(encoding="utf-8")
    parts = re.split(r"(?m)^(?=## )", t)
    for p in parts:
        if p.startswith(f"## {sid}"):
            rows = [l for l in p.splitlines() if re.match(r"\|\s*W\d+\s*\|", l)]
            return rows
    raise SystemExit(f"no key for {sid}")


def conversation(sid):
    t = (RUN / sid / f"{sid}_P1.md").read_text(encoding="utf-8")
    return t.split("## Conversation", 1)[1].strip()


def checks(sid):
    return (RUN / sid / "checks.md").read_text(encoding="utf-8")


def clean(s):
    return re.sub(r"\b(DEV-\d|SEAL-\d|M1-B)\b", "this scenario", s)


keys = {}
for ri, reader in enumerate(["reader1", "reader2"], start=1):
    order = IDS[:]
    random.Random(ri * 7919).shuffle(order)
    letters = "ABCDE"
    mapping = {letters[i]: order[i] for i in range(5)}
    keys[reader] = mapping
    d = OUT / reader
    d.mkdir(parents=True, exist_ok=True)
    sheet = ["# Scoring sheet", "", "Five conversations, lettered A to E. Each has: the conversation, a list of items to watch for, and the output of some automatic checks.", ""]
    expected = {}
    for L, sid in mapping.items():
        rows = key_section(sid)
        expected[L] = [re.match(r"\|\s*(W\d+)", r).group(1) for r in rows]
        sheet += [f"---", f"## Conversation {L}", "", "### The conversation", "", conversation(sid), "",
                  "### Items to watch for", "",
                  "| # | Rule or step | Type | Watch for | When |", "|---|---|---|---|---|"] + [clean(r) for r in rows] + [
                  "", "### Automatic checks (a script ran these; suspects are only suspects)", "", checks(sid), ""]
    text = "\n".join(sheet)
    hits = sorted(set(m.group(0).lower() for m in LEAK.finditer(text)))
    if hits:
        print(f"{reader}: possible leak words in sheet: {hits}")
    (d / "sheet.md").write_text(text, encoding="utf-8")
    shutil.copy(ROOT / "instructions_as_run.md", d / "rules.md")
    shutil.copy(ROOT / "tools" / "rubric.md", d / "rubric.md")
    shutil.copy(ROOT / "tools" / f"reader_task_prompt.md", d / "task_prompt.md")
    v = (ROOT / "tools" / "validate_scores_template.py").read_text(encoding="utf-8").replace("__EXPECTED__", json.dumps(expected))
    (d / "validate_scores.py").write_text(v, encoding="utf-8")

(OUT / "SEALED-KEY-do-not-open-before-scoring.json").write_text(json.dumps(keys, indent=1), encoding="utf-8")
print("built", [str(OUT / r) for r in ("reader1", "reader2")])
