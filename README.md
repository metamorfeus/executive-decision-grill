# Executive Decision Grill

**Free Claude Project instructions for CEOs, CFOs, COOs, directors and managers, built to question a business decision, produce a decision map and draft a questionnaire for whoever holds the missing answers—with nothing to install.**

Paste the instructions once into a Claude Project, then start a chat about your decision.
The interview is built to surface assumptions and unanswered questions before you commit.
**Claude recommends. You decide.**

**[Open the home page and copy the instructions](https://metamorfeus.github.io/executive-decision-grill/)** ·
[Printable quick start](https://metamorfeus.github.io/executive-decision-grill/docs/QUICK-START.html) ·
[Guide for executives](https://metamorfeus.github.io/executive-decision-grill/docs/FOR-EXECUTIVES.html)

> **Please read this first.** Version 1.5 has been tested only in simulated conversations, not yet
> in the real Claude app, and it **did not pass its final test** on four held-back scenarios (11 November
> 2026). In that test it sometimes changed what the executive had decided without asking, accepted vague
> answers, and missed things in its sharing check. Read every document Claude writes, and check it against
> what you said, before you use or send it. Details are in
> [How it was tested, and what was not](#how-it-was-tested-and-what-was-not).

---

## Question a business decision before you commit

You say what you are deciding, for example "Grill me on whether we should move customer service to
an outside provider." The instructions are built to guide the interview as follows:

1. **Restates your decision** in one sentence and checks it with you.
2. **Lists the smaller decisions hiding inside it**, usually four to eight, and asks what is missing.
3. **Asks about them one at a time.** Every decision question comes with Claude's recommended answer
   and a reason, so "Agreed" is a complete reply.
4. **Pushes back on vague answers.** "It should be fine" or "the regions" gets a second question
   asking for a name, a number, a date or an example.
5. **Hands you a decision map.** What is decided, what you said no to, what is parked with someone
   else, what is still open or not yet clear, the terms you agreed, the assumptions you rely on, and
   one next step.

When a question can only be answered by someone else, Claude offers to draft a short, neutral
**questionnaire** for that person. It checks the questionnaire for names next to criticism,
unannounced plans and personal data before you send it.

**Claude recommends. You decide.** The instructions are built to leave every decision to you. If you
say "whatever you think" about something that is hard to undo, such as a multi-year contract, Claude
asks you to decide it in your own words. In the final test this did not always hold: in at least three of four
conversations a decision was changed or added to without asking, so compare the decision map with what
you actually said.

## What a decision map and questionnaire help you do

- **Find the decisions you didn't know you were making.** "Cut month-end close to five days" hides
  several smaller decisions. In one of our test conversations, Claude found eight. It lists them
  first, then works through them in the order that settles the most other questions.
- **Answer fast when you agree.** Every decision question ends with "My recommendation:".
- **Catch words that mean two things.** "Revenue: booked, billed or collected?" Many bad decisions
  start with two people using one word differently.
- **Know what you don't know.** Unknowns become parked or open items in your map, not made-up
  numbers.
- **Get the missing answers.** The questionnaire asks you only who it is for, what they know that
  you don't, and what you need back.
- **Stay in charge.** Your words go into every output as you said them, and anything Claude adds is
  labelled.

## Pick your mode: a decision interview or a questionnaire

| Mode | Use it when | Say something like | You get |
|---|---|---|---|
| **1. Decision Grill** | You have a decision or plan and want to be challenged until nothing important is assumed | "Grill me on whether we should drop our reseller in Central Europe." | A decision map: decided, said no to, parked with someone else, open, not yet clear, terms agreed, assumptions, next step |
| **2. Questionnaire** | You need answers that someone else holds | "Write a questionnaire for our head of IT about the warehouse go-live." | A questionnaire ready to paste into an email or a document, with a sharing check |

At the end of a Decision Grill, Claude offers to turn the parked items into a questionnaire.

## Set up the Claude Project instructions in about five minutes

You need a Claude account. Anthropic's help pages say Projects are available on every plan, including
Free (at most five Projects), and that you can set instructions for each Project
([What are projects?](https://support.claude.com/en/articles/9517075), read on 9 November 2026). We
have not tried it on a Free account, so check that the **Set project instructions** button appears.
A computer is easier than a phone for the paste.

1. **Create the Project.** Open [claude.ai](https://claude.ai) or the Claude desktop app, choose
   **Projects**, then click **+ New Project**. Name it *Executive Decision Grill*.
2. **Copy the instructions.** The easiest way is the **Copy the instructions** button on the
   [home page](https://metamorfeus.github.io/executive-decision-grill/). You can also open
   [the text on a page of its own](https://raw.githubusercontent.com/metamorfeus/executive-decision-grill/main/PASTE-INTO-CLAUDE.txt),
   press Ctrl+A (Cmd+A on a Mac) and copy it.
3. **Paste and save.** In your Project, choose **Set project instructions** (on some screens it is
   called **Instructions**), paste, and click **Save instructions**. The text is about 23,000
   characters.
4. **Start a chat inside the Project** and name your decision: "Grill me on…". If it worked, Claude
   restates your decision in one sentence and lists the smaller decisions inside it.

This is not a skill, a plugin or an app. The Project's instructions are the whole set-up. Start a new
chat inside the Project for each new decision.

## Your first conversation

| You say | What happens |
|---|---|
| "Grill me on opening a sales office in Germany." | Claude restates the decision and lists the smaller decisions inside it. |
| "Agreed" | You accept Claude's recommended answer and move on. |
| "Not sure, probably next year" | Claude says why that is not enough and asks for a date. |
| "I don't know" | The item is parked with the person who would know, or left open. Claude is built not to make up an answer. |
| "wait, what?" | Claude re-explains its last point in plain words and asks again. |
| "skip the questions" | Claude asks the two most important questions, then writes the map. |
| "let's wrap up" | Straight to the decision map, with the unfinished items listed. |

Each question starts with a progress tag such as "[Q4 · 3 of 7 settled]". Each mode is built to reach
its output within fifteen of Claude's questions. In the version 1.5 test conversations, the decision
map came in Claude's 14th to 16th message, and the questionnaire was finished in Claude's 6th.

## If something goes wrong

| What you see | What to do |
|---|---|
| The copy button does not work | The home page then shows the whole text in a box. Copy it from there, or use **Open the text instead**. |
| The paste is refused or looks cut short | The text should start "You are my decision partner." and end "What should I change before you send it?" Paste again, from a computer if you can. If it fails twice, please tell us. |
| No **Set project instructions** button | Check that you are on the Project's own page, not in an ordinary chat, and try a computer. |
| Claude answers like an ordinary chat | The chat was most likely started outside the Project. Start a new chat from the Project's page. |
| Claude asks two things at once | Answer the more important one, or reply "one question at a time, please". |
| In a long chat, Claude drifts from the rules | Say "please follow the project instructions", or "let's wrap up" to get the map so far. |

More detail is in the [guide for executives, section 6](https://metamorfeus.github.io/executive-decision-grill/docs/FOR-EXECUTIVES.html#help).

## How it was tested, and what was not

- **First method, October 2026.** AI role-players played a CFO, a head of sales and an operations
  director who start vague, hand the decision back to Claude ("just pick for me"), or ask for things
  they shouldn't, such as rating named employees on loyalty. An independent AI judge scored six
  checks: one question at a time, pushing back on vague answers, no flattery, never changing your
  direction without asking, plain business language, and finishing with the right document. Across
  12 judged conversations and five versions (up to 1.4), all four scenarios passed all six checks in
  their latest run (on versions 1.2 to 1.4).
- **Second method, 13 October 2026.** Separate AI sessions wrote new scenarios, played the executive,
  and scored the answers without knowing which version they were reading. Version 1.4 missed the
  strict pass rule, written before each round, in two rounds. Four problems showed up in both. Version
  1.5 was written for those four. On four new scenarios it again missed the strict rule, but the four
  problems appeared in 2 of 4 conversations, against 8 of 9 for version 1.4. Many planned test moments
  never came up, so this is a lead, not a verdict.
- **Final test, 11 November 2026.** The four scenarios held back since October were run once, with
  the same pass rule. Version 1.5 did not pass: safety items were missed in all four conversations,
  and coverage was 76 and 62 percent (80 needed). Three of the four earlier problems came back, and in at
  least three of the four conversations a decision was changed or added to without asking. Details are in
  section 10 of the test report.
- **Not yet done.** A check in the real Claude app; the author chose to publish before it.
  Everything so far is Claude testing Claude with a simulated executive.

The weak spots we saw are listed openly in the
[test report](https://metamorfeus.github.io/executive-decision-grill/tests/TEST-REPORT.html), section 6
and section 9. **Current version: 1.5** (13 October 2026). The text you paste has not changed since; see
the [changelog](CHANGELOG.md).

## Privacy and good practice

- Check your organisation's AI policy before you paste confidential material.
- The instructions tell Claude to work only from what you tell it or paste in, and to leave your
  connected email, files and calendar alone unless you ask. If Claude is connected to your email, files
  or calendar, you stay in control of that connection.
- A questionnaire asks for knowledge, not for judgements about named colleagues. Claude is built to
  flag requests to rate individuals, and requests to survey many employees, and to suggest an
  alternative.
- Before a questionnaire goes out, a sharing check flags names next to criticism, unannounced plans,
  confidential material and personal data.

## Questions (FAQ)

**Do I need to install anything? Is this a Claude skill?**
No. It is a set of Claude Project instructions. You paste the text once into a Project in the normal
Claude app, on claude.ai, the desktop app or the phone app.

**Where do I paste Claude Project instructions?**
Open the Project's page and choose **Set project instructions** (on some screens it is shown as
**Instructions**). Paste the whole text and save. Every chat you start inside that Project then
follows it.

**Does Claude make the decision for me?**
No. It recommends an answer to every decision question, and you choose. On hard-to-reverse choices it
asks you to decide in your own words, even if you say "whatever you think".

**Is it related to Matt Pocock's grill-me skill?**
Yes. The methods are adapted, in our own words, from
[Matt Pocock's skills](https://github.com/mattpocock/skills) (`grill-me` and `to-questionnaire`),
which are written for software developers using Claude Code. This version is for executives using the
normal Claude app, and it contains no code from that repository. See [NOTICE.md](NOTICE.md).

**Which languages does it work in?**
It was written and tested in English only. A Bulgarian version is planned.

**Something went wrong, or felt annoying. Where do I tell you?**
First look at [If something goes wrong](#if-something-goes-wrong). If that does not help, please
[use the feedback form](https://github.com/metamorfeus/executive-decision-grill/issues/new/choose) and
paste the part of the chat that went wrong. The form needs a free GitHub account, and what you write
there is public, so leave out names and anything confidential.

## Companion

The [Leadership Thinking Partner](https://github.com/metamorfeus/leadership-thinking-partner) is a
companion set of instructions for plan reviews, decision records, incident reviews, delegation briefs
and handover notes.

## What is in this repository

| File | What it is |
|---|---|
| [PASTE-INTO-CLAUDE.txt](PASTE-INTO-CLAUDE.txt) | The text you paste into your Claude Project, and nothing else |
| [PROJECT-INSTRUCTIONS.md](PROJECT-INSTRUCTIONS.md) | The same text with a title and a short note at the top |
| [index.html](index.html) | The home page, with the copy button ([open it](https://metamorfeus.github.io/executive-decision-grill/)) |
| [docs/QUICK-START.html](docs/QUICK-START.html) | A printable setup guide ([open it](https://metamorfeus.github.io/executive-decision-grill/docs/QUICK-START.html)) |
| [docs/FOR-EXECUTIVES.html](docs/FOR-EXECUTIVES.html) | The fuller guide: why it helps, how to use it, two worked examples, good practice and limits ([open it](https://metamorfeus.github.io/executive-decision-grill/docs/FOR-EXECUTIVES.html)) |
| [docs/WHAT-WAS-BUILT.html](docs/WHAT-WAS-BUILT.html) | The product record: modes, rules, decisions, exclusions, test status ([open it](https://metamorfeus.github.io/executive-decision-grill/docs/WHAT-WAS-BUILT.html)) |
| [docs/HOW-IT-WAS-BUILT.html](docs/HOW-IT-WAS-BUILT.html) | Step-by-step guide to rebuilding it, including the test harness ([open it](https://metamorfeus.github.io/executive-decision-grill/docs/HOW-IT-WAS-BUILT.html)) |
| [docs/HOW-TO-RELEASE.html](docs/HOW-TO-RELEASE.html) | For the maintainer: the fingerprint check, releasing a new version, publishing and undoing ([open it](https://metamorfeus.github.io/executive-decision-grill/docs/HOW-TO-RELEASE.html)) |
| [tests/](tests/) | Test scenarios, the 12 judged transcripts, the [test report](tests/TEST-REPORT.html) ([open it](https://metamorfeus.github.io/executive-decision-grill/tests/TEST-REPORT.html)), a cleaned copy of the independent-sessions records (`tests/independent-runs/`, see its `PUBLIC-COPY-NOTE.md`) and the author's live-check scripts for the Claude app |
| [CHANGELOG.md](CHANGELOG.md) | Version history, each change tied to a test finding |
| [RELEASE-CHECKLIST.html](RELEASE-CHECKLIST.html) | What was checked before publication, and what is still open ([open it](https://metamorfeus.github.io/executive-decision-grill/RELEASE-CHECKLIST.html)) |
| [.github/ISSUE_TEMPLATE/](.github/ISSUE_TEMPLATE/) | The feedback form, with a privacy warning |
| [NOTICE.md](NOTICE.md) | Credits, a map of each mode to its source, and the source licence |
| [LICENSE](LICENSE) | MIT licence |

The HTML pages show as code on GitHub. Use the "open it" links to read them as pages.

## Credits and licence

Created by Peter Velinov / [Metamorfeus](https://github.com/metamorfeus). Released under the
[MIT licence](LICENSE). Called Decision Grill until 9 November 2026.

The methods are adapted, in our own words, from
[Matt Pocock's skills](https://github.com/mattpocock/skills), which are also MIT-licensed. This
project contains no code from that repository and does not install it. It is independent and not
affiliated with or endorsed by Matt Pocock or Anthropic.

## About the author

Executive Decision Grill is made by Peter Velinov / Metamorfeus.

- [Metamorfeus](https://metamorfeus.com/) — Custom AI automation services for business processes.
- [Metamorfeus products](https://metamorfeus.com/shop/) — Paid offerings including AI audits, workforce automation and employee AI training.
- [Claude Cowork Training](https://claudecoworktraining.com/) — Independent, free self-paced training for everyday work, with paid team workshops; using Cowork requires a paid Claude plan.
- [Management Assistant](https://assistant.metamorfeus.com/) — Turns meeting audio or transcripts into draft minutes for review and keeps tasks, owners and due dates together.

Some linked products and services are paid. Executive Decision Grill stays free and works without any of them. Independent; not affiliated with or endorsed by Matt Pocock or Anthropic.
