"""Format check for the watch-for lists.

Prints only counts and PASS/FAIL lines, never scenario or list text.
Run: python check_keys.py
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent

KEY_FILES = {
    "watch-for-dev.md": ("# Watch-for lists: development", "scenarios-dev.md"),
    "watch-for-sealed.md": ("# Watch-for lists: sealed", "scenarios-sealed.md"),
    "watch-for-replay.md": ("# Watch-for list: replay", "scenarios-replay.md"),
}
RECORD = "keywriter-record.md"

TYPES = {
    "SAFETY-HARD",
    "SAFETY-DIRECTION",
    "SAFETY-INVENT",
    "SAFETY-PRIVACY",
    "SAFETY-OUTPUT",
    "COVERAGE",
}
MODE_STEPS = {"1": range(1, 5), "2": range(1, 6)}
SCEN_ID_RE = re.compile(r"^## ([A-Z0-9]+-[A-Z0-9]+)\b")
KEY_ID_RE = re.compile(r"^## ([A-Z0-9]+-[A-Z0-9]+)\s*$")
HEADER_ROW = "| # | Rule or step | Type | Watch for | When |"

failures = 0


def result(label, ok):
    global failures
    if not ok:
        failures += 1
    print(f"{'PASS' if ok else 'FAIL'} {label}")


def valid_ref(cell):
    """True if the cell names at least one rule or mode step, and nothing invalid."""
    found = 0
    for n in re.findall(r"Rule (\d+)", cell):
        if not 1 <= int(n) <= 14:
            return False
        found += 1
    for mode, step in re.findall(r"Mode (\d) Step (\d)", cell):
        if mode not in MODE_STEPS or int(step) not in MODE_STEPS[mode]:
            return False
        found += 1
    if re.search(r"Mode 2 principle", cell):
        found += 1
    if re.search(r"Choosing a mode", cell):
        found += 1
    return found > 0


def scenario_ids(path):
    return [m.group(1) for line in path.read_text(encoding="utf-8").splitlines()
            if (m := SCEN_ID_RE.match(line))]


def parse_key_file(path):
    """Return (first line, {id: [rows]}, stray row count)."""
    lines = path.read_text(encoding="utf-8").splitlines()
    sections, current, stray = {}, None, 0
    for line in lines:
        m = KEY_ID_RE.match(line)
        if m:
            current = m.group(1)
            sections.setdefault(current, [])
            continue
        if not line.startswith("|"):
            continue
        if line.strip() == HEADER_ROW or re.fullmatch(r"\|(-+\|)+", line.strip()):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if current is None or not cells[0].startswith("W"):
            stray += 1
            continue
        sections[current].append(cells)
    return (lines[0] if lines else ""), sections, stray


def check_list(sid, rows):
    n = len(rows)
    numbering = [r[0] for r in rows] == [f"W{i}" for i in range(1, n + 1)]
    shape = all(len(r) == 5 and all(r) for r in rows)
    types_ok = shape and all(r[2] in TYPES for r in rows)
    refs_ok = shape and all(valid_ref(r[1]) for r in rows)
    safety = sum(1 for r in rows if len(r) > 2 and r[2].startswith("SAFETY-"))
    output = sum(1 for r in rows if len(r) > 2 and r[2] == "SAFETY-OUTPUT")
    rule3 = sum(1 for r in rows if len(r) > 2 and r[2] == "COVERAGE"
                and re.search(r"Rule 3\b", r[1]))
    rule4 = sum(1 for r in rows if len(r) > 2 and r[2] == "COVERAGE"
                and re.search(r"Rule 4\b", r[1]))
    print(f"{sid}: items={n} safety={safety} output={output} rule3={rule3} rule4={rule4}")
    result(f"{sid} item count 8-14", 8 <= n <= 14)
    result(f"{sid} numbering W1..W{n}", numbering)
    result(f"{sid} five filled columns", shape)
    result(f"{sid} valid types", types_ok)
    result(f"{sid} valid rule/step", refs_ok)
    result(f"{sid} has SAFETY item", safety >= 1)
    result(f"{sid} has SAFETY-OUTPUT item", output >= 1)
    result(f"{sid} has rule 3 COVERAGE item", rule3 >= 1)
    result(f"{sid} has rule 4 COVERAGE item", rule4 >= 1)
    return n, safety


def main():
    counts = {}
    total_scenarios = 0
    for key_name, (heading, scen_name) in KEY_FILES.items():
        expected = scenario_ids(HERE / scen_name)
        total_scenarios += len(expected)
        key_path = HERE / key_name
        result(f"{key_name} exists", key_path.exists())
        if not key_path.exists():
            continue
        first, sections, stray = parse_key_file(key_path)
        result(f"{key_name} heading", first.strip() == heading)
        result(f"{key_name} no stray rows", stray == 0)
        result(f"{key_name} lists match scenarios ({len(expected)} expected, "
               f"{len(sections)} found)", list(sections) == expected)
        for sid in expected:
            if sid in sections:
                counts[sid] = check_list(sid, sections[sid])

    record_path = HERE / RECORD
    result(f"{RECORD} exists", record_path.exists())
    if record_path.exists():
        text = record_path.read_text(encoding="utf-8")
        for sid, (n, safety) in counts.items():
            m = re.search(rf"^- {re.escape(sid)} — items: (\d+) — SAFETY items: (\d+) — note: \S",
                          text, re.M)
            result(f"{RECORD} line for {sid} matches counts",
                   bool(m) and int(m.group(1)) == n and int(m.group(2)) == safety)

    print(f"scenarios={total_scenarios} lists={len(counts)} "
          f"items={sum(n for n, _ in counts.values())} failures={failures}")
    print("OVERALL PASS" if failures == 0 else "OVERALL FAIL")
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
