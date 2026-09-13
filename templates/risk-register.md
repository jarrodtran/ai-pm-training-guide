# Risk Register Template

Fill-in-the-blank template for the AIPM 520 risk module (M6) and the RSK 550 complete register (M1). The AI PM's relationship to risk is adversarial-by-default and constructive-by-design. The differentiator between a plan and governance is **detection**: "we mitigate hallucinations with retrieval" is a plan; "we sample 2% of sessions weekly and score them against the golden set, with the trend reported monthly" is a system. A register without detection is a list of fears; with detection, it is an operating plan.

**Product / feature:** [NAME]
**Register version / review date:** [VERSION — REVIEWED [CADENCE], OWNER: [NAME]]
**Risk appetite note:** [ONE LINE — e.g. "no irreversible actions without a human; nothing shipped below the regression gate"]

---

## The Five Risk Families

| Risk family | Likelihood (H/M/L) | Impact (H/M/L) | Mitigation (the plan) | Detection mechanism (the system — what signal, what cadence, what threshold triggers action) | Owner |
|---|---|---|---|---|---|
| **Hallucination** — wrong confident output | [H/M/L] | [H/M/L] | [RETRIEVAL OVER IMPROVISATION, SOURCE LINKS, GUARDRAILS, HUMAN REVIEW ON HIGH-STAKES SLICES] | [e.g. weekly sample of ___% of sessions scored against the golden set; pass rate below ___% triggers re-eval; "I don't know" rate tracked] | [NAME] |
| **Bias** — skewed training data or thresholds producing skewed outcomes for some users | [H/M/L] | [H/M/L] | [BALANCED EVAL SET, THRESHOLD ADJUSTMENT, HUMAN REVIEW FOR HIGH-IMPACT SLICES] | [e.g. eval results decomposed by segment (language, usage pattern, access route); differential error rate above ___ points vs. the average triggers action] | [NAME] |
| **Privacy** — PII leaking through prompts, training data, or logs; conversation data outliving its purpose | [H/M/L] | [H/M/L] | [PII MASKED BEFORE PROMPTS LEAVE THE VPC, RETENTION LIMITS, NO TRAINING ON USER DATA WITHOUT A LEGAL BASIS] | [e.g. PII scan on sampled logs and prompts; retention enforced by a deletion job with an alert when it fails; access logs reviewed] | [NAME] |
| **Security** — prompt injection (direct and indirect via retrieved documents); attacker-controlled text becoming executable instruction | [H/M/L] | [H/M/L] | [TREAT MODEL OUTPUT AS UNTRUSTED DATA, ISOLATE INSTRUCTIONS FROM CONTENT, LEAST-PRIVILEGE TOOLS, VALIDATE TOOL-CALL ARGUMENTS, RED-TEAM BEFORE LAUNCH] | [e.g. red-team suite re-run on every material change; injection attempts logged and trended; tool calls above least-privilege blocked and alerted] | [NAME] |
| **Compliance** — GDPR, EU AI Act, sector rules, and the contracts signed with customers | [H/M/L] | [H/M/L] | [EU AI ACT RISK-CLASS MAPPING, CONSENT BASIS DOCUMENTED, PRE-LAUNCH REVIEW GATE, LEGAL REVIEW WHERE REQUIRED] | [e.g. pre-launch gate checklist signed per release; incident response runbook with severity levels and rollback triggers; regulator/legal review calendar] | [NAME] |

---

## Notes

- **Hardest to detect in this product:** [RISK + WHY] — spend effort there accordingly.
- **Cross-cutting owner question:** risks that cross product, legal, and security need one accountable owner; name who arbitrates: [NAME].
- **Incident posture (RSK 550 M4):** rollback trigger = [SIGNAL + THRESHOLD], pullable by [NAME / ROLE], within [___ HOURS].

---

## Done when

- [ ] All five families are rows, each with likelihood, impact, mitigation, **detection mechanism**, and owner
- [ ] Every detection mechanism names a signal, a cadence, and a threshold that triggers action — no "we monitor it"
- [ ] The hardest-to-detect risk is named, with a reason
- [ ] A rollback trigger and the person who can pull it are written down
- [ ] Register has a review cadence and a version number
