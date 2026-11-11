# Changelog

Versions of `PROJECT-INSTRUCTIONS.md`. Test runs are labelled by version: R1 = v1.0, R2 = v1.1,
and so on. Every change after v1.0 is tied to the test finding that caused it.

## Risk resolution — 2026-11-11 (no change to the text you paste)

- Anthropic's help pages on Projects and on length limits were read again on 11 November 2026. They still say Projects and project instructions are available on every plan, including Free (at most five Projects), with the buttons "+ New Project", "Set project instructions" and "Save instructions", and still advise keeping instructions concise. `docs/FOR-EXECUTIVES.html` now gives the new date.
- **Final held-back test of version 1.5: did not pass.** The four scenarios held back since 13 October were run once, with the pass rule committed beforehand. Safety items were missed in all four conversations under both readers; coverage 76.0% and 62.0% (80% needed). Peter chose to publish version 1.5 with the result stated openly. README, home page, guide for executives, product record and test report (new section 10) now say so, and the README and guide ask readers to check every decision map against what they said.
- `RELEASE-CHECKLIST.html`: new section 1c; risks R1 to R7 updated with Peter's decisions and his acceptance of what remains disclosed ("Yes, I accept these six"); the published set is now 915 files.
- New record `tests/independent-runs/2026-11-11_final-heldback-v1.5/`, with the held-back scenarios and lists now published; `tests/independent-runs/PUBLIC-COPY-NOTE.md` has a dated addendum; the maintainer guide's sealed-ID check now expects that record too.
- The text you paste is unchanged: 22,793 characters, SHA-256
  `9a987f08eb138da683199d8cb2c5e831a800340bd91647e52db8201f141bc036`.
- Before-copies: `archive/before-risk-resolution_2026-11-11/` and `archive/before-final-result_2026-11-11/` (not published).

## Publication wording — 2026-11-10 (no change to the text you paste)

- Peter chose on 10 November 2026 to publish before the live check in the Claude app, changing his earlier decision to publish only after it. The live check is still pending.
- `RELEASE-CHECKLIST.html`: the publication decision is updated, and the privacy check now says that the organisation's name appears in local folder paths in the test records (risk R5) instead of saying there are no employer names.
- `docs/HOW-TO-RELEASE.html`, `docs/HOW-IT-WAS-BUILT.html` and `docs/WHAT-WAS-BUILT.html` no longer say that the live check comes before publishing.
- `RELEASE-CHECKLIST.html` and `tests/TEST-REPORT.html`: links now use the site's accent colour, as on the other pages. In dark mode they were the browser's default dark blue and hard to read.
- Risk R5 now gives the measured count: 77 published files show the organisation's folder path.
- The text you paste is unchanged: 22,793 characters, SHA-256
  `9a987f08eb138da683199d8cb2c5e831a800340bd91647e52db8201f141bc036`. Both instruction files and the test records are untouched.
- Before-copies: `archive/before-publication_2026-11-10/` and `archive/before-publication_2026-11-10_fixes/` (not published).

## Description and author links — 2026-11-10 (no change to the text you paste)

- Peter approved the specific description naming CEOs, CFOs, COOs, directors and managers, the decision map and the questionnaire, with nothing to install. README, home page, guide introductions and page metadata now use that message.
- Added the same About the author block to the README, home page, four reader guides and test report, with four neutrally described links checked on 2026-11-10. Some linked products and services are paid; none is required.
- No author block was added to the maintainer pages, legal notice, changelog, issue configuration or instruction files.
- The quick start is described as printable rather than promising one printed page after the author block was added.
- Updated the prepared GitHub About line and replaced the general c-suite topic with coo; the list still has 20 topics. Nothing is published. Publication remains after the live check and Peter's explicit approval.
- The text you paste is unchanged: 22,793 characters, SHA-256
  `9a987f08eb138da683199d8cb2c5e831a800340bd91647e52db8201f141bc036`. Both instruction files and the test records are untouched.
- Before-copies: `archive/before-description-and-links_2026-11-10/` (not published).

## Pre-publication review — 2026-11-10 (no change to the text you paste)

- The text you paste is unchanged: 22,793 characters, SHA-256
  `9a987f08eb138da683199d8cb2c5e831a800340bd91647e52db8201f141bc036`, checked after every batch of edits.
- Documents corrected: the message counts now come from the version 1.5 tests; "every question comes with
  a recommendation" now says "every decision question"; behaviour is described as "built to" everywhere;
  the Free-plan sentence now cites Anthropic's help page (read 9 November 2026); "skip the questions" is
  reported as played once, on version 1.4; the product record lists every file and states the test result
  of version 1.5; the build guide points to the paste file.
