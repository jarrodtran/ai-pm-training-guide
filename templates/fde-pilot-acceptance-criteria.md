# Pilot Acceptance Criteria Template

Fill-in-the-blank template for Module 4 of the FDE-PM Field Manual (`../fde-pm-field-manual.md`). This document defines "done" in measurable terms **before the first demo**. A demo can always be arranged to look good; a pre-agreed bar, on a client-authored test set, cannot be moved afterwards. Two disciplines make it work: thresholds are proposed by your side and **agreed** by the client's, and every threshold names its measurement method.

**Engagement:** [CLIENT — ENGAGEMENT] · **Version:** [V1.0] · **Agreed on:** [DATE — BEFORE ANY DEMO] · **Proposed by:** [PM] · **Accepted by:** [CLIENT SPONSOR NAME + ROLE], [INTERNAL OWNER NAME]

---

## 1. Business outcome (the one number)

> [BUSINESS THRESHOLD, WITH BASELINE, TARGET, MEASUREMENT SOURCE, COHORT, AND DATE.]
> Example: *"Median handling time for policy questions falls from 11 to ≤ 12 minutes for the trained cohort (n ≥ 400 assisted calls) by 2026-12-01, measured from ticket timestamps in [system]."*

| Item | Value |
|---|---|
| Baseline (value, source, date) | [ ] |
| Target | [ ] |
| Measurement source | [ ] |
| Cohort / sample requirement | [ ] |
| Measurement window | [ ] |
| Who computes it | [ ] |

## 2. Quality thresholds (on the client-authored golden set)

| Slice | Threshold | Scorer | Notes |
|---|---|---|---|
| Overall | ≥ [__]% | [deterministic checks · LLM-judge with calibration sample of __% · human review] | Golden set: [N] cases, version [__], authored by [client role + us] |
| Adversarial / injection slice | ≥ [__]% | [ ] | Cases written to attempt policy override and data extraction |
| Rare / long-tail slice | ≥ [__]% | [ ] | Cases the client considers hard but real |
| High-stakes / safety slice | **[__]% human review — not a score** | Human | Auto-answering is disabled on this slice by design |
| Citation validity | ≥ [__]% of citations resolve to an authoritative source | Deterministic | Cited-source requirement comes from [client compliance/legal] |

**False-answer rate:** ≤ [__]%, defined operationally as [UNSUPPORTED CLAIM · WRONG DOCUMENT VERSION · WRONG ENTITY · WRONG PROCEDURE STEP]. Adjudicated by [NAME/ROLE] within [__] business days.

## 3. Operational thresholds

| Metric | Threshold | Measurement |
|---|---|---|
| p95 end-to-end latency | ≤ [__] s | Production telemetry, [__]-day window |
| Cost per successful outcome | ≤ $[__] | Telemetry: tokens, infra, retries, failures, human review time |
| Escalation handoff completeness | ≥ [__]% include the structured diagnostic summary | Sampled review of [N] escalations |
| Availability | ≥ [__]% during [SUPPORT WINDOW] | Monitoring |
| Rollback time | ≤ [__] minutes | Drill, dated [__] |

## 4. Adoption criteria

- ≥ [__]% of the target team using the system weekly by week [__], with training complete for [__]% of staff.
- Feedback channel live, with [__]% of users having submitted at least one item by week [__].
- Named client-side owner for evals, data quality, and the feedback loop: [NAMES].

## 5. Failure definitions and adjudication

| What counts as a failure | How it is detected | Who adjudicates | SLA |
|---|---|---|---|
| [e.g. unsupported claim in an auto-returned answer] | [review sample · user report] | [role] | [__ days] |
| [e.g. missed escalation on a high-stakes case] | [case review] | [role] | [__ days] |
| [e.g. data disclosed beyond the requester's entitlements] | [audit log review · security test] | [security] | [immediate] |

## 6. Measurement method (who, what, when)

- **Who runs the measurement:** [NAME / TEAM]
- **Data access required:** [SYSTEMS, EXPORT PATH, ANY CONTRACTUAL PERMISSIONS NEEDED]
- **Dates:** baseline [__] · interim [__] · final [__]
- **Report format and audience:** [ONE PAGE, TO SPONSOR AND INTERNAL OWNER, WITH THRESHOLD TABLE AND RAW COUNTS]

## 7. Sign-off

| Role | Name | Date | Signature / written acknowledgment |
|---|---|---|---|
| Client sponsor | [ ] | [ ] | [ ] |
| Internal owner | [ ] | [ ] | [ ] |
| Eval owner | [ ] | [ ] | [ ] |

## 8. What happens below the bar

- **Within [__] weeks of the final measurement:** rework within scope, at no additional charge, addressing the specific failing slices.
- **Beyond that:** [PAID EXTENSION WITH REVISED CRITERIA / TERMINATION CLAUSE / REDUCED-SCOPE GO-LIVE WITH DOCUMENTED LIMITATIONS — choose one and state it here, not later].

---

## Done when

- [ ] Every threshold has a number, a scorer, and a measurement source
- [ ] The golden set is client-authored or client-co-authored, versioned, and sized
- [ ] At least one slice is explicitly human-reviewed rather than scored
- [ ] The business outcome names a baseline, a cohort, and a measurement window
- [ ] Cost per successful outcome — not per call — is included
- [ ] Failure definitions are operationally stated and an adjudicator is named
- [ ] Sign-off is dated *before* the first demo
- [ ] The below-the-bar consequences are written down, including the termination or extension option
