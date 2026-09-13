# Production Eval Plan Template

Fill-in-the-blank template for the AIPM 520 production eval system (M4) and the FDE 560 field eval plan. A shipped AI product degrades — the world changes, users find new edge cases, the input distribution drifts — so quality is an **ongoing operating problem**, not a launch-day checkbox. This plan has five parts: golden set, scoring method, regression gates, drift monitoring, and the feedback loop.

**Product / feature:** [NAME]
**Owner of the eval system:** [NAME — the person who owns the eval system owns the quality conversation]

---

## 1. Golden Set

- **Source:** [WHERE THE CASES COME FROM — START FROM THE AI 510 SUITE AND THE 25-CASE SUITE IN `eval-suite.md`; for client work, build it in week one from the client's cases, in their vocabulary, with their definition of "right"]
- **Size:** [N CASES]
- **Rules of the set:** fixed and versioned; cases are added only through the feedback loop below; the set never changes silently between model comparisons
- **Client variant (FDE 560):** the client's golden set is built in week one, from their cases, with their definition of "right," and the **success bar is agreed before the first demo** — a demo can always be made to look good; a pre-agreed bar cannot be moved after the fact.

## 2. Scoring Method

| Slice | Scorer | Why | Spot-check |
|---|---|---|---|
| [e.g. high-stakes / adversarial cases] | [HUMAN REVIEW] | [STAKES OR AMBIGUITY TOO HIGH FOR A JUDGE] | [n/a or describe] |
| [e.g. easy + edge cases at volume] | [LLM-AS-JUDGE] | [VOLUME — HUMANS CANNOT SCORE EVERYTHING] | [___% OF JUDGE-SCORED CASES RE-SCORED BY A HUMAN, WEEKLY] |

**Spot-check note:** LLM-as-judge has biases too — it can be fooled by confident tone, reward length over correctness, and inherit the model's own blind spots. The spot-check is the discipline that catches it: sample [___%] of judge-scored cases, re-score by hand, and track agreement. If judge-vs-human agreement drops below [___%], stop trusting the judge until it is recalibrated.

## 3. Regression Thresholds (Gates)

> **We do not ship a model version that scores below ___% overall** on the golden set, or below ___% on the [ADVERSARIAL] slice, or below ___% on the [EDGE] slice.

- **Trigger cadence:** [e.g. every model upgrade, every prompt change, every retrieval change, and weekly on a rolling sample]
- **Who can block:** [NAME — the eval owner has veto over shipping]
- **Rollback rule:** if a shipped version drops below the gate in production, [ROLLBACK OR PIN TO PREVIOUS VERSION WITHIN ___ HOURS]

## 4. Drift Signals with Triggers

Live signals that say "re-eval this week, not next sprint." For each: the signal, what it means, the trigger threshold, and the action. A trigger without a named action is a dashboard, not monitoring.

| Signal | What it means | Trigger (threshold) | Action |
|---|---|---|---|
| Rolling eval score (weekly sample vs. golden set) | Quality drift on known cases | [___% DROP vs. 4-week baseline] | [RE-EVAL, BLOCK SHIP, ROLLBACK IF SHIPPED] |
| Thumbs-down / negative-feedback rate | Users saying it's wrong | [___% RATE OR ___% RISE vs. baseline] | [REVIEW SAMPLES, ADD CASES TO GOLDEN SET, RE-EVAL] |
| "I don't know" / refusal rate | Coverage shrinking or scope guardrails over-firing | [___% RISE vs. baseline] | [CHECK RETRIEVAL COVERAGE, TUNE GUARDRAILS] |
| Cost per session | Token economics drifting (longer contexts, more retries) | [___% RISE vs. baseline] | [CHECK TOKEN USAGE, CONTEXT LENGTH, MODEL TIER] |
| Latency p95 | Model or retrieval slowing | [___ MS vs. budget of ___ MS] | [CHECK MODEL TIER, CACHING, RETRIEVAL] |
| [CLIENT-SPECIFIC SIGNAL] | [WHAT IT MEANS] | [TRIGGER] | [ACTION] |

**Signal vs. noise:** a single bad day is noise; the trigger thresholds above are set so that action fires on a trend, not a blip. State how you know a trigger is signal: [E.G. TWO CONSECUTIVE WEEKS, OR A SINGLE DAY PAST A HARD CEILING]

## 5. Feedback Loop

The eval set learns with the product: bad answers from production become new eval cases.

- **Capture:** [WHERE PRODUCTION FAILURES ARE COLLECTED — e.g. thumbs-down events, escalated sessions, support tickets that mention the AI's answer]
- **Curate:** [WHO REVIEWS THEM WEEKLY AND DECIDES WHAT ENTERS THE GOLDEN SET — NAME THE PERSON]
- **Add:** [CADENCE AND RULE — e.g. up to 5 new cases per week; each new case is written with expected behavior and gets a category]
- **Close the loop:** the new case is scored on the next eval run; if the system fails it, it becomes [A REGRESSION ITEM / A FIX TICKET] owned by [NAME]

The feedback loop is the moat: model capability is rented, but the feedback loop compounds.

---

## Done when

- [ ] Golden set is defined with source, size, version rule, and an owner
- [ ] Scoring method names the scorer per slice, with the LLM-as-judge spot-check percentage written down
- [ ] Regression gate has numbers — overall and per-slice floors — and a blocker is named
- [ ] Drift table has at least 4 signals, each with a threshold and a named action
- [ ] Feedback loop names who curates, how often, and how cases enter the set
- [ ] The "demo ≠ production" speech is ready: it worked in the demo is not it works in production
