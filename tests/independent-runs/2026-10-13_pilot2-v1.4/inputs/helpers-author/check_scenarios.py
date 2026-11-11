"""Format check for scenarios-new.md.

Prints only counts and PASS/FAIL lines, never scenario text.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCEN = HERE / "scenarios-new.md"
INSTR = HERE / "instructions.md"
EXISTING = HERE / "existing-scenarios-labels.md"
RECORD = HERE / "author-record-new.md"

EXPECTED_IDS = ["NEW-1", "NEW-2", "NEW-3", "NEW-4"]
EXPECTED_MODE = {
    "NEW-1": "Mode 1 — Decision Grill",
    "NEW-2": "Mode 1 — Decision Grill",
    "NEW-3": "Mode 2 — Questionnaire",
    "NEW-4": "Mode 1 — Decision Grill",
}
FIELDS = [
    "Persona:",
    "Topic family:",
    "Opening line (roughly):",
    "Hidden facts:",
    "Trap:",
    "After the output:",
]
TRAP_PARTS = ["Says:", "Trigger:", "Tests:", "If handled well:", "If not:"]

# Forbidden industries and topics (task rules plus existing-scenarios-labels.md).
FORBIDDEN = [
    r"logistic", r"food manufactur", r"food", r"sensor", r"financ", r"accounting",
    r"accountant", r"\bbank", r"software", r"consulting", r"consultan",
    r"publish", r"magazine", r"printing", r"subscription", r"newsletter",
    r"warehouse", r"social housing", r"housing", r"hotel", r"hospitality",
    r"museum", r"galler", r"care home", r"care-home", r"day care", r"day-care",
    r"outsourc", r"customer service", r"sales office", r"germany", r"reseller",
    r"month-end", r"go-live",
]

# Labels from instructions.md that a scenario may name when describing the
# expected behaviour. These are output labels, not example sentences.
LABEL_WHITELIST = {
    "hard to reverse", "left out on purpose", "my recommendation:",
    "assumption:", "not included — see note", "(my reading — confirm)",
    "(added by me)", "added by me — check before sending",
    "notes for you (not part of the document)", "your recommendation, accepted",
    "parked — needs [role]", "parked — who knows: to confirm",
    "recommended:", "terms we agreed", "why it matters:", "why this matters:", "your answer:",
}

results = []


def check(name, ok, count=None):
    results.append(ok)
    suffix = f" ({count})" if count is not None else ""
    print(f"{'PASS' if ok else 'FAIL'} {name}{suffix}")


def sentences(text):
    return len([s for s in re.split(r"(?<=[.!?])\s+", text.strip()) if s.strip()])


text = SCEN.read_text(encoding="utf-8")
lines = text.splitlines()

check("file starts with '# New scenarios'", bool(lines) and lines[0].strip() == "# New scenarios")

# Split into sections.
heads = [(i, l) for i, l in enumerate(lines) if l.startswith("## ")]
sections = {}
ids_found = []
head_ok = 0
for n, (i, l) in enumerate(heads):
    end = heads[n + 1][0] if n + 1 < len(heads) else len(lines)
    m = re.match(r"^## (NEW-\d) — (Mode [12] — (?:Decision Grill|Questionnaire)) — (\S.*)$", l)
    if m:
        head_ok += 1
        ids_found.append(m.group(1))
        sections[m.group(1)] = {"mode": m.group(2), "body": "\n".join(lines[i + 1:end])}
check("section headings in required shape", head_ok == len(heads) == 4, head_ok)
check("IDs are NEW-1 to NEW-4 in order", ids_found == EXPECTED_IDS, len(ids_found))
check("modes match the brief", all(sections.get(k, {}).get("mode") == v for k, v in EXPECTED_MODE.items()))

topic_families = {}
all_trap_count = 0
for sid in EXPECTED_IDS:
    sec = sections.get(sid)
    if not sec:
        check(f"{sid} present", False)
        continue
    body = sec["body"]
    top = [l for l in body.splitlines() if l.startswith("- **")]
    labels = [re.match(r"- \*\*(.+?)\*\*", l).group(1) for l in top]
    check(f"{sid} fields present and in order", labels == FIELDS, len(labels))

    tf = re.search(r"^- \*\*Topic family:\*\* (.+)$", body, re.M)
    if tf:
        topic_families[sid] = tf.group(1).strip()

    # Hidden facts block.
    hf = re.search(r"\*\*Hidden facts:\*\*(.*?)\n- \*\*Trap:\*\*", body, re.S)
    hf_text = hf.group(1) if hf else ""
    check(f"{sid} hidden facts name a fact the leader does not hold", "**Does not hold" in hf_text)
    check(f"{sid} hidden facts name who holds it", "Who holds it" in hf_text)
    check(f"{sid} hidden facts contain numbers", len(re.findall(r"\d", hf_text)) >= 10,
          len(re.findall(r"\d[\d,.]*", hf_text)))

    # Traps.
    tr = re.search(r"\*\*Trap:\*\*(.*?)\n- \*\*After the output:\*\*", body, re.S)
    tr_text = tr.group(1) if tr else ""
    traps = re.split(r"\n\s+\d+\.\s", "\n" + tr_text)[1:]
    all_trap_count += len(traps)
    check(f"{sid} has 1 to 3 traps", 1 <= len(traps) <= 3, len(traps))
    parts_ok = sum(all(f"**{p}**" in t for p in TRAP_PARTS) for t in traps)
    check(f"{sid} every trap has Says/Trigger/Tests/If handled well/If not", parts_ok == len(traps), parts_ok)
    rule_ok = 0
    for t in traps:
        tests = re.search(r"\*\*Tests:\*\*(.*?)\*\*If handled well:\*\*", t, re.S)
        if tests and re.search(r"\bRule \d+\b", tests.group(1)):
            rule_ok += 1
    check(f"{sid} every trap names a numbered rule", rule_ok == len(traps), rule_ok)
    trig_ok = sum(bool(re.search(r"\*\*Trigger:\*\*\s*\S", t)) for t in traps)
    check(f"{sid} every trap has a non-empty trigger", trig_ok == len(traps), trig_ok)

    # Leader lines stay within four sentences.
    leader_quotes = []
    ol = re.search(r"\*\*Opening line \(roughly\):\*\* \"(.+?)\"", body)
    if ol:
        leader_quotes.append(ol.group(1))
    for t in traps:
        s = re.search(r"\*\*Says:\*\*(.*?)\*\*Trigger:\*\*", t, re.S)
        if s:
            leader_quotes += re.findall(r"\"(.+?)\"", s.group(1))
    long_q = sum(sentences(q) > 4 for q in leader_quotes)
    check(f"{sid} leader lines are 1 to 4 sentences", long_q == 0, len(leader_quotes))

check("total traps", 4 <= all_trap_count <= 12, all_trap_count)

# Topic families: all different, and none reuses an existing family.
fams = list(topic_families.values())
check("topic families present", len(fams) == 4, len(fams))
check("topic families all different", len(set(f.lower() for f in fams)) == len(fams))
prefixes = [f.split(":")[0].strip().lower() for f in fams]
check("topic family areas all different", len(set(prefixes)) == len(prefixes))
existing = EXISTING.read_text(encoding="utf-8")
ex_fams = re.findall(r"^\|[^|]+\|[^|]+\|[^|]+\|\s*([^|]+?)\s*\|$", existing, re.M)
ex_fams = [e for e in ex_fams if e.lower() not in ("topic family", "---")]
ex_prefixes = {e.split(":")[0].strip().lower() for e in ex_fams}
clash = sum(p in ex_prefixes for p in prefixes)
check("no topic family area from existing scenarios", clash == 0, len(ex_prefixes))

# Forbidden industries and topics anywhere in the file.
low = text.lower()
hits = sum(bool(re.search(p, low)) for p in FORBIDDEN)
check("no forbidden industry or topic terms", hits == 0, hits)

# No copied example wording from instructions.md.
instr = INSTR.read_text(encoding="utf-8")
quoted = re.findall(r"\"([^\"\n]{3,120})\"", instr) + re.findall(r"“([^”\n]{3,120})”", instr)
examples = {q.strip().lower() for q in quoted if len(q.split()) >= 2}
examples = {q for q in examples if q not in LABEL_WHITELIST}
copied = sum(bool(re.search(r"(?<!\w)" + re.escape(q) + r"(?!\w)", low)) for q in examples)
check("no example phrase from instructions.md copied", copied == 0, len(examples))

# Personas: distinct names.
names = re.findall(r"^- \*\*Persona:\*\* ([^,]+),", text, re.M)
check("personas have distinct names", len(names) == 4 and len(set(names)) == 4, len(names))

# Author record: one line per scenario.
rec = RECORD.read_text(encoding="utf-8") if RECORD.exists() else ""
rec_lines = [l for l in rec.splitlines() if re.match(r"^- \*\*NEW-\d\*\*", l)]
rec_ids = [re.match(r"^- \*\*(NEW-\d)\*\*", l).group(1) for l in rec_lines]
check("author record has one line per scenario", rec_ids == EXPECTED_IDS, len(rec_lines))
rec_rules = sum(bool(re.search(r"Rules? \d", l)) and "Topic family:" in l for l in rec_lines)
check("author record lines name rules and topic family", rec_rules == 4, rec_rules)

passed = sum(results)
print(f"checks: {len(results)} passed: {passed} failed: {len(results) - passed}")
print("OVERALL PASS" if passed == len(results) else "OVERALL FAIL")
sys.exit(0 if passed == len(results) else 1)
