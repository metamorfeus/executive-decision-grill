# Pilot 2 record: 2026-10-13_pilot2-v1.4

Second independent-sessions run for Decision Grill instructions v1.4 (run label P2), on four NEW scenarios
written by a new author session. No old transcript was used. Preview page with the (unchanged) pass rule:
`docs/sessions/decision-grill/independent-sessions-pilot2-run-preview_2026-10-13.html` in the BOOK-GRAPH_RAG
repository. Result page: `docs/sessions/decision-grill/independent-sessions-pilot2-result_2026-10-13.html`.
**Read-only from now on.**

## Contents
`inputs/` + `inputs.sha256` (instructions as run, scenarios, watch-for lists, helper prompts/results, scripts);
`runs/NEW-1..4/` (transcript, every raw reply, `summary.json`, `checks.json`/`checks.md`); `readers/` (each
reader's sheet, `scores.json`, `record.md`, `result.json`; `letter-key.json` opened only after scoring);
`analysis-console.txt`, `cost-summary.json`. The four sealed scenarios were not opened or run.

## Known gaps and defects (stated, not hidden)
- **Defect in the instructions as run (all runs of both pilots).** `inputs/instructions_as_run.md` begins with
  211 characters of the tail of the setup comment (`You are my decision partner" to the end of this file ... -->`),
  because the file was cut at the first occurrence of that phrase, which sits inside the comment. The real
  instructions follow unchanged. The text in a Claude Project would not have this prefix. The preview pages
  describe the text as starting at "You are my decision partner"; that was inexact.
- NEW-1 and NEW-4 were stopped by the running-total spend stop ($11 for the conversations) before their end;
  NEW-2 ran to the 18-turn cap. They were not rerun (owner's choice). The readers were told a stopped
  conversation is not an assistant failure.
- The watch-for lists carry scenario details (names, planned user lines). Both readers noted this under "Leaks"
  and inferred a scripted user.
- Assistant and executive both Sonnet; Claude Code adds a short fixed environment block (see the first preview).
- AI-written scenarios, AI-written lists, AI readers. A lead, not a release claim.
