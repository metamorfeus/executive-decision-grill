import glob, json, subprocess
R = r"C:\OD\OneDrive - ADVANCED HARMONY ASSOCIATION\METAMORFEUS\DECISION-GRILL\tests\independent-runs\2026-10-13_pilot3-v1.5"
conv = sum(json.load(open(f))["cost_usd_total"] for f in glob.glob(R + r"\runs\FRESH-*\summary.json"))
c = lambda p: json.load(open(p, encoding="utf-8-sig"))["total_cost_usd"]
o = dict(conversations=round(conv, 2), author=round(c(R + r"\inputs\helpers-author\result.json"), 2),
         keywriter=round(c(R + r"\inputs\helpers-keywriter\result.json"), 2),
         reader1=round(c(R + r"\readers\reader1\result.json"), 2), reader2=round(c(R + r"\readers\reader2\result.json"), 2))
o["pilot3_total"] = round(sum(o.values()), 2)
o["all_three_pilots_with_45.81"] = round(o["pilot3_total"] + 45.81, 2)
json.dump(o, open(R + r"\cost-summary.json", "w"), indent=1)
print(o)

readme = """# Pilot 3 record: 2026-10-13_pilot3-v1.5

Re-test of Decision Grill instructions **v1.5** (run label P3) on four FRESH scenarios written by a new author
session. No old transcript was used. Preview page (pass rule, unchanged):
`docs/sessions/decision-grill/independent-sessions-pilot3-run-preview_2026-10-13.html`. Result page:
`docs/sessions/decision-grill/independent-sessions-pilot3-result_2026-10-13.html` (BOOK-GRAPH_RAG repository).
**Read-only from now on.**

## Contents
`inputs/` + `inputs.sha256` (instructions as run, the full v1.5 product file, scenarios, watch-for lists, helper
prompts/results, scripts); `runs/FRESH-1..4/` (transcript, every raw reply, `summary.json`, `checks.json`/`.md`);
`readers/` (each reader's sheet, `scores.json`, `record.md`, `result.json`; `letter-key.json` opened only after
scoring); `analysis-console.txt`, `cost-summary.json`. The four sealed scenarios were not opened or run.

## Corrections and limits (stated, not hidden)
- The instructions text given to the assistant now starts at the real first line (22,793 characters, sha256 in
  `inputs.sha256`). In pilots 1 and 2 it began with 211 characters of a setup-comment fragment. This run is
  therefore set up slightly differently from those two.
- Many planned traps never occurred (the leader never handed over a choice in FRESH-1, FRESH-2 had no late fact
  or "skip ahead", FRESH-3 had no not-yet-told line). Both readers marked those items `not_tested` and noted it
  under "Leaks". About 27 to 29 percent of items were untested.
- Assistant and executive both Sonnet; Claude Code adds a short fixed environment block (see the pilot 1 preview).
- One run of four conversations. AI-written scenarios, lists and readers. A lead, not a release claim.
"""
open(R + r"\README.md", "w", encoding="utf-8").write(readme)

# changelog status line + result sentence (CRLF kept)
P = r"C:\OD\OneDrive - ADVANCED HARMONY ASSOCIATION\METAMORFEUS\DECISION-GRILL\CHANGELOG.md"
b = open(P, "rb").read().decode("utf-8")
old = "## v1.5 — 2026-10-13 (drafted, not yet tested)"
assert b.count(old) == 1
b = b.replace(old, "## v1.5 — 2026-10-13 (tested once, pilot 3)")
old2 = "**Not yet\r\ntested.** A re-test should use a new scenario set and fix a defect found in the pilots' test setup: the\r\ninstructions text given to the assistant began with 211 characters of the setup comment."
if old2 not in b:
    old2 = old2.replace("\r\n", "\n")
    eol = "\n"
else:
    eol = "\r\n"
assert b.count(old2) == 1, "tested paragraph not found"
new2 = ("**Tested once** on four fresh scenarios (pilot 3), with the setup defect fixed (the instructions text given to the" + eol +
        "assistant had begun with 211 characters of the setup comment in pilots 1 and 2). It still failed the" + eol +
        "pre-written pass rule under both readers (one form item in a questionnaire, one scenario under the 60 percent" + eol +
        "floor, about 27 to 29 percent of items untested), but the four recurring patterns largely did not recur where" + eol +
        "the situation arose: 2 of 4 conversations showed any of them, against 8 of 9 under version 1.4. Many planned" + eol +
        "traps never occurred, so the hand-over half of the first pattern is untested. Leftovers noted, not fixed: the" + eol +
        "reply after a sign-off is two sentences, the reason in rule 10 runs past one sentence, \"How to answer\" can" + eol +
        "omit a time estimate, and facts can still be parked without asking. Result page:" + eol +
        "`docs/sessions/decision-grill/independent-sessions-pilot3-result_2026-10-13.html`.")
b = b.replace(old2, new2)
open(P, "wb").write(b.encode("utf-8"))
print("changelog updated")
