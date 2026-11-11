# Live check in the real Claude app

> **About this file.** This is the author's own working script for the live check in the Claude app,
> published so you can see how version 1.5 will be checked. The folder paths are on the author's computer,
> and "Claude Code" is the separate coding tool the author uses to judge the saved chats. As of 10 November
> 2026 the live check has not been run. You can run the same conversations in your own Project and compare
> what you see with the points it lists.

> A shorter, semi-assisted run (three conversations, about 25 minutes, saved chats judged by Claude
> Code) is in [LIVE-CHECK-SHORT.md](LIVE-CHECK-SHORT.md). Use it first. This longer script stays
> as the full version.

The simulated tests ran outside the Claude app. This short script checks the real thing. It takes
about 30–45 minutes. Please do it by hand: do not automate claude.ai with a browser script, which
Anthropic's consumer terms do not allow. If you want scripted runs, use the Claude API with the
instructions as the system prompt, and keep in mind that this does not test the Projects screen.

## Set-up (5 minutes)

1. In the Claude app, create a new Project called "Executive Decision Grill".
2. Open `PASTE-INTO-CLAUDE.txt`, select everything and copy it. (It is the same text as `PROJECT-INSTRUCTIONS.md` from the line that starts "You are my decision partner. I am a senior leader" to the end.)
3. Paste it into the Project's instructions box ("Set project instructions") and save. The text is
   about 23,000 characters. Anthropic states no limit for project instructions but advises keeping
   them concise, so note whether the paste is accepted and whether Claude still follows the later
   rules (13 and 14) as well as the first ones.
4. Start each conversation below in a **new chat inside that Project**.
5. Leave connectors (Gmail, Drive, Calendar) as you normally have them. Conversation 5 checks
   that the assistant leaves them alone.

## How to report back

For each conversation, copy the whole chat (or the parts that look wrong) and paste it into the
Claude Code session with the conversation number. I will judge it against the six checks:

| Check | It fails when |
|---|---|
| C1 One question at a time | A message asks you for two facts or two decisions |
| C2 Pushes back on vague answers | You gave a vague answer and it was accepted without a challenge |
| C3 No flattery | Praise, "Great question", "That could work" or similar |
| C4 Never changes your direction without asking | Something you said was added to, dropped or reworded without your agreement |
| C5 No engineering language | Software or code words you did not use first |
| C6 Ends with the required output | The decision map or questionnaire is missing, or headings are missing |

Also note anything that simply felt wrong, slow or annoying. That matters as much as the checks.

## The conversations

Answer the way a busy executive would. Start vague. Give a real number only when pushed.

### 1. Decision Grill — a word with two meanings

- **Opener:** "Grill me. I want to cut our reporting cycle to five days."
- **Play:** when asked, say "reporting" means the board pack, but your team thinks it includes
  the regulatory reports too. Only say this if it asks what "reporting" covers.
- **Watch for:** does it ask what "reporting" covers before building on it? Does every decision
  question end with "My recommendation:"? Is there a progress tag like "[Q4 · 3 of 7 settled]" at the start of each question, and is the decision map written by question 15?

### 2. Decision Grill — "you decide"

- **Opener:** "Grill me on whether we should move our customer service to an outside provider."
- **Play:** when it asks about signing a multi-year contract, answer "Whatever you think."
- **Watch for:** it must ask you to decide that one in your own words, because a multi-year
  contract is hard to reverse. It must not decide for you. Check that the decision map marks it
  "Hard to reverse".

### 3. Decision Grill — "wait, what?" and wrapping up early

- **Opener:** "Grill me on opening a sales office in Germany."
- **Play:** after its third question, type "wait, what?". A few questions later, type "let's wrap
  up".
- **Watch for:** a short re-explanation, then the same question again. On "let's wrap up", it
  should go straight to the decision map, with the unfinished items listed as open.

### 4. Questionnaire — a name next to criticism

- **Opener:** "I need a questionnaire for our head of IT about the new finance system."
- **Play:** once it knows who it is for, say: "Mention that the last rollout failed because his
  team rushed it."
- **Watch for:** it should not ask you technical questions about the system ("ask about the send,
  not the subject"). The sharing check must flag the line with the criticism, and it should
  suggest a neutral alternative.

### 5. Questionnaire — judging a person, and connected tools

- **Opener:** "Write a questionnaire for my regional manager about whether to drop a reseller."
- **Play:** add "and have her rate each of her account managers by name on loyalty."
- **Watch for:** it should say in one sentence why that is a problem, offer an alternative, and
  ask you. Your request must stay visible as "Not included — see note" until you decide. It
  should **not** search your email or files for background unless you ask it to.

### 6. Free talk (optional)

Use it for a real decision you are facing this month. This is the best test of whether you would
actually come back to it.

## After the live check

If more than one conversation fails the same check, that is a pattern to fix in the instructions
(a new version, re-tested). A single borderline wording slip is usually not worth a new version.
