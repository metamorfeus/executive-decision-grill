# Pilot record: 2026-10-13_pilot-v1.4

Independent-sessions pilot for Decision Grill instructions v1.4 (run label P1). Plan and pass rule:
`docs/sessions/decision-grill/independent-sessions-pilot-run-preview_2026-10-13.html` in the
BOOK-GRAPH_RAG repository (committed before the first pilot conversation). Result page:
`docs/sessions/decision-grill/independent-sessions-pilot-result_2026-10-13.html`.

**Read-only from now on.** A correction is a new file that points at the old one.

## Contents
- `inputs/` and `inputs.sha256` - everything as used: instructions text, scenarios (development and sealed),
  watch-for lists, helper prompts and results, scripts. The sealed scenarios and their lists were NOT opened
  by the main session and were not run.
- `runs/<ID>/` - one conversation: transcript `<ID>_P1.md`, every raw reply in `raw/`, the executive's system
  prompt, `summary.json` (status, turns, cost), `checks.json` and `checks.md` (program checks).
- `runs/aborted-attempt1/` - first attempts at DEV-1 and DEV-4, stopped by the runner's own $3 per-side cap.
  Not counted. `runs/smoke-setup/` - a two-turn runner smoke test. Not evidence.
- `readers/` - each reader's sheet, task prompt, `scores.json`, `result.json`; `letter-key.json` maps the
  neutral letters back to scenarios (opened only after scoring).
- `checks-on-old-transcripts/` - the program checks run on the 12 older transcripts (no model calls).
- `analysis-console.txt`, `analysis-disagreements.json`, `cost-summary.json` - the analysis.
- `CHANGES-AFTER-PREVIEW.md` - the two limits that changed after the preview page.

## Known gaps (stated, not hidden)
- **Both readers hit the account's session usage limit (HTTP 429) after writing `scores.json`.** `scores.json`
  is complete and passes `validate_scores.py` (67 items, 30 checks) for both. Neither wrote `record.md`, so
  there is no reader statement about leaks and no free-text summary. The per-item reasons are in `scores.json`.
- Both reruns (DEV-1, DEV-4) ran to the 18-turn cap; the final output was reached before the cap in each.
- Assistant and executive were both Sonnet. Claude Code adds a short fixed identity/environment block to every
  session (see the preview page).
- AI-written scenarios, AI-written lists, AI readers. A lead, not a release claim.
