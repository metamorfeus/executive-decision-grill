import json, re, collections
from pathlib import Path
R = Path(r"C:\dev\dg-final-2026-11-11")
K = Path(r"C:\dev\dg-final-2026-11-11\heldback")
key = json.load(open(R / "readers" / "letter-key.json"))
types = {}
for f in ["watch-for-held-back.md"]:
    cur = None
    for line in (K / f).read_text(encoding="utf-8").splitlines():
        m = re.match(r"## (\S+)", line)
        if m: cur = m.group(1)
        m = re.match(r"\|\s*(W\d+)\s*\|[^|]*\|\s*([A-Z-]+)\s*\|", line)
        if m: types[(cur, m.group(1))] = m.group(2)
res = {}
for rd in ["reader1", "reader2"]:
    d = json.load(open(R / "readers" / rd / "scores.json", encoding="utf-8"))
    per = collections.defaultdict(lambda: {"met": 0, "not_met": 0, "not_tested": 0, "safety_fail": [], "items": {}})
    for x in d["items"]:
        sid = key[rd][x["sheet"]]; t = types[(sid, x["item"])]
        p = per[sid]; p[x["verdict"]] += 1; p["items"][x["item"]] = x["verdict"]
        if x["verdict"] == "not_met" and t.startswith("SAFETY"): p["safety_fail"].append((x["item"], t, x["turn"], x["quote"][:110], x["reason"][:200]))
    checks = collections.defaultdict(dict)
    for c in d["checks"]: checks[key[rd][c["sheet"]]][c["check"]] = (c["verdict"], c["turn"], c["quote"][:90], c["reason"][:160])
    res[rd] = {"per": per, "checks": checks, "other": [(key[rd][o["sheet"]], o["rule"], o["turn"]) for o in d["other"]]}
out = {}
for rd in res:
    print("=====", rd)
    new = ["SEAL-1", "SEAL-2", "SEAL-3", "SEAL-4"]
    tm = tn = tt = 0
    for sid in new:
        p = res[rd]["per"][sid]; tot = p["met"] + p["not_met"]
        pct = 100 * p["met"] / tot if tot else 0
        print(f"{sid}: met {p['met']} not_met {p['not_met']} not_tested {p['not_tested']} -> {pct:.0f}% | SAFETY not_met: {[(a,b) for a,b,*_ in p['safety_fail']]}")
        if sid in new: tm += p["met"]; tn += p["not_met"]; tt += p["not_tested"]
    allp = 100 * tm / (tm + tn)
    print(f"NEW SCENARIOS TOTAL: met {tm}, not_met {tn}, not_tested {tt} -> {allp:.1f}% ; not_tested share {100*tt/(tm+tn+tt):.1f}%")
    print("six checks fails:", {sid: [c for c, v in res[rd]['checks'][sid].items() if v[0] == 'fail'] for sid in new})
    print("other notes:", collections.Counter(s for s, *_ in res[rd]["other"]))
# agreement
agree = tot = 0; dis = []
for sid in ["SEAL-1", "SEAL-2", "SEAL-3", "SEAL-4"]:
    a = res["reader1"]["per"][sid]["items"]; b = res["reader2"]["per"][sid]["items"]
    for it in a:
        tot += 1
        if a[it] == b[it]: agree += 1
        else: dis.append((sid, it, types[(sid, it)], a[it], b[it]))
print("\nITEM AGREEMENT:", agree, "of", tot, f"({100*agree/tot:.0f}%)")
print("disagreements:", dis)
# combined (stricter)
rank = {"not_met": 0, "not_tested": 1, "met": 2}
print("\nCOMBINED (stricter) safety not_met per scenario:")
for sid in ["SEAL-1", "SEAL-2", "SEAL-3", "SEAL-4"]:
    a = res["reader1"]["per"][sid]["items"]; b = res["reader2"]["per"][sid]["items"]
    comb = {it: min(a[it], b[it], key=lambda v: rank[v]) for it in a}
    m = sum(v == "met" for v in comb.values()); n = sum(v == "not_met" for v in comb.values())
    print(sid, "combined met", m, "not_met", n, f"{100*m/(m+n):.0f}%", [it for it, v in comb.items() if v == "not_met"])
json.dump({"dis": dis}, open(R / "analysis-disagreements.json", "w"), indent=1)
