ROOT = r"C:\OD\OneDrive - ADVANCED HARMONY ASSOCIATION\METAMORFEUS\AI_CYBORG\PLAYBOOK\BOOK-GRAPH_RAG\docs\sessions\decision-grill"
p1 = open(ROOT + r"\independent-sessions-pilot2-result_2026-10-13.html", encoding="utf-8").read()
head = p1.split("<h1>")[0].replace("Pilot 2 Result", "Pilot 3 Result")
body = open(r"C:\dev\dg-pilot3-2026-10-13\tools\result3_body.html", encoding="utf-8").read()
open(ROOT + r"\independent-sessions-pilot3-result_2026-10-13.html", "w", encoding="utf-8").write(head + '<div class="wrap">\n' + body)
print("written")
