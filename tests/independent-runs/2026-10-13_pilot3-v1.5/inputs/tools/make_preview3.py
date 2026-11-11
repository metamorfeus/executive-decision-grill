import hashlib
ROOT = r"C:\OD\OneDrive - ADVANCED HARMONY ASSOCIATION\METAMORFEUS\AI_CYBORG\PLAYBOOK\BOOK-GRAPH_RAG\docs\sessions\decision-grill"
REC = r"C:\OD\OneDrive - ADVANCED HARMONY ASSOCIATION\METAMORFEUS\DECISION-GRILL\tests\independent-runs\2026-10-13_pilot3-v1.5"


def sh(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


si = sh(REC + r"\inputs\instructions_as_run.md")
ss = sh(REC + r"\inputs\helpers-author\scenarios-fresh.md")
sw = sh(REC + r"\inputs\helpers-keywriter\watch-for-fresh.md")
p1 = open(ROOT + r"\independent-sessions-pilot2-run-preview_2026-10-13.html", encoding="utf-8").read()
head = p1.split("<h1>")[0].replace("Pilot 2 Run Preview", "Pilot 3 Run Preview")
body = open(r"C:\dev\dg-pilot3-2026-10-13\tools\preview_body.html", encoding="utf-8").read()
body = body.replace("@@SI@@", si).replace("@@SS@@", ss).replace("@@SW@@", sw).replace("@@REC@@", REC)
open(ROOT + r"\independent-sessions-pilot3-run-preview_2026-10-13.html", "w", encoding="utf-8").write(head + '<div class="wrap">\n' + body)
print("written", si[:8], ss[:8], sw[:8])
