# Metrics Tree

Course: PM 501 — Product Management Fundamentals · Module 5 (Metrics, Funnels & Instrumentation)
Project: [PROJECT NAME] · Author: [NAME] · Date: [YYYY-MM-DD]

A metric is a contract about what success means. The tree makes success legible: north star at the top, drivers below it, guardrails at the side. If you didn't log it, it didn't happen — so this document ends with the event list that makes every number above it visible.

## North star

[NORTH STAR — the one number that best captures delivered value for users. Not "downloads" or "queries" — the value users get, not the motion you make. Define it precisely enough that two people could not disagree about whether it went up.]

Definition: [EXACT DEFINITION — who is counted, what counts as active, over what window]
Why this number: [WHY IT CAPTURES VALUE BETTER THAN THE ALTERNATIVES YOU REJECTED]

## Drivers (leading indicators)

The levers under the north star. Leading indicators predict the future; lagging indicators confirm it. A north star needs both.

| Driver | Type (leading / lagging) | Definition | Target |
|---|---|---|---|
| [DRIVER 1 — e.g. activation rate] | Leading | [EXACT DEFINITION] | [TARGET] |
| [DRIVER 2 — e.g. weekly retention] | Lagging | [EXACT DEFINITION] | [TARGET] |
| [DRIVER 3] | [TYPE] | [EXACT DEFINITION] | [TARGET] |

[ONE LINE ON HOW THE DRIVERS CONNECT TO THE NORTH STAR — the causal story you are betting on.]

## Guardrails

The numbers that must not silently degrade. For AI features these always include model-quality metrics. If the north star goes up and a guardrail goes red, the PM's move is to stop optimizing and fix the guardrail.

| Guardrail metric | Threshold | What red means | Owner |
|---|---|---|---|
| [GUARDRAIL — e.g. hallucination rate] | [THRESHOLD — e.g. < 2% of answers flagged] | [WHAT HAPPENS IF BREACHED] | [OWNER] |
| [MODEL-QUALITY — eval score on [EVAL SET]] | [THRESHOLD — e.g. ≥ 90% pass] | [WHAT HAPPENS IF BREACHED] | [OWNER] |
| [COST — cost per session] | [THRESHOLD — e.g. ≤ $0.05] | [WHAT HAPPENS IF BREACHED] | [OWNER] |
| [OTHER GUARDRAIL — e.g. latency] | [THRESHOLD] | [WHAT HAPPENS IF BREACHED] | [OWNER] |

[EVAL SETS AND THRESHOLDS ARE SPECIFIED IN eval-suite.md. WHO GETS ALERTED AND ON WHAT CADENCE.]

## Funnel

Where value leaks: acquisition → activation → retention → referral.

| Stage | Definition | Conversion (current or target) | Where value leaks / biggest drop-off |
|---|---|---|---|
| Acquisition | [HOW USERS ARRIVE] | [% OR N] | [OBSERVED DROP-OFF] |
| Activation | [FIRST MOMENT OF VALUE] | [%] | [OBSERVED DROP-OFF] |
| Retention | [RETURN BEHAVIOR, OVER WHAT WINDOW] | [%] | [OBSERVED DROP-OFF] |
| Referral | [USERS BRINGING OTHERS] | [%] | [OBSERVED DROP-OFF] |

## Event list (instrumentation)

Every event you would log to see the funnel. If it wasn't logged, it didn't happen.

| Event | Trigger | Properties |
|---|---|---|
| [EVENT NAME — verb, e.g. searched] | [USER ACTION OR SYSTEM CONDITION THAT FIRES IT] | [user id, timestamp, query, result count, latency, model version, cost, ...] |
| [EVENT NAME] | [TRIGGER] | [PROPERTIES] |
| [EVENT NAME] | [TRIGGER] | [PROPERTIES] |
| [EVENT NAME] | [TRIGGER] | [PROPERTIES] |

[EVENTS THAT NEED TO EXIST BUT DON'T YET — and who is responsible for adding them before launch.]

## Done when

- [ ] The north star is defined precisely enough that two people cannot disagree about whether it moved
- [ ] Drivers include both a leading and a lagging indicator, each with a definition and a target
- [ ] Guardrails include model-quality metrics (eval score, hallucination rate, cost per session) with thresholds
- [ ] Every funnel stage has a definition and a conversion figure or measurement plan
- [ ] Every metric in this tree is produced by at least one event in the event list
- [ ] An engineer could implement the event list from the trigger and properties columns alone
