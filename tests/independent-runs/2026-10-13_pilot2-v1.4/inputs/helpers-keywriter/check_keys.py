"""Format check for watch-for-new.md. Prints only counts and PASS/FAIL lines."""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
KEYS = HERE / "watch-for-new.md"
EXPECTED = ["NEW-1", "NEW-2", "NEW-3", "NEW-4"]
TYPES = {"SAFETY-HARD", "SAFETY-DIRECTION", "SAFETY-INVENT",
         "SAFETY-PRIVACY", "SAFETY-OUTPUT", "COVERAGE"}
RULE_RE = re.compile(r"(Rule (1[0-4]|[1-9])\b|Mode [12] (Step [1-5]|principle))")


def parse(text):
    sections, current = {}, None
    for line in text.splitlines():
        m = re.match(r"^## (\S+)\s*$", line)
        if m:
            current = m.group(1)
            sections[current] = []
            continue
        if current and line.startswith("| W"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            sections[current].append(cells)
    return sections


def main():
    text = KEYS.read_text(encoding="utf-8")
    sections = parse(text)
    failures = 0

    def report(ok, label):
        nonlocal failures
        print(f"{'PASS' if ok else 'FAIL'} {label}")
        if not ok:
            failures += 1

    report(text.splitlines()[0] == "# Watch-for lists: new scenarios", "heading")
    for sid in EXPECTED:
        rows = sections.get(sid, [])
        report(bool(rows), f"{sid} has a list")
        report(all(len(r) == 5 for r in rows), f"{sid} rows have 5 cells")
        report([r[0] for r in rows] == [f"W{i}" for i in range(1, len(rows) + 1)],
               f"{sid} numbered W1..W{len(rows)}")
        report(all(r[2] in TYPES for r in rows if len(r) == 5), f"{sid} valid types")
        report(all(RULE_RE.search(r[1]) for r in rows if len(r) == 5),
               f"{sid} rule/step present")
        report(all(r[3] and r[4] for r in rows if len(r) == 5),
               f"{sid} watch-for and when filled")
        report(8 <= len(rows) <= 14, f"{sid} 8-14 items")
        safety = sum(1 for r in rows if len(r) == 5 and r[2].startswith("SAFETY-"))
        output = sum(1 for r in rows if len(r) == 5 and r[2] == "SAFETY-OUTPUT")
        report(safety >= 1, f"{sid} at least one SAFETY item")
        report(output >= 1, f"{sid} has SAFETY-OUTPUT")
        print(f"COUNT {sid} items={len(rows)} safety={safety}")
    report(set(sections) == set(EXPECTED), "no extra sections")
    print(f"{'PASS' if failures == 0 else 'FAIL'} overall ({failures} failures)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
