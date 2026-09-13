# Productization Memo Template

Fill-in-the-blank template for Module 5 of the FDE-PM Field Manual (`../fde-pm-field-manual.md`). This is the gate document that turns "three clients asked for the same thing" into a funded, deprecation-planned capability — or into a documented decline. One page of evidence beats ten pages of narrative: executives fund the memo that shows the ledger rows, the numbers, and the migration plan.

**Pattern ID:** [P-NNN] · **Author:** [PM] · **Date:** [YYYY-MM-DD] · **Decision requested from:** [WHO] · **By:** [DATE]

---

## 1. The pattern

[WHAT RECURS, IN PLAIN LANGUAGE. Then the ledger evidence.]

| Instance | Client | Build date | Effort (eng-days) | What was identical | What was client-specific |
|---|---|---|---|---|---|
| 1 | [ ] | [ ] | [ ] | [ ] | [ ] |
| 2 | [ ] | [ ] | [ ] | [ ] | [ ] |
| 3 | [ ] | [ ] | [ ] | [ ] | [ ] |

**Overlap estimate:** ~[__]% of each bespoke build was the same work.

## 2. Signal test

| Test | Evidence | Verdict |
|---|---|---|
| Frequency (≥3 instances) | [ ] | [pass/fail] |
| Cost (bespoke is expensive to repeat) | [ ] | [pass/fail] |
| Willingness to pay for a configured version | [ ] | [pass/fail] |
| Differentiation (close to core, defensible) | [ ] | [pass/fail] |

*If any test fails, the memo's recommendation is a documented decline — see section 9.*

## 3. The product, precisely

- **Core (built once, maintained by the platform team):** [components, interfaces, what a new client gets out of the box]
- **Configurable axes (per-client without code):** [corpus sources · taxonomy · thresholds · destinations · entitlements · branding]
- **Stays bespoke (and why):** [the genuinely client-specific part, with the reason it is not configurable]
- **What we would delete from the bespoke versions:** [file/module/component count, maintenance items, duplication]
- **Enterprise-ready gaps to close before it is sellable:** [security review items · evals · docs · support tier · packaging]

## 4. The market and the packaging

| Question | Answer |
|---|---|
| Who buys it | [roles, industries, size] |
| How it is packaged | [feature of an existing product · add-on module · separate SKU · included in enterprise tier] |
| Price point and unit | [per site · per seat · per resolution · platform fee] |
| Pricing model and rationale | [outcome · seat · usage · platform-fee + overage — and why, tied to what the client can verify and to the displaced-cost baseline from the ROI model] |
| What the existing clients get | [migration, maintenance, roadmap influence — be specific, this is the consent conversation] |
| What they keep | [their configuration, their data, their differentiation] |

## 5. Migration and deprecation

This section is what makes productization real. Without it, the bespoke path survives and you maintain two systems per pattern.

| Step | Detail | Owner | Date |
|---|---|---|---|
| Migration path for each existing bespoke instance | [ ] | [ ] | [ ] |
| Freeze date for the bespoke branch | [ ] | [ ] | [ ] |
| Removal date for the bespoke branch | [ ] | [ ] | [ ] |
| Client communication and consent | [ ] | [ ] | [ ] |
| Support model during migration | [ ] | [ ] | [ ] |

## 6. Cost, return, and margin effect

| Line | Value | Basis |
|---|---|---|
| Build cost (platform team) | [ ] | [estimate range + confidence] |
| Run-rate (maintenance, eval, support) | [ ] / month | [ ] |
| Expected reuse-rate effect | [+__ points] | [ ] |
| Expected time-to-first-deploy effect | [−__ days] | [ ] |
| Support-load effect per client | [−__ hours/month] | [ ] |
| Margin effect at 3 / 6 / 12 adopters | [ ] | [ ] |

## 7. Risks

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Client A considers the capability their competitive differentiation and objects | [ ] | [ ] | [ ] |
| Commercial exposure: the core encodes one client's specifics | [ ] | [ ] | [ ] |
| Platform team capacity does not materialise | [ ] | [ ] | [ ] |
| A competitor copies the capability | [ ] | [ ] | [ ] |
| Migration reveals hidden per-client dependencies | [ ] | [ ] | [ ] |

## 8. Decision requested

> [BUILD NOW · BUILD NEXT QUARTER · DECLINE] — with the reasoning in two sentences, and the consequence of each alternative.

## 9. If we decline

- **What we tell the clients:** [LANGUAGE FOR THE CONVERSATION]
- **What we do instead:** [BESPOKE, PRICED AND SEQUENCED · THIRD-PARTY COMPONENT · NOTHING, WITH THE TRADE-OFF STATED]
- **When we would revisit:** [THE LEDGER CONDITION THAT WOULD CHANGE THE ANSWER]

---

## Done when

- [ ] Ledger rows are cited as evidence for every claim of recurrence
- [ ] All four signal tests have explicit verdicts with evidence
- [ ] The configurable axes are named — the abstraction is concrete, not aspirational
- [ ] Migration *and deprecation* are scheduled with owners and dates
- [ ] Margin effect is shown at more than one adoption level
- [ ] Client consent is addressed in writing, not implied
- [ ] A decision is explicitly requested from a named person by a named date
- [ ] The decline path exists too — so a "no" is as documented as a "yes"
