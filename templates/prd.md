# Product Requirements Document (PRD)

Course: PM 501 — Product Management Fundamentals · Module 3 (Spec Writing)
Project: [PROJECT NAME]
Feature: [FEATURE NAME]
Author: [NAME] · Date: [YYYY-MM-DD] · Version: [VERSION]

A PRD is a decision document, not a wish list. It records the problem (with evidence), the users, the success metrics, the scope, and the requirements in a form engineers can build from. Quality test for the whole document: could an engineer build this without asking me ten questions? If not, tighten.

## Problem & evidence

[PROBLEM STATEMENT — 1-2 sentences, restated from your discovery notes, grounded in interview evidence.]

The evidence:

- "[QUOTE — verbatim from a discovery interview]" — [PERSON, ROLE], interview [DATE]. This demonstrates [WHAT BEHAVIOR OR PAIN THE QUOTE PROVES].
- "[SECOND QUOTE OR BEHAVIORAL EVIDENCE]" — [PERSON, ROLE], interview [DATE]. Demonstrates [WHAT IT PROVES].
- [THIRD EVIDENCE ITEM — frequency of the problem, cost of the workaround, or what the user paid]

[WHY THIS PROBLEM IS WORTH SOLVING NOW — timing, frequency of pain, cost of inaction. If a claim has no evidence behind it, label it explicitly: "ASSUMPTION: ...".]

## Target users

| Persona | Who they are | Job in their words (JTBD) | What success looks like for them |
|---|---|---|---|
| [PERSONA NAME] | [ROLE, CONTEXT — 1-2 sentences] | "When ___, I want ___, so I can ___" | [OUTCOME THEY WOULD NOTICE] |
| [PERSONA NAME] | [ROLE, CONTEXT] | "[JTBD STATEMENT]" | [OUTCOME] |

[WHO IS EXPLICITLY NOT A TARGET USER — and why. This is scope discipline at the persona level.]

## Success metrics

North star: [NORTH STAR METRIC — the one number that best captures delivered value, not motion].

| Metric | Type | Target | How measured |
|---|---|---|---|
| [NORTH STAR] | North star | [TARGET + TIMEFRAME] | [DATA SOURCE / EVENT] |
| [GUARDRAIL — e.g. hallucination rate] | Guardrail | [THRESHOLD] | [DATA SOURCE / EVAL] |
| [MODEL-QUALITY METRIC — eval score on [EVAL SET]] | Guardrail | [THRESHOLD] | [EVAL RUN — see eval-suite.md] |
| [LEADING INDICATOR — e.g. activation rate] | Leading | [TARGET] | [DATA SOURCE] |
| [LAGGING INDICATOR — e.g. retention] | Lagging | [TARGET] | [DATA SOURCE] |

For AI features, guardrails must include model-quality metrics: eval score, hallucination rate, and cost per session. An AI feature that grows engagement while eroding trust is a slow-motion failure. [A/B TEST PLAN — what you will compare and how you will judge the result. An A/B test showing +10% clicks while hallucination doubles is a loss dressed as a win.]

## Scope

### In scope

- [FEATURE / BEHAVIOR] — serves [OUTCOME OR STORY]
- [FEATURE / BEHAVIOR] — serves [OUTCOME OR STORY]

### Out of scope

- [FEATURE] — because [REASON]. The out-of-scope list is a promise to stakeholders about what you are not doing; it is where scope creep lives.
- [FEATURE] — because [REASON]

## User stories & acceptance criteria

The unit of requirements is the user story — "as a ___, I want ___, so ___" — with acceptance criteria written as given/when/then. An engineer can verify them, a tester can automate them, and you can defend them.

### Story 1. [SHORT TITLE]

As a [PERSONA], I want [ACTION], so [OUTCOME].

Acceptance criteria (all must pass):
- Given [CONTEXT / PRECONDITION], when [ACTION TRIGGERED], then [OBSERVABLE RESULT]
- Given [CONTEXT], when [EDGE CASE OR FAILURE], then [OBSERVABLE RESULT — including the refusal/error behavior for AI features]
- Given [CONTEXT], when [EDGE CASE], then [OBSERVABLE RESULT]

### Story 2. [SHORT TITLE]

As a [PERSONA], I want [ACTION], so [OUTCOME].

Acceptance criteria (all must pass):
- Given [CONTEXT], when [ACTION], then [OBSERVABLE RESULT]
- Given [CONTEXT], when [EDGE CASE], then [OBSERVABLE RESULT]

## Risks

| Risk | Likelihood (H/M/L) | Impact (H/M/L) | Mitigation |
|---|---|---|---|
| [RISK — e.g. model quality below threshold, cost overrun, user confusion] | [H/M/L] | [H/M/L] | [MITIGATION] |
| [RISK] | [H/M/L] | [H/M/L] | [MITIGATION] |

Score the hidden AI costs explicitly: model quality risk, eval effort, and per-interaction cost. An AI feature can win on RICE impact and lose on economics.

## Open questions

- [QUESTION] — [WHO NEEDS TO ANSWER / BY WHEN]
- [QUESTION] — [WHO NEEDS TO ANSWER / BY WHEN]

Resolve these before build starts, or name an owner and a date for each.

## Ten-question test (self-check)

Grade the PRD before it leaves your desk. If any answer is no or weak, fix the document.

1. Is the problem stated in 1–2 sentences, grounded in interview evidence? [YES / NO]
2. Could an engineer build this without asking you ten questions? [YES / NO]
3. Is every acceptance criterion testable as given/when/then? [YES / NO]
4. Does every user story trace to an evidence-backed problem? [YES / NO]
5. Is the out-of-scope list explicit, with reasons? [YES / NO]
6. Are success metrics measurable, with targets and data sources? [YES / NO]
7. Are model-quality metrics named as guardrails (eval score, hallucination rate, cost per session)? [YES / NO]
8. Is the north star a measure of delivered value, not motion? [YES / NO]
9. Are risks scored and mitigated, including the AI-specific ones? [YES / NO]
10. If this shipped today, would you know by week four whether it is working? [YES / NO]

## Done when

- [ ] Problem & evidence cites real interview quotes, not opinions
- [ ] Every acceptance criterion is given/when/then and verifiable
- [ ] Scope in/out is explicit, with a reason for every out-of-scope item
- [ ] Success metrics include a north star, guardrails, and model-quality thresholds
- [ ] All ten questions in the ten-question test pass
- [ ] An engineer could build from this without asking ten questions
