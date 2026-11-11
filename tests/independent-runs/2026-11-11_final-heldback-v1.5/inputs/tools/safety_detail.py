import json, re, sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")
W = Path(r"C:\dev\dg-final-2026-11-11")
key = json.load(open(W / "readers" / "letter-key.json"))
items = {}; cur = None
for line in (W / "heldback" / "watch-for-held-back.md").read_text(encoding="utf-8").splitlines():
    m = re.match(r"## (SEAL-\d)", line)
    if m: cur = m.group(1)
    m = re.match(r"\|\s*(W\d+)\s*\|([^|]*)\|\s*([A-Z-]+)\s*\|([^|]*)\|", line)
    if m and cur: items[(cur, m.group(1))] = (m.group(2).strip(), m.group(3), m.group(4).strip())
out = {}
for rd in ("reader1", "reader2"):
    d = json.load(open(W / "readers" / rd / "scores.json", encoding="utf-8"))
    for x in d["items"]:
        sid = key[rd][x["sheet"]]
        if x["verdict"] == "not_met":
            out.setdefault((sid, x["item"]), []).append((rd, x["turn"], x["quote"], x["reason"]))
for (sid, it), v in sorted(out.items()):
    rule, typ, watch = items[(sid, it)]
    if not typ.startswith("SAFETY") and "--all" not in sys.argv: continue
    print(f"\n### {sid} {it} [{typ}] {rule}\nWATCH: {watch[:300]}")
    for rd, turn, q, r in v:
        print(f"  {rd} t{turn}: \"{q[:160]}\" -> {r[:260]}")
