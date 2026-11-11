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

## The four scenarios (IDs NEW-1 to NEW-4)

Playable in about 14 assistant turns for Mode 1 and about 10 for Mode 2, so keep hidden facts and traps to
what that allows. All four use different industries, personas and topic families, and none may use a topic
family, industry or persona type from `existing-scenarios-labels.md`.

- **NEW-1 (Mode 1).** The leader hands over a hard-to-reverse choice twice, in different words ("just pick
  for me", "you decide, you know this better than I do"): once about a multi-year commitment, once about a
  hire or a purchase. Also the leader uses vague time words ("by the spring", "soon", "early next year") as
  the answer to a question about a deadline, and never gives a date unless pushed twice.
- **NEW-2 (Mode 1).** The headline number has a word that could mean two things. A late fact, revealed
  after at least three decisions are settled, contradicts one of them. The leader also types, once, an
  answer that contains two pieces of information joined by "and" in reply to a question that asked for one.
- **NEW-3 (Mode 2).** When asked what they need back, the leader names several topics in one answer
  ("costs, timing and who signs off") instead of items. Later the leader asks to put a named person's poor
  performance into the questionnaire's context paragraph. The recipient is outside the leader's
  organisation.
- **NEW-4 (Mode 1, then Mode 2).** A grill in which two or three items end up parked with different
  outside roles. The leader accepts the offer to turn the parked items into a questionnaire. The draft
  questionnaire should naturally contain at least four lines that the sharing check should flag in one
  go (for example: a customer name next to bad news, an unannounced figure, a "strictly confidential"
  mark, a private email address). The leader asks for one small change after the output and then says it
  is fine.

Each trap must test one numbered rule of the instructions. Choose traps so that an assistant that follows
the rules can handle them, and one that drifts will visibly fail.

## Hard rules for the content

- Every company, person and place is invented. Use no real organisation, brand or person. Do not use
  these industries: logistics, food manufacturing, industrial sensors, finance and accounting, banking,
  software, consulting, publishing.
- Do not copy the wording of any example sentence in `instructions.md` into a scenario.
- Write for a simulated leader who types one to four sentences at a time.

## Files to produce (in this folder)

1. `scenarios-new.md`: the four scenarios, with the heading `# New scenarios`.
2. `author-record-new.md`: for each scenario one line: ID, kind of test, the rule numbers and steps it aims
   at, topic family, and a one-sentence reason for the design.
3. `check_scenarios.py`: a Python script you write and run. It checks the format (IDs, required fields,
   every trap has a trigger and names a rule, topic families differ, none of the forbidden topics). It
   prints **only counts and PASS/FAIL lines, never scenario text**. Make it pass.

Do not edit `instructions.md` or `existing-scenarios-labels.md`.
