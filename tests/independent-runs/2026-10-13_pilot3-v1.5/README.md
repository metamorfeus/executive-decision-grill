# Pilot 3 record: 2026-10-13_pilot3-v1.5

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
