"""Program checks for one Decision Grill transcript (instructions v1.4 profile).

Output: JSON with three groups.
  must      - plain-word or structure rules a script decides (these can fail a run).
  suspects  - lines a reader must judge (a script cannot decide them).
  counts    - numbers to report (never pass/fail).
Usage: python check_transcript.py <transcript.md> [--json out.json] [--md out.md]
"""
import json, re, sys
from pathlib import Path

BAN_OPEN = ["good", "great", "perfect", "excellent", "fair", "right", "thanks", "thank you"]
BAN_PHRASE = ["interesting approach", "that could work", "you might want to consider", "great question",
              "i can see why you'd think that", "many ways to think about this", "great point"]
JARGON = ["leverage", "bandwidth", "workstream", "alignment", "stakeholder management"]
ENGINEERING = [r"\bapi\b", r"\brepo\b", r"\bgit\b", r"\bgithub\b", r"\bdeploy(ed|ing|ment)?\b", r"\bship(ped|ping)?\b",
               r"\bpr\b", r"regression test", r"stack trace", r"\bcode\b", r"\bsoftware\b", r"\bscript\b"]
INVITES = [r"\btell me\b", r"\blet me know\b", r"\bplease confirm\b", r"\bconfirm\b", r"\bcheck whether\b",
           r"\bcan you\b", r"\bcould you\b", r"\bwould you\b", r"\bdo you want me to\b", r"\bplease (say|check|choose)\b"]
MAP_HEADINGS = ["the decision", "decided", "what we said no to", "parked", "open", "not yet clear",
                "terms we agreed", "assumptions we rely on", "next step"]
Q_PARTS = ["purpose", "from", "to", "context", "how to answer", "questions", "anything else"]
NOTES = "notes for you (not part of the document)"
WAIT = re.compile(r"wait,? what|i'?m lost|what do you mean", re.I)
IMPATIENT = re.compile(r"skip the questions|skip ahead|get to the point|just give me the answer", re.I)
WRAP = re.compile(r"let'?s wrap up|write it up|i'?m done with questions|can we wrap", re.I)
THANKS = re.compile(r"that'?s fine|it'?s fine|thank|i'?m done|looks good|that'?s all", re.I)


def parse(path):
    t = Path(path).read_text(encoding="utf-8").split("## Judge verdict")[0]
    parts = re.split(r"^### (Executive|Assistant) \(turn (\d+)\)\s*$", t, flags=re.M)
    return [(parts[i], int(parts[i + 1]), parts[i + 2].strip()) for i in range(1, len(parts), 3)]


def sentences(text):
    text = re.sub(r"\[Q\d+[^\]]*\]", "", text)
    text = re.sub(r"^\s*([-*]|\d+\.)\s+", "", text, flags=re.M)
    return [s for s in re.split(r"(?<=[.!?])\s+|\n+", text) if s.strip()]


def norm(s):
    return re.sub(r"\s+", " ", s.lower()).strip(" .,;:\"“”'")


