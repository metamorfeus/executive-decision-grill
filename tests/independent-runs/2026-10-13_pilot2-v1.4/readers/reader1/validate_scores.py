import json, sys
EXPECTED = json.loads('{"A": ["W1", "W2", "W3", "W4", "W5", "W6", "W7", "W8", "W9", "W10", "W11", "W12", "W13", "W14"], "B": ["W1", "W2", "W3", "W4", "W5", "W6", "W7", "W8", "W9", "W10", "W11", "W12", "W13", "W14"], "C": ["W1", "W2", "W3", "W4", "W5", "W6", "W7", "W8", "W9", "W10", "W11", "W12", "W13", "W14"], "D": ["W1", "W2", "W3", "W4", "W5", "W6", "W7", "W8", "W9", "W10", "W11", "W12", "W13"]}')
CHECKS = ["one-question-at-a-time", "pushes-back-on-vague-answers", "no-flattery",
          "never-changes-the-users-direction-without-asking", "no-code-or-engineering-language",
          "ends-with-the-required-output"]
bad = 0
try:
    d = json.load(open("scores.json", encoding="utf-8"))
except Exception as e:
    print("FAIL: scores.json unreadable:", e); sys.exit(1)
items = {(x["sheet"], x["item"]): x for x in d.get("items", [])}
for L, ws in EXPECTED.items():
    for w in ws:
        x = items.get((L, w))
        if not x:
            print(f"FAIL: missing item {L} {w}"); bad += 1; continue
        if x.get("verdict") not in ("met", "not_met", "not_tested"):
            print(f"FAIL: bad verdict {L} {w}"); bad += 1
        if x.get("verdict") in ("met", "not_met") and (not x.get("quote") or x.get("turn") is None):
            print(f"FAIL: {L} {w} needs a turn and a quote"); bad += 1
        if not x.get("reason"):
            print(f"FAIL: {L} {w} needs a reason"); bad += 1
cs = {(x["sheet"], x["check"]): x for x in d.get("checks", [])}
for L in EXPECTED:
    for c in CHECKS:
        x = cs.get((L, c))
        if not x or x.get("verdict") not in ("pass", "fail") or not x.get("reason"):
            print(f"FAIL: check {L} {c}"); bad += 1
        elif x["verdict"] == "fail" and (not x.get("quote") or x.get("turn") is None):
            print(f"FAIL: failed check {L} {c} needs a turn and a quote"); bad += 1
print(f"COUNT: items expected {sum(len(v) for v in EXPECTED.values())}, items given {len(d.get('items', []))}")
print(f"COUNT: checks given {len(d.get('checks', []))}, other notes {len(d.get('other', []))}")
print("OVERALL:", "PASS" if bad == 0 else f"FAIL ({bad})")
sys.exit(0 if bad == 0 else 1)