- Added: an "If something goes wrong" section (README, guide for executives, quick start); a maintainer
  how-to, `docs/HOW-TO-RELEASE.html`; a feedback form with a privacy warning; a social preview image and
  share tags; a link back to the home page on every page.
- Home page: the copy button now fetches the text when the page loads, so it also works in Safari, and
  shows the text in a box with a Select all button when copying fails.
- `.gitattributes` now stores `tests/independent-runs/` byte for byte, so the published fingerprints of the
  test records still match on every computer.
- Pages: darker small grey text for contrast, a main landmark and visible keyboard focus. The live-check
  scripts and the runner protocol carry a note that they are the author's own working files.
- Copies of the files before this review are in `archive/before-review_2026-11-09/` (not published).

## Name change — 2026-11-09 (no change to the text you paste)

- The product is now called **Executive Decision Grill** (it was Decision Grill), before its publication on
  GitHub as `metamorfeus/executive-decision-grill`. Mode 1 keeps its name, "Decision Grill", inside the
  instructions.
- Only the title line of `PROJECT-INSTRUCTIONS.md` changed. The text you paste (from "You are my decision
  partner. I am a senior leader" to the end, 22,793 characters) is byte for byte the tested v1.5, SHA-256
  `9a987f08eb138da683199d8cb2c5e831a800340bd91647e52db8201f141bc036`. The version stays 1.5.
- New `PASTE-INTO-CLAUDE.txt`: exactly that text, so it can be copied as a whole file.
- Documents prepared for publication: a new README, a home page (`index.html`) for GitHub Pages, page
  descriptions, a release checklist, and a cleaned public copy of `tests/independent-runs/` (the four sealed
  scenarios and a local user path removed; see `tests/independent-runs/PUBLIC-COPY-NOTE.md`).

## v1.5 — 2026-10-13 (tested once, pilot 3)

From the two independent-sessions pilots on version 1.4 (first pilot: four new scenarios and a replay;
second pilot: four fresh scenarios). Both failed their pre-written pass rule under both blind readers.
Four patterns appeared in **both** pilots, in eight different conversations, written by two different
author sessions and scored by two different pairs of readers, so each is tied to one change. Evidence:
`docs/sessions/decision-grill/independent-sessions-pilot-result_2026-10-13.html` and
`docs/sessions/decision-grill/independent-sessions-pilot2-result_2026-10-13.html` in the author's private
working repository (not published); the records are in `tests/independent-runs/`.

- **Step 3, "Hard to reverse"** rewritten as a check before every decision question. Every option is
  checked, including the one recommended and any that looks easy; the message names which options are hard
  to undo; the label sits inside the question message. (Pattern: it was said only after the leader chose.
  First pilot's reseller replay: the main rollout and the hires never marked, and the assistant's own pick
  recorded after "Just pick for me". Second pilot: a ten-year property commitment presented as the easy
  option, a three-year supply deal marked only in the map.) **Counterweight:** it is a label, not a second
  question; choices that are easy to change are not marked.
- **Rule 1** extended from "and" to "or". An "or" between two different things the leader would each have to
  answer is two questions; "or" is fine only between the options of one choice. The test is whether one part
  can be answered without the other. If the second part is not worth its own question, it becomes an
  "Assumption:". (Pattern: first pilot DEV-1 turn 9 and DEV-4 turns 1 and 2; second pilot NEW-4 turn 6.)
  **Counterweight:** no extra questions; the question budget is unchanged.
- **Rule 3**: the push is the next message, and an answer is parked or recorded only after the push. A time
  that is not a date is vague, so a deadline needs a date. A vague answer is never recorded as a decision or
  as agreed; it is a leaning or an "Assumption:". (Pattern: "by the spring" accepted; "Plenty" and "low
  forties" parked or used; "a few of the team would muck in" recorded as a decided rota.)
  **Counterweight:** push limits are unchanged (once on a fact, twice on a decision), and "I do not know"
  is parked, not pushed.
- **Rule 13** (the sharing check) is now run once per category, not by general impression, and a line that
  only makes sense because someone has not been told yet counts as an unannounced change. **Rule 10**: the
  alternative offered for a ruled-out request is a neutral fact or a question about what happens next, never
  a criticism that a role held by one person would still point at. (Pattern: first pilot DEV-4, two lines
  missed on the first pass; second pilot NEW-3, an unannounced line missed and a criticism kept under a
  one-person role.) **Counterweight:** the check does not flag what the reader already knows, and stays a
  list of lines plus one question.
- **Rule 14**, final check: a questionnaire has every part of Mode 2 Step 4, including the closing
  question. (A fifth, small change. It comes from a script finding in the second pilot, not from one of the
  four patterns: the NEW-3 questionnaire had no closing question. Drop it if it is not wanted.)

Size of the whole file: 21,432 to 23,091 characters (about 8 percent more). The text you paste is 22,793
characters.
Documents updated to v1.5 on 2026-10-13, in one pass: README, FOR-EXECUTIVES, WHAT-WAS-BUILT, TEST-REPORT (new section 9),
HOW-IT-WAS-BUILT (pointer only), QUICK-START and the two live-check scripts (length now about 23,000 characters).
Statements that "wait, what?" and "skip the questions" were never tested were corrected: both were played in
later simulations and met under both readers. The wording of where to start copying was tightened to "the line that
starts 'You are my decision partner. I am a senior leader'", because the same phrase also sits inside the comment at
the top of the file (that comment line was reworded too; the instructions text itself is unchanged, hash-checked).
Copies of the files before this pass are in `archive/docs-before-v1.5-update_2026-10-13/`. The examples in the new text (the headcount or
the location, next quarter, in good time) were checked against the scenarios and the example list: none
matches a scenario. Version 1.4 is kept at `archive/PROJECT-INSTRUCTIONS_v1.4_2026-10-13.md`. **Tested once** on four fresh scenarios (pilot 3), with the setup defect fixed (the instructions text given to the
assistant had begun with 211 characters of the setup comment in pilots 1 and 2). It still failed the
pre-written pass rule under both readers (one form item in a questionnaire, one scenario under the 60 percent
floor, about 27 to 29 percent of items untested), but the four recurring patterns largely did not recur where
the situation arose: 2 of 4 conversations showed any of them, against 8 of 9 under version 1.4. Many planned
traps never occurred, so the hand-over half of the first pattern is untested. Leftovers noted, not fixed: the
reply after a sign-off is two sentences, the reason in rule 10 runs past one sentence, "How to answer" can
omit a time estimate, and facts can still be parked without asking. Result page:
`docs/sessions/decision-grill/independent-sessions-pilot3-result_2026-10-13.html`.

## v1.4 — 2026-10-05

From batch R4 (v1.3): M2-A **PASS** (the multi-topic fix worked). M2-B FAIL on C1 only: "…so confirm
they are meant to differ" sat beside "What is missing from this list?".

- Rule 1 rewritten around its principle: the test is what a sentence asks of the user, not its
  grammar. Any sentence asking the user to answer, confirm, check or choose is a question, and a
  message that asks a question contains no other such sentence. The extra ask becomes the next
  question, or a "(my reading — confirm)" list entry. Rule 14's check matches. (The v1.1 fix listed
  only "Tell me if…" and "Let me know…"; "…so confirm they are meant to differ" slipped through.)
- Mode 2 Step 2: a possible overlap or conflict between two items is written into the list as a
  "(my reading — confirm)" entry, not asked separately. Every such entry states an actual reading.
  (R4 M2-A: one entry had no reading.) A duplicated sentence was removed.
- Mode 2 Step 3: skipped when earlier answers already gave how and when the recipient answers.
  (R4 M2-B: the user had said "our one-to-one next Tuesday"; the judge noted no rule covered it.)

## v1.3 — 2026-10-05

From batch R3 (v1.2): M1-A **PASS** (13 turns) and M1-B **PASS** (14 turns), down from hitting the
18-turn cap in R2. The pacing fix worked. M2-A failed C2 a second time.

- Mode 2 Step 2: when the user names several topics in one answer, the assistant asks a choice of
  meanings for the most important one, and writes its proposed reading of each of the others into
  the list, marked "(my reading — confirm)". It never settles a topic's meaning only inside the
  questionnaire. (R3 M2-A: "the fallback… and what support the vendor gives" arrived together;
  the one-question rule left "support" unpushed, and the assistant defined it itself in Q12.)
- Mode 2 Step 2: at most two items of the assistant's own (R3: it drafted six). Whenever the list
  changes, it is shown again with "What is missing from this list?", and confirming the list
  confirms every marked item. (R3: the list changed in turn 6 and was never re-shown.)

## v1.2 — 2026-10-05

From batch R2 (v1.1): 1 of 4 passed. M1-A and M1-B hit the 18-turn cap with no decision map (C6).
M2-A failed C2 (a topic accepted as a fact). M2-B passed. The v1.1 additions had no pacing
counterweight. This version supplies one and makes the limits mechanical.

- Mode 1 Step 2: the map lists **decisions only** (four to eight). Facts are not map items.
  (R2: M1-A spent nine questions digging into "how many days today" and "what filled days 7 to
  10", and reached 2 of 8 settled by turn 14.)
- Mode 1 Step 3: new **progress tag with a question counter**, "[Q4 · 3 of 7 settled]". New
  **budget**: at most two questions per map item, the waiting-items question by Q12, the map by
  Q15. Facts are asked once, pushed once, then taken as an assumption or parked. Word-sharpening is
  one question per word, as a choice between meanings with the unit included, for at most two
  words. (R2: "close" took four questions.) Parked items name a role only if the user named one.
  (R2 M1-B: "Parked — needs Legal" was invented.)
- Rule 1: "whatever works" on a decision that is not hard to reverse accepts the recommendation.
  (R2: hedged answers were counted as settled with no rule behind it.)
- Rule 2: the reaction is one or two sentences, covering what the answer proves and what it doesn't.
  The "what evidence would change your view" element is removed. (R2: reactions of four to five
  sentences in every test, and "if Stefan says…" promises in M2-A.) A finished document comes first,
  with at most one sentence before it.
- Rule 3: for a fact, one push is enough.
- Rule 5: items the assistant adds are marked "(added by me)" in the list, and confirming the list
  confirms them.
- Rule 10: in a questionnaire, the "Not included — see note" marker goes in the notes, quoting the
  user, so the document stays clean. (R2 M2-A: the marker sat inside the document.)
- Rule 11: "skip ahead", "get to the point" and similar now count as impatience. (R2 M1-A: "skip
  ahead to how to hit 5" was ignored.)
- Mode 2 Step 2: an item has a fact, number, date, name or yes/no as its answer. A topic gets one
  push, as a choice between likely meanings. (R2 M2-A: "barcode scanning on all 3 shifts".)
- Mode 2 Step 4: no vague words ("ready", "support") in questions without saying what they mean,
  and no added time, place or scope words unless listed under "Added by me". An unknown sender role
  becomes "[your name and role]".
- The examples were chosen so that they do not mirror any test scenario.

## v1.1 — 2026-10-05

From the pilot M1-A R1 (v1.0), which passed all six checks. The judge's other observations
pointed at patterns likely to repeat, so they were fixed before the batch.

- Rule 1 and rule 14: an invitation without a question mark ("Tell me if…", "Let me know…")
  counts as a second ask. (R1 turn 14 asked "Tell me if you want it split in two" next to a
  question.)
- Rule 2: the three-sentence reaction limit includes notes about what was recorded, parked or
  added. (Turns 4, 6 and 12 had four sentences.)
- Rule 3: when the user says someone else holds a fact, one push is enough, then park it. This
  removes the conflict with "push up to two times".
- Rule 5: an item the assistant adds to a list or map is announced and treated as its own until
  confirmed. Anything left out of an output is listed under "Left out on purpose".
- Mode 1 Step 2: a commitment the user mentions (a tool, a contract, a hire) goes on the map as a
  decision. (R1: the quoted 3-year tool was never decided and never marked "Hard to reverse".)
- Mode 1 Step 3: always sharpen the unit of the headline number (R1: "5 days" was never settled as
  working or calendar days). "Hard to reverse" examples now include a multi-year contract and
  buying a tool. New "Waiting items" step: the user decides whether items stay open until a
  parked fact arrives. (R1: the assistant decided this itself.)
- Mode 1 Step 4: open items can carry "Hard to reverse". Accepting the questionnaire offer keeps
  the decision map as the grill's result (R1: the judge flagged that C6 was ambiguous).
- Pacing counterweight: when the opening message states the decision clearly, Steps 1 and 2
  share one message.

## v1.0 — 2026-10-05

First version, built from the approved value review
(`AI_CYBORG/PLAYBOOK/BOOK-GRAPH_RAG/ONE_OFF_SOURCES/MATTPOCOCK-SKILLS-EXEC-VALUE-REVIEW_2026-10-05.html`, private, not published)
and decisions D1–D5 (one instructions file; clients, course buyers and book readers; two modes;
English first; standalone folder).

- Two modes: Decision Grill (from `grilling`) and Questionnaire (from `to-questionnaire`).
- Fourteen standing rules. Rules 1–5, 7 and 11–13 are shortened from the Leadership Thinking
  Partner v1.6 (rules 9–10 are its privacy rules, extended with questionnaire-specific limits),
  and each now starts with the behaviour wanted, with only a short list of banned
  phrases kept as a guardrail.
- New compared with the Leadership Thinking Partner: "My recommendation:" after every decision
  question (rule 1), use only what the user gives you, with connected tools left alone unless
  asked (rule 6), the "Wait, what?" re-explain (rule 8), the questionnaire-specific part of the
  privacy limits (rules 9–10), and a final-output check that the user "would remember making every decision"
  (rule 14).
- Every example question in the instructions was checked to be a single question.