def main():
    path = sys.argv[1]
    msgs = parse(path)
    user_text = " ".join(m for r, n, m in msgs if r == "Executive").lower()
    asst = [(n, m) for r, n, m in msgs if r == "Assistant"]
    user = {n: m for r, n, m in msgs if r == "Executive"}

    def is_final(m):
        low = m.lower()
        if NOTES in low:
            return True
        return sum(1 for h in MAP_HEADINGS if re.search(r"(?m)^\W*" + re.escape(h), low)) >= 6

    final_turns = [n for n, m in asst if is_final(m)]
    first_final = final_turns[0] if final_turns else None
    must, sus, counts = [], [], {}

    # --- plain-word rules (every assistant message) ---
    for n, m in asst:
        low = m.lower()
        first = re.sub(r"^[\W_]+", "", re.sub(r"\[Q\d+[^\]]*\]", "", m)).lower()
        for b in BAN_OPEN:
            if re.match(re.escape(b) + r"\b", first):
                must.append({"check": "banned-opening-word", "turn": n, "evidence": first[:60]})
        for b in BAN_PHRASE:
            if b in low:
                must.append({"check": "banned-phrase", "turn": n, "evidence": b})
        for j in JARGON:
            if j in low and j not in user_text:
                must.append({"check": "jargon-word", "turn": n, "evidence": j})
        for pat in ENGINEERING:
            mm = re.search(pat, low)
            if mm and mm.group(0) not in user_text:
                sus.append({"check": "engineering-word", "turn": n, "evidence": mm.group(0)})

    # --- one question mark per message while gathering ---
    gathering = [(n, m) for n, m in asst if first_final is None or n < first_final]
    qbad = []
    for n, m in gathering:
        stripped = re.sub(r"[“\"][^”\"\n]{0,200}[”\"]", "", m)  # ignore quoted user words
        qm = stripped.count("?")
        if qm != 1:
            qbad.append(n)
            sus.append({"check": "question-marks-not-one", "turn": n, "evidence": f"{qm} question marks"})
        low = stripped.lower()
        hits = [p for p in INVITES if re.search(p, low)]
        if hits and "?" in stripped:
            body = [s for s in sentences(stripped) if any(re.search(p, s.lower()) for p in INVITES)]
            if body:
                sus.append({"check": "possible-second-ask", "turn": n, "evidence": body[0][:140]})
        if "?" in stripped and "my recommendation:" not in low:
            sus.append({"check": "question-without-recommendation-line", "turn": n,
                        "evidence": "reader decides: decision question or fact question?"})
        sents = sentences(stripped.split("?")[0] if "?" in stripped else stripped)
        if len(sents) > 3:
            sus.append({"check": "long-reaction", "turn": n, "evidence": f"{len(sents)} sentences before the question"})
    counts["question_mark_not_one"] = len(qbad)
    counts["gathering_messages"] = len(gathering)

    # --- progress tag (Mode 1) ---
    tags = [(n, re.search(r"\[Q(\d+) · (\d+) of (\d+) settled\]", m)) for n, m in gathering]
    tagged = [(n, t) for n, t in tags if t]
    counts["tagged_messages"] = len(tagged)
    if tagged:
        qnums = [int(t.group(1)) for n, t in tagged]
        if qnums != list(range(1, len(qnums) + 1)):
            sus.append({"check": "progress-tag-numbering", "turn": tagged[0][0], "evidence": f"sequence {qnums}"})
        if max(qnums) > 15:
            must.append({"check": "more-than-15-questions", "turn": tagged[-1][0], "evidence": f"Q{max(qnums)}"})
        first_tag_turn = tagged[0][0]
        for n, m in gathering:
            if n > first_tag_turn and "?" in m and not re.search(r"\[Q\d+ · \d+ of \d+ settled\]", m):
                sus.append({"check": "question-without-progress-tag", "turn": n,
                            "evidence": "reader decides (may be Mode 2 after a hand-over)"})
        counts["max_Q"] = max(qnums)

    # --- final output structure ---
    for n, m in asst:
        if not is_final(m):
            continue
        if n != first_final:   # later documents are revisions (changed parts only): not checked for structure
            continue
        low = m.lower()
        if NOTES not in low:
            must.append({"check": "final-output-missing-notes-line", "turn": n, "evidence": NOTES})
        else:
            before = low.split(NOTES)[0]
            if "your answer:" in before or "purpose" in before[:600]:
                kind = "questionnaire"
            else:
                kind = "map"
            counts[f"final_output_turn_{n}"] = kind
            if kind == "map":
                missing = [h for h in MAP_HEADINGS if not re.search(r"(?m)^\W*" + re.escape(h), before)]
                if missing:
                    must.append({"check": "map-missing-headings", "turn": n, "evidence": ", ".join(missing)})
                head_sents = len(sentences(m.split("\n\n")[0]))
                if head_sents > 1 and not re.match(r"\W*(the decision|\*\*the decision)", before.strip()):
                    sus.append({"check": "text-before-document", "turn": n, "evidence": f"{head_sents} sentences before the document"})
            else:
                missing = [p for p in Q_PARTS if p not in before]
                if missing:
                    must.append({"check": "questionnaire-missing-parts", "turn": n, "evidence": ", ".join(missing)})
                ans = before.count("your answer:")
                counts[f"questions_with_answer_line_turn_{n}"] = ans
                if "sharing check" not in low:
                    must.append({"check": "questionnaire-missing-sharing-check", "turn": n, "evidence": "no 'Sharing check'"})
                if "coverage" not in low or "added by me" not in low:
                    sus.append({"check": "questionnaire-notes-incomplete", "turn": n, "evidence": "coverage / added-by-me missing"})
            counts[f"markers_turn_{n}"] = {k: low.count(k) for k in ["assumption:", "recommended:", "(added by me)", "not included — see note", "not done", "hard to reverse"]}
            # numbers in the final output that no user message contains
            for num in set(re.findall(r"(?<![\w.])(?:€|\$)?\d[\d,.]*\d(?:%|k|m)?(?![\w])|\b\d{2,}\b", before)):
                nn = num.lower().lstrip("€$")
                if nn not in user_text and nn.strip(",.") not in user_text:
                    sus.append({"check": "number-not-in-user-messages", "turn": n, "evidence": num})
            # quotes of the user's words (map only)
            if kind == "map":
                for q in re.findall(r"[“\"]([^”\"\n]{12,220})[”\"]", before):
                    if norm(q) not in norm(user_text):
                        sus.append({"check": "quote-not-word-for-word", "turn": n, "evidence": q[:140]})

    # --- reactions to special user messages ---
    prev_q = None
    for n, m in asst:
        u = user.get(n, "")
        if WAIT.search(u):
            sents = sentences(re.sub(r"\[Q\d+[^\]]*\]", "", m).split("?")[0])
            sus.append({"check": "after-wait-what", "turn": n, "evidence": f"{len(sents)} sentences before the repeated question"})
        if IMPATIENT.search(u):
            sus.append({"check": "after-impatience", "turn": n,
                        "evidence": "final output" if is_final(m) else f"not final output; {m.count('?')} question mark(s)"})
        if WRAP.search(u):
            sus.append({"check": "after-wrap-up-request", "turn": n,
                        "evidence": "final output" if is_final(m) else "not final output"})
            if is_final(m) and "not done" not in m.lower():
                sus.append({"check": "wrap-up-without-not-done-list", "turn": n,
                            "evidence": "reader decides: was gathering cut short, or was this a normal confirmation?"})
        if first_final is not None and n > first_final and THANKS.search(u):
            s = sentences(m)
            if "?" in m or len(s) > 1:
                sus.append({"check": "reply-after-thanks-not-one-sentence-no-question", "turn": n,
                            "evidence": f"{len(s)} sentences, {m.count('?')} question mark(s)"})

    counts["assistant_turns"] = len(asst)
    counts["first_final_output_turn"] = first_final
    out = {"transcript": str(path), "must": must, "suspects": sus, "counts": counts}
    args = sys.argv[2:]
    if "--json" in args:
        Path(args[args.index("--json") + 1]).write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
    if "--md" in args:
        L = [f"# Program checks", "", "## Must-never rules decided by script", ""]
        L += ([f"- turn {x['turn']}: **{x['check']}** — {x['evidence']}" for x in must] or ["- none"])
        L += ["", "## Suspects for the reader to judge (the script cannot decide these)", ""]
        L += ([f"- turn {x['turn']}: {x['check']} — {x['evidence']}" for x in sus] or ["- none"])
        L += ["", "## Counts", ""] + [f"- {k}: {v}" for k, v in counts.items()]
        Path(args[args.index("--md") + 1]).write_text("\n".join(L) + "\n", encoding="utf-8")
    if "--json" not in args and "--md" not in args:
        print(json.dumps(out, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()
