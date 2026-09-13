# Discovery RFC Template — Client AI Engagement

Fill-in-the-blank template for Module 2 of the FDE-PM Field Manual (`../fde-pm-field-manual.md`). The RFC is the **internal** document that lets the FDE lead, the account team, and the PM disagree cheaply — before anything is promised to the client. It is written before the feasibility memo, and the feasibility memo before the price.

**Engagement:** [CLIENT — ENGAGEMENT NAME] · **RFP/RFC author:** [PM] · **Date:** [YYYY-MM-DD] · **Version:** [V0.1 — DRAFT]

---

## 1. Problem statement (with numbers)

One paragraph a CFO would accept as fact. No adjectives that cannot be checked.

> [THE PROBLEM], costing [CLIENT] approximately [N UNITS — HOURS, DOLLARS, ERRORS, DAYS] per [PERIOD], owned by [NAMED PERSON / ROLE]. Source: [SYSTEM EXPORT / TIME-AND-MOTION / INTERVIEW — WITH DATE].

- **The ask as stated by the client:** [VERBATIM OR CLOSE PARAPHRASE]
- **The problem behind the ask:** [WHAT YOU BELIEVE IS ACTUALLY WRONG, AND WHY]
- **Baseline metrics:** volume [__] · cycle time [__] · error/defect rate [__] · cost per unit [__] · headcount-equivalent [__]

## 2. Who is affected — and who loses

| Person / role | How their work changes | Displaced judgment, status, or headcount narrative | Their likely stance |
|---|---|---|---|
| [ROLE — e.g. desk lead] | [CHANGE] | [WHAT THEY LOSE OR GAIN] | [CHAMPION / NEUTRAL / BLOCKER] |
| [ROLE] | [CHANGE] | [ ] | [ ] |

## 3. Evidence log

| Evidence | Type | Source | Date | What it shows |
|---|---|---|---|---|
| [QUOTE / NUMBER / OBSERVATION] | [interview · system export · observation · document] | [WHO/WHAT] | [DATE] | [INTERPRETATION] |

Rules: quotes are verbatim; numbers carry a source and a date; interpretations are labelled as interpretations.

## 4. Current state (the real process, including workarounds)

[STEP-BY-STEP AS IT ACTUALLY HAPPENS, including the spreadsheet, the WhatsApp group, the printer, the phone call. Note the cycle time of each step and where records are re-keyed.]

- **Documented process vs. actual process — the divergence:** [WHERE THEY DIFFER AND WHY IT MATTERS]
- **Existing workarounds we must not break:** [LIST]

## 5. Constraints

| Constraint | Detail | Source / owner | Does it eliminate any option? |
|---|---|---|---|
| Data access | [ ] | [ ] | [ ] |
| Residency / sovereignty | [ ] | [ ] | [ ] |
| Security / compliance | [ ] | [ ] | [ ] |
| Latency / availability | [ ] | [ ] | [ ] |
| Budget / commercial | [ ] | [ ] | [ ] |
| Client change calendar | [ ] | [ ] | [ ] |
| Politics / works council / union | [ ] | [ ] | [ ] |

## 6. Instrument analysis (Module 2 decision matrix)

Fill with the **client's** numbers, and always include the deterministic baseline and a retrieval-only option.

| Instrument | Verdict | Reasoning (with the client number that decides it) |
|---|---|---|
| Deterministic rules / workflow | [yes · partial · no] | [ ] |
| Classic ML | [ ] | [ ] |
| Retrieval / search only | [ ] | [ ] |
| RAG (retrieval + generation with citations) | [ ] | [ ] |
| Fine-tune / distill | [ ] | [ ] |
| Prompt optimization only | [ ] | [ ] |
| Agentic tool use | [ ] | [ ] |
| Human-in-the-loop | [ ] | [ ] |
| Process change | [ ] | [ ] |

**Deterministic baseline:** if we did this with rules alone we would achieve [__], which is [sufficient / not sufficient] because [__].

## 7. Proposed path — and why not the others

[THE RECOMMENDATION IN TWO PARAGRAPHS. Name the increments: what ships first, what is deliberately deferred, what is explicitly out.]

**Open technical questions and how we resolve them:** [NAMED SPIKE, DURATION, THE QUESTION IT ANSWERS]

## 8. What would make us say no

The falsifiable conditions. Writing these is what makes the RFC honest.

- If [CONDITION — e.g. the client cannot grant read-only access to the corpus before week 3], then we [RESTRICT SCOPE TO X / DECLINE].
- If [CONDITION], then [RESPONSE].
- If [CONDITION], then [RESPONSE].

## 9. Open questions, owners, dates

| Question | Owner | Needed by | Consequence if unanswered |
|---|---|---|---|
| [ ] | [NAME] | [DATE] | [ ] |

*A blank is not acceptable. "Unknown" is acceptable, with an owner.*

## 10. Effort range and confidence

| Phase | Low | High | Basis of estimate | Confidence |
|---|---|---|---|---|
| Discovery & data readiness | [ ] | [ ] | [ ] | [HIGH/MED/LOW] |
| Build (increment 1) | [ ] | [ ] | [ ] | [ ] |
| Evals & acceptance | [ ] | [ ] | [ ] | [ ] |
| Deployment & security work | [ ] | [ ] | [ ] | [ ] |
| **Run-rate after go-live (monthly)** | [ ] | [ ] | [ ] | [ ] |

## 11. Recommendation and decision requested

> [BUILD THIS INCREMENT / RUN A SPIKE FIRST / DECLINE WITH THE FOLLOWING ALTERNATIVE]

**Decision requested from:** [WHO] · **By:** [DATE]

---

## Done when

- [ ] The problem statement contains a number, a named owner, and a sourced baseline
- [ ] "Who loses" is answered honestly, with a candidate champion named
- [ ] The current state includes the workarounds, not just the documented process
- [ ] The matrix includes a deterministic baseline and a retrieval-only option
- [ ] The "what would make us say no" section contains at least one falsifiable condition
- [ ] Every open question has an owner and a date
- [ ] A run-rate estimate exists alongside the build estimate
- [ ] A decision is explicitly requested from a named person by a named date
