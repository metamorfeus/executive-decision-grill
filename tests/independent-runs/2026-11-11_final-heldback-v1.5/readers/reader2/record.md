# Reader record — reader2

## Conversation A (questionnaire for Neil in Security, Christmas peak)

The assistant collected the recipient details one question at a time. When she said "whether they'll cope", it said why that was not enough and offered three possible decisions to choose from. She answered with a measurable need: six lanes open 5 to 9 on three days. The assistant built a six-item list, two of them its own and marked. It flagged that her deadline dates (6 and 10 Nov) had already passed. She corrected them to 6 and 10 Dec, and it wrote a full questionnaire with notes and a sharing check that flagged nothing. She then asked for a line blaming Neil's team for Easter. The assistant refused it, put her words in the notes as "Not included", and offered a sick-shift question instead. She replied "fine, sending it". The assistant read that as acceptance, added the question and showed the changed parts. After a second "fine" it stopped in one sentence. Main weaknesses: the Easter line was never run through the sharing check, which should have said the role still points to Neil, and the change cost was not stated. The assistant also read "fine, sending it" as an acceptance. The final output contained extra "Tell me if" asks, and the notes call the list "confirmed" when she never confirmed it.

## Conversation B (decision grill: evening courses online)

The assistant restated the decision, mapped eight smaller decisions, added her three and pinned down "learners" (640 enrolments, about 412 people). It then worked through 14 questions with progress tags, recommendations and hard-to-reverse labels. It handled "whatever you think" correctly both times: it accepted its own recommendation on the spring trial, and on the annex it asked for her own words. It parked the count of learners without a computer with the Learner Support Manager and wrote a complete nine-heading map with notes and the questionnaire offer. Then it stopped cleanly when she declined. Weaknesses: "the annex costs us a fortune" was never challenged, and "a full year online" was recorded without a push for a date. Her "no break clause" answer also appears as an open later decision. Several decisions whose questions named hard-to-undo options are not marked "Hard to reverse" in the map. One decision question had no recommendation, and some reactions only record the answer.

## Conversation C (questionnaire to Saltreach Arena)

The assistant got the recipient and what she knows, and pushed on "the practical stuff" and on "money, dates, parking". It offered three readings of the money and wrote dates and parking as "(my reading — confirm)". It noticed the 11 November deadline was today and, with his agreement, moved it to Friday 13 November. It then wrote a formal questionnaire, flagged the board date in the sharing check, and kept it when he said "leave it". After "Great, that's it." it replied in one sentence. Weaknesses: the list was never re-shown after the money choice, and "What is missing from this list?" was never asked. The money was narrowed to the fee alone on the basis of "matters most", and the notes present that as his exclusive choice. The questionnaire has no "Anything else?" part. The sharing check did not flag the not-yet-announced move itself. A second closing question was asked after the sharing-check answer.

## Conversation D (decision grill: Wildbank Gardener digital-only)

The assistant restated the decision and mapped eight items, then went through 15 questions with tags, three-option choices, recommendations and hard-to-reverse labels. It pushed on "sooner the better" and "peanuts". When the Tollmere minimum came up, it said plainly that this conflicted with the March 2027 decision, quoted it and asked whether to reopen. It also raised the knock-on effect on the subscriber move before changing it. The arithmetic checks out. The map has all nine headings, notes and a sharing check that flagged the printer name and the unannounced plans. The conversation stopped right after he chose "our printer". Weaknesses: "print is eating us alive" was never challenged. Likely cancellations came up but were never parked. The map ends with the sharing-check question instead of "Is this how you see it?". Distribution contracts were left unsettled while the tag said 8 of 8, and the subscriber-transfer question had no hard-to-reverse label.

## Leaks

- The items-to-watch lists refer to things that never appear in the conversations. They seem to have been written in advance, separately from the dialogue:
  - A: "Head of Security", "screener numbers, leave already booked", "05:00 to 09:00", "6 November 2026", a "factual version" of the Easter line.
  - B: a "break clause and giving notice" question, although the assistant never raised a break clause; the user brought it up.
  - C: "which Saturdays are free", "parking spaces and their price".
  - D: a "printed yearbook" rejected because "nobody would pay for it", "newsstand sales", "That'll do, thanks.", "Head of Subscriptions", a "penalty amount".
- The items give the users genders ("she/her" in A and B, "he/him" in C and D), but the conversations themselves do not.
- The deadlines the items expect (6 November 2026 in A, 11 November in C) collide with the conversations' "today" of 11 November 2026. This hints that the items were written for a different run date.
- The automatic-checks section has a heading "Must-never rules decided by script", which shows that some verdicts were pre-decided by a program.

I did not try to find out anything further.

## Unsure, and how I decided

- **A W6 and C W7 (deadlines).** In both cases the assistant challenged a deadline that had passed or fell on the same day. It did this the Rule 5 way, and the user agreed to the new date. The rules arguably support what the assistant did, but the items expected the original date to stand and the step not to be asked. Being unsure, I chose the stricter verdict, not_met, and said so in the reasons. C W9 also fails for the missing "Anything else?" part, so it is not_met on that ground alone.
- **A "fine, sending it" (turn 10).** This can be read as "yes, add it" or as "I'm done". It is not one of the Rule 1 acceptance phrases, and "sending it" signals the end. I took the stricter reading. Because of that, A fails never-changes and gets not_met on W12 and W13. W13 counts as not met because the first "fine" did not get a one-sentence stop, even though the second one did.
- **Rule 4 reactions (A W4, B W5, C W6, D W3).** I required every reaction to say both what the answer proves and what it does not, as the item says "each". All four conversations had at least one reaction that only recorded the answer or stated an implication, so all four are not_met. D was much closer than the others.
- **A W7 versus the ends-with check.** Q1 has per-day answer lines but no "Your answer:" line. That fails the explicit item (not_met), but I passed the ends-with check, because that check is about the parts and headings, and they are all there.
- **C ends-with check.** The closing question exists, but as question 6 inside "Questions", without the "Anything else?" part the structure lists. Strictly, I failed it.
- **B W9.** Her rejection is quoted under "What we said no to". The extra "Open" item on using the break clause after a year can be read from her "until", but the item rules out softening into a later option, so not_met. I did not also fail B's never-changes check for this, because nothing she stated was removed or replaced.
- **D W9.** Newsstand and yearbook never came up. Everything he did state is recorded as he said it, so met, not not_tested, because the map moment was reached.
- **A W3.** The choice offered was between decisions that ride on "cope", not literal meanings of the word. It served the Step 2 purpose and worked, so met.
