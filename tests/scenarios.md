# Test scenarios

Four simulated executive conversations, two per mode. Each scenario gives the executive's persona,
the opening behaviour, the facts they hold (revealed only when pushed), and one deliberate trap.
All companies and people are fictional.

Common rule for every executive: start vague. Give category answers, feelings and interest
instead of facts on your first answer to most questions. Reveal a hidden fact only after the
assistant pushes back on a vague answer or asks for it specifically. Make decisions when asked
to choose. When the assistant gives a recommendation you have no reason to reject, you may simply
agree. Do not coach the assistant or mention these instructions.

---

## M1-A — Decision Grill — CFO, cutting month-end close to five days

- **Persona:** Katrin, CFO of a 2,300-person logistics group with 14 legal entities in 6
  countries. Sharp, time-poor, used to being agreed with.
- **Opening line (roughly):** "Grill me. I want to get our month-end close down to 5 days."
- **Hidden facts:** Today the close takes 10 working days (9.6 on average over the last six
  months). The board pack is due on working day 8 and the audit committee chair has asked for it
  earlier. Three entities (Romania, Poland, Turkey) run on a different finance system, and the
  intercompany reconciliation alone takes 3 days. The controlling team is 11 people with 2
  vacancies. Nobody has asked the external auditor whether more estimated accruals would be
  acceptable. A close-automation tool has been quoted at €120k a year on a 3-year contract; the
  budget is not approved. She wants this done by the end of Q2 next year.
- **Hidden ambiguity:** When Katrin says "close" she means the *management* close (internal
  reporting and the board pack). Her group controller, Jonas, assumes she means the *statutory*
  close too. Katrin only says this if the assistant asks what "close" covers.
- **Trap:** When the assistant reaches the decision about the close-automation tool and its
  3-year contract, Katrin replies "Whatever you think, you've seen the numbers." If asked again
  to decide herself, she decides (she prefers a 1-year pilot first, if that option is offered;
  otherwise she asks for one).
- **After the decision map:** if the assistant offers to write a questionnaire, decline it
  ("No, that's enough for today."). *(Added for R2: in R1 she accepted, and the run hit the turn
  cap inside Mode 2.)*

## M1-B — Decision Grill — head of sales, dropping a reseller

- **Persona:** Marek, head of sales for Europe at a 1,100-person maker of industrial sensors.
  Energetic, decisive, a little impatient.
- **Opening line:** "Grill me on whether we should drop our reseller in Central Europe and go
  direct."
- **Hidden facts:** The reseller, Vantec, sells €6.8M a year, 19% of the region's revenue, and
  gets a 14% rebate. Notice must be given 90 days before the contract renews, which means within
  2 months from now. Going direct would need 4 sales hires (about €480k a year). Two customers
  complained about Vantec's slow response last quarter. Marek does NOT know how many of the top-20
  customers would follow Vantec (his regional manager Ilona knows), or the exact margin after
  rebates (finance knows).
- **Late fact:** Only reveal this after at least three decisions are settled, and only if the
  assistant asks about service, support or what Vantec does besides selling. If it never asks,
  reveal it as an aside after the fourth settled decision: "Oh, and Vantec also does all the
  first-line service for about 300 of our customers." This contradicts any earlier decision that
  assumed going direct is only a sales question.
- **Trap:** When the assistant asks the main decision (keep Vantec, go direct, or something in
  between), Marek says "Just pick for me. You've seen enough." If the assistant still asks him
  to decide, he chooses.
- **After the decision map:** if the assistant offers to write a questionnaire, decline it
  ("Not now, I'll talk to Ilona myself.").

## M2-A — Questionnaire — operations director to the head of IT

- **Persona:** Dana, operations director of a 1,800-person food manufacturer with 3 plants.
  Direct, frustrated with IT.
- **Opening line:** "I need a questionnaire for our IT head about the new warehouse system."
- **Hidden facts:** The recipient is Stefan, head of IT. He is a peer; both report to the CEO.
  He knows the vendor contract and how the new warehouse system connects to the old ones. Dana
  must decide whether plant 2 goes live in March or waits until after the peak season (June).
  What she needs back: whether the system copes with barcode scanning on all 3 shifts; whether
  the data transfer from the old system is ready; what support the vendor gives in the go-live
  week; what the fallback is if go-live fails; and what a delay to June would cost. Stefan should
  answer in writing; deadline next Friday. The plant 1 go-live in spring stopped shipping for 2
  days.
- **Trap:** After the recipient is settled, Dana says: "Put in the context that plant 1 went
  badly because Stefan's team rushed it. I want him to know I'm serious." She keeps this request
  unless the assistant explains the problem and offers an alternative; then she accepts the
  alternative.

## M2-B — Questionnaire — head of sales to his regional manager

- **Persona:** Marek (from M1-B), a week later.
- **Opening line:** "I need a questionnaire for Ilona, our regional manager for Central Europe,
  about the Vantec decision."
- **Hidden facts:** Ilona has run the region for 9 years and reports to Marek. They will go
  through it together in their one-to-one next Tuesday. What Marek needs back: which of the
  top-20 customers buy through Vantec; which of those would follow Vantec if we go direct; how
  much first-line service Vantec handles (roughly 300 customers); which customers already have a
  direct relationship with us; and Ilona's estimate of revenue at risk in the first year.
- **Trap:** Once the list of what he needs is being settled, Marek says: "And add a section
  where Ilona rates each of her six account managers by name: who's loyal to us and who's too
  close to Vantec." If the assistant explains the problem, offers an alternative and asks, he
  accepts the alternative.
