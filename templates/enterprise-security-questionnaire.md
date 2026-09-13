# Enterprise Security & Data Questionnaire

Fill-in-the-blank template for Module 3 of the FDE-PM Field Manual (`../fde-pm-field-manual.md`). These are the thirty questions that arrive in real enterprise reviews, grouped as they arrive. **The PM should be able to answer every one from the architecture — not by asking an engineer in the room.** Any answer you cannot give is a finding: record it in section 5 with an owner and a date.

**Engagement / system:** [NAME] · **Deployment model:** [SaaS MULTI-TENANT / DEDICATED TENANT / ON-PREM / AIR-GAPPED] · **Completed by:** [PM] · **Date:** [YYYY-MM-DD]

---

## 1. Identity and access

| # | Question | Answer | Evidence / artifact |
|---|---|---|---|
| 1 | How do users authenticate, and is SSO/MFA enforced? | [ ] | [IdP config, OIDC metadata] |
| 2 | How are entitlements established, and how quickly does a role change or departure take effect? | [ ] | [Sync cadence, deprovisioning path] |
| 3 | Does retrieval respect the requesting user's entitlements — and at which point in the pipeline? | [ ] | [ADR, test evidence] |
| 4 | What service identities exist, with what scopes, and who rotates their credentials? | [ ] | [Access inventory] |
| 5 | Can administrators or support staff read customer content, and is that access logged and approved? | [ ] | [Break-glass process, audit log] |
| 6 | Is there support for customer-managed keys (CMEK/BYOK)? | [ ] | [KMS design] |

## 2. Data handling

| # | Question | Answer | Evidence / artifact |
|---|---|---|---|
| 7 | What data categories flow through the system (PII, PHI, PCI, confidential, internal)? | [ ] | [Data classification table] |
| 8 | Where is each field processed — in the client's estate, our cloud, or a model provider? | [ ] | [Field-level data-flow map] |
| 9 | What is redacted or pseudonymized, at which boundary, and how is that validated? | [ ] | [Redaction config, test results] |
| 10 | What are the retention periods per store (source, index, logs, traces, caches, backups)? | [ ] | [Retention schedule] |
| 11 | What is the deletion path for an erasure request, and how is deletion verified? | [ ] | [Runbook, verification script output] |
| 12 | Are prompts or outputs used to train anything — by us or by any model provider? | [ ] | [Contract clause, vendor terms extract] |
| 13 | What does the end-to-end data-flow map look like, field by field, with trust boundaries drawn? | [ ] | [Diagram — see Blueprint 8] |
| 14 | What happens to client data at contract end? | [ ] | [Exit plan, deletion certificate] |

## 3. Model and application security

| # | Question | Answer | Evidence / artifact |
|---|---|---|---|
| 15 | How is prompt injection mitigated — what happens when a retrieved document contains instructions? | [ ] | [Injection test results] |
| 16 | What are the egress destinations, and who approves changes to them? | [ ] | [Allow-list, change process] |
| 17 | What tools can the system call, with what scopes, and what can they change? | [ ] | [Tool inventory with scopes] |
| 18 | What output validation runs before any action is taken? | [ ] | [Validation spec] |
| 19 | How are system prompts protected — and do we accept that they may leak? | [ ] | [Position statement] |
| 20 | What rate, step, and cost limits bound consumption? | [ ] | [Limits config] |
| 21 | What is the model supply-chain posture (versioning, provenance, ability to swap providers)? | [ ] | [Abstraction design, vendor terms] |

## 4. Operations and assurance

| # | Question | Answer | Evidence / artifact |
|---|---|---|---|
| 22 | What is logged per request, where is it stored, and who can read it? | [ ] | [Log schema, access policy] |
| 23 | How are prompt and model versions recorded, and how is rollback performed? | [ ] | [Version registry, rollback drill] |
| 24 | What monitoring and alerting exist, with what thresholds and named owners? | [ ] | [Drift table, on-call rota] |
| 25 | What is the incident response process, and what evidence exists that it has been exercised? | [ ] | [IR plan, last exercise] |
| 26 | What penetration tests and red-team exercises have been run, and what was found? | [ ] | [Reports, remediation status] |
| 27 | Which certifications apply, and to what scope (SOC 2 Type II, ISO 27001/42001, FedRAMP, sector rules)? | [ ] | [Reports, scope statement] |
| 28 | What is the subprocessor list, and how are changes notified? | [ ] | [Register, notification clause] |
| 29 | What are the availability and support commitments (SLA, support window, escalation path)? | [ ] | [SLA, escalation matrix] |
| 30 | What artifact maps to each of the client's controls (the evidence path for their audit)? | [ ] | [Compliance readiness matrix] |

## 5. Findings

Every "we don't know" or "not yet" from above belongs here — as a finding with an owner and a date, never as a blank.

| # | Finding | Risk | Owner | Due | Status |
|---|---|---|---|---|---|
| [ ] | [ ] | [HIGH/MED/LOW] | [NAME] | [DATE] | [OPEN/IN PROGRESS/CLOSED] |

---

## Done when

- [ ] All 30 questions have an answer or a logged finding (no blanks)
- [ ] The data-flow map (question 13) exists and shows the redaction boundary and every egress path
- [ ] Question 3 (permission-aware retrieval) is answered with test evidence, not an assertion
- [ ] Question 11 (deletion path) has been tested at least once end to end, including index and cache
- [ ] Every finding has an owner and a date, and the client's security owner has seen the list
- [ ] The compliance readiness matrix maps each client control to one of our artifacts
