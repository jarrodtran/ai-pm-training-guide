# Data Plan Template

Fill-in-the-blank template for the AIPM 520 data module (M3) and the DATA 530 governance module (M4). Every AI product runs on data, and most product failures trace back to a data assumption made early and never revisited. Three distinctions organize the subject: **quality vs. quantity** (1,000 clean, labeled examples beat 100,000 messy ones), **retrieval data vs. fine-tuning data** (retrieval is the default lever; fine-tuning is the exception you must argue for), and the **data flywheel** (usage → feedback → better evals and products → more usage — the compounding strategic asset).

**Product / feature:** [NAME]
**Data plan owner:** [NAME]

---

## 1. Data Inventory

What data exists, what's missing, and who owns each source. "If it wasn't logged, it didn't happen" — mark which sources are already instrumented.

| Data source | What it contains | Format / volume | Exists or missing | Owner | Instrumented? (DATA 530) |
|---|---|---|---|---|---|
| [e.g. support tickets] | [CONTENT, LANGUAGE, DATE RANGE] | [e.g. 40k tickets, CSV export] | [EXISTS / PARTIAL / MISSING] | [NAME] | [YES / NO] |
| [SOURCE 2] | [CONTENTS] | [FORMAT / VOLUME] | [EXISTS / PARTIAL / MISSING] | [NAME] | [YES / NO] |
| [SOURCE 3] | [CONTENTS] | [FORMAT / VOLUME] | [EXISTS / PARTIAL / MISSING] | [NAME] | [YES / NO] |

## 2. Quality Assessment

Clean beats big: the model learns the pattern, not the noise, and noise costs more than absence. Assess each source and name the quality owner — data quality is an ongoing practice with owners and monitoring, like any production system (schema drift, silent gaps, and label rot each need detection, or your eval set quietly decays).

| Data source | Suspected quality issues | Impact on the product if unfixed | Quality owner |
|---|---|---|---|
| [SOURCE] | [e.g. labels inconsistent, 30% outdated, duplicates] | [WHAT BREAKS — RETRIEVAL MISSES, BIASED EVALS, WRONG ANSWERS] | [NAME] |
| [SOURCE] | [ISSUES] | [IMPACT] | [NAME] |

**Retrieval-first default:** the default architecture is retrieval (corpus maintained like documentation); fine-tuning is the exception you must argue for — the burden of proof lives here: [WHEN FINE-TUNING WOULD EARN ITS COST, IF EVER]

## 3. Collection Plan

How the missing data gets collected — ethically, with consent, and feeding the flywheel.

- **What to collect:** [DATA NEEDED, PRIORITIZED]
- **How (ethically):** [COLLECTION MECHANISM — e.g. opt-in feedback widget, in-flow corrections, ratings; consent basis documented; user data is not yours to train on without an explicit legal basis]
- **Consent basis:** [WHAT USERS ARE TOLD AND AGREE TO — GDPR vocabulary: consent, purpose limitation, transparency]
- **Flywheel capture:** what feedback from usage would improve the product, and how it is captured:
  - [e.g. ratings → weekly review → new eval cases → better golden set]
  - [e.g. corrections → retrieval fix → fewer corrections]
- **Where the flywheel breaks:** [e.g. enterprise product with 12 customers produces too little feedback to learn from — what replaces it?]

## 4. PII Exposure Map

Know what PII is and where it lives in your product. For each source that carries personal data: the type of PII, where it flows, the consent basis, retention, and access controls. Governance is what keeps the flywheel legal and trusted.

| Data source | PII present? | PII types | Where it flows (prompts, training, logs, vendor APIs) | Consent basis | Retention | Access controls |
|---|---|---|---|---|---|---|
| [SOURCE] | [YES / NO] | [e.g. names, emails, account numbers, conversation text] | [e.g. into prompts → sent to model vendor; stored in logs ___ days] | [LEGAL BASIS — CONSENT / CONTRACT / LEGITIMATE INTEREST — TBD WITH LEGAL] | [___ DAYS / INDEFINITE / NONE] | [WHO CAN READ, WHO CAN EXPORT, WHO CAN DELETE] |
| [SOURCE] | [YES / NO] | [PII TYPES] | [FLOWS] | [BASIS] | [RETENTION] | [ACCESS] |

**Rules of the road:** PII is masked before prompts leave the [VPC / TRUST BOUNDARY]; retention is enforced by a deletion job with an alert; no training on user data without an explicit legal basis; GDPR and EU AI Act vocabulary governs what global products may do even if you are not in Europe.

---

## Done when

- [ ] Inventory lists every source with exists/missing and an owner
- [ ] Quality assessment names issues and a quality owner per source
- [ ] Collection plan states the consent basis and how the flywheel captures feedback
- [ ] PII map covers every source that carries personal data: types, flows, consent, retention, access
- [ ] The retrieval-first default is stated, and the fine-tuning case (if any) carries its burden of proof
