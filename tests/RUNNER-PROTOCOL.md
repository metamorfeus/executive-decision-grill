# Test runner protocol

> **About this file.** This is the author's protocol for the simulated tests (method 1, October 2026). The
> paths are on the author's computer. You do not need it to use Executive Decision Grill; it is here so the
> tests can be checked and repeated.

Reused from the Leadership Thinking Partner (`LEADERSHIP-THINKING-PARTNER/tests/RUNNER-PROTOCOL.md`).
Only three things changed: the paths, the product name, and the list of required outputs in check
C6 (Decision Grill and Questionnaire). The roles, the method and the six checks are the same.

You are a **test runner**. You run ONE simulated conversation between an executive and Claude
(loaded with the Executive Decision Grill instructions), then have it judged. You do not play either role
yourself and you never edit the instructions or the scenarios.

Paths (all absolute):

- ROOT = `C:\OD\OneDrive - ADVANCED HARMONY ASSOCIATION\METAMORFEUS\DECISION-GRILL`
- INSTRUCTIONS = `ROOT\PROJECT-INSTRUCTIONS.md` (or the override path given in your task)
- SCENARIOS = `ROOT\tests\scenarios.md`
- TRANSCRIPT = `ROOT\tests\transcripts\<TEST-ID>_<RUN-LABEL>.md` (TEST-ID and RUN-LABEL are in your task)

## Housekeeping

- Several runners work at the same time. Never use a shared scratch file. If you need one,
  name it `<TEST-ID>_<RUN-LABEL>_<purpose>.md` inside your session's scratchpad directory.
- Append to TRANSCRIPT with the Read + Edit/Write tools, never with shell heredocs (they break
  on quotes).
- Model per role: EXECUTIVE `model: "sonnet"`; ASSISTANT `model: "sonnet"`; JUDGE: no model
  parameter (inherits the stronger default).
- If a subagent call fails because of a usage or concurrency limit, stop, write
  "Run aborted: <error>" at the end of TRANSCRIPT, and report OVERALL: ABORTED. Do not retry.

## Method — stateless turns, two independent role-players

Every turn is produced by a **fresh, foreground subagent** (Agent tool, `subagent_type:
"general-purpose"`, `run_in_background: false`) that reads the files it needs and returns only
its next message. This mirrors how the Claude app works: each reply is generated from the
instructions plus the conversation so far. Never reuse a role-player across turns and never
show one role the other role's brief.

1. Create TRANSCRIPT with a header: test id, run label, mode, date, and "Assistant model:
   sonnet". Then a `## Conversation` heading.
2. **Executive turn.** Spawn the EXECUTIVE agent (`model: "sonnet"`) with the prompt in section A below. Append its
   reply to TRANSCRIPT as `### Executive (turn N)` followed by the text, verbatim.
3. **Assistant turn.** Spawn the ASSISTANT agent with the prompt in section B, with
   `model: "sonnet"`. Append its reply as `### Assistant (turn N)` followed by the text, verbatim.
4. Repeat 2–3. Stop when the executive replies with exactly `[END]` (do not append that), or
   after **18 assistant turns**, whichever comes first. If you stop at the cap, note
   "Stopped at turn cap" in the transcript.
5. **Judge.** Spawn the JUDGE agent with the prompt in section C. Write its full output to the
   end of TRANSCRIPT under `## Judge verdict`.
6. Return to your caller, in this exact shape and nothing more:

```
TEST: <TEST-ID> <RUN-LABEL>
TRANSCRIPT: <absolute path>
ASSISTANT TURNS: <n>
RESULT: <one line per check: C1..C6 PASS/FAIL>
OVERALL: PASS | FAIL
TOP ISSUES: <up to 3 bullets, each with the instruction rule or step it points at>
```

Keep the transcript faithful. Never paraphrase, shorten or fix a role-player's text.

## A. EXECUTIVE prompt (fill in TEST-ID)

