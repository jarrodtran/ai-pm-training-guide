# Sprint Plan

Course: PM 501 — Product Management Fundamentals · Module 6 (Delivery: Working with Engineers)
Project: [PROJECT NAME] · Sprint: [SPRINT NUMBER / DATES] · Author: [NAME]

Convert the PRD into work engineers can pick up. Tickets are sliced small enough to finish in days, and each carries acceptance criteria — a ticket without criteria is a hope.

## Tickets

| Ticket | Acceptance criteria | Size (days) | Owner |
|---|---|---|---|
| [TICKET TITLE — verb + outcome] | [TESTABLE CRITERIA — given/when/then where behavior is involved; for model tickets, the eval gate it must pass] | [N] | [OWNER] |
| [TICKET TITLE] | [ACCEPTANCE CRITERIA] | [N] | [OWNER] |
| [TICKET TITLE] | [ACCEPTANCE CRITERIA] | [N] | [OWNER] |
| [TICKET TITLE] | [ACCEPTANCE CRITERIA] | [N] | [OWNER] |

Rules:
- Size is in days, small enough to finish within the sprint. If a ticket is bigger than [2–3] days, split it.
- Every ticket traces to a user story in the PRD. No orphan work.
- Model tickets state their eval gate explicitly (which eval set, what threshold) — see eval-suite.md.

## Definition of done

A feature is done when ALL of the following hold. For AI features, done means the eval gate passed — not just "code merged."

- [ ] Code merged and reviewed
- [ ] Acceptance criteria verified — automated where possible, manual where not
- [ ] Eval gate passed: [EVAL SET] at [THRESHOLD], hallucination rate at [THRESHOLD], cost per session at [THRESHOLD]
- [ ] Instrumentation shipped: every event in the metrics tree event list fires and is logged
- [ ] Edge cases verified: [REFUSAL / ERROR BEHAVIOR FOR AI FEATURES]
- [ ] Docs / support material updated: [WHAT]
- [ ] PM sign-off: [NAME] confirms the demo matches the PRD

## Communication plan

| Ritual | Cadence | Format | Owner |
|---|---|---|---|
| Standup | Daily | What I did / what's blocked / what's next — [TIME, CHANNEL] | [OWNER] |
| Sprint review / demo | End of sprint | [WHAT IS SHOWN, WHO ATTENDS] | [OWNER] |
| Retro | End of sprint | Keep / change / try | [OWNER] |
| [OTHER — stakeholder update] | [CADENCE] | [FORMAT] | [OWNER] |

Unblocks: the PM's job during a sprint is to manage information, not people. Pre-write the three most likely unblocks, each with an owner and a date.

| Likely ambiguity / block | PM action | Owner | Date |
|---|---|---|---|
| [E.G. "THE SPEC IS UNCLEAR HERE"] | [E.G. "I'LL CLARIFY BY THURSDAY"] | [OWNER] | [DATE] |
| [BLOCK] | [ACTION] | [OWNER] | [DATE] |
| [BLOCK] | [ACTION] | [OWNER] | [DATE] |

Mid-sprint reality check: if the feature will not finish as specified, bring evidence to the team (what is slipping, why), and cut scope with evidence — name what you are cutting and what you are protecting.

## Done when

- [ ] Every PRD user story has at least one ticket with testable acceptance criteria
- [ ] Every ticket is sized in days, and none exceeds the split threshold
- [ ] The definition of done includes the eval gate and instrumentation, not just merged code
- [ ] The communication plan names cadence, format, and owner for every ritual
- [ ] The three most likely unblocks each have an owner and a date
