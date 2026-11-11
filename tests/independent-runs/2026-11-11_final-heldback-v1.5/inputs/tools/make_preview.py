import hashlib
DOCS = r"C:\OD\OneDrive - ADVANCED HARMONY ASSOCIATION\METAMORFEUS\AI_CYBORG\PLAYBOOK\BOOK-GRAPH_RAG\docs\sessions\decision-grill"
W = r"C:\dev\dg-final-2026-11-11"
REC = r"C:\OD\OneDrive - ADVANCED HARMONY ASSOCIATION\METAMORFEUS\DECISION-GRILL\tests\independent-runs\2026-11-11_final-heldback-v1.5"
def sh(p): return hashlib.sha256(open(p, "rb").read()).hexdigest()
si = sh(W + r"\instructions_as_run.md"); ss = sh(W + r"\heldback\scenarios-held-back.md"); sw = sh(W + r"\heldback\watch-for-held-back.md")
p3 = open(DOCS + r"\independent-sessions-pilot3-run-preview_2026-10-13.html", encoding="utf-8").read()
head = p3.split("<h1>")[0].replace("Pilot 3 Run Preview", "Final Held-back Run Preview")
assert "Final Held-back Run Preview" in head, "title not replaced"
body = open(W + r"\tools\preview_body.html", encoding="utf-8").read()
body = body.replace("@@SI@@", si).replace("@@SS@@", ss).replace("@@SW@@", sw).replace("@@REC@@", REC)
assert "@@" not in body
out = DOCS + r"\final-heldback-run-preview_2026-11-11.html"
open(out, "w", encoding="utf-8").write(head + body)
print("written", out, si[:8], ss[:8], sw[:8])
