# Statement of Work Template — Client AI Engagement

Fill-in-the-blank template for the FDE 560 scoping module (M2). Three disciplines matter most: **measurement in the contract** (a scope that promises quality without defining how quality is measured is a lawsuit with a demo attached — the golden set and success bar belong in the SOW, not in a slide); **the out-of-scope section is the whole game** (AI engagements live on scope creep — "can it also…" — and the explicit won't-list is your only defense that doesn't damage the relationship); and the **operating handoff** (if the client can't operate it after you leave, you built a demo, not a system). This template is preceded by the feasibility memo (`feasibility.md`), which is written before the price is.

**Client:** [CLIENT NAME] · **Engagement:** [NAME] · **Period:** [START — END] · **SOW version:** [V1.0 — DATE]

---

## 1. Scope — In

What will be built, stated as concrete capabilities with input → output. No "intelligent assistant" language; every line must be testable.

- [CAPABILITY 1 — e.g. "Answer questions about the client's policy docs by retrieving from the client's corpus and citing sources; refuse out-of-scope topics."]
- [CAPABILITY 2]
- [CAPABILITY 3]

**Architecture (composable, boring):** [MODEL + RETRIEVAL + TOOLS + GUARDRAILS + HUMAN-IN-THE-LOOP — ONE PARAGRAPH OR BOXES-AND-ARROWS REFERENCE; THE HUMAN HANDOFF MARKED]

## 2. Scope — Out (the won't-list — defend each line)

- [WON'T 1 — e.g. "No autonomous actions: the system cannot issue refunds, send email, or modify records without human approval."]
- [WON'T 2 — e.g. "No training or fine-tuning on client data; retrieval-only."]
- [WON'T 3 — e.g. "No integration with legacy system X; data exported manually."]
- [WON'T 4 — anything that would need a new data source, a new model, or a new integration]

Every "can it also…" that comes up later is answered by this list. If a line is not defensible, remove it and reprice — the won't-list is not a wish list.

## 3. Data Access & Security

- **Data the client provides:** [WHAT, WHERE IT LIVES (CLIENT VPC / SHARED ENV), FORMAT, VOLUME]
- **How it is accessed:** [ACCESS MECHANISM, CREDENTIALS, LEAST-PRIVILEGE]
- **PII handling:** [PII TYPES PRESENT, MASKING BEFORE PROMPTS LEAVE THE TRUST BOUNDARY, NO TRAINING ON USER DATA]
- **Retention & deletion:** [RETENTION PERIOD, DELETION JOB, WHAT HAPPENS AT ENGAGEMENT END]
- **Security/compliance basis:** [GDPR / EU AI ACT RISK CLASS / SECTOR RULES — WITH THE OPEN QUESTIONS TAKEN TO LEGAL]

## 4. Eval Criteria (measurement in the contract)

- **Client golden set:** [N CASES — BUILT IN WEEK ONE FROM THE CLIENT'S CASES, IN THEIR VOCABULARY, WITH THEIR DEFINITION OF "RIGHT" — SEE `eval-suite.md`]
- **Scoring method:** [HUMAN REVIEW ON HIGH-STAKES SLICES, LLM-AS-JUDGE AT VOLUME WITH SPOT-CHECK — SEE `production-eval-plan.md`]
- **Success bar (agreed before the first demo, in writing):** the system scores **___%** on the golden set, with **___%** on the [ADVERSARIAL / HIGH-STAKES] slice, measured on [DATE]. A demo can always be made to look good; a pre-agreed bar cannot be moved after the fact.
- **What happens below the bar:** [REWORK WITHIN SCOPE / ADDITIONAL PAID PHASE / TERMINATION CLAUSE]

## 5. Success Metrics

- **Primary:** [THE METRIC THAT MEANS THE ENGAGEMENT WORKED — e.g. resolution rate, time-to-answer, deflection rate — WITH DEFINITION AND BASELINE FROM DISCOVERY]
- **Guardrails (treated as primary, per DATA 530):** [HALLUCINATION / ERROR RATE, ESCALATION RATE, COST PER SESSION, LATENCY P95 — WITH THRESHOLDS]
- **Measurement basis:** [INSTRUMENTATION — EVENTS AND PROPERTIES (MODEL VERSION ON EVERY EVENT) — WHO OWNS LOGGING ON EACH SIDE]

## 6. Human-in-the-Loop Design

| What gets reviewed | By whom (client side) | At what stakes | Escalation path |
|---|---|---|---|
| [e.g. refund / high-value actions] | [ROLE — e.g. team lead] | [HIGH — irreversible] | [e.g. action blocked until human approves; if unreviewed in ___ min, escalates to ___] |
| [e.g. flagged low-confidence answers] | [ROLE] | [MEDIUM] | [PATH] |
| [e.g. routine answers] | [NONE — SYSTEM] | [LOW] | [n/a — sampled in evals] |

## 7. Handoff & Operating Manual

The operating manual is the deliverable: how the system is measured, monitored, and maintained after handoff, with owners named on the client side. If the client can't operate it, you built a demo.

- **Deliverables at handoff:** [OPERATING MANUAL, EVAL RUNBOOK, MODEL/PROMPT VERSION LOG, ACCESS INVENTORY]
- **Client-side owners:** [WHO OWNS EVALS, WHO OWNS DATA QUALITY, WHO OWNS THE FEEDBACK LOOP — NAMED ROLES]
- **What to do when it degrades:** [DRIFT SIGNALS + TRIGGERS FROM `production-eval-plan.md` — ROLLBACK TRIGGER, WHO PULLS IT, SUPPORT WINDOW AFTER HANDOFF (___ WEEKS), THEN WHAT]
- **Training / change management:** [TRAINING SESSIONS, FEEDBACK CHANNEL FOR USERS, CLIENT CHAMPION: [NAME]]

---

## Done when

- [ ] Scope-in lines are testable (input → output), scope-out has a defendable won't-list
- [ ] Data access, PII handling, retention, and security/compliance basis are written down
- [ ] Eval criteria and the success bar are in the SOW with numbers, agreed before any demo
- [ ] Success metrics include guardrails with thresholds, and instrumentation is owned
- [ ] HITL design names the reviewer, the stakes, and the escalation path per action type
- [ ] Operating manual handoff names client-side owners and the "when it degrades" runbook
