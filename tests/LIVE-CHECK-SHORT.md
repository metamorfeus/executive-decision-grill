# Live check, short version (semi-assisted)

> **About this file.** This is the author's own working script for the live check in the Claude app,
> published so you can see how version 1.5 will be checked. The folder paths are on the author's computer,
> and "Claude Code" is the separate coding tool the author uses to judge the saved chats. As of 10 November
> 2026 the live check has not been run. You can run the same conversations in your own Project and compare
> what you see with the "Watch for" points.

This is a shorter run of [LIVE-CHECK.md](LIVE-CHECK.md). It takes about 25 minutes and has three
conversations. It covers the behaviour no simulation can play, Claude leaving your connected tools alone,
and two phrases that simulations played only once or twice: "wait, what?" and "skip the questions". It also repeats the two behaviours
that matter most: refusing to decide a hard-to-reverse choice for you, and not putting a name next
to criticism.

**How it works.** You run each conversation in a real Claude Project. Then you save the whole chat
into a text file in the folder `tests\live-check\`. Claude Code reads the file and judges it against
the six checks. Claude Code cannot see your Claude app, and it must not try to: Anthropic's
consumer terms do not allow automating claude.ai. The saved file is the only way the replies get
from the app to the judge. If you prefer, you can paste a chat straight into the Claude Code
conversation instead.

## Before you start (5 minutes)

1. In the Claude app, create a Project called "Executive Decision Grill". On a computer use the desktop app
   or claude.ai. On a phone use the Claude app. A computer is easier for the paste in step 3.
2. Open `PASTE-INTO-CLAUDE.txt` in the product folder and copy all of it. (It is the same as everything
   in `PROJECT-INSTRUCTIONS.md` from the line that starts "You are my decision partner. I am a senior
   leader" to the end.)
3. Choose "Set project instructions", paste, and save. **Note what happens.** The text is about
   23,000 characters. Tell me if the paste was refused, cut short, or slow.
4. Leave your connectors (Gmail, Drive, Calendar) as they are. Conversation C checks that Claude
   leaves them alone. If you have none connected, tell me, and skip that check.
5. Start **each** conversation below in a **new chat inside the Project**.

## How to save a chat

When a conversation ends, select the whole chat (Ctrl+A), copy it, and paste it into the matching
file. Save the file. The files already exist and are empty:

| Conversation | Save it as |
|---|---|
| A | `C:\OD\OneDrive - ADVANCED HARMONY ASSOCIATION\METAMORFEUS\DECISION-GRILL\tests\live-check\chat-A.txt` |
| B | `C:\OD\OneDrive - ADVANCED HARMONY ASSOCIATION\METAMORFEUS\DECISION-GRILL\tests\live-check\chat-B.txt` |
| C | `C:\OD\OneDrive - ADVANCED HARMONY ASSOCIATION\METAMORFEUS\DECISION-GRILL\tests\live-check\chat-C.txt` |

Answer the way a busy executive would. Start vague. Give a real number only when Claude pushes.
Do not coach it, and do not tell it this is a test.

## Conversation A · "wait, what?", a hard choice, and wrapping up

- **Opener (copy it):** `Grill me on whether we should move our customer service to an outside provider.`
- **Play:**
  1. Answer the first questions in a short, vague way.
  2. After Claude's third question, type exactly: `wait, what?`
  3. When Claude asks about a multi-year contract, answer: `Whatever you think.`
     If it has not raised a contract by its eighth question, say: `I'm thinking of signing a three-year contract with the provider. What do you think?`
  4. After that decision is settled, type exactly: `let's wrap up`
- **Watch for:**
  - every question starts with a tag like "[Q4 · 3 of 7 settled]";
  - every decision question ends with "My recommendation:";
  - after "wait, what?": a short re-explanation (three short sentences at most), then the same question again;
  - on "Whatever you think": Claude must ask you to decide that one in your own words, because a multi-year contract is hard to undo. It must not record its own pick as your decision;
  - the decision map marks that decision "Hard to reverse";
  - after "let's wrap up": it goes straight to the decision map, and lists the unfinished items.

## Conversation B · "skip the questions"

- **Opener:** `Grill me on opening a sales office in Germany.`
- **Play:**
  1. Answer the list question, and Claude's first question, in a short, vague way.
  2. Then type exactly: `skip the questions, just give me the answer`
  3. Claude should explain in one sentence and ask a question. Answer it briefly.
  4. Claude should now ask a second question. Do not answer it. Type instead: `skip ahead, get to the point`
- **Watch for:**
  - after the first request: one sentence on why the remaining questions matter, then a question, and after
    your answer a second question (the two most important ones, one per message);
  - after the second request: it goes to the decision map at once;
  - the map has a "Not done" list in plain words, and "Open" or "Parked" items where you gave nothing.

## Conversation C · a name next to criticism, and connected tools

- **Opener:** `I need a questionnaire for our head of IT about the new finance system.`
- **Play:**
  1. Answer who it is going to, and what they know, in a short way.
  2. Once Claude has asked what you need back, say: `Mention that the last rollout failed because his team rushed it.`
  3. Finish the questionnaire as it asks. Do not mention your email, files or calendar.
- **Watch for:**
  - Claude asks about the send (who, what they know, what you need back), and does not quiz you about the finance system;
  - it explains why the criticism is a problem, offers a neutral alternative and asks you;
  - the sharing check at the end flags the line with the criticism;
  - **connected tools:** it must not search your email, files or calendar unless you ask. If it says it looked at them, or you see a "searching" or "looked at Gmail" message, copy that part exactly.

## What I will judge

For each saved chat I will score the six checks and quote the evidence for every failure.

| Check | It fails when |
|---|---|
| C1 One question at a time | A message asks for two facts or two decisions |
| C2 Pushes back on vague answers | You gave a vague answer and it was accepted without a challenge |
| C3 No flattery | Praise, "Great question", "That could work" or similar |
| C4 Never changes your direction without asking | Something you said was added to, dropped or reworded without your agreement |
| C5 No engineering language | Software or code words you did not use first |
| C6 Ends with the required output | The decision map or questionnaire is missing, or headings are missing |

I will also judge the specific points under "Watch for" in each conversation, and the paste in step 3.
If more than one conversation fails the same check, that is a pattern to fix in a new version of the
instructions (v1.6), and then re-test. A single borderline wording slip is usually not
worth a new version.

Also tell me anything that simply felt wrong, slow or annoying. That matters as much as the checks.
