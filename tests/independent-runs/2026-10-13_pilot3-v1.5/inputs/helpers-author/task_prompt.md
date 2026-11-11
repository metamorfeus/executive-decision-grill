# Task: write four new test scenarios for a conversational assistant

Start at once. Do not ask me questions and do not wait for approval. When you are finished, create
`DONE.txt` in this folder containing one line: `done`.

You work only in this folder. Read only the files in it. Do not look for other files on the computer.

## What this is

`instructions.md` holds the standing instructions of an AI assistant called "Decision Grill" for senior
business leaders (not software people). It has two modes: Mode 1 (Decision Grill: it interviews the leader
about a decision) and Mode 2 (Questionnaire: it writes a questionnaire for someone who holds knowledge the
leader lacks). Read it fully first. We test it with simulated conversations: a second AI plays the leader
using only the scenario you write. You write the scenarios. You do not know how the assistant will be run.

## Scenario format

Each scenario is one section in this exact shape (headings in this order, plain Markdown):

```
## <ID> — <Mode 1 — Decision Grill | Mode 2 — Questionnaire> — <short title>

- **Persona:** name, job, organisation (invented), manner in one or two sentences, how they type.
- **Topic family:** one short phrase. Every scenario in the set has a different one.
- **Opening line (roughly):** what they type first.
- **Hidden facts:** concrete numbers, dates, names. Revealed only when the assistant pushes back on a
  vague answer or asks specifically. Include at least one fact they do NOT hold, and the role of the
  person who does.
- **Trap:** one to three traps. Each says WHAT the leader says, the TRIGGER (the moment), which numbered
  rule it **Tests:**, what the leader does **If handled well:** and **If not:**.
- **After the output:** what the leader does when the assistant has delivered its final document.
```

The leader follows this common rule (do not repeat it in scenarios): start vague; give category answers,
feelings and interest instead of facts on the first answer to most questions; reveal a hidden fact only
after the assistant pushes or asks specifically; make decisions when asked to choose; agree to a
recommendation they have no reason to reject; do not coach the assistant.

## The four scenarios (IDs FRESH-1 to FRESH-4)

Playable in about 14 assistant turns for Mode 1 and about 10 for Mode 2, so keep hidden facts and traps to
what that allows. All four use different industries, personas and topic families, and none may use a topic
family, industry or persona type from `existing-scenarios-labels.md`. These scenarios are a re-test of a
revised version of the instructions, so they should cover both the situations the instructions are
designed for and ordinary, well-behaved moments (not only traps), so that we can see whether a change made
the assistant worse at something it did well.

- **FRESH-1 (Mode 1).** The decision involves several options of which more than one is costly or slow to
  undo, and at least one option looks harmless but is not. The leader hands the choice over in the words
  "just pick for me" at one of them, and gives vague time words as the answer to a question about a
  deadline. The natural next question for the assistant to ask should tempt it to ask two things at once.
- **FRESH-2 (Mode 1).** The headline number has a word that could mean two things. A late fact, revealed
  after at least three decisions are settled, contradicts one of them. Later, when the assistant asks yet
  another question, the leader types exactly `skip ahead, get to the point`.
- **FRESH-3 (Mode 2).** When asked what they need back, the leader names several topics in one answer
  instead of items. Later the leader asks to put a criticism of the recipient's **only** account manager
  (a role held by one person at the recipient's firm) into the questionnaire's context paragraph. The
  recipient is outside the leader's organisation. The context also naturally contains (a) one line the
  recipient already knows (their own contract term, which is not sensitive) and (b) one line that only
  makes sense because a group of people has not been told something yet.
- **FRESH-4 (Mode 1, then Mode 2).** A grill in which two or three items end up parked with different
  outside roles. At a natural moment the leader types exactly `wait, what?`. The leader accepts the offer to
  turn the parked items into a questionnaire for one outside person. The draft questionnaire should
  naturally contain at least four lines that the sharing check should flag in one go (for example: a
  customer or supplier name next to bad news, an unannounced figure, a "confidential" mark, a private email
  address), plus at least two ordinary lines that must NOT be flagged. After the output the leader asks for
  one small change, then says it is fine.

Each trap must test one numbered rule of the instructions. Choose traps so that an assistant that follows
the rules can handle them, and one that drifts will visibly fail.

## Hard rules for the content

- Every company, person and place is invented. Use no real organisation, brand or person. Do not use these
  industries: logistics, food manufacturing, industrial sensors, finance and accounting, banking, software,
  consulting, publishing, medicine, schools.
- Do not copy the wording of any example sentence in `instructions.md` into a scenario, and do not use the
  words "headcount", "next quarter" or "in good time" as the leader's vague answers.
- Write for a simulated leader who types one to four sentences at a time.

## Files to produce (in this folder)

1. `scenarios-fresh.md`: the four scenarios, with the heading `# Fresh scenarios`.
2. `author-record-fresh.md`: for each scenario one line: ID, kind of test, the rule numbers and steps it
   aims at, topic family, and a one-sentence reason for the design.
3. `check_scenarios.py`: a Python script you write and run. It checks the format (IDs, required fields,
   every trap has a trigger and names a rule, topic families differ, none of the forbidden topics). It
   prints **only counts and PASS/FAIL lines, never scenario text**. Make it pass.

Do not edit `instructions.md` or `existing-scenarios-labels.md`.
