# FDE Hiring Scorecard Template

Fill-in-the-blank template for Module 5 of the FDE-PM Field Manual (`../fde-pm-field-manual.md`). The biggest lever on the flywheel is who you hire into it — and the cost of hiring wrong is a team that ships demos instead of systems, or ships systems and writes down nothing. Score every candidate on all seven dimensions **with evidence**, not impressions.

**Candidate:** [NAME] · **Role:** [FORWARD DEPLOYED ENGINEER / FDE LEAD / PLATFORM] · **Panel:** [PM, FDE LEAD, +1] · **Date:** [YYYY-MM-DD]

---

## 1. Scorecard

| Dimension | Score (1–4) | Evidence (what they said or did, verbatim or from an exercise) |
|---|---|---|
| Domain immersion | [ ] | [ ] |
| Data detective instinct | [ ] | [ ] |
| Boring-glue pragmatism | [ ] | [ ] |
| Client-room communication | [ ] | [ ] |
| Ownership past handoff | [ ] | [ ] |
| Harvest instinct | [ ] | [ ] |
| Judgment under pressure | [ ] | [ ] |

**Scale anchor:** 4 = I would bet a client on this, from direct evidence · 3 = solid evidence, minor gaps · 2 = plausible but unproven · 1 = no evidence or counter-evidence.

## 2. Signal questions (bank — pick 4–5 per interview; ask for stories, not opinions)

- Domain immersion: *"Tell me about a time you learned an unfamiliar domain under a deadline — what did you read, who did you shadow, what did you get wrong?"*
- Data detective: *"Tell me about a case where the data was wrong and the system was right. How did you find it?"*
- Boring-glue: *"What's the most boring thing you've built that mattered, and how long did you maintain it?"*
- Client room: *"Describe a time you told a client no, and what you said."*
- Ownership: *"Tell me about a system you owned after launch — what broke at 2am and what did you learn?"*
- Harvest: *"When did you notice you were building the same thing a second time, and what did you do about it?"*
- Judgment: *"Walk me through the hardest production incident you handled alone, and the call you made with incomplete information."*
- Ambiguity: *"Tell me about a project where the requirements turned out to be wrong. When did you realize, and what did you do?"*

## 3. Working exercises

**The data dig (20–30 min).** Provide a small messy dataset (raw export, duplicated records, one bad join) and one real question. Record:

- [ ] Explored the data before proposing a solution
- [ ] Named the quality problems unprompted
- [ ] Wrote the boring pipeline (clean → join → answer), not just the clever part
- [ ] Asked a clarifying question that showed they understood the *business* behind the data

**The client roleplay (10–15 min).** A stakeholder asks for something that does not need AI and is out of scope. Record:

- [ ] Diagnosed before proposing (asked "what's the problem behind this?")
- [ ] Said no (or "not yet") with a price and an alternative, rather than vague agreement
- [ ] Left the stakeholder feeling heard and respected

## 4. Reject signals (any one → decline, documented)

- [ ] Asks who owns the roadmap before who owns the client
- [ ] Cannot name a boring thing they built that mattered
- [ ] Blames the client for a failed deployment
- [ ] Cites only greenfield or personal projects
- [ ] Cannot explain a technical trade-off in plain words
- [ ] "I don't do support / on-call."

## 5. Decision

| Item | Answer |
|---|---|
| Recommendation | [HIRE / NO-HIRE / HOLD — compare against one more] |
| Deciding dimension | [THE ONE DIMENSION THAT SETTLED IT] |
| Red flags (if any, and why they were not disqualifying) | [ ] |
| Calibration note | [WHAT WE EXPECT TO SEE IN 90 DAYS — becomes the check in the 30/60/90 plan] |
| Signed (panel) | [NAMES] |

**Calibration discipline:** every hire gets a 90-day check against their scores. If a dimension repeatedly over- or under-predicts performance, re-weight it — the scorecard is an instrument, not a ritual. Record the calibration outcome on the next page of `templates/30-60-90.md`.

---

## Done when

- [ ] All seven dimensions scored with evidence, not impressions
- [ ] At least one working exercise was run (data dig or roleplay)
- [ ] Every reject signal checked; any hit is documented
- [ ] The decision names the single deciding dimension
- [ ] A 90-day calibration expectation is written down
