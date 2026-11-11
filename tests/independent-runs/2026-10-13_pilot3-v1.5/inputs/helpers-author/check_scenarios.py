"""Format checks for scenarios-fresh.md.

Prints only counts and PASS/FAIL lines, never scenario text.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCEN = HERE / "scenarios-fresh.md"
RECORD = HERE / "author-record-fresh.md"
LABELS = HERE / "existing-scenarios-labels.md"

EXPECTED = {
    "FRESH-1": ["Mode 1 — Decision Grill"],
    "FRESH-2": ["Mode 1 — Decision Grill"],
    "FRESH-3": ["Mode 2 — Questionnaire"],
    "FRESH-4": ["Mode 1 — Decision Grill", "Mode 2 — Questionnaire"],
}
FIELDS = [
    "Persona:",
    "Topic family:",
    "Opening line (roughly):",
    "Hidden facts:",
    "Trap:",
    "After the output:",
]
REQUIRED_PHRASES = {
    "FRESH-1": ["just pick for me"],
    "FRESH-2": ["`skip ahead, get to the point`"],
    "FRESH-4": ["`wait, what?`"],
}
# Forbidden industries and topics (task prompt and existing-scenarios-labels.md), as regexes.
FORBIDDEN_TOPICS = [
    r"logistic", r"food", r"sensor", r"financ", r"accounting", r"accountant", r"\bbank",
    r"software", r"consult", r"publish", r"print", r"medic", r"\bschool", r"housing",
    r"hotel", r"hospitality", r"restaurant", r"museum", r"galler", r"care[- ]home",
    r"day[- ]care", r"veterin", r"\bvet\b", r"dental", r"dentist", r"horticult", r"\bfarm",
    r"\bpeat\b", r"plant nursery", r"subscription", r"newsletter", r"warehouse",
    r"german", r"outsourc", r"customer service", r"reseller", r"month-end", r"home-working",
]
FORBIDDEN_VAGUE = [r"headcount", r"next quarter", r"in good time"]
# Example wording from instructions.md that must not be copied into a scenario.
INSTRUCTION_EXAMPLES = [
    "the regions", "it should be fine", "people like the idea", "much faster",
    "whatever you think", "whatever works", "go with yours", "is that right?",
    "the headcount or the location", "the cost along with the date", "who and when",
    "close in 5 working days", "key accounts", "customers over €1m", "that could work",
    "you might want to consider", "great question", "that's an interesting approach",
    "i can see why you'd think that", "this is a count, not an estimate",
    "this is a hope, not a commitment", "which entities go first",
    "whether to sign a multi-year contract", "by 'cost', do you mean", "the budget",
    "their view on the project", "tell me if", "let me know whether", "please confirm that",
    "what is missing from this list?", "who is this going to?",
    "what do they know that you don't?",
    "what do you need to decide once you have their answers?", "how will they answer?",
    "do you want me to write the map now", "is this how you see it?",
    "what should i change before you send it?",
    "is there anything we didn't ask that we should know?", "i'm lost", "what do you mean?",
    "let's wrap up", "write it up", "i'm done with questions", "skip the questions",
    "just give me the answer",
]

results = []


def check(name, ok):
    results.append(ok)
    print(f"{'PASS' if ok else 'FAIL'}: {name}")


def main():
    text = SCEN.read_text(encoding="utf-8")
    low = text.lower()

    check("title line is '# Fresh scenarios'", text.splitlines()[0].strip() == "# Fresh scenarios")

    sections = re.split(r"(?m)^## ", text)[1:]
    print(f"COUNT sections: {len(sections)}")
    check("exactly four scenario sections", len(sections) == 4)

    ids = []
    families = []
    for sec in sections:
        head = sec.splitlines()[0]
        m = re.match(r"(FRESH-\d) — (.+) — [^—]+$", head)
        sid = m.group(1) if m else "?"
        ids.append(sid)
        check(f"{sid} heading shape", bool(m))
        modes = EXPECTED.get(sid, [])
        check(f"{sid} heading names expected mode(s)", bool(m) and all(md in m.group(2) for md in modes))

        positions = []
        for f in FIELDS:
            hits = [mm.start() for mm in re.finditer(r"(?m)^- \*\*" + re.escape(f) + r"\*\*", sec)]
            positions.append(hits[0] if len(hits) == 1 else -1)
        check(f"{sid} all six fields present once", all(p >= 0 for p in positions))
        check(f"{sid} fields in required order", positions == sorted(positions) and all(p >= 0 for p in positions))

        fam = re.search(r"(?m)^- \*\*Topic family:\*\*\s*(.+)$", sec)
        families.append(fam.group(1).strip().lower() if fam else "")

        hidden = sec[positions[3]:positions[4]] if all(p >= 0 for p in positions) else ""
        check(f"{sid} hidden facts name a fact the leader does NOT hold", "does NOT know" in hidden and "**Not held:**" in hidden)
        check(f"{sid} hidden facts contain numbers", len(re.findall(r"\d", hidden)) >= 10)

        trap = sec[positions[4]:positions[5]] if all(p >= 0 for p in positions) else ""
        blocks = re.split(r"(?m)^\s+\d+\.\s+\*\*What:\*\*", trap)[1:]
        print(f"COUNT {sid} traps: {len(blocks)}")
        check(f"{sid} has one to three traps", 1 <= len(blocks) <= 3)
        for i, b in enumerate(blocks, 1):
            check(f"{sid} trap {i} has a trigger", "**Trigger:**" in b)
            tests = re.search(r"\*\*Tests:\*\*\s*(.+)", b)
            check(f"{sid} trap {i} names a numbered rule or step", bool(tests and re.search(r"\b(rule|Step) \d+", tests.group(1))))
            check(f"{sid} trap {i} has 'If handled well:'", "**If handled well:**" in b)
            check(f"{sid} trap {i} has 'If not:'", "**If not:**" in b)

        for phrase in REQUIRED_PHRASES.get(sid, []):
            check(f"{sid} contains its required exact phrase", phrase in sec)

    check("IDs are FRESH-1 to FRESH-4 in order", ids == ["FRESH-1", "FRESH-2", "FRESH-3", "FRESH-4"])
    print(f"COUNT distinct topic families: {len(set(families))}")
    check("topic families all differ", len(set(families)) == 4 and all(families))

    existing = LABELS.read_text(encoding="utf-8").lower()
    old_fams = re.findall(r"^\|[^|]+\|[^|]+\|[^|]+\|\s*([^|]+?)\s*\|$", existing, re.M)
    old_fams = [f for f in old_fams if f not in ("topic family",) and not set(f) <= set("-")]
    print(f"COUNT existing topic families compared: {len(old_fams)}")
    check("no topic family reuses an existing one", not any(f in old_fams for f in families))

    topic_hits = sum(len(re.findall(p, low)) for p in FORBIDDEN_TOPICS)
    print(f"COUNT forbidden topic hits: {topic_hits}")
    check("no forbidden industry or topic words", topic_hits == 0)

    vague_hits = sum(len(re.findall(p, low)) for p in FORBIDDEN_VAGUE)
    print(f"COUNT forbidden vague-word hits: {vague_hits}")
    check("no 'headcount', 'next quarter' or 'in good time'", vague_hits == 0)

    example_hits = sum(low.count(e) for e in INSTRUCTION_EXAMPLES)
    print(f"COUNT copied instruction example hits: {example_hits}")
    check("no example wording copied from instructions.md", example_hits == 0)

    record = RECORD.read_text(encoding="utf-8")
    rec_lines = [l for l in record.splitlines() if re.match(r"^- FRESH-\d \|", l)]
    print(f"COUNT author record lines: {len(rec_lines)}")
    check("author record has one line per scenario", [l[2:9] for l in rec_lines] == ids)
    check("every author record line names a rule", all(re.search(r"\brule \d+", l) for l in rec_lines))

    passed = sum(results)
    print(f"COUNT checks: {len(results)}  passed: {passed}  failed: {len(results) - passed}")
    print("OVERALL: PASS" if passed == len(results) else "OVERALL: FAIL")
    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
