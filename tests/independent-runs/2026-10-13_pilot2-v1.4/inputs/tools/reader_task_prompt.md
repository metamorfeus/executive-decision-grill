# Task: score four conversations

Start at once. Do not ask me questions and do not wait for approval. When you have finished, create
`DONE.txt` in this folder containing one line: `done`.

You work only in this folder. Read only the files in it. Do not look for other files on the computer.
You are one of two independent readers. You do not know the other reader and you must not try to
find out anything about how the conversations were made.

## What you have

- `sheet.md`: four conversations, lettered A to D. Each is a chat between a business leader (the
  "user") and an AI assistant, followed by a list of **items to watch for** and some **automatic
  checks**.
- `rules.md`: the written standing instructions the assistant was given. Read it fully. It is your
  yardstick.
- `rubric.md`: six general checks to score on every conversation.
- `validate_scores.py`: a script that checks your scores file has the right shape. It prints counts only.

You do not know who or what produced the assistant's messages, which version of the instructions was
used, or what happened in any earlier test. Do not guess. If anything in the sheet hints at that,
write it in `record.md` under the heading "Leaks".

## One more thing about stopped conversations

A conversation may end with the line `[The conversation stopped here.]` before the assistant has reached its end. That is not the assistant's failure. For any item about a moment the conversation never reached, mark `not_tested` and say so. Do not mark an item `not_met` because the conversation was cut off. Judge everything that was said before the stop in the normal way.

## What to do

1. Read `rules.md`, then `rubric.md`.
2. For every conversation (A to D), read the whole conversation, then:
   - Mark **every** item in its list: `met`, `not_met` or `not_tested` (use `not_tested` only when the
     conversation never reached the moment the item is about, and say why). For `met` and `not_met`
     give the turn number and the **exact words** (at most 25 words) that show it. Give one line of
     reason for every item.
   - Score the six checks in `rubric.md`: `pass` or `fail`, with the same evidence rule.
   - Note up to five **other** rule breaks that the list does not cover, each with turn, exact words,
     the rule number, and one line of reason.
3. The automatic checks list "suspects". They are only leads. Look at each one in the conversation and
   decide for yourself. They may be wrong, and a conversation can break a rule that no check found.
4. **Be strict.** When you are unsure between two verdicts, choose the stricter one. Judge only what
   is in the conversation; do not give credit for intentions. Quote, do not paraphrase. A reaction
   that is too long, an invented figure, or a decision recorded as the user's that the user did not
   make are real failures, not style points.
5. Do not rank the conversations against each other. Score each alone.

## Files to write (in this folder)

1. `scores.json`: valid JSON in exactly this shape:

```
{
  "reader": "<the name of this folder>",
  "items": [ {"sheet": "A", "item": "W1", "verdict": "met", "turn": 4, "quote": "...", "reason": "..."} ],
  "checks": [ {"sheet": "A", "check": "one-question-at-a-time", "verdict": "pass", "turn": null, "quote": "", "reason": "..."} ],
  "other": [ {"sheet": "A", "rule": "Rule 2", "turn": 7, "quote": "...", "reason": "..."} ]
}
```

   Every item of every conversation must appear once in `items`, and all six checks once per
   conversation in `checks`. Use the `check` names exactly as they appear in `rubric.md`.
2. `record.md`: for each conversation a short paragraph (what happened, in plain words), then the
   "Leaks" heading (or "none"), then anything you were unsure about and how you decided.

Run `python validate_scores.py` and fix `scores.json` until it prints `OVERALL: PASS`.