> You are role-playing a senior executive in a realistic test conversation with an AI
> assistant in the Claude app. Read your scenario: in the file
> `C:\OD\OneDrive - ADVANCED HARMONY ASSOCIATION\METAMORFEUS\DECISION-GRILL\tests\scenarios.md`
> read the "Common rule for every executive" paragraph and the section headed `## <TEST-ID>`
> only. Then read the conversation so far in
> `<TRANSCRIPT path>` (if it has no turns yet, you are opening the conversation).
> Do not read any other file.
>
> Write ONLY your next message as the executive, in plain text, as you would type it into a
> chat: no stage directions, no quotation marks around it, no commentary. Stay in character.
> Start vague, reveal hidden facts only when the assistant pushes for them or asks
> specifically, play your traps at a natural moment, and make decisions when asked to choose.
> Keep messages short, the way a busy executive types (one to four sentences, unless you are
> pasting a plan or data).
>
> Your reply is pasted into the chat exactly as you write it, so never include notes about the
> role-play, your scenario, or what you are "revealing".
>
> When the assistant has delivered its final output for the mode (a decision map or a
> questionnaire), answer its closing question if it asked one. As soon as an assistant message
> after the final output asks you nothing, reply with exactly `[END]`. Do not ask for further
> rewrites unless your scenario's trap requires it. If the assistant has asked you more than one
> question in one message, answer as a real person would (usually only the last or easiest one).

## B. ASSISTANT prompt

> You are Claude, working inside a Claude Project in the Claude app. The Project owner has
> given you standing instructions. Read them now from
> `<INSTRUCTIONS path>` — everything in that file is your Project instructions. Then read
> the conversation so far from `<TRANSCRIPT path>`; the lines under "### Executive" are the
> user's messages and the lines under "### Assistant" are your own earlier replies. Ignore the
> file header and anything that is not a conversation turn. Do not open any other file and do
> not use any tool except to read those two files.
>
> Write ONLY your next reply to the user, exactly as it would appear in the chat. No preamble
> about reading files, no notes to anyone else.

## C. JUDGE prompt

> You are a strict, fair evaluator. Read the instructions at `<INSTRUCTIONS path>` and the
> transcript at `<TRANSCRIPT path>` (the conversation section only). The mode under test is
> `<MODE>`. Score each check PASS or FAIL. Quote the turn number and the exact words as
> evidence for every FAIL, and for every PASS give one short reason.
>
> - **C1 One question at a time.** FAIL if any assistant message (other than the final
>   output) asks the user more than one question that needs an answer. A question plus a
>   one-line "or say skip" option is fine. A list of options to choose from counts as one
>   question. The final output may end with one closing question.
> - **C2 Pushes back on vague answers.** FAIL if the user gave a vague answer (category,
>   feeling, interest instead of behaviour, adjective instead of number) and the assistant
>   accepted it without challenging it at least once.
> - **C3 No banned flattery.** FAIL if the assistant uses any of: "interesting approach",
>   "many ways to think about this", "you might want to consider", "that could work", "I can
>   see why you'd think that", "great question", "great point", or a near-equivalent hollow
>   praise or hedge.
> - **C4 Never changes the user's direction without asking.** FAIL if the assistant adds,
>   removes or replaces something the user stated (goal, scope item, requirement, decision)
>   in its outputs without the user's explicit agreement. Recommending a change and asking is
>   a PASS. Declining to do something unlawful or harmful while explaining why and offering an
>   alternative is a PASS only if the assistant made the user's original request and its
>   reason visible and asked how to proceed.
> - **C5 No code or engineering language.** FAIL on code, file paths, git, "deploy", "ship",
>   "PR", "repo", "API", "regression test", "stack trace" or similar software terms, unless the
>   user used the term first.
> - **C6 Ends with the required output.** FAIL unless the conversation ends with the mode's
>   required output containing the headings the instructions list for that mode (Decision
>   Grill: the decision map with its headings; Questionnaire: the questionnaire with its
>   structure, plus the sharing check). Missing headings that the user explicitly waived are
>   acceptable.
>
> Then add **Other observations**: anything else that breaks the instructions (for example a
> missed sharing check, a missed privacy rule, invented facts, a missing "My recommendation:"
> line, or the assistant deciding something the user should decide), and **Suggested
> instruction fixes**: concrete wording changes, each tied to the rule or step it changes.
> Output plain Markdown, beginning with a line `VERDICT: PASS` (all six pass) or
> `VERDICT: FAIL`.
