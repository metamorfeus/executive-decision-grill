"""Format check for watch-for-fresh.md. Prints only counts and PASS/FAIL lines."""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
KEY_FILE = HERE / "watch-for-fresh.md"
SCENARIOS = ["FRESH-1", "FRESH-2", "FRESH-3", "FRESH-4"]
TYPES = {
    "SAFETY-HARD", "SAFETY-DIRECTION", "SAFETY-INVENT",
    "SAFETY-PRIVACY", "SAFETY-OUTPUT", "COVERAGE",
}
HEADER = "| # | Rule or step | Type | Watch for | When |"


def rule_ok(cell):
    rules = [int(n) for n in re.findall(r"\bRule (\d+)", cell)]
    if rules and all(1 <= n <= 14 for n in rules):
        return True
    return bool(re.search(r"\bMode [12]\b", cell)) and not rules


def split_sections(text):
    sections = {}
    current = None
    for line in text.splitlines():
        m = re.match(r"^## (\S+)\s*$", line)
        if m:
            current = m.group(1)
            sections[current] = []
        elif current:
            sections[current].append(line)
    return sections


def check_section(lines):
    failures = []
    if HEADER not in [l.strip() for l in lines]:
        failures.append("header")
    rows = [l.strip() for l in lines if re.match(r"^\|\s*W\d+", l.strip())]
    for i, row in enumerate(rows, start=1):
        cells = [c.strip() for c in row.strip("|").split("|")]
        if len(cells) != 5:
            failures.append(f"row {i} columns")
            continue
        num, rule, typ, watch, when = cells
        if num != f"W{i}":
            failures.append(f"row {i} numbering")
        if typ not in TYPES:
            failures.append(f"row {i} type")
        if not rule_ok(rule):
            failures.append(f"row {i} rule")
        if not watch or not when:
            failures.append(f"row {i} empty cell")
    safety = sum(1 for r in rows if "| SAFETY-" in r)
    output = sum(1 for r in rows if "| SAFETY-OUTPUT |" in r)
    if not 8 <= len(rows) <= 14:
        failures.append("item count")
    if safety < 1:
        failures.append("no safety item")
    if output < 1:
        failures.append("no safety-output item")
    return len(rows), safety, failures


def main():
    text = KEY_FILE.read_text(encoding="utf-8")
    all_pass = True
    if not text.startswith("# Watch-for lists: fresh scenarios"):
        print("FAIL title")
        all_pass = False
    sections = split_sections(text)
    for sid in SCENARIOS:
        if sid not in sections:
            print(f"{sid}: FAIL missing")
            all_pass = False
            continue
        items, safety, failures = check_section(sections[sid])
        status = "PASS" if not failures else "FAIL " + ", ".join(failures)
        print(f"{sid}: items={items} safety={safety} {status}")
        all_pass = all_pass and not failures
    extra = [s for s in sections if s not in SCENARIOS]
    if extra:
        print(f"FAIL unexpected sections={len(extra)}")
        all_pass = False
    print("OVERALL: PASS" if all_pass else "OVERALL: FAIL")
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
