# The Forward Deployed Product Manager
## Field Manual & Technical Study Guide

**Companion technical reference to the AI-PM Graduate Program · 5 modules · ~90 hours · self-paced**
**Version 1.5 · sources verified September 12, 2026**

This is a personal field manual — reference material for your own work, not coursework. Read it before the room, keep it open in the room, use its templates after the room.

---

## Why this manual exists

A PM on a Forward Deployed team is judged in two rooms. In the **client room**, they are judged on whether the problem is real, the scope is honest, and the promise is measurable. In the **engineering design review**, they are judged on whether they can follow the architecture, spot the edge case that will break the pilot, and argue for the boring option that ships.

Most PM material trains the first room. This manual trains the second: the technical substrate, the architecture trade-offs, the enterprise compliance mechanics, the evaluation and ROI apparatus, and the productization engine that converts deployments into a platform.

> **Relationship to the rest of the program.** FDE 560 (elective, 4 weeks, `courses/fde560.html`) teaches the FDE *operating model* — lifecycle, scoping, field evals, productization. This manual is the deeper technical companion: five modules, ~90 hours, aimed at engineering-grade literacy rather than coverage. Where a template already exists in `templates/`, this manual points to it instead of duplicating it.

---

## The role, defined at the seam

A PM does not write the production code. The PM owns the **decisions** that determine whether the code was worth writing. The clean division:

| Decision | PM owns | FDE owns | The seam (joint work) |
|---|---|---|---|
| Which problem is worth solving | ✓ | consults | Discovery RFC, feasibility memo |
| What "working" means | ✓ | consults | Golden set, acceptance thresholds |
| Instrument choice (AI vs. pipeline vs. rules) | ✓ with FDE | ✓ with PM | Decision matrix, architecture spike |
| How it is built | — | ✓ | Design review, ADR (PM reviews, FDE authors) |
| Data access and permissions | negotiates with client | implements | Security questionnaire, access inventory |
| Scope changes | ✓ | estimates | Change control, won't-list |
| Delivery cadence and unblocking | ✓ | ✓ | Embedded triage, escalation matrix |
| Quality in production | co-owns | ✓ | Eval owner, drift triggers, rollback rule |
| Whether it becomes product | ✓ | consults | Pattern ledger, productization memo |

**The reframe that matters:** the PM is not a translator between business and engineering. The PM is the person who keeps the *decision record* honest — because in enterprise deployments, the failures are rarely technical. They are decisions made implicitly, by nobody, in a meeting nobody wrote down.

---

## The diagnostic spine: five gates

Every engagement — pilot, expansion, or rescue — passes through five gates. Each module of this manual owns one.

| # | Gate | The question | Module | What it costs when skipped |
|---|---|---|---|---|
| 1 | **Problem reality** | Is the problem real, quantified, and owned by someone with budget? | 2 | A technically perfect system nobody uses |
| 2 | **Instrument choice** | Is this an AI problem, a deterministic data pipeline problem, or a change-management failure? | 2 | Paying model prices and model variance for a job a SQL join does exactly |
| 3 | **Data & access feasibility** | Can the data legally, technically, and practically reach the system? | 3 | A pilot that dies in security review, or a demo on data you can never have in production |
| 4 | **Eval & acceptance** | Can we define and measure "done" in the client's terms, before the demo? | 4 | Contested acceptance, unpaid rework, an unhappy reference call |
| 5 | **Productization** | Is this the third instance of a pattern, or a one-off? | 5 | An FDE team that is permanently bespoke — high revenue per head, zero enterprise value |

### The three diagnoses, spelled out

The single most valuable judgment this role requires is telling these three apart *in the first meeting*.

| Diagnosis | Signals | Correct response |
|---|---|---|
| **AI problem** | Unstructured input (text, images, audio, documents); fuzzy or judgment-laden output; the "right answer" varies by context; volume too high for humans, ambiguity too high for rules | Retrieval + model + eval suite; expect iterative quality work; scope the eval before the build |
| **Deterministic data pipeline problem** | Structured input; rules exist and are knowable; auditability or exactness required (money, eligibility, safety); the hard part is *getting to* clean data, not deciding | Build the pipeline: connectors, CDC, transformation, semantic layer. Do **not** put a model in the decision path where a rule is exact and defensible |
| **Change-management failure** | The tool exists; adoption is the problem; workarounds and shadow spreadsheets persist; the ask is "make people use it" | No new system. Sponsorship, process design, incentives, training, workflow redesign. Say this plainly and you become the most trusted person in the room |

Most enterprise "AI projects" are two of these three stacked. The PM's job in discovery is to name which one each layer is, and to price each layer separately.

---

## The AI product lifecycle

The five gates are decision checkpoints. The lifecycle is the sequence they sit in — and in AI, that sequence is a loop, not a line. Classic software ships and is finished; an AI product ships and immediately begins drifting as the models, the data, and the world change underneath it.

| Phase | What happens | The artifact that closes it | Owned by |
|---|---|---|---|
| **1 · Frame** | Decide whether this is an AI problem, a deterministic data problem, or a change-management problem | A problem statement with a number and a named owner | Gates 1–2 · M2 |
| **2 · Discover & scope** | Discovery workshop, current-state walkthrough, instrument decision, feasibility | Discovery RFC · feasibility memo · SOW | Gates 1–2 · M2 |
| **3 · Data readiness** | Sources, access, entitlements, quality, residency — the phase that quietly decides the outcome | Data-flow map · readiness assessment · ADRs | Gate 3 · M3 |
| **4 · Design & spike** | Architecture, guardrails, deployment model; the riskiest assumption tested with a time-boxed spike | Blueprints · ADRs · spike result | M1 · M3 |
| **5 · Define "done"** | Golden set, acceptance thresholds, measurement method — agreed *before* the build finishes | Signed pilot acceptance criteria | Gate 4 · M4 |
| **6 · Build** | Integration, retrieval and model layers, human-in-the-loop, observability | Working system · eval report | M1 · M4 |
| **7 · Pilot** | Real users, real data, shadow and canary runs, human review on the high-stakes slices | Measured results against the agreed thresholds | M4 |
| **8 · Launch** | Rollout, training, support model, SLOs, and a rollback armed before go-live | Operating manual with named owners | M4 · M5 |
| **9 · Operate & evaluate** | Drift monitoring, regression gates, the feedback loop, incident response | Eval system running permanently · incident runbook | M4 |
| **10 · Iterate** | Model, prompt, retrieval, and cost changes — every one of them through the eval gate | Change record · cost review | M1 B5 · M4 |
| **11 · Scale & productize** | The third instance of the pattern becomes a core capability; bespoke versions are deprecated | Pattern ledger · productization memo | Gate 5 · M5 |
| **12 · Retire** | Sunset, migrate users, delete data, decommission the model | Sunset memo · deletion evidence | M3 · M5 |

**Three things that make the AI lifecycle different from a software lifecycle:**

1. **Phase 5 comes before phase 6, not after.** You define "done" before you build, because in AI the evaluation *is* the specification — an unevaluated requirement is a wish.
2. **Phases 9–10 never end.** The input distribution drifts, the corpus ages, and the model provider ships changes under you. The back half of the lifecycle is an operating loop, not a launch event — which is why the eval suite runs forever rather than once.
3. **Data is a second flywheel.** Usage generates labels — outcomes, corrections, escalations — that can improve the next version, but only if consent, governance, and the feedback loop were designed in at phase 3. Teams that discover this at phase 9 have already lost the data they needed.

---

## How to use this manual

**Reading order.** Modules 1–2 before your first client conversation. Module 3 before anyone says the word "data". Module 4 before anyone says the word "done". Module 5 quarterly, as your engagement portfolio accumulates.

**The method.** Each module has the same four parts:

- **A · Core PM competencies & mental models** — the instincts, stated as rules you can defend under pressure
- **B · Technical vocabulary & architecture blueprints** — the exact terms, patterns, and diagrams you must be able to draw on a whiteboard
- **C · Reading list & real-world case studies** — verified sources, labeled by evidence type
- **D · The field playbook** — templates, protocols, and the artifacts you produce

**Verification discipline.** Every URL in this manual was checked on September 12, 2026 — direct HTTP fetch (status 200) or proxy fetch where the site blocks automated clients (Palantir blog, ACM Queue, HHS, ISO, SEC). Source *types* are labeled: **[primary]** (the operator's own documentation or engineering writing), **[research]** (peer-reviewed or preprint), **[vendor]** (published by a party selling something), **[standard]** (regulatory or accreditation body). Appendix C is the reference bank with per-URL status and verification method. Re-verify quarterly; in this field links are stable and content is not.

### Time budget

| Module | Study | Field work | Total |
|---|---|---|---|
| 1 · The technical substrate | 12 h | 6 h (diagram teardown, ADR) | 18 h |
| 2 · Discovery, scoping & trade-offs | 10 h | 6 h (discovery RFC, decision matrix) | 16 h |
| 3 · Integration & compliance mechanics | 11 h | 5 h (security questionnaire, deployment decision) | 16 h |
| 4 · Evals, acceptance & ROI | 12 h | 8 h (pilot acceptance criteria, ROI model) | 20 h |
| 5 · The FDE flywheel & orchestration | 8 h | 4 h (pattern ledger, productization memo) | 12 h |
| Integration · worked end-to-end case | 4 h | 4 h (Appendix E) | 8 h |
| **Total** | **57 h** | **33 h** | **90 h** |

At 5 hours/week that is ~18 weeks; at 8 hours/week, ~11 weeks. It is designed to be read alongside live work — every field artifact in Module 2–5 has a real engagement it can be used on, and using it on one is worth more than reading the module twice.

### Artifact map

| Module | Field artifact | Where it lives |
|---|---|---|
| 1 | Architecture review record + ADR | `templates/adr.md`, §M1-D protocol |
| 2 | Discovery RFC; feasibility + instrument decision matrix | `templates/fde-discovery-rfc.md`, `templates/feasibility.md` |
| 3 | Enterprise security & data questionnaire; deployment model decision | `templates/enterprise-security-questionnaire.md` |
| 4 | Pilot acceptance criteria; ROI model | `templates/fde-pilot-acceptance-criteria.md`, `templates/cost-model.md`, `templates/production-eval-plan.md` |
| 5 | Pattern ledger; productization memo | `templates/pattern-ledger.md`, `templates/productization-memo.md` |

---

# Module 1 — The Technical Substrate
### What the PM must grasp to earn technical respect

> **Gate owned:** none directly — this module is the substrate all five gates sit on. Its test is social, not procedural: an FDE team decides in the first two design reviews whether the PM's technical comments are worth listening to, and that verdict is expensive to reverse.

---

## 1A · Core PM competencies & mental models

Twelve models. Each is stated as a rule you can say out loud in a design review, with the failure it prevents.

**1. Capability is not reliability.** A model that can do something is not a component you can ship. The gap between "it did that well" and "it does that well 99% of the time, including on inputs it has never seen, at p95 latency inside budget" is where entire engagements die. *Say in the room:* "What's the failure rate, and what does a failure cost the user?" Anyone who cannot answer has not tested it.

**2. The seam is the product.** Enterprise AI value is created at the seam between the client's systems of record and the model's capability — not in the model, which everyone rents from the same three vendors. Consequently the defensible assets are integration, data quality, evaluation, and workflow design. *Prevents:* strategizing about model choice while ignoring the integration that decides success.

**3. Provenance beats model choice.** For any answer the system produces, you must be able to trace: which sources, which retrieval, which prompt version, which model version, which permissions applied at query time. *Say in the room:* "Can we reconstruct why this specific answer was produced, six months from now, for an auditor?" If no: you have a demo.

**4. Pay for determinism where stakes are high.** Non-determinism costs testability. Every non-deterministic step you add (a model call, an agent decision, an LLM judge) is a step you cannot unit-test with certainty. Rules, lookups, and constraints should own the irreversible, monetary, and safety-critical branches. *Prevents:* the "the model told it to issue the refund" incident.

**5. Context is a budget, not a bucket.** Tokens cost money, latency, and accuracy. Longer context is not better context: models attend unevenly across long inputs, and mid-context information is measurably the least reliably used. Everything in the context window (system prompt, retrieved chunks, tool schemas, history) must earn its place. *Say in the room:* "What's our token budget per request by component, and what's the evidence each component helps?"

**6. Agents are state machines, not prompts.** A production agent is an explicit graph: typed state, named transitions, tool contracts, an approval interrupt before consequential actions, a step budget, and a terminal fallback that hands off to a human. *Prevents:* "we gave it tools and let it figure it out" — the design that passes a demo and dies at customer #2.

**7. Contracts over hope.** Every integration needs a named contract — schema, version, owner, error semantics, retry policy, idempotency key, rate limit, and what happens on partial failure. *Say in the room:* "What does the contract say when this call fails halfway through?" Silence here is the most expensive silence in enterprise delivery.

**8. Read the diagram for the data, not the boxes.** Boxes-and-arrows diagrams hide the truth in the arrows. Trace one record end to end: where it originates, what transforms it, what can drop or mangle it, where it is duplicated, what it costs to move, and who owns it at each hop. The PM who can do this aloud is trusted immediately; the one who asks "what does this box do?" is not.

**9. Every integration has an owner problem.** The technical risk is rarely the API; it is *the client's* team, change calendar, upgrade cycle, and ticket queue. On-prem and legacy integrations are staffed by people with other priorities and no incentive to help you. Naming the client-side owner, in writing, in the SOW, is a technical decision.

**10. Latency and cost are product features.** A 6-second answer used 40 times a day is a different product from a 400-millisecond answer used 400 times a day — and a 6-second answer that costs $0.40 per call has a different business case from one that costs $0.004. p95 (not average) is the number users experience; tail latency compounds in agentic loops, where steps multiply. *Say in the room:* "What's the p95 end-to-end, and cost per successful outcome — not per call?"

**11. If you cannot measure it in the client's terms, you cannot accept it.** Every capability needs an evaluation set built from the client's own cases, scored the client's way, with a bar agreed before the first demo. *Prevents:* the "it looks good" acceptance conversation, which is unwinnable.

**12. Pick your rung on the abstraction ladder.** Model → API → application → workflow → ontology/data model. Each rung up is more client-specific and more defensible; each rung down is more reusable and more commoditized. The PM's judgment is which rung the *value* sits on for this client — and which rung the *product* should own next quarter.

---

## 1B · Technical vocabulary & architecture blueprints

Everything below is expected to be usable in conversation without notes. Definitions are one line, deliberately: precision without an essay.

### B1 · Interfaces and integration

| Term | What it is | Why the PM must know it |
|---|---|---|
| **REST** | Resource-oriented HTTP API: verbs (`GET`/`POST`), status codes, statelessness, JSON payloads | The default integration; the PM should read a spec and spot missing pagination, versioning, and rate limits |
| **gRPC** | Binary RPC over HTTP/2 using Protocol Buffers; supports streaming in both directions | Common for internal service-to-service and high-volume paths; the PM should know it means *contract-first* and streaming-capable |
| **GraphQL** | Client-specified query shape over a typed schema | Common in enterprise app layers; watch for query-cost and authorization complexity |
| **Idempotency key** | Client-supplied token so a retried write happens once | The difference between "we sent it twice" and "we charged them twice" |
| **Webhook** | Server-to-server push on an event | Pairs with retries, signatures, and replay — ask about all three |
| **Event stream (Kafka)** | Append-only, partitioned, replayable log; producers/consumers, offsets, consumer groups | Enterprise-scale integration backbone; replayability makes reprocessing possible — a huge eval and audit asset |
| **Schema registry** | Versioned, enforced schemas for messages on a stream | Without it, "the data contract changed and nobody told us" |
| **CDC (change data capture)** | Streaming inserts/updates/deletes out of a database (e.g. Debezium) | The standard, lowest-risk way to get legacy data into a modern pipeline without touching the source app |
| **Batch vs. streaming** | Scheduled bulk transfer vs. continuous | Determines whether the product can promise "within 5 minutes" or "by tomorrow at 6am" |
| **Semantic layer** | Governed, reusable metric/entity definitions over the warehouse | Where "one definition of *active customer*" is enforced; the PM cares because metrics disputes are political, not technical |
| **Ontology / domain model** | Explicit business entities, relationships, and actions over the data | The named rung where enterprise AI earns its keep: decisions and actions attached to modeled objects, not to tables |

### B2 · Data stores & pipelines

| Term | What it is | Why the PM must know it |
|---|---|---|
| **OLTP vs. OLAP** | Row-oriented transactional store vs. column-oriented analytical store | Explains why "just query the production DB for analytics" is refused |
| **Warehouse / lakehouse** | Analytic store (Snowflake, BigQuery, Databricks) / unified lake + warehouse architecture | Where features, retrieval corpora, and eval data come from |
| **Medallion architecture** | Bronze (raw) → silver (cleaned/conformed) → gold (business-level) layering | The vocabulary for "how far along is the data" — most client data starts at bronze and no one says so |
| **ELT / dbt** | Extract-Load-Transform; SQL-based transformation with tests and lineage | Lineage and tests are how you answer "where did this number come from?" |
| **MDM / golden record** | Master data management; the single agreed version of a customer/product | The unglamorous prerequisite for nearly every enterprise AI claim |
| **Data quality / observability** | Freshness, volume, schema, distribution, and null checks with alerts | "The model was wrong" is often "the upstream feed was empty for nine hours" |
| **Vector index** | Approximate-nearest-neighbor structure over embeddings (HNSW, IVF-PQ) | Recall/latency/cost trade-off — a product decision, not just a library choice |
| **ACL-aware retrieval** | Retrieval filtered by the *user's* permissions at query time | The single most common enterprise blocker: an assistant that retrieves everything it can see is a data-leak incident |

### B3 · Model mechanics

| Term | What it is | Why the PM must know it |
|---|---|---|
| **Token** | Sub-word unit of text; the unit of billing, context, and speed | Every cost and latency estimate is a token estimate |
| **Context window** | Maximum tokens the model can attend to in one call | Sets the ceiling on retrieval + history + instructions; forces chunking and summarization strategy |
| **Embedding** | Dense vector representation of text; similarity via cosine/dot product | The basis of semantic retrieval; quality varies by domain, so benchmark on *your* corpus |
| **Chunking** | Splitting documents into retrievable units | Chunk size and overlap are among the highest-leverage quality knobs in a RAG system |
| **Hybrid retrieval** | Keyword (BM25) + dense vectors, fused | Usually beats either alone in enterprise text full of part numbers, SKUs, and acronyms |
| **Reranker** | Cross-encoder that rescores top-N candidates | Cheap quality win: fewer irrelevant chunks in the prompt |
| **Structured output / constrained decoding** | Model output forced to a JSON Schema | Converts "the model said something" into an interface a system can consume; the backbone of reliable automation |
| **Tool / function calling** | Model selects and parameterizes a declared function | How agents act; the tool schema is a contract and needs the same discipline as an API |
| **Prompt caching** | Reusing computed prefix state across calls | Large cost/latency win for long, stable system prompts and document prefixes |
| **Context engineering** | Deliberately assembling the minimum viable context per step; compaction, summarization, tool-result pruning | The discipline that separates agents that survive long sessions from those that degrade |
| **Temperature / sampling** | Randomness control on generation | Extraction wants near-zero; drafting wants some. Wrong setting here looks like "the model is flaky" |
| **Reasoning vs. non-reasoning models** | Models that emit internal deliberation before answering vs. single-pass | Reasoning costs tokens and latency; worth it for planning/analysis, wasteful for classification |
| **Distillation / small-model routing** | Sending easy requests to a cheap model, hard ones to an expensive one | The standard lever for unit economics: FrugalGPT, RouteLLM, Hybrid LLM (see 1C) |
| **Fine-tuning vs. LoRA** | Continued training on your data; low-rank adaptation for cheap variants | Rarely the first lever. It changes *form and tone reliably*; it does not add fresh knowledge as reliably as retrieval |
| **Guardrails** | Input/output policy enforcement: PII redaction, injection screening, topic limits, output validators | The layer that makes an assistant acceptable to SecOps; must be logged, versioned, and owned |
| **Prompt injection** | Untrusted content in the context (a document, an email, a web page) carrying instructions the model may obey | The security failure mode unique to LLM systems: data becomes instructions. Never solve it with prompting alone |

### B4 · Operations & observability

| Term | What it is | Why the PM must know it |
|---|---|---|
| **Tracing** | Per-request span tree over every step: retrieval, prompt assembly, model call, tool call, post-processing (OpenTelemetry semantics) | Without traces, every quality complaint is unresolvable |
| **Prompt / model versioning** | Every artifact that shapes output, under version control and stampable on every result | The prerequisite for rollback and for trustworthy comparisons |
| **Shadow deployment** | New version runs alongside production without serving users | The safe way to evaluate a change before it touches a workflow |
| **Canary** | Roll a change to a small share of traffic with gates | Standard enterprise change-control vocabulary |
| **Drift** | Input distribution, retrieval corpus, or upstream data changing over time | Quality decays without code changing. This is why evals run forever, not once |
| **SLO / SLI / error budget** | Target, measured indicator, and permitted shortfall | The vocabulary that lets a PM negotiate reliability trade-offs instead of arguing feelings |
| **p50 / p95 / p99** | Latency percentiles | p95 is what users feel; p99 is what the client's VIP users complain about; agents multiply steps |
| **Cost per successful outcome** | Total spend ÷ successful completions (not per API call) | The only unit-economics number an executive will accept; retries and failures belong in the numerator |

### B5 · Model selection, routing, and cost cascade

Most pipelines should use *more than one* model. The PM's job is the tier decision per step — made on evidence, not on "we use the best model everywhere."

| Term | What it is | Why the PM must know it |
|---|---|---|
| **Model tier** | Frontier API · mid-tier API · open-weight self-hosted · on-device/small | The four price/quality/latency bands between which every step should be placed |
| **Routing** | Sending each request to the cheapest model that meets its quality bar (classifier-based, preference-based like RouteLLM, or a cascade) | The single biggest cost lever: easy requests are most of the volume and need little of the capability |
| **Cascade / fallback** | Try cheap first; escalate to a stronger model on low confidence, then to a human | Cheaper than always-frontier, and it makes "when we escalate" explicit |
| **Distillation** | Train a small student model on a frontier model's outputs (synthetic labels) | Turns "works sometimes" into "works at a fraction of the cost for this narrow step" — after eval parity |
| **Quantization** | Compressing weights (GGUF/GPTQ/AWQ; 4-bit/8-bit) | The air-gap and on-prem enabler: 4-bit open-weight models run on client hardware |
| **Throughput vs. TTFT vs. cost** | The three-way trade on self-hosted models | Self-hosting is a throughput and operations decision, not just a privacy one |
| **Model abstraction / provider swap** | Keeping the model behind an interface so swaps are configuration | The design that makes routing, fallback, and vendor de-risking possible (ties to 3B and the Intercom case) |
| **Benchmark contamination** | Public leaderboard scores drift as test data leaks into training | Never select a tier on a public benchmark; re-run on *your* golden set (ties to the Leaderboard Illusion in 4C) |

**Which tier for which step — a starting default, always re-verified on your own eval set:**

| Step in the pipeline | Usually wins | Why | Watch out |
|---|---|---|---|
| Intent classification, entity extraction, triage | Small distilled / fine-tuned model | High volume, near-deterministic, latency- and cost-sensitive | Over-modeling a step a rules table does better |
| Retrieval + grounded, cited answer | Mid-tier or frontier API | Retrieval does the heavy lifting; the model summarizes found text | Long contexts → lost-in-the-middle; fix retrieval quality first |
| Complex planning, multi-step reasoning, code synthesis | Frontier reasoning model | Rare and high-stakes; worth the tokens | Cost and latency multiply in agent loops — budget them |
| High-volume, low-stakes generation (drafts, summaries) | Distilled / local open-weight | Cost-per-thousand is the deciding metric | Measure parity on the long tail, not just the average |
| Guardrail / safety screening of inputs and outputs | Small dedicated classifier | Fast, cheap, auditable; a screening model should not be the model it screens | A general model judging itself is blind to its own errors |
| Air-gapped / data-sensitive / regulated | Open-weight self-hosted (weights frozen) | Residency and isolation force it (Module 3) | Frozen weights mean no vendor updates — plan the patch cadence |

**Five rules the PM enforces:**

1. **Never pick a tier without a shared eval set.** Run the candidate model on *your* golden set, on *your* cost and latency budget — not the vendor's benchmark. Procurement is evaluation, not shopping.
2. **Route, don't upsize.** A cascade usually matches always-frontier quality at a fraction of cost. Ask for the routing design before accepting "best model everywhere."
3. **Distill only when form, tone, or format is the problem** (ties to the Module 2 instrument matrix) — and only after the student scores parity with the teacher, including the rare-case slices.
4. **Keep the model behind an abstraction.** A provider swap or tier change should be configuration, not a rewrite (the Intercom rebuild is the cautionary tale — see 3C case 3).
5. **Quantization is the air-gap enabler, not a free lunch.** It unlocks on-prem, but rare-case and safety performance quantize worst — verify them specifically.

References: RouteLLM · FrugalGPT · Hybrid LLM (see 1C); quantization — [huggingface.co](https://huggingface.co/docs/transformers/en/quantization/overview) and [ggml.ai](https://ggml.ai/) · *primary*.

### B6 · GitHub: the delivery surface

FDE work happens inside the client's repository as much as inside the client's systems, so the PM must read that surface fluently — without writing code in it. (One distinction worth keeping straight: **Git** is the version-control system; **GitHub** is a hosted platform built on top of it. Clients may use GitHub, GitLab, or Bitbucket — the concepts transfer, the interface does not.)

| Term | What it is | Why the PM must know it |
|---|---|---|
| **Repository** | The project's code, history, and settings | Where the system being built actually lives; who can access it is a governance question (M3) |
| **Branch** | An isolated line of development | FDE work ships on branches; "which branch is the client running?" is a delivery question, not a trivia question |
| **Commit** | A recorded change with a message | The engineering audit trail — commit messages are the code's changelog |
| **Pull request (PR)** | A proposed change, with diff, discussion, and review | The PM's main engineering surface: reading PRs is how you follow the build without interrupting it |
| **Reviewer / approval / CODEOWNERS** | Required reviewers, sometimes enforced per file path | Maps directly to your RACI — who must approve what, enforced rather than assumed |
| **Merge / squash / rebase** | The ways a change lands on the main branch | Explains "why isn't my fix in yet?" without convening a status meeting |
| **Issue** | A tracked task, bug, or request | Where scope creep becomes visible; the SOW's won't-list belongs here — labeled, and closed with a reason |
| **Label / milestone / project board** | Categorization, grouping by target date, workflow views | Your triage taxonomy (bug · feature · config · product gap · decline) should live in the labels |
| **Actions / CI (continuous integration)** | Automated build, test, and checks on every change | "Is it green?" — CI status is the visible edge of your regression gate (Blueprint 11) |
| **Checks / branch protection** | Required status checks and rules before merge | How a quality gate becomes enforced instead of aspirational |
| **Release / tag / changelog** | A versioned, shipped snapshot | What you tell the client they received — and the anchor for a rollback |
| **Dependabot / secret scanning / security advisories** | Automated dependency, secret, and vulnerability alerts | Security findings that appear on the client's repo; know they exist and who owns the fix |
| **README / wiki / discussions** | Documentation and knowledge surfaces | Where the operating manual and onboarding live — or should, if they don't yet |
| **GitHub Enterprise / self-hosted / SSO** | Client-hosted GitHub running on their identity | Many enterprises require it; it brings residency, access, and audit implications (M3) |
| **Git history / blame / bisect** | The forensic record of what changed, when, and by whom | The instrument for "when did this break?" — pairs with the incident runbook (M4 4D) |

**What the PM actually does in GitHub:** reads pull requests and their summaries (not the code); triages issues, labels them, and closes out-of-scope ones with a reason; asks about red CI the same day rather than at the end of the sprint; reads release notes before telling a client what shipped; checks branch protection and CODEOWNERS when a review gets bypassed under deadline pressure; and never commits to the client's main branch. The repository is the second delivery surface — the one where your decisions become visible to engineers.

### Blueprint 1 — Retrieval-augmented answer service

```
  ┌────────────┐   ┌───────────┐   ┌───────────────┐   ┌──────────────┐
  │ Sources    │──▶│ Ingest &  │──▶│ Chunk + embed │──▶│ Vector index │
  │ (docs, SOR,│   │ normalize │   │ (+ metadata:  │   │ + keyword    │
  │ tickets)   │   │ ACL tags  │   │  ACL, source, │   │ index (BM25) │
  └────────────┘   └───────────┘   │  version)     │   └──────┬───────┘
                                   └───────────────┘          │
  User query ──▶ [Guard: input] ──▶ [Retrieve: ACL-filtered ──┘
                                     hybrid] ──▶ [Rerank top-k]
                                                        │
                ┌───────────────────────────────────────┘
                ▼
        [Prompt assembly: instructions + retrieved chunks + schema]
                ▼
        [Model call: structured output + citations]
                ▼
        [Validate: schema, citation existence, policy] ──fail──▶ [Fallback: refuse or escalate]
                ▼
        [Respond + cite]  ▸ every step logged: prompt version, model version, retrieval IDs, permissions
```

**Failure modes this diagram exists to expose:** retrieval that ignores permissions (leak); citations the model invents (fabrication); stale index (correct answer, last quarter's policy); chunking that splits a table from its header (silent wrongness); no fallback path (confident nonsense instead of a handoff); no trace (unresolvable complaint).

### Blueprint 2 — Agent as an explicit state machine

```
 [Intake] ─▶ [Classify / triage] ─┬─▶ [Simple → direct answer] ──────────────┐
                                  │                                          │
                                  └─▶ [Plan] ─▶ [Tool call (typed schema)] ──┤
                                                   │                         │
                                                   ▼                         │
                                            [Observe / validate result]      │
                                                   │                         │
                                    ┌──────────────┴────────┐                │
                                    ▼                       ▼                │
                            [Retry ≤ N, backoff]   [Verify: policy, state,   │
                                     │              irreversibility]         │
                                     │                      │               │
                                     │            ┌─────────┴─────────┐     │
                                     │            ▼                   ▼     │
                                     │   [HUMAN APPROVAL]      [Compose    │
                                     │    interrupt + resume    response] ──┘
                                     │            │
                                     └────────────┴─▶ [Escalate to human queue]  (budget / step limit / low confidence)
```

**The PM's questions on this diagram:** What is the step budget? What happens at budget exhaustion? Which actions require approval, and what is the SLA on approval? What is the state that persists if the process dies mid-run — and is that state durable or in memory? What is the audit record for an approval? What prevents a tool result from containing instructions (injection) that the agent then executes?

### Blueprint 3 — Enterprise integration and action loop

```
 Systems of record            Data platform                 AI service              Action
 ┌──────────────┐        ┌────────────────────┐      ┌──────────────────┐   ┌──────────────┐
 │ ERP · CRM ·  │──CDC──▶│ Bronze (raw) ──▶   │      │ Retrieval +      │   │ Write-back   │
 │ ticketing ·  │        │ Silver (clean,     │─────▶│ model + guards + │──▶│ to SOR with  │
 │ telemetry    │◀──API──│  conformed) ──▶    │      │ eval logging     │   │ approval +   │
 └──────────────┘        │ Gold (semantic /   │      └──────────────────┘   │ audit trail  │
        ▲                │  ontology)         │              │              └──────────────┘
        │                └────────────────────┘              │                      │
        │                          ▲                        ▼                      ▼
        │                          │                 [Trace store]        [Outcome events]
        └──────────── outcome feedback (closed loop: decisions → results → labels) ────────┘
```

**The PM's questions:** who owns each arrow? What breaks when the SOR vendor upgrades? How long does a correction take to propagate end to end? Can we replay a day of events in a sandbox to test a change? Where does the closed loop's label data come from, and is it consented for that use?
## 1C · Reading list & real-world case studies

**How to read for this role.** Papers at PM depth: abstract, introduction, the figure that shows the method, the results table, the limitations. Engineering posts in full. Case studies with the source label in mind — vendor-published numbers are what the vendor chose to publish, which makes them a claim about positioning as much as about performance.

### Papers and primary technical writing

| Source | Type | Why it earns your time |
|---|---|---|
| Vaswani et al. 2017 — *Attention Is All You Need* · [arxiv.org/abs/1706.03762](https://arxiv.org/abs/1706.03762) | research | The architecture everything you buy is built on; you need the shape of it, not the math |
| Brown et al. 2020 — *Language Models are Few-Shot Learners* · [arxiv.org/abs/2005.14165](https://arxiv.org/abs/2005.14165) | research | Why prompting works at all — and why "in-context learning" is not learning |
| Liu et al. 2023 — *Lost in the Middle* · [arxiv.org/abs/2307.03172](https://arxiv.org/abs/2307.03172) | research | Position-dependent degradation in long contexts; the evidence behind "context is a budget" |
| Lewis et al. 2020 — *Retrieval-Augmented Generation* · [arxiv.org/abs/2005.11401](https://arxiv.org/abs/2005.11401) | research | The pattern that most enterprise assistants still are |
| Malkov & Yashunin — *HNSW* · [arxiv.org/abs/1603.09320](https://arxiv.org/abs/1603.09320) | research | Why vector search is approximate, and what "recall@k" costs you |
| Yao et al. 2022 — *ReAct* · [arxiv.org/abs/2210.03629](https://arxiv.org/abs/2210.03629) | research | The reasoning+acting loop that all agent frameworks implement |
| Wang et al. 2023 — *Survey on LLM-based Autonomous Agents* · [arxiv.org/abs/2308.11432](https://arxiv.org/abs/2308.11432) | research | One-stop map of planning, memory, tool use, and their failure modes |
| Khattab et al. 2023 — *DSPy* · [arxiv.org/abs/2310.03714](https://arxiv.org/abs/2310.03714) | research | Prompt optimization as compilation; the vocabulary for "prompt work is engineering" |
| FrugalGPT · [arxiv.org/abs/2305.05176](https://arxiv.org/abs/2305.05176) · RouteLLM · [arxiv.org/abs/2406.18665](https://arxiv.org/abs/2406.18665) · Hybrid LLM · [arxiv.org/abs/2404.14618](https://arxiv.org/abs/2404.14618) | research | Model routing and cascade economics: how serious teams cut cost without cutting quality |

### Practitioner canon (read in full, no skimming)

| Source | Type | Why |
|---|---|---|
| Anthropic — *Building Effective Agents* · [anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents) | primary | The best short argument for simple, composed patterns over frameworks; read before any agent architecture meeting |
| Anthropic — *Effective context engineering for AI agents* · [anthropic.com/engineering/effective-context-engineering-for-ai-agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | primary | The discipline that makes long-running agents viable |
| Anthropic — *Contextual Retrieval* · [anthropic.com/news/contextual-retrieval](https://www.anthropic.com/news/contextual-retrieval) | primary | A concrete, measured retrieval improvement; a template for "measure the knob" thinking |
| Karpathy — *Intro to Large Language Models* · [youtube.com/watch?v=zjkBMFhNj_g](https://www.youtube.com/watch?v=zjkBMFhNj_g) | primary | The one-hour foundation, still the best |
| Wolfram — *What Is ChatGPT Doing… and Why Does It Work?* · [writings.stephenwolfram.com](https://writings.stephenwolfram.com/2023/02/what-is-chatgpt-doing-and-why-does-it-work) | primary | Intuition for why "it predicts plausible text" produces both capability and error |
| Google — *API Design Guide* · [cloud.google.com/apis/design](https://cloud.google.com/apis/design) | primary | The house style for the interfaces you will be negotiating over |
| ArXiv-style ADRs · [adr.github.io](https://adr.github.io/) · Fowler on ADRs · [martinfowler.com/bliki/ArchitectureDecisionRecord.html](https://martinfowler.com/bliki/ArchitectureDecisionRecord.html) | primary | The decision-record habit this module makes you adopt |
| C4 model · [c4model.com](https://c4model.com/) | primary | A shared vocabulary for "what level of diagram are we looking at?" |
| *Enterprise Integration Patterns* · [enterpriseintegrationpatterns.com](https://www.enterpriseintegrationpatterns.com/) | primary | Names for the messaging problems you will meet for the next decade: routing, transformation, dead-letter, competing consumers |
| Kleppmann — *Designing Data-Intensive Applications* · [dataintensive.net](https://dataintensive.net) | primary | The single best book for the PM who wants engineering credibility about data |
| databricks.com/glossary/medallion-architecture · docs.getdbt.com · databricks.com/research (Lakehouse) | primary/vendor | Where client data actually is, and how it gets trustworthy enough to build on |
| gRPC intro · [grpc.io](https://grpc.io/docs/what-is-grpc/introduction/) · Protocol Buffers · [protobuf.dev](https://protobuf.dev/) · Kafka intro · [kafka.apache.org/intro](https://kafka.apache.org/intro) · Azure Cloud Design Patterns · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/architecture/patterns/) | primary | The interface and streaming primitives; skim the pattern catalogue once so the names are familiar |
| OpenTelemetry docs · [opentelemetry.io/docs](https://opentelemetry.io/docs/) · tiktoken · [github.com/openai/tiktoken](https://github.com/openai/tiktoken) · pgvector · [github.com/pgvector/pgvector](https://github.com/pgvector/pgvector) · MTEB leaderboard · [huggingface.co/blog/mteb](https://huggingface.co/blog/mteb) | primary | Tracing, token counting, vector storage, embedding benchmarks — the four tools that make cost/latency/quality conversations concrete |
| OpenAI — structured outputs · [platform.openai.com/docs/guides/structured-outputs](https://platform.openai.com/docs/guides/structured-outputs) · Prompt caching · [docs.anthropic.com](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching) | primary | The two features that most improve reliability and cost in practice |

### Case studies

Each case is read for one decision-making lesson, not for a summary.

**1 · Palantir — *A Day in the Life of a Forward Deployed Software Engineer*** · [blog.palantir.com](https://blog.palantir.com/a-day-in-the-life-of-a-palantir-forward-deployed-software-engineer-45ef2de257b1) · *primary*
The canonical description of the role you are building a team around. Read it for the *shape of the day*: time with users, time in the data, time negotiating scope. **Hold this question:** in that day, which hours are product work — and who owns them?

**2 · Palantir — *Dev versus Delta: Demystifying engineering roles*** · [blog.palantir.com](https://blog.palantir.com/dev-versus-delta-demystifying-engineering-roles-at-palantir-ad44c2a6e87) · *primary*
Palantir's own split between product engineers ("Devs") and forward-deployed engineers ("Deltas"). **Extract:** the delta role is defined by deployment context, not by seniority — which is why a PM working with them must hold deployment context in their head constantly. **Hold this question:** which of my FDEs' frustrations are actually a missing product road map decision?

**3 · Palantir — *The Baseline Team: forward-deployed infrastructure engineering*** · [blog.palantir.com](https://blog.palantir.com/the-baseline-team-and-forward-deployed-infrastructure-engineering-at-palantir-efd84e72e40b) · *primary*
How Palantir supports a fleet running across cloud providers, on-prem hardware, and government networks. **Extract:** the operational reality behind the phrase "multi-environment" — and the cost of treating on-prem as a detail. **Hold this question:** what would it cost my team to support the environments our sales team is promising?

**4 · Palantir — *Ontology-Oriented Software Development*** · [blog.palantir.com](https://blog.palantir.com/ontology-oriented-software-development-68d7353fdb12) · *primary, opinionated*
An argument that the industry over-invests in components and under-invests in integration, and that the enterprise's modeled entities — the ontology — are the layer where value and defensibility accumulate. **Extract:** the intellectual case for the "seam is the product" model in 1A. **Hold this question:** where is my team's ontology — or are we rebuilding integration glue per client?

**5 · Palantir — *How Foundry's Ontology Deploys Data Science to the Front Line*** · [blog.palantir.com](https://blog.palantir.com/how-palantir-foundrys-ontology-deploys-data-science-to-the-front-line-7a9679bdfd01) · *primary*
Written by a Forward-Deployed Architect: models are only useful when connected to the operational decisions and actions they inform, in a closed loop. **Extract:** the closed-loop argument in Blueprint 3. **Hold this question:** in our last pilot, did we ever learn whether the client's decisions actually changed?

**6 · Uber — *Domain-Oriented Microservice Architecture*** · [uber.com/blog](https://www.uber.com/us/en/blog/microservice-architecture/) · *primary*
Uber's restructuring of thousands of microservices into bounded domains. **Extract:** architecture is an organizational decision; unbounded service graphs become unownable. **Hold this question:** which parts of our client integration are "graph of doom" that nobody owns?

**7 · Uber — *Meet Michelangelo*** · [uber.com/blog](https://www.uber.com/us/en/blog/michelangelo-machine-learning-platform/) · *primary*
The internal ML platform: data management, training, deployment, monitoring as shared infrastructure. **Extract:** what platformization actually means when it works — a paved road, not a library. Compare with your own third-engagement bespoke work (Module 5).

**8 · Uber — *From Predictive to Generative: How Michelangelo Accelerates Uber's AI Journey*** · [uber.com/blog](https://www.uber.com/us/en/blog/from-predictive-to-generative-ai/) · *primary*
How an existing ML platform absorbed generative capabilities. **Extract:** the migration pattern (gateways, evaluation, cost controls) — the same problem your product faces when the model landscape shifts under it.

**9 · Stripe — *APIs as infrastructure: future-proofing Stripe with versioning*** · [stripe.com/blog/api-versioning](https://stripe.com/blog/api-versioning) · *primary*
Versioning as a promise to a decade of integrators. **Extract:** interfaces are long-lived contracts with external parties; the cost of a breaking change is measured in customers, not commits. **Hold this question:** which of our client-specific "temporary" interfaces are now load-bearing?

**10 · Databricks — *Lakehouse* (CIDR paper)** · [databricks.com/research](https://www.databricks.com/research/lakehouse-a-new-generation-of-open-platforms-that-unify-data-warehousing-and-advanced-analytics) · *primary (with vendor interest)*
The argument for one substrate for both analytics and ML rather than duplicated pipelines. **Extract:** "one copy of the data" is an architectural position with real cost consequences — and a vendor position.

**11 · Intercom — *Meet Fin*** · [intercom.com/blog](https://www.intercom.com/blog/announcing-intercoms-new-ai-chatbot/) and *Intercom × Anthropic × AWS* · [aws.amazon.com](https://aws.amazon.com/solutions/case-studies/intercom-anthropic/) · *vendor*
A shipping AI support product described in components: retrieval-only grounding, ~15–20 subcomponents, resolution rate reported at 56% average (up to 80–90% in some deployments) after 30 days. **Extract:** what a *scoped* AI product actually contains — and how the headline "resolution rate" hides the escalation path, the subcomponents, and the definition of "resolved". **Hold this question:** if a vendor quotes a resolution rate at me, what is the denominator?

**12 · Copilot: vendor claim vs. independent study** — GitHub's research post (n=95, task time ~1h11m vs. 2h41m, vendor) · [github.blog](https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness) versus an independent field study finding no statistically significant difference in weekly activity (arXiv:2509.20353). **Extract:** the same product, two credible measurements, different conclusions — because the *design* determines what you can see. This is Module 4 in miniature. **Hold this question:** what measurement design would let me defend a claim to a skeptical CFO?

---

## 1D · The field playbook

### The architecture review protocol (60 minutes, PM-led)

You are not there to review the code. You are there to make sure the *decision* the architecture encodes is one you can defend to the client and to your own product road map. Time-boxed agenda:

| Min | Step | What you are actually doing |
|---|---|---|
| 0–5 | **Frame** | Restate the client outcome and the acceptance definition in one sentence. Everyone re-aligns or the review starts with a correction — both are wins |
| 5–15 | **Data walk** | Trace one record end to end, out loud, on the diagram. Origin, transforms, ownership changes, permissions. This is where 80% of surprises live |
| 15–25 | **Interface contracts** | For each arrow crossing a boundary: schema, version, owner, auth, rate limit, failure semantics, retry/idempotency |
| 25–35 | **Failure drill** | "It's 3am, this component is down / returning garbage / returning plausible-but-wrong data. What does the user see, and who is paged?" |
| 35–45 | **Cost & latency** | Token budget by component, cost per successful outcome, p95 end-to-end. Compare against the business case, not against last quarter |
| 45–50 | **Security & permissions** | Where data crosses a trust boundary; whether retrieval honors the asking user's entitlements; what is logged and for how long |
| 50–58 | **Reversibility** | Which decisions are one-way doors (schema, tenancy model, data residency, vendor lock-in) and which are cheap to change later |
| 58–60 | **Record** | Name the ADRs to be written this week, with owners. No ADR, no decision — it's just a meeting |

### The 14 questions that expose hand-waving

Ask these in the cadence above; the answers tell you whether the plan is real.

**Data (1–4).** 1) Where does this data originate, and does the client own it in writing? 2) What is the freshness requirement, and what actually meets it today? 3) What happens to records that don't fit the schema — dropped, defaulted, or blocked? 4) What is the backfill plan if the pipeline is wrong for a week?

**Model and retrieval (5–7).** 5) What exactly is in the context window, per component, and which of it is evidence-based? 6) What does the system do when confidence is low — refuse, degrade, or guess? 7) What is our evaluation set, how many cases, and who wrote them?

**Failure (8–10).** 8) What is the worst plausible failure, and what does the user see? 9) What is the rollback procedure and how long does it take? 10) What is the client's cure for a wrong action — and is it reversible?

**Operations (11–14).** 11) Who is paged, on what threshold, and with what runbook? 12) What is logged, where, for how long, and who can read it? 13) What is the cost per successful outcome, and what is the sensitivity to usage doubling? 14) What breaks when the client's legacy system upgrades on its own schedule?

If, after these, you still cannot say the plan aloud without hedging, the honest move is not a longer review — it is a two-week spike with a written question it answers. That is a decision the PM makes and funds.

### The instrument triage (draw this on the whiteboard)

```
 Is the input unstructured (text / image / audio / documents)?
   │
   ├─ NO ─▶ Are the decision rules knowable and stable?
   │          ├─ YES ─▶ Is exactness or auditability required?  ──YES──▶ DETERMINISTIC
   │          │                                                    PIPELINE / RULES
   │          └─ NO ──▶ Do we have labels for past decisions?  ──YES──▶ CLASSIC ML
   │                                                                (gradient boosting first)
   └─ YES ─▶ Do we need synthesis, or retrieval of an existing answer?
              ├─ RETRIEVAL ONLY ──▶ SEARCH + RANKING (no generation)
              └─ SYNTHESIS NEEDED ─▶ Can a grounded, cited answer satisfy the bar?
                        ├─ YES ─▶ RAG + EVAL SUITE      ← then measure before adding anything
                        └─ NO  ─▶ Is it FORM/TONE/format that's failing, with data available?
                                    ├─ YES ─▶ FINE-TUNE or DISTILL (small model, narrow task)
                                    └─ NO  ─▶ AGENTIC WORKFLOW WITH HUMAN APPROVAL + GUARDRAILS
                                              (and ask again whether the workflow can be simplified)

 In every branch: is the real constraint process change, not technology? ──▶ NAME IT AND SAY IT OUT LOUD
```

### ADR (Architecture Decision Record) — the habit this module installs

One page per consequential decision, numbered, in the repo, never edited after acceptance (superseded instead). Structure:

```
# ADR-014 — Retrieval uses per-user ACL filtering at query time

Status:  Accepted (2026-09-12)   Supersedes: —   Deciders: [PM, FDE lead, client security]
Context: The assistant answers questions over documents with mixed sensitivity. Retrieval
         currently indexes all documents; any user can receive content from any document.
Decision: Retrieval applies the requesting user's entitlements from the client IdP (group
         membership synced hourly). Index stores ACL tags per chunk; filtering happens before
         ranking. Cache keys include the entitlement set.
Consequences: + Prevents cross-team disclosure, which is the blocker in security review.
              − Retrieval latency +~80ms; entitlement sync lag up to 1h must be documented;
                index size grows ~15% with ACL metadata.
Alternatives rejected: (a) post-filter after ranking — leaks via rank position and wastes
         tokens; (b) separate index per team — 40+ indexes, unmaintainable;
         (c) document-level only — too coarse for shared spaces.
Review date: quarterly, or on any change to the client's group model.
```

The full fill-in version is at `templates/adr.md`. The discipline that matters: **the "Consequences" section is the PM's section.** Costs, trade-offs, and the thing you are giving up are what make an ADR honest — and they are exactly what is missing from most engineering docs.

---

# Module 2 — Client Discovery, Technical Scoping & Architecture Trade-offs

> **Gates owned:** 1 (problem reality) and 2 (instrument choice). This is the module that decides whether the rest of the engagement is worth doing. Its failure mode is not a bad architecture — it is a good architecture for the wrong problem, delivered with a promise nobody can measure.

---

## 2A · Core PM competencies & mental models

**1. The ask is not the problem.** "We want an AI assistant" is a request, not a diagnosis. Behind it is a process, a queue, a cost, a person's week. *Practice:* never leave a discovery session without writing the problem as a sentence containing a number and a name — "*the claims intake team spends 14 hours a week re-keying faxes, and Maria owns that queue.*"

**2. Quantify the status quo before proposing anything.** Without a baseline (volume, cycle time, error rate, cost per transaction, headcount-equivalent), no benefit can ever be proven — and the pilot becomes a taste test. *Say in the room:* "What does this cost you today, per week, in hours or dollars? Who would know?" If nobody knows, the first deliverable is a measurement, not a system.

**3. Value = decision-quality improvement × volume × trust − cost of adoption.** Any factor at zero makes the product zero. A 3% quality improvement at 10,000 decisions a day with high trust beats a 40% improvement at 20 decisions a week with low trust. And adoption cost — training, workflow change, new review steps — is subtracted, not ignored.

**4. Find who loses.** Every automation moves judgment, headcount narrative, or status. The displaced person becomes either your adoption champion or your quiet saboteur, and that is decided in how you design their new role, not in the model. Ask early: *whose job changes, and what do they get instead?*

**5. The SOW is a constraint document first.** Its job is to make the unwritten assumptions written: data access, dependencies, acceptance, out-of-scope, change control, and who owns what. Ambiguity in a SOW does not create flexibility; it creates dispute at exactly the moment the relationship is most fragile.

**6. The "no" is a deliverable.** Saying "this is not an AI problem, here is the number that shows why, and here is the cheaper path" early is the single cheapest trust-building act available to you. Late no's cost deals, reputation, and quarters.

**7. Price the run-rate, not just the build.** Every system has a maintenance cost: evals, monitoring, data fixes, model upgrades, prompt drift, client-side turnover, support. A pilot priced without a run-rate is a subsidy that becomes a resentful internal cost center in month seven. *Frame:* build cost, then monthly run-rate, then the internal owner of that run-rate.

**8. Climb the buy → adapt → build ladder.** Configure an existing product; extend it; integrate it; only then build. Building is justified when the pattern is core to the client's differentiation, when nothing credible exists, or when integration cost dominates either way — and not because it is more fun or more fundable.

**9. Distinguish one-way from two-way doors.** Tenancy model, data residency, identity model, and schema ownership are one-way doors — they are cheap in month one and expensive in month twenty. UI choices, prompt structure, and scoring thresholds are two-way doors and should be decided fast, by whoever is closest.

**10. The complexity budget is finite and it is not yours alone.** Every special case for every client is drawn against future velocity. "Edge-case bloat" is the failure mode where every customer's request is honored and the system becomes unshippable. The PM's counter-move is not refusal; it is *pricing*: "yes — as configuration, at this cost, on this date."

**11. Expectation math: the demo illusion.** A demo can be arranged to look excellent. Pre-agreed acceptance thresholds, on a client-authored test set, are the only defense. Set the bar before the demo, in writing, and the conversation afterwards is arithmetic rather than taste.

**12. The client's process is the spec — the documented one is fiction.** Shadow the work. Watch the spreadsheet, the WhatsApp group, the printer. The gap between the official process and the real one is where your integration complexity and your adoption risk both live.

**13. Fifth-stakeholder discipline.** Procurement, legal, security, data governance, and the client's IT operations appear late and can veto. Bringing them into discovery — as informed participants, not as approvers of a finished plan — compresses weeks of "we didn't know you needed that."

**14. You are negotiating a decision, not a document.** The SOW, the RFC, and the ADR are instruments for aligning people. When they stop aligning and start defending, the PM's job is to get the humans back in a room with the numbers.

---

## 2B · Technical vocabulary & architecture blueprints

### B1 · Discovery instruments and qualification

| Instrument | What it is | What it produces |
|---|---|---|
| **JTBD interview** | Questions about the job the user is trying to get done and the alternatives they use now | The functional/emotional job, and the competition (often a spreadsheet) |
| **Mom Test discipline** | Talk about their life, not your idea; ask about past behaviour and specifics, never hypotheticals or opinions | Evidence that survives the client's politeness |
| **Current-state walkthrough** | Trace one real case through the whole process with the people who touch it | Cycle time, hand-offs, queues, workarounds, data entry points |
| **Time-and-motion / queue observation** | Measured observation of a workflow, timing each step | The baseline numbers that make ROI possible |
| **Artifact archaeology** | Collect the spreadsheets, exports, and shadow databases the process already produces | The real schema, the real exceptions, and who is already maintaining a workaround |
| **Stakeholder map** | Economic buyer, champion, blocker, affected users, security/legal/procurement | The plan for who must be won, and when |
| **Qualification frame (e.g. MEDDPICC)** | Metrics, economic buyer, decision criteria, decision process, paper process, identified pain, champion, competition | Sales-side hygiene; the FDE PM must speak it to avoid surprising the account team — and to avoid being used as free technical cover |
| **Technical feasibility spike** | A short, time-boxed build to answer one named question | Evidence instead of opinion for the architecture review |
| **Data readiness assessment** | Inventory of sources, freshness, quality, access, permissions, and retention | The gate 3 input; the most common reason pilots slip |

### B2 · Scoping documents

| Document | Purpose | Must contain | Owner |
|---|---|---|---|
| **Discovery RFC** | Align internally on what the problem is before promising anything to the client | Problem statement with numbers, users, evidence, current state, constraints, open questions, proposed path, what would make us say no | PM |
| **Feasibility memo** | Set expectations *before* the price | Instrument recommendation with reasoning, what the system will and won't do, risks, data dependencies, effort range | PM + FDE lead |
| **SOW** | The contract: scope in/out, data access, acceptance, metrics, HITL, handoff | See `templates/sow.md`; the measurement section is the part that prevents disputes | PM |
| **ADR** | Record a consequential technical decision and its consequences | Context, decision, consequences (costs named), alternatives rejected | FDE lead; PM reviews |
| **Pilot acceptance criteria** | Define "done" in measurable terms, in advance | Business threshold, quality thresholds, operational thresholds, measurement method, who signs | PM |
| **Change control** | Govern scope movement without damaging trust | What counts as a change, who estimates, who approves, what it costs, what it displaces | PM |

### B3 · The instrument decision matrix

The single most useful artifact in this module. Rows are the criteria that actually decide; columns are the instruments people propose. Score each cell honestly, then let the matrix carry the argument in the room.

| Criterion (in order of how often it decides) | Rules / workflow engine | Classic ML (GBM etc.) | Retrieval / search only | RAG | Fine-tune / distill | Prompt optimization only | Agentic tool use | Human-in-the-loop | Process change |
|---|---|---|---|---|---|---|---|---|---|
| **Labels / ground truth available** | n/a | **Required** | n/a | Partial | **Required (high volume)** | n/a | n/a | n/a | n/a |
| **Tolerance for wrong answers** | Must be ~zero | Low | Low (returns items, human decides) | Low–medium | Low–medium | Medium | Medium | Very low (human decides) | n/a |
| **Auditability / explainability required** | **Best** (rules are readable) | Medium | Good (returned items) | Medium (cite sources) | Poor (opaque weights) | Medium | Poor | **Best** | n/a |
| **Unstructured input** | ✗ | needs features | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | n/a |
| **Freshness requirement** | instant | retrain cycle | index refresh | index refresh | retrain cycle | instant | instant | instant | instant |
| **Latency budget** | ms | ms–s | ms | 1–5 s | 1–5 s | 1–5 s | seconds–minutes | human-scale | n/a |
| **Cost per unit** | ~$0 | ~$0 | low | low–medium | low (inference) + training | low | medium–high | highest | lowest |
| **Time to first version** | days | weeks–months | days | 1–3 weeks | weeks + data work | days | 2–6 weeks | days | days–weeks |
| **Drift risk** | low (until rules change) | medium | low | medium | medium–high | low | high | none | none |
| **Maintenance burden** | low | medium (monitoring, retraining) | low | medium (eval + index) | high (data, retrain, eval) | low | high (tools, prompts, evals) | high (staffing) | process owner |
| **Reversibility** | high | medium | high | high | low | high | medium | high | high |

**How to use it in the room.** Fill the client-facing criteria *with the client's numbers* (tolerance, latency budget, cost ceiling), then show which instruments survive. The matrix turns "we want AI" into "given your tolerance for error and your audit requirement, these three instruments remain — here is what each costs."

**The two rules that keep it honest.** First, require a *deterministic baseline* to be specified for every AI proposal — what would the rules version score? If nobody can say, you do not yet know whether AI is buying anything. Second, require a *retrieval-only* option to be considered whenever the answer already exists somewhere in the client's corpus. Generating a summary of an existing correct answer is often pure cost, latency, and risk.

### B4 · Enterprise system vocabulary

| Term | Meaning | Why it decides architecture |
|---|---|---|
| **System of record (SOR)** | The authoritative store (ERP, CRM, EMR, ITSM) | You integrate *to* it; you generally do not replace it in a pilot |
| **System of engagement** | Where users work (portal, ticketing UI, email, Teams) | Where adoption actually happens; often the real integration point |
| **System of intelligence** | The analytics/AI layer over both | Where your system sits — and it means you are a guest in someone else's architecture |
| **ERP / CRM / ITSM / EMR** | SAP/Oracle; Salesforce/Dynamics; ServiceNow; Epic/Cerner | Each has its own integration religion (IDocs, SOAP, REST, HL7/FHIR) and its own consultant ecosystem |
| **Data gravity** | Data accumulates mass: applications, pipelines, and people gather around it, so moving it is expensive and slow | Explains why "just send us the data" is often a multi-quarter project and why the deployment model is a data decision |
| **MDM / golden record** | Master data management; the agreed authoritative version of an entity | The prerequisite for cross-system answers; without it, the same customer has five identities |
| **CMDB / change advisory board** | Configuration management DB; the board that approves production changes | Your pilot's deployment calendar and code of conduct on a client network |
| **IdP / SSO** | Identity provider (Entra ID, Okta, Ping) and single sign-on | Determines whether the system can honor the user's entitlements — the ACL-aware retrieval requirement |
| **Data residency / sovereignty** | Legal constraints on where data may be processed | Narrows the deployment model before you write any code |

### Blueprint 4 — The three-tier scope ladder

Most disputes come from a client hearing "pilot" and expecting "production." Draw the tiers and price them separately.

```
 TIER 1 · PILOT (weeks)                 TIER 2 · PRODUCTION-READY (1–2 quarters)      TIER 3 · SCALE (ongoing)
 ────────────────────────────────       ──────────────────────────────────────        ─────────────────────────────
 One workflow, one team                 All users in the workflow                     Multi-site, multi-BU, multi-region
 Curated data subset                    Governed, monitored pipelines                 SLA-backed, on-call, capacity planning
 Success measured on 50–150 cases       Golden set + regression gates + drift alerts   Continuous eval, quarterly re-baseline
 Human reviews everything               HITL only on high-stakes actions               Tiered review by risk class
 Hard-coded prompts / model             Versioned prompts, model-pinning, rollback     Model portfolio + routing for cost/quality
 Manual runbook                         Operating manual with named owners             Documented support model + on-call rota
 Security: read-only, sandboxed         SSO, ACL-aware retrieval, audit logs, DLP       Certified (SOC 2 / ISO scope), pen-tested
 Cost: internal estimate                Cost per outcome measured and reported          Unit economics contracted / outcome pricing
 What you are allowed to say:           What you are allowed to say:                    What you are allowed to say:
 "it works on this workflow"            "it works for the team, measurably"             "it works at scale, and here is the number"
```

**The PM's rule:** never let a Tier 1 artifact be described with Tier 2 language. The word "production" is a promise with a price attached.

### Blueprint 5 — Discovery to contract flow

```
 [Client ask]
      │
      ▼
 [Discovery workshop + current-state walkthrough + time & motion]   ──▶ outputs: quantified problem, users, baseline
      │
      ▼
 [Discovery RFC]  (internal: problem, evidence, constraints, what would make us say no)
      │
      ├─▶ "not worth doing" ──▶ [Written no + cheaper alternative]  ←  the deliverable, not a lost deal
      │
      ▼
 [Instrument decision matrix] + [technical feasibility spike if a named question is open]
      │
      ▼
 [Feasibility memo]  (what it will and won't do, effort range, risks)  ──▶ client sees this BEFORE pricing
      │
      ▼
 [SOW: scope in/out · data access · acceptance · metrics · HITL · handoff · change control]
      │
      ├─▶ [ADRs for one-way-door decisions]
      │
      ▼
 [Pilot acceptance criteria, signed before the first demo]  ──▶ Module 4
```

---

## 2C · Reading list & real-world case studies

### Required

| Source | Type | Why |
|---|---|---|
| Kotter 1995 — *Leading Change: Why Transformation Efforts Fail* · [hbr.org](https://hbr.org/1995/03/leading-change-why-transformation-efforts-fail-2) | primary | The canonical anatomy of change failure: no urgency, no coalition, no short-term wins, declaring victory early. Your diagnostic for the third diagnosis |
| Christensen et al. — *Know Your Customers' "Jobs to Be Done"* · [hbr.org](https://hbr.org/2016/09/know-your-customers-jobs-to-be-done) | primary | The framing that surfaces the real job (and the real competitor, usually a spreadsheet) |
| Fitzpatrick — *The Mom Test* (~$10) | book | The discipline that stops discovery from producing polite fiction |
| Anthropic — *Building Effective Agents* · [anthropic.com](https://www.anthropic.com/engineering/building-effective-agents) | primary | The composition-first argument; use it to resist agentic over-scope in SOW conversations |
| Google Cloud — *RAG vs. fine-tuning* · [cloud.google.com/blog](https://cloud.google.com/blog/products/ai-machine-learning/rag-vs-fine-tuning) | vendor | A clear statement of the trade-off from a vendor with both products; read for the structure of the argument, discount the marketing |
| OpenAI — Structured outputs and evaluation best practices · [platform.openai.com](https://platform.openai.com/docs/guides/structured-outputs) · [developers.openai.com](https://developers.openai.com/api/docs/guides/evaluation-best-practices) | primary | The mechanics behind "make the model return something a system can use" and "define done before you build" |
| DSPy · [arxiv.org/abs/2310.03714](https://arxiv.org/abs/2310.03714) · RouteLLM · [arxiv.org/abs/2406.18665](https://arxiv.org/abs/2406.18665) · FrugalGPT · [arxiv.org/abs/2305.05176](https://arxiv.org/abs/2305.05176) | research | Prompt work and model routing as engineering with measurable outcomes — the vocabulary for "this is a cost decision, not a taste decision" |
| SOW and ADR templates · `templates/sow.md` · [adr.github.io](https://adr.github.io/) | primary | The instruments this module produces |

### Case studies

**1 · Intercom Fin — what a scoped AI product actually contains** · [intercom.com/blog](https://www.intercom.com/blog/announcing-intercoms-new-ai-chatbot/) · [aws.amazon.com case study](https://aws.amazon.com/solutions/case-studies/intercom-anthropic/) · [intercom.com: From resolutions to outcomes](https://www.intercom.com/blog/from-resolutions-to-outcomes-evolving-how-fin-delivers-value/) · *vendor*
Fin launched in March 2023 as a retrieval-grounded, source-citing support agent. The AWS case study reports average resolution rates of **56% within 30 days of deployment, with some customers reaching up to 90%**, and more than 4,000 customers. It also documents why the problem was hard: the pipeline had to judge whether a question is answerable, apply support-policy-compliant guidance, and generate the answer — several distinct components, with hallucination protection called out as the central risk. Intercom's own later post reports the average at 76% as Fin took on more complex work. **Read it for three lessons:** (a) a "simple chatbot" is a system of many parts — scope accordingly; (b) a headline metric without its denominator, its customer mix, and its definition of "resolved" is not evidence; (c) the number moves when the definition and the mix move, so pin the definition in the contract.

**2 · Klarna — the vendor claim and the reversal** · [openai.com/index/klarna](https://openai.com/index/klarna/) · [klarna.com press release](https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/) · *vendor*, versus [Forbes, May 2025](https://www.forbes.com/sites/quickerbettertech/2025/05/18/business-tech-news-klarna-reverses-on-ai-says-customers-like-talking-to-people) and [Fortune, May 2025](https://fortune.com/2025/05/09/klarna-ai-humans-return-on-investment) · *independent press*
The 2024 vendor narrative: 2.3M conversations in month one, work equivalent to ~700 agents, resolution time from ~11 minutes to under 2, an estimated $40M profit improvement, two-thirds of chats handled. The 2025 reporting: the company re-hiring humans for quality, with the CEO stating customers prefer talking to people for some interactions. **Read it for the lesson this module exists to teach:** a technically successful deployment can still be a business and change-management problem. Ask of any pilot: what happened to *trust*, *complexity*, and *the humans*, not just to the containment rate? Both the vendor numbers and the reversal are exhibits — and neither tells you what will happen in your client's context.

**3 · Copilot — measurement design decides the conclusion** · [GitHub research post](https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness) · *vendor* · [arXiv:2509.20353](https://arxiv.org/abs/2509.20353) · *research* · [Cui et al., MIT, Microsoft/Accenture RCTs](https://economics.mit.edu/sites/default/files/inline-files/draft_copilot_experiments.pdf) · *research*
The vendor study (n=95, controlled task, ~1h11m vs. ~2h41m) found a large speed-up; an independent longitudinal case study found no statistically significant rise in commit-based activity metrics. Different populations, different tasks, different metrics — and both defensible. **Read it for:** the habit of asking "what exactly was measured, on whom, with what counterfactual?" before repeating any number. This is the intellectual core of Module 4.

**4 · The client ask you will actually receive (composite exercise).** A client's operations director asks for "an AI assistant that answers policy questions to cut ticket handling time." Worked through in Appendix E: discovery produces a quantified baseline; the matrix eliminates fine-tuning and agentic autonomy; the SOW scopes retrieval-only answer-with-citation, 150-case golden set, three-tier HITL, and a change to the *ticket form* that turns out to matter more than the assistant. Use Appendix E as the template for your own first engagement.

---

## 2D · The field playbook

### Discovery workshop agenda (half day, PM + FDE lead)

| Block | Minutes | Content | Output |
|---|---|---|---|
| Frame | 10 | Why we're here, what we will and won't decide today | Shared expectation |
| Current state | 60 | Walk one real case end to end, with the people who touch it. Time each step. Watch for workarounds | Process map + baseline numbers |
| Pain and cost | 40 | Where does it hurt, what does it cost (hours, errors, delay, customer impact), who carries it | Quantified problem statement |
| Data and systems | 50 | Sources, owners, freshness, access path, permissions, residency, retention | Data readiness assessment (feeds Module 3) |
| Definition of success | 30 | What must be true in 90 days for this to have been worth it — with the number | Draft acceptance thresholds |
| Constraints and risks | 30 | Security, legal, procurement, IT change calendar, union/works-council considerations, change management | Risk list with owners |
| Close | 10 | What happens next, by when, and who is the single point of contact on each side | Named owners and dates |

**Two rules.** No demo in the discovery workshop — it short-circuits the diagnosis. And every "we'd need…" gets written as an assumption with an owner, not as an agreement.

### The Discovery RFC (structure)

Fill-in version: `templates/fde-discovery-rfc.md`. Skeleton and the reasoning behind each section:

```
1. Problem statement (with numbers)      — the sentence you'd say to the client's CFO
2. Who is affected, and who loses         — users, displaced roles, champions
3. Evidence                               — quotes, observations, timings, system exports. Labeled by source
4. Current state                          — the real process, including workarounds
5. Constraints                            — data, security, residency, latency, budget, change calendar, politics
6. Instrument analysis                    — the decision matrix, filled with the client's numbers, including a
                                            deterministic baseline and a retrieval-only option
7. Proposed path (and why not the others) — the decision, stated plainly enough to be argued with
8. What would make us say no              — the falsifiable conditions. Writing these is what makes the RFC honest
9. Open questions with owners and dates   — anything unknown, never a blank
10. Estimated effort range                — with the confidence basis, not a single number
```

**Write it before the client sees a proposal.** The RFC is the internal document that lets the FDE lead, the account team, and you disagree *cheaply*.

### The decision matrix, worked (the composite case from Appendix E)

Client numbers gathered in discovery: 4,200 policy tickets/month; median handling 11 minutes; 22% of tickets are the same ~40 questions; the client's compliance team requires **citation to the authoritative policy document**; a **wrong answer is costly** (member-facing); latency expectation is **under 3 seconds**; there is an existing policy corpus in SharePoint with a messy version history.

| Instrument | Survives? | Why |
|---|---|---|
| Deterministic rules / workflow | Partial | Survives for routing and for the 22% of repetitive questions — becomes the *baseline* and the fallback path |
| Classic ML | ✗ | No labels for "correct answer" at volume; the task is retrieval and phrasing, not classification |
| Retrieval / search only | Partial | Survives as the improvement to the current search experience; fails the client's requirement for a *phrased, cited* answer |
| RAG (retrieval + generation with citation) | **Yes** | Meets citation, latency, and freshness requirements; corpus already exists; maintainable with an eval suite |
| Fine-tune | ✗ | Would not fix the freshness problem (policy changes quarterly) and cannot provide citations; training data would be answers the client does not have |
| Prompt optimization only | ✗ | No grounding; fails the citation requirement |
| Agentic tool use | ✗ (this phase) | Adds irreversibility and latency with no requirement behind it; revisit for ticket *actions*, not answers |
| Human-in-the-loop | **Yes** | Three tiers: auto-answer with citation (low stakes), review-before-send (medium), escalate (high) |
| Process change | **Yes** | The discovery finding: tickets are mis-routed because the intake form has 4 free-text fields; fixing the form is a prerequisite, not an add-on |

The RFC's recommendation writes itself: *RAG answer-with-citation, retrieval-only fallback, rules-based routing, a 150-case client-authored golden set, three HITL tiers, and an intake-form change that ships in the same quarter.* That is a scope a client can sign — and a scope your FDEs can build.

---

# Module 3 — Enterprise Integration & Compliance Mechanics

> **Gate owned:** 3 (data and access feasibility). This is the module where promising pilots die — not because the model was wrong, but because the data could not legally or technically reach it, the deployment model was decided by sales, or no one designed how permissions would survive retrieval. The PM who owns this module is the reason the pilot reaches production.

---

## 3A · Core PM competencies & mental models

**1. Compliance is architecture.** Security and privacy requirements are design inputs, not a review you pass at the end. Every one of them changes the shape of the system — which is why the security reviewer belongs in discovery, not in the last week of the pilot.

**2. Draw the trust boundaries first.** Each boundary crossing is a controlled interface: authentication, encryption, logging, DLP, and an owner. Most enterprise AI risk is a box in the wrong place relative to a boundary, not a missing control.

**3. Least privilege is a design property.** Narrow scopes, purpose-named service accounts, short-lived credentials, no shared "integration user." The question that finds problems: *what is the maximum damage this credential could do if it were stolen, and how would we know?*

**4. "Who can see what" is the product question.** If retrieval honors only the service account's permissions, every user sees everything the system can see. That is a data-protection incident waiting for the first internal audit. Permission-aware retrieval is non-negotiable in multi-team enterprises.

**5. Residency and sovereignty decide the deployment model before the architecture.** If the data may not leave a country, a region, or the client's network, then the model provider, the control plane, and the telemetry path are all constrained — and retrofitting those constraints later is a rebuild.

**6. Air-gap changes everything.** No fetching dependencies, no vendor telemetry, offline model weights, updates by sneakernet or a managed pipeline, longer patch cycles, and hardware limits that determine what models are even possible. The PM's job is to know the cadence implied by the client's environment *before* promising a delivery date.

**7. Auditability means reconstructing any decision later.** For every consequential output: what went in, which versions produced it, whose entitlements applied, who approved, and what changed as a result. If that cannot be answered six months later, the system is not enterprise-ready no matter how good it looks.

**8. Retention and deletion are features, not policy documents.** Right-to-erasure, legal hold, and index/cache propagation interact: deleting a record from the system of record does not delete the embedding, the cached prompt, the log, or the fine-tune. Design the deletion path end to end, or the first erasure request becomes an incident.

**9. Vendor terms are part of the architecture.** Is training on your data allowed? What is the retention window? Where is data processed? Who are the subprocessors? Is there an opt-out, and does it survive a model upgrade? These are contract questions with engineering consequences — get them answered in writing, per environment.

**10. Blast radius is a design decision.** Ask what the system can change irreversibly: send an email, issue a credit, close a ticket, update a record. Then design approval, reversibility, and rate limits around exactly those actions. Everything else can be loosened.

**11. Inherit the client's controls; do not rebuild their programme.** Enterprises already run SOC 2, ISO 27001, or a sector framework. Your job is to produce *evidence mapped to their controls* — not to invent a parallel model. The faster you can say "here is the artifact for your control X," the faster you ship.

**12. Compliance has a price — quote it.** Penetration tests, audit scope extensions, legal review cycles, evidence automation, additional tenancy, and slower releases are costs. Unpriced compliance is how pilots exceed budget without anyone having made a decision.

**13. Agents add a new class of security failure.** Retrieved content becomes instructions (prompt injection), tools can be abused beyond their intent, and an agent with network access can exfiltrate. Treat retrieved text as untrusted data, tools as privileged capabilities, and egress as a controlled boundary.

**14. The client's security team is your co-designer.** Bring them the data-flow diagram early and ask what would make them comfortable. Most security teams say yes to well-designed systems and no to surprises — and their sign-off, earned in month one, is worth more than any feature you could add later.

---

## 3B · Technical vocabulary & architecture blueprints

### B1 · Identity and access

| Term | What it is | Why it decides your design |
|---|---|---|
| **OIDC / OAuth 2.0** | Identity layer (tokens, claims) and the authorization framework (scopes, grants) | How the system learns who the user is and what they may do |
| **SAML** | Legacy enterprise SSO assertion protocol | Still dominant in some client estates; expect to support both |
| **SCIM** | Standard for provisioning/deprovisioning users and groups | Group sync is what makes ACL-aware retrieval possible; deprovisioning is what makes it safe |
| **Service account / workload identity / mTLS** | Non-human identities and mutually authenticated machine connections | Integrations should not impersonate a human; audit trails depend on this |
| **RBAC / ABAC / ReBAC** | Role-based, attribute-based, relationship-based access control | RBAC for coarse roles, ABAC for context (region, clearance, department), ReBAC for "who reports to whom / who is on the deal" |
| **ACL-aware retrieval** | Filtering retrieved content by the requesting user's entitlements | The pattern that prevents the assistant from becoming a disclosure channel |
| **Row/column-level security** | Enforcement inside the data platform | Often already exists in the client's warehouse — reuse rather than reinvent |
| **Tenant isolation (silo / pool / bridge)** | Separate infrastructure per tenant, shared with logical separation, or hybrid | A one-way door: cheap now, expensive later |
| **JIT / just-enough access** | Time-boxed, approved elevation | The language security teams want to hear for admin and support paths |
| **KMS / CMEK / BYOK** | Key management, customer-managed keys, bring-your-own-key | Frequently the difference between an approved and a rejected deployment |
| **Secrets management** | Vault/KMS-backed credentials, rotation, no secrets in prompts or repos | "The API key was in the system prompt" is an instant finding |

### B2 · Deployment and network

| Term | What it means | Implication |
|---|---|---|
| **SaaS multi-tenant** | Shared infrastructure, logical isolation | Fastest, cheapest; may fail residency or isolation requirements |
| **Dedicated tenant / single-tenant VPC** | Isolated network and storage per client | Common enterprise compromise; higher cost and operational burden |
| **Private connectivity** | PrivateLink / VPC Service Controls / private endpoints | Keeps traffic off the public internet — often a hard requirement |
| **Control plane / data plane split** | Vendor manages orchestration; data and compute stay in the client's environment | The standard pattern for regulated clients; requires a disciplined release process |
| **On-premises** | Runs in the client's data centre | Client controls patching and hardware; expect slow upgrades and capacity surprises |
| **Air-gapped** | No network path out | Offline model weights, offline updates, no vendor telemetry, sneakernet cadence, hardware-bound model choice |
| **Egress allow-list** | Explicit outbound destinations | Constrains model providers and third-party services to named endpoints |
| **FedRAMP / IL levels** | US government authorisation tiers | Determines whether you can even bid on some public-sector work; authorisation takes quarters |
| **Data residency** | Legal/contractual location constraints | Determines region strategy, model availability, and support staffing |

### B3 · Data protection and governance

| Term | What it is | Why the PM needs it |
|---|---|---|
| **Data classification** | Public / internal / confidential / restricted, with handling rules | Drives what may be sent where; the basis of every design argument |
| **PII / PHI / PCI / CPNI** | Personal, health, card, and communications data categories | Each carries distinct rules and disclosure duties |
| **Pseudonymization / tokenization** | Replacing identifiers with tokens, reversibly under control | Enables usefulness without raw identifiers in prompts; the standard redaction pattern |
| **Redaction boundary** | The line beyond which no raw identifiers cross (Presidio-style detection) | The single most useful thing to draw in a security review |
| **DLP** | Data loss prevention scanning at egress | Often already deployed by the client; your system must survive it |
| **Encryption at rest / in transit / CMEK** | Standard protections, customer-managed keys | Table stakes in enterprise reviews |
| **Retention schedule / legal hold** | How long data lives; what cannot be deleted | Conflicts with erasure requests; needs legal input, not engineering guesses |
| **Right to erasure / DSAR** | Deletion and access rights (GDPR-style) | Requires a designed deletion path across store, index, cache, and logs |
| **Purpose limitation / consent** | Data used only for declared purposes | Determines whether pilot data can train anything (usually: no) |
| **DPIA / DPA / subprocessor register** | Impact assessment, data processing agreement, list of third parties | The paperwork that gates launch in EU contexts; the PM should know which one is missing |
| **Lineage / data-flow map** | Where data comes from and goes | The artifact that makes security review fast |

### B4 · Standards, frameworks, and rules the PM should be able to name

| Framework | What it covers | Why it appears in your engagements |
|---|---|---|
| **SOC 2 (AICPA)** | Trust services criteria: security, availability, processing integrity, confidentiality, privacy; Type I point-in-time vs. Type II over a period | The default enterprise assurance question; your client will ask for your report and expect evidence for their scope |
| **ISO/IEC 27001 / 27017 / 27018** | Information security management; cloud-specific; cloud privacy | Common in European, government, and large-enterprise procurement |
| **ISO/IEC 42001:2023** | AI management system (AIMS) requirements | The AI-specific management standard now appearing in enterprise questionnaires |
| **NIST AI RMF 1.0 + Generative AI Profile (NIST AI 600-1)** | Voluntary AI risk framework: govern, map, measure, manage; GenAI-specific risks | The vocabulary for AI risk conversations with US enterprises and agencies; the playbook is the practical companion |
| **NIST SP 800-162 (ABAC) / SP 800-207 (Zero Trust)** | Attribute-based access control guidance; zero-trust architecture | How security architects describe the access model you must fit into |
| **NIST SP 800-53 / 800-171 / CMMC** | Control catalogues; federal contractor requirements | Appears whenever the client is a defence or federal contractor |
| **EU AI Act** | Risk-tiered regulation: prohibited practices, high-risk systems with conformity obligations, transparency duties, general-purpose model obligations, phased application | Determines whether your use case carries documentation, human-oversight, and logging duties in the EU |
| **GDPR** | Lawful basis, transparency, data-subject rights, DPIA, restrictions on solely automated decisions | The most common legal frame for European personal data; also the template many other jurisdictions copy |
| **HIPAA (Privacy, Security, Breach Notification Rules)** | US health data | Sets the bar for PHI: BAAs, minimum necessary, audit controls |
| **Sector rules** | PCI DSS (cards), GLBA (finance), FERPA (education), FedRAMP (US federal) | Determine whether the engagement is even addressable with your deployment model |
| **OWASP Top 10 for LLM Applications** (2025 list) | The reference list of LLM application risks: prompt injection, sensitive information disclosure, supply chain, data and model poisoning, improper output handling, excessive agency, system prompt leakage, vector and embedding weaknesses, misinformation, unbounded consumption | The checklist a security team will run; the PM should be able to map each item to a design decision in the architecture |
| **CISA/NCSC *Guidelines for Secure AI System Development*** | Joint secure-by-design guidance for AI systems | The most useful cross-government articulation of secure AI design; good source for review questions |
| **AWS SaaS Tenant Isolation Strategies / Azure tenancy models** | Practical isolation patterns per layer | The vocabulary for "how isolated is isolated?" in a review |

### Blueprint 6 — Deployment model decision

|  | SaaS multi-tenant | Dedicated tenant / single-tenant VPC | On-premises (client data centre) | Air-gapped |
|---|---|---|---|---|
| **Data residency** | Region-selectable; data leaves client's estate | Region-pinned; data in client's cloud estate | Fully in client's estate | Fully isolated |
| **Isolation** | Logical (shared infra) | Physical/logical per tenant | Full | Full |
| **Update cadence** | Continuous | Weekly/continuous with client windows | Monthly–quarterly; client-approved changes | Quarterly+; offline packages |
| **Ops burden on you** | Lowest | Medium | High (remote access, debugging) | Highest |
| **Compliance evidence** | Your certifications | Your certifications + client's controls | Client's controls; you supply documentation | Client's controls; documentation only |
| **Model options** | Frontier APIs | Frontier APIs, private endpoints, some open weights | Open-weight models sized to their hardware | Open-weight only, frozen versions |
| **Typical client** | Mid-market, low-sensitivity | Regulated enterprise, multi-team | Government, defence, hospital systems | Defence, intelligence, some industrial |
| **Watch out for** | Residency and isolation objections | Cost per client; tenancy sprawl | Client change control; hardware limits | Model quality parity; support expectations |

**The PM's move:** decide the model *with the client's security lead present*, in discovery, and write it into the SOW. Deployment model is the decision most often made implicitly by whoever wrote the proposal — and the most expensive one to reverse.

### Blueprint 7 — Identity and permission-aware retrieval

```
  Client IdP (Entra ID / Okta)                    Entitlement service
   groups · roles · clearances   ──── SCIM ────▶  sync (hourly) + on-demand check
        ▲                                                │
        │ (user logs in via OIDC)                        ▼
  ┌───────────┐     query + identity context      ┌──────────────────────┐
  │  User     │──────────────────────────────────▶│ Retrieval gate:      │
  └───────────┘                                   │ filter candidates by │
                                                  │ user's entitlements  │
   Index (per chunk: source, version, ACL tags) ◀──┤ BEFORE ranking       │
                                                  └──────────┬───────────┘
                                                             ▼
                                          [Prompt: retrieved chunks + cited sources]
                                                             ▼
                                          [Answer + citations, logged with: user, entitlement set,
                                           entitlement-sync timestamp, retrieval IDs, model/prompt version]
  Cache key MUST include the entitlement set ── otherwise user B receives user A's cached answer.
```

**The four traps.** (1) Post-filtering after ranking — leaks through rank position, and wastes prompt tokens on content the user may not see. (2) Stale entitlements — someone who changed teams yesterday can still retrieve their old team's documents until sync runs; state the lag and, where it matters, check on demand. (3) Caches without entitlement in the key — a cross-user leak with an innocuous cause. (4) Object-level gaps — document-level ACLs are often too coarse for shared spaces; check whether the client has object-level permissions at all before promising them.

### Blueprint 8 — Data flow with trust boundaries

```
 ┌─────────────────────────── CLIENT TRUST BOUNDARY ───────────────────────────┐
 │  Systems of record  →  staging/curated zone  →  [REDACTION BOUNDARY]        │
 │        (raw PII)            (raw PII)              │  pseudonymized,         │
 │                                                    │  minimized fields,      │
 │                                                    │  provenance retained    │
 └────────────────────────────────────────────────────┼─────────────────────────┘
                                    encrypted in transit (TLS, private endpoint)
                                                      ▼
                      ┌───────────────────────────────┴──────────────────────────────┐
                      │  YOUR CONTROL PLANE   (metadata, orchestration, logs)         │
                      │  no raw client data beyond what policy permits; tenant-tagged │
                      └───────────────────────────────┬──────────────────────────────┘
                     egress via allow-listed endpoints; every call logged and costed
                                                      ▼
                      ┌──────────────────────────────────────────────────────────────┐
                      │  MODEL PROVIDER (or in-estate open weights, if residency rules)│
                      │  contract terms: no training on inputs · zero/limited retention│
                      │  · region pinned · subprocessor list current                   │
                      └──────────────────────────────────────────────────────────────┘
```

**The PM's checklist on this diagram:** what exactly crosses each boundary (field by field)? What is the justification for each field? Who can read the logs? How long are they retained? What is the deletion path for each store? What happens if the provider's terms change?

### Blueprint 9 — Agent tool security model

```
 Retrieved/untrusted content ──▶ [treat as DATA, never instructions]
                                     │  provenance tags on every chunk
                                     ▼
                         [Input screening: injection patterns, instruction-like content]
                                     │
                     ┌───────────────┴────────────────┐
                     ▼                                ▼
          [Read-only tools]                 [Write / consequential tools]
           scoped tokens                     approval interrupt · rate limits ·
           narrow schemas                    reversibility · idempotency key ·
           no egress                         audit record of approver + payload
                     │                                │
                     └──────────────┬─────────────────┘
                                    ▼
                     [Output validation before acting: schema, allow-list of permitted
                      targets, value-range checks, no raw model text executed as code]
                                    ▼
                     [Egress control: only allow-listed destinations; log every outbound call]
```

**The five agent-specific controls to demand:** (1) untrusted content never treated as instructions; (2) tool scopes narrower than the agent's apparent need; (3) every consequential action behind an approval or an explicit policy with an audit record; (4) egress allow-list, so an injected instruction cannot exfiltrate; (5) a step/token budget, because "unbounded consumption" is both a security and a cost finding.

---

## 3C · Reading list & real-world case studies

### Required

| Source | Type | Why |
|---|---|---|
| OWASP — *Top 10 for LLM Applications* · [genai.owasp.org/llm-top-10](https://genai.owasp.org/llm-top-10/) | standard | The checklist security teams actually run. Map each item to a design decision in your architecture before review |
| NIST — *AI Risk Management Framework* · [nist.gov/itl/ai-risk-management-framework](https://www.nist.gov/itl/ai-risk-management-framework) · *Playbook* · [nist.gov](https://www.nist.gov/itl/ai-risk-management-framework/nist-ai-rmf-playbook) · *Generative AI Profile (NIST AI 600-1)* · [nvlpubs.nist.gov](https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.600-1.pdf) | standard | Govern/map/measure/manage gives you the structure for an AI risk register a client's risk function will recognise |
| CISA/NCSC — *Guidelines for Secure AI System Development* · [cisa.gov](https://www.cisa.gov/news-events/news/dhs-cisa-and-uk-ncsc-release-joint-guidelines-secure-ai-system-development) | standard | Secure design/development/deployment/operation questions, phrased in a way non-specialists can use in reviews |
| ISO/IEC 42001:2023 · [iso.org/standard/42001](https://www.iso.org/standard/42001) | standard | If your client's questionnaire mentions AI governance, this is the standard they mean |
| AICPA — SOC suite · [aicpa-cima.com](https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2) · AWS SOC FAQ · [aws.amazon.com/compliance/soc-faqs](https://aws.amazon.com/compliance/soc-faqs/) · Google Cloud SOC 2 · [cloud.google.com](https://cloud.google.com/security/compliance/soc-2) | standard/primary | The assurance artifacts you will be asked to provide, map, or inherit |
| AWS — *SaaS Tenant Isolation Strategies* · [docs.aws.amazon.com](https://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/saas-tenant-isolation-strategies.html) · Azure — *Tenancy models* · [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/considerations/tenancy-models) | primary | The isolation vocabulary you need the day a client asks "are we separate?" |
| NIST SP 800-162 (ABAC) · [csrc.nist.gov](https://csrc.nist.gov/pubs/sp/800/162/upd2/final) · SP 800-207 (Zero Trust) · [csrc.nist.gov](https://csrc.nist.gov/pubs/sp/800/207/final) | standard | The access-model vocabulary used by the architects reviewing your design |
| EU AI Act · [artificialintelligenceact.eu](https://artificialintelligenceact.eu/) · GDPR text · [gdpr-info.eu](https://gdpr-info.eu/) · HHS HIPAA · [hhs.gov/hipaa](https://www.hhs.gov/hipaa/index.html) | standard | The regulatory frames that decide documentation, oversight, and logging duties — read the risk tiers, not the whole regulation |
| Presidio · [microsoft.github.io/presidio](https://microsoft.github.io/presidio/) · NeMo Guardrails · [github.com/NVIDIA/NeMo-Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) | primary | The concrete implementations of redaction and guardrails you will cite to security teams |
| AWS — *Well-Architected Framework* (security pillar) · [aws.amazon.com/architecture/well-architected](https://aws.amazon.com/architecture/well-architected/) | primary | The review-question style that makes design reviews productive |

### Case studies

**1 · Palantir — *The Baseline Team: forward-deployed infrastructure engineering*** · [blog.palantir.com](https://blog.palantir.com/the-baseline-team-and-forward-deployed-infrastructure-engineering-at-palantir-efd84e72e40b) · *primary*
Read this one specifically for the *environment* problem: the same product running across multiple clouds, on-prem hardware, and government networks, with a dedicated team whose job is keeping that fleet operable. **Extract:** multi-environment support is a product cost with a team attached — if your company promises on-prem without such a team, the PM is the person who has to say so.

**2 · Palantir — *Foundry documentation*** · [palantir.com/docs/foundry](https://www.palantir.com/docs/foundry/) · *primary*
Skim the deployment and security sections for how a platform vendor describes tenancy, access control, and auditability to enterprise buyers. **Extract:** the vocabulary and the degree of specificity a serious security organisation expects. **Hold this question:** could my team produce a page like this for our system today?

**3 · Intercom Fin on Amazon Bedrock / Anthropic** · [aws.amazon.com](https://aws.amazon.com/solutions/case-studies/intercom-anthropic/) · *vendor*
A shipping AI product that had to satisfy enterprise customers on model choice, data handling, and vendor relationships — including moving model providers and rebuilding substantial parts of the system. **Extract:** model vendors are replaceable *if* you designed the abstraction early; the compliance conversation is easier when the model layer is swappable and the data path is owned by you.

**4 · Scenario: "our security team will not approve sending data to any model provider."** A composite you will meet in some form. The resolution that works is rarely an argument — it is a design: (a) redact/pseudonymize before the boundary (Presidio-style), (b) run open-weight models in the client's estate for the sensitive path, with the frontier model reserved for the non-sensitive path, (c) prove *eval parity* between the two paths rather than assuming the smaller model is worse, and (d) put retrieval and logging in the client's estate so only the minimum text crosses. This is expensive, slower, and often the only viable path — and the PM who proposes it in discovery, with numbers, wins the account.

---

## 3D · The field playbook

### The enterprise security & data questionnaire

Full fill-in version: `templates/enterprise-security-questionnaire.md`. The PM should be able to answer all of these from the architecture, not by asking an engineer. Grouped as they arrive in real reviews:

**Identity & access (1–6).** 1) How do users authenticate, and is SSO/MFA enforced? 2) How are entitlements established, and how quickly does a change (role change, departure) take effect? 3) Does retrieval respect the requesting user's entitlements — and where in the pipeline? 4) What service identities exist, with what scopes, and who rotates their credentials? 5) Can administrators read customer content, and is that access logged and approved? 6) Is there support for customer-managed keys?

**Data handling (7–14).** 7) What data categories flow through the system (PII, PHI, PCI, confidential)? 8) Where is each field processed (in-estate, your cloud, provider)? 9) What is redacted or pseudonymized, at which boundary, and how is it validated? 10) What are retention periods per store (source, index, logs, traces, caches, backups)? 11) What is the deletion path for an erasure request, and how is it verified? 12) Are prompts/outputs used to train anything — by you or any provider? 13) What is the data-flow map, field by field? 14) What happens to client data at contract end?

**Model and application security (15–21).** 15) How is prompt injection mitigated — what happens when a retrieved document contains instructions? 16) What are the egress destinations, and who approves changes? 17) What are the tools the system can call, with what scopes? 18) What output validation runs before any action is taken? 19) How are system prompts protected — and do we accept that they may leak? 20) What are the rate/step/cost limits that bound consumption? 21) What is the model/vendor supply-chain posture (versioning, provenance, ability to swap)?

**Operations & assurance (22–30).** 22) What is logged per request, where, and who can read it? 23) How are prompt/model versions recorded and rolled back? 24) What monitoring and alerting exist, with what thresholds? 25) What is the incident response process and past evidence? 26) What penetration tests and red-team exercises have been run, and what was found? 27) Which certifications (SOC 2 Type II, ISO 27001/42001, FedRAMP) apply, and to what scope? 28) What is the subprocessor list, and how are changes notified? 29) What is the SLA, and what are the availability and support commitments? 30) What is the audit evidence path for the client's own controls (artifact per control)?

**Discipline:** any answer you cannot give from the architecture is a finding. Record it as an open item with an owner and a date — that is the artifact that turns a security review from an ambush into a checklist.

### Compliance readiness matrix (fill one per engagement)

| Client control / requirement | Our artifact | Owner | Status | Date | Gap → action |
|---|---|---|---|---|---|
| SSO + MFA enforced for all users | OIDC integration config; IdP metadata | FDE lead | ✓ | — | — |
| Least-privilege service identities | Access inventory + rotation policy | FDE lead | ◐ | — | rotate legacy integration key |
| Permission-aware retrieval | Blueprint 7 + ADR-014; test evidence | FDE lead | ✓ | — | — |
| Data residency in [region] | Deployment model: dedicated tenant in-estate | PM | ✓ | — | — |
| Erasure / DSAR within N days | Deletion runbook + verification script | PM | ◐ | — | index + cache deletion not yet tested |
| No training on client data | Vendor terms extract + DPA clause | Legal | ✓ | — | — |
| AI governance (ISO 42001 / client policy) | AI risk register mapped to client's controls | PM | ○ | — | map register to control IDs |
| Pen test before production | Scope + provider + date | Security | ○ | — | book |

Legend: ✓ evidenced · ◐ partial · ○ not started. The matrix is the PM's instrument — it is a schedule, not a form.

### Prompt-injection and abuse test plan (outline)

Run before production, on the real system, with results in writing:

1. **Direct injection** — user turns: instructions that attempt to override policy, reveal the system prompt, or extract data.
2. **Indirect injection** — plant instructions in a retrieved document, a ticket body, a filename, a calendar invite, a web page the agent browses; verify they are treated as data.
3. **Tool abuse** — attempt to call tools with out-of-scope parameters, chain tools to reach a forbidden destination, or use an allowed tool to read another team's content.
4. **Data exfiltration** — attempt to encode sensitive content into a URL, a markdown image, a log field, or an outbound call.
5. **Resource exhaustion** — long loops, recursive tool use, oversized inputs; verify step and cost limits fire and fail safely.
6. **Cross-tenant / cross-user probes** — with two accounts at different entitlement levels, attempt to retrieve the other's content (including via cache).
7. **Failure honesty** — force failures of each dependency and verify the user sees a safe, truthful message rather than a confident wrong answer.

**The pass criterion is not "nothing got through."** It is: every attempt is either blocked or detected-and-logged, and the response to detection is defined.

---

# Module 4 — Quality Assurance, Evals & ROI Metrics (Defining "Done")

> **Gate owned:** 4 (eval and acceptance). Everything before this module produces a system. This module decides whether anyone can *prove* it works, whether the client will sign, and whether the next engagement — or the next quarter's budget — happens.

---

## 4A · Core PM competencies & mental models

**1. Evals are the specification.** A requirement that cannot be evaluated is a wish. When the client says "it should be accurate," the PM's translation is: *on N cases drawn from your own history, scored this way, by this judge, with this threshold, measured on this date.* Writing the eval *is* writing the spec — and it is the PM's job, not the engineer's.

**2. Define done before the demo.** A demo can always be arranged to look good. A pre-agreed bar, on a client-authored set, cannot be moved afterwards. The single most valuable sentence in a pilot contract: "the system meets the agreed thresholds on the client's golden set by [date], measured by [method]."

**3. Four layers of evaluation, all necessary.** (i) *Component* — does retrieval find the right context; does the parser extract the right fields. (ii) *Task* — does the end-to-end answer meet the bar on the golden set. (iii) *Regression* — does this change break anything that worked yesterday. (iv) *Online* — do users and business metrics move in production. Teams that only build layer (ii) cannot explain failures or prevent regressions.

**4. Build the golden set from the client's cases, in the client's vocabulary, with the client's definition of "right."** If your team authors the test set alone, you have authored the answer to "is it good?" — and the client will not accept it. Co-authoring is also the fastest way to surface disagreement about the requirement itself.

**5. Judge the judge.** LLM-as-judge scales evaluation but inherits biases: it can favour longer answers, prefer its own family's style, and be swayed by position in a comparison. Pairwise comparisons are generally more reliable than absolute scores. Human-calibrated agreement must be measured and re-measured — and the calibration number is what makes judge-based results quotable.

**6. Abstention is a feature.** A system that says "I don't know, here is the source, here is the escalation path" is more valuable than one that always answers. Measure refusal/escalation rates *and* their correctness: false refusals destroy trust as efficiently as wrong answers.

**7. Choose thresholds by cost of error, not by ambition.** The right target is stated jointly: *"auto-answer 60% of volume at a false-answer rate below 1%"* — because precision at an automation rate is the only form of this promise that survives contact with an operations budget. Ask: what does one wrong answer cost, in money, in trust, in regulatory exposure? Then set the threshold.

**8. Measure the business, not the model.** Model quality is an instrument reading. The client buys cycle time, resolution rate, error rate, cost per transaction, and revenue. Report both, always in that order (business first), and never present a model metric as if it were an outcome.

**9. Baseline first, or you have no claim.** The counterfactual — what the client's process does today — is the denominator of every ROI statement. Without it, improvements are anecdotes. Establish the baseline *before* the intervention, in writing, ideally from the client's own systems.

**10. Attribution discipline.** A pilot runs alongside training, a process change, and seasonality. If you cannot isolate your effect, report the pattern honestly: what moved, what else moved at the same time, and what would falsify your explanation. Executives forgive uncertainty; they do not forgive being misled.

**11. Instrument the cost side as carefully as the value side.** Cost per successful outcome, retries, human review time, data pipeline spend, and support load all belong in the model. So does the client's *own* time: the review hours your HITL design creates are a real cost, often the largest one, and they are the reason some "successful" pilots get quietly retired.

**12. Drift is normal; monitoring is the product.** Inputs change, corpora change, upstream data changes, providers change models under you. The eval suite is not a launch gate; it is an operating system that runs forever, with owners and thresholds.

**13. Evals have a lifecycle cost, and it must be priced.** Every eval case is an asset requiring curation; ambiguous cases require adjudication; judges require calibration. A 150-case golden set with an owner and a monthly review process is worth more than a 5,000-case set nobody maintains.

**14. Goodhart's law is an operational risk.** The moment a metric becomes the target, it degrades: teams optimize for judge-friendliness, agents learn to game the scoring rubric, dashboards get tuned. Rotate metrics, keep human spot-checks, and hold periodic unstructured reviews where people read actual outputs without scores attached.

**15. The honest no-go.** Sometimes the eval says no: the bar is not met, the cost of failure is too high, the data is not there. Delivering that conclusion with evidence, before the client's budget is burned, is a mark of professional maturity — and it is the reason clients trust the next recommendation.

---

## 4B · Technical vocabulary & architecture blueprints

### B1 · Evaluation vocabulary

| Term | What it is | Why the PM must know it |
|---|---|---|
| **Golden set / test set** | Fixed, versioned set of cases with expected behaviours | The contract's measuring instrument; authoring it is a requirements activity |
| **Slice** | A defined subset (high-stakes, adversarial, rare language, new-customer cases) | Aggregate scores hide catastrophic slice failures; always report per-slice |
| **LLM-as-judge** | Model scoring another model's output, pointwise or pairwise | Scaling mechanism; requires calibration and spot-checks |
| **Pairwise preference / Elo** | Comparing two outputs rather than scoring one absolutely | More reliable than absolute scores; how leaderboards work |
| **Judge calibration / agreement** | Agreement rate between judge and human on a labelled sample (e.g. Cohen's kappa) | The number that makes judge-based claims defensible |
| **Groundedness / faithfulness** | Whether the answer is supported by the retrieved context | The core RAG quality metric; separate from fluency |
| **Hallucination / fabrication rate** | Rate of unsupported or invented content | The metric executives actually care about; define it operationally, per claim or per answer |
| **Context precision / recall** | Whether the right chunks were retrieved, and how much noise came with them | Diagnoses whether a failure is retrieval or generation |
| **Precision / recall / F1** | Errors of commission vs. omission, and their balance | Tie them to business cost: a false positive may cost 1×, a false negative 50× |
| **Pass@k** | Success within k attempts | Relevant when retries are allowed; changes the economics of a design |
| **Exact match / rubric scoring / semantic similarity** | Three grading styles for different task types | Choose before you have data; changing the grader invalidates comparisons |
| **Human-in-the-loop (HITL) / on-the-loop** | Human decides vs. human reviews samplings | The design lever that makes aggressive automation acceptable |
| **Annotation guideline / inter-annotator agreement** | Written rubric for human labelers; consistency measure | If two humans disagree, the case is not a valid test — it is a requirements bug |
| **Regression gate** | Automated threshold check that blocks a change | The mechanism that keeps quality from silently degrading |
| **Contamination / leakage** | Test cases present in training data or prompts | Inflates scores; check before quoting |
| **Shadow / canary / A-B** | Parallel run without users; small traffic share; controlled experiment | The three ways to test in production without betting the client |
| **Drift detection** | Statistical monitoring of inputs, outputs, and quality over time | Converts "it feels worse" into a threshold and an action |

### B2 · Operations, latency, and cost vocabulary

| Term | What it is | Why the PM must know it |
|---|---|---|
| **TTFT** | Time to first token | Perceived responsiveness in streaming UIs |
| **Tokens per second** | Generation throughput | Determines whether a long answer is usable in a workflow |
| **p50 / p95 / p99** | Latency percentiles | p95 governs user experience; tail latency compounds in agent loops |
| **Cost per query / per resolution / per successful outcome** | Cost at three levels of honesty | Only the third survives scrutiny, because failures and retries are in the numerator |
| **Cache hit rate** | Share of requests served from cache | Often the largest single cost lever; also a correctness risk if cache keys omit identity |
| **Retry / backoff / circuit breaker** | Resilience patterns around model and tool calls | Retries hide cost and latency; visible retries hide failures |
| **SLO / SLI / error budget** | Objective, indicator, permitted shortfall | How reliability trade-offs get negotiated rather than argued |
| **Deflection / containment rate** | Share of interactions resolved without a human | The classic support metric — and the one most often quoted without its denominator |
| **Cycle time / handle time** | Elapsed time per unit of work | The most transferable operations metric across industries |
| **Unit economics** | Cost and margin per unit of value delivered | What turns a pilot into a business; the number a CFO asks for |
| **Payback period** | Time until cumulative benefit exceeds cost | How capital allocation decisions actually get made |
| **Toil / on-call load** | Recurring manual operational work | What your product adds to the client's team; a hidden adoption cost |

### B3 · Metrics that lie (know these by name)

| Metric | The lie | The correction |
|---|---|---|
| **Resolution rate** | Denominator and definition shift; easy cases inflate it | Pin the definition, publish the mix, report per-segment and alongside escalation rate |
| **Average latency** | Hides the tail users complain about | Report p95/p99 with the workload |
| **Accuracy** | Unspecified task mix and threshold | Always with set, scorer, threshold, and slice table |
| **"Time saved per user"** | Self-reported; often aspirational | Measure the process, not the perception; triangulate with system data |
| **Adoption (logins)** | Usage ≠ value | Pair with depth (tasks completed) and outcome (decisions changed) |
| **Cost per call** | Ignores retries, failures, review time | Cost per successful outcome |
| **Model benchmark scores** | Leaderboards shift, contaminate, and reward different skills than your task | Evaluate on your own cases; treat public benchmarks as market intelligence only |
| **"X% of AI projects fail"** | Widely repeated, rarely sourced with a method | Use as a hypothesis, never as evidence; demand the sample, the definition of failure, and the date |

### B4 · Safety, harm, and adversarial evaluation

Accuracy evals measure whether the system is *right*. Harm evals measure whether the system is *safe to be wrong with* — a different axis, and a system can be 98% accurate and still unsafe on the 2%. Guardrails are evaluated too: a guardrail that blocks everything is a product failure (over-refusal), not a pass.

| Term | What it is | Why the PM must know it |
|---|---|---|
| **Red-teaming** | Structured, adversarial attempts — human and model — to elicit harmful or policy-violating output | The probe that finds the 2%; run before launch and on every model/prompt change |
| **Harm taxonomy** | The policy categories that make "harmful" countable: hate, harassment, violence, sexual content, self-harm, dangerous/CBRN content, PII exposure, IP leakage | The rubric; scope it to the client's domain and jurisdiction before red-teaming |
| **Safety refusal / over-refusal** | Declining a harmful request (good) vs. declining a safe one (a quality bug) | Over-refusal is silent churn; measure it alongside accuracy |
| **Jailbreak** | Bypassing safety behavior via phrasing, role-play, encoding, or translation | A moving target; re-test after every model upgrade because safety behavior shifts under you |
| **Injection-as-harm** | Untrusted content that induces the model to *produce* harm (ties to Module 3 prompt injection) | The boundary between security and safety; log it under both taxonomies |
| **Fairness / subgroup performance** | Performance and refusal rates measured per demographic or segment | Aggregate scores hide disparity; report the slice table |
| **Demographic parity vs. calibrated/equalized metrics** | Different, mutually incompatible fairness definitions | Choose — and write down — which one the domain requires before measuring; it is a product/legal decision, not a statistics detail |
| **Toxicity / guard classifier** | A separate fast model that screens inputs and outputs | Screening should be done by a model that is not the one being screened |
| **Model / system card** | The disclosure artifact: intended use, evals, limitations, safety posture | Turns "we tested it" into something a client or regulator can read |
| **AI incident** | A harmful, rights-violating, or safety-relevant output or decision with consequences | Needs a pre-written response path, not an improvised one |
| **Incident response / disclosure** | Detect → contain → notify → investigate → remediate → disclose | The runbook in 4D; the kill switch and rollback must exist before launch |

### Blueprint 10 — The evaluation architecture (offline → shadow → online)

```
 ┌─────────────── OFFLINE (fast, cheap, every change) ──────────────────────────┐
 │  Golden set (N cases, versioned, client co-authored)                          │
 │    ├─ deterministic checks: schema valid, citations resolve, format correct   │
 │    ├─ programmatic metrics: exact match, field-level precision/recall, latency│
 │    ├─ LLM-as-judge (pairwise vs. reference where possible) + calibration sample│
 │    └─ human review of high-stakes + adjudication of disputed cases            │
 │  Gate: overall floor + per-slice floors + adversarial slice floor             │
 └───────────────────────────────┬───────────────────────────────────────────────┘
                                 ▼
 ┌─────────────── SHADOW (real traffic, no user impact) ─────────────────────────┐
 │  New version runs on live inputs; outputs compared to production and to        │
 │  expected behaviour; cost/latency measured at real volume; no writes allowed   │
 └───────────────────────────────┬───────────────────────────────────────────────┘
                                 ▼
 ┌─────────────── CANARY (small share, reversible) ──────────────────────────────┐
 │  x% of traffic; rollback trigger defined in advance; on-call informed;          │
 │  business metrics watched alongside quality metrics                            │
 └───────────────────────────────┬───────────────────────────────────────────────┘
                                 ▼
 ┌─────────────── ONLINE (steady state, forever) ────────────────────────────────┐
 │  Quality: rolling sample scored vs. golden set · thumbs/feedback rate ·         │
 │           refusal rate · escalation rate · negative-feedback themes            │
 │  Business: cycle time · resolution/deflection · error rate · cost per outcome  │
 │  Ops: p95 latency · cost per successful outcome · retry rate · incident count  │
 │  Loop: bad production outputs → reviewed weekly → new golden-set cases          │
 └───────────────────────────────────────────────────────────────────────────────┘
```

**The PM's rule for this diagram:** every arrow needs an owner and a threshold. An eval system without a named owner degrades into a dashboard within a quarter.

### Blueprint 11 — The change pipeline (how quality survives velocity)

```
 [Proposed change: prompt · model version · retrieval tweak · tool · data refresh]
                    │
                    ▼
   [Eval run on golden set] ── below floor? ──▶ BLOCK (fix or re-scope)
                    │ pass
                    ▼
   [Shadow on live sample] ── cost/latency or quality regression? ──▶ BLOCK
                    │ pass
                    ▼
   [Canary x% with rollback trigger armed] ── trigger fires? ──▶ ROLLBACK (≤ minutes)
                    │ pass
                    ▼
   [Production + monitoring; model/prompt versions recorded on every response]
                    │
                    ▼
   [Weekly review: sample failures → new golden-set cases → backlog]
```

**This pipeline is what makes "we use AI in production" a defensible statement.** It is also the artifact that satisfies a client's change-control board: they can see exactly what happens before their workflow changes.

### Blueprint 12 — The ROI model (structure, with a worked example)

Build it as a table with the client's own numbers, all inputs sourced, and sensitivity shown.

| Line | Input | Source | Worked example |
|---|---|---|---|
| Volume | Units per month | Client ticketing system | 4,200 tickets |
| Current cost per unit | Fully loaded handling minutes × cost per minute | Time-and-motion study | 11 min × $0.85/min ≈ $9.35 |
| Current monthly cost | Volume × cost per unit | — | ≈ $39,270 |
| Automation rate at target precision | % auto-resolved without human | Pilot measurement | 42% |
| Automated unit cost | Tokens + infra + review share | Pilot telemetry | ≈ $0.31 |
| Human share after automation | Remaining tickets × handle time | Pilot measurement | 58% × 11 min |
| Monthly cost after | Automated + human + run-rate | — | ≈ $22,900 + $1,800 run-rate |
| Gross monthly benefit | Before − after | — | ≈ **$14,500** |
| One-time build | Effort × rate + environment | Estimate range | $120,000–$160,000 |
| Payback | Build ÷ monthly benefit | — | ≈ 8–11 months |
| Sensitivity | Automation rate 30% vs. 50%; false-answer cost | — | At 30%: payback ≈ 15 months. **State it.** |

**Five rules for the model.** (1) Every input has a source; unsourced inputs are labelled ASSUMPTION and shown in a separate block. (2) Model the failure cost explicitly — one wrong answer a week that consumes a supervisor's hour belongs in the model. (3) Include your run-rate and the client's review time. (4) Show sensitivity: the three inputs that swing the answer by more than the decision threshold. (5) Re-measure after go-live and publish the delta — including when it is worse than projected.

---

## 4C · Reading list & real-world case studies

### Required

| Source | Type | Why |
|---|---|---|
| Zheng et al. 2023 — *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena* · [arxiv.org/abs/2306.05685](https://arxiv.org/abs/2306.05685) | research | The paper that established LLM-as-judge **and** documented its biases; read the bias section carefully, it is the operational content |
| Es et al. 2023 — *RAGAS: Automated Evaluation of Retrieval Augmented Generation* · [arxiv.org/abs/2309.15217](https://arxiv.org/abs/2309.15217) | research | Faithfulness/answer-relevance/context metrics — the vocabulary for diagnosing whether retrieval or generation failed |
| Liang et al. 2022 — *Holistic Evaluation of Language Models (HELM)* · [arxiv.org/abs/2211.09110](https://arxiv.org/abs/2211.09110) | research | What rigorous, multi-metric, scenario-based evaluation looks like at scale |
| Chiang et al. 2024 — *Chatbot Arena* · [arxiv.org/abs/2403.04132](https://arxiv.org/abs/2403.04132) · Singh et al. 2025 — *The Leaderboard Illusion* · [arxiv.org/abs/2504.20879](https://arxiv.org/abs/2504.20879) | research | Pairwise human evaluation, and how leaderboards can be gamed — the PM's defense against benchmark-driven model selection |
| Bavaresco et al. 2024 — *Judging the Judges* · [arxiv.org/abs/2406.12624](https://arxiv.org/abs/2406.12624) | research | Alignment and vulnerabilities of judges; the evidence base for calibration discipline |
| Ji et al. 2022 — *Survey of Hallucination in NLG* · [arxiv.org/abs/2202.03629](https://arxiv.org/abs/2202.03629) · Liu et al. 2023 — *Evaluating Verifiability in Generative Search Engines* · [arxiv.org/abs/2304.09848](https://arxiv.org/abs/2304.09848) | research | How fabrication is measured; citation-quality reality in generated answers |
| Jimenez et al. 2023 — *SWE-bench* · [arxiv.org/abs/2310.06770](https://arxiv.org/abs/2310.06770) | research | The model of a task benchmark with executable verification — the pattern to imitate with your own cases |
| OpenAI — *Evaluation best practices* · [developers.openai.com](https://developers.openai.com/api/docs/guides/evaluation-best-practices) · Evals framework · [github.com/openai/evals](https://github.com/openai/evals) · promptfoo · [github.com/promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) · DeepEval · [github.com/confident-ai/deepeval](https://github.com/confident-ai/deepeval) · Ragas docs · [docs.ragas.io](https://docs.ragas.io/) | primary | The practical tooling; you should have run one of these on a real task |
| Langfuse · [langfuse.com/docs](https://langfuse.com/docs) · LangSmith · [docs.smith.langchain.com](https://docs.smith.langchain.com/) · Evidently · [evidentlyai.com](https://www.evidentlyai.com/ml-in-production/model-monitoring) | primary | Tracing, datasets, online scoring, and drift monitoring — where evals live once they are operational |
| Forsgren et al. 2021 — *The SPACE of Developer Productivity* · [queue.acm.org](https://queue.acm.org/detail.cfm?id=3454124) · DORA · [dora.dev](https://dora.dev/) | research | The framework for multi-dimensional productivity measurement — directly transferable to "did AI help the team?" |
| Google SRE — *SLOs* · [sre.google](https://sre.google/sre-book/service-level-objectives/) · *Eliminating Toil* · [sre.google](https://sre.google/sre-book/eliminating-toil/) · Dean & Barroso — *The Tail at Scale* · [research.google](https://research.google/pubs/pub40801/) | primary/research | Reliability as a negotiated budget; tail latency; the operational vocabulary your client's platform team already uses |
| Ganguli et al. 2022 — *Red Teaming Language Models to Reduce Harms* (Anthropic) · [arxiv.org/abs/2209.07858](https://arxiv.org/abs/2209.07858) | research | The reference method for red-teaming: human + model red-teamers, harm taxonomy, scaling behaviors, and lessons — the template for the plan in 4D |
| AI Incident Database · [incidentdatabase.ai](https://incidentdatabase.ai/) | research/community | The public record of real AI harms; read recent entries in your client's sector before writing the harm taxonomy — reality beats imagination |

### Case studies — all of these are measurement-design cases

**1 · Intercom Fin — the metric that moved because the definition moved** · [intercom.com/blog](https://www.intercom.com/blog/from-resolutions-to-outcomes-evolving-how-fin-delivers-value/) · *vendor*
The same vendor reported an average resolution rate around 56% (30 days after launch, per the AWS case study) and later reported 76%, explicitly because Fin now handles more complex work and the metric's meaning evolved. **Extract:** a moving metric is not fraud — it is what happens when a metric meets a changing population, which is precisely why the definition, denominator, and mix belong in the contract (and in the SOW's acceptance section).

**2 · Klarna — success metrics and the human cost they omitted** · [openai.com/index/klarna](https://openai.com/index/klarna/) · *vendor* · [fortune.com](https://fortune.com/2025/05/09/klarna-ai-humans-return-on-investment) · *independent press*
Containment, handle time, and estimated profit improvement were the reported wins; the reported reversal came with a customer-experience rationale. **Extract:** the ROI model must include the metrics that resist the narrative — trust, escalation quality, churn risk, employee morale. If your model cannot represent a reversal, it is a sales model, not a decision model.

**3 · Copilot — three credible studies, three conclusions** · [github.blog](https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness) · *vendor* · [arXiv:2509.20353](https://arxiv.org/abs/2509.20353) · *research* · [Cui et al., MIT](https://economics.mit.edu/sites/default/files/inline-files/draft_copilot_experiments.pdf) · *research* · [METR study](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) · *research*
A controlled task study found a large speed-up; a longitudinal case study found no significant change in activity metrics; RCTs at Microsoft/Accenture found effects that varied by population; and METR's randomized trial found experienced open-source maintainers took **19% longer** with AI tools while estimating afterwards that they had been ~20% faster (METR has since published updated data for later tool generations — itself a lesson in how quickly these findings expire). **Extract (the most important lesson in this module):** self-reported productivity and system-measured productivity diverge, and "with AI" questions are only answerable with a counterfactual. Design the measurement before the pilot starts, and prefer system data over preference data when the decision is about money.

**4 · The contested "95% of pilots fail" statistic.** A widely repeated claim from MIT's 2025 *GenAI Divide* report (and its many derivatives) reporting that the vast majority of enterprise GenAI pilots deliver no measurable P&L impact. **Extract:** treat statistics about AI failure as *hypotheses to test in your own engagement*, not as evidence about yours — and read how the claim is defined (measurable P&L impact vs. deployment vs. satisfaction) before repeating it. This is the `Metrics that lie` table applied to the industry's favourite number.

**5 · The harmful-output incident (composite).** A customer-facing assistant answers a safety-adjacent query with confident, wrong, and potentially harmful guidance. The team had no harm taxonomy, no kill switch, no disclosure path — and the client learned about it from an end user. **Extract:** accuracy evals would have passed this system (the answer was fluent and on-topic); only a harm eval would have caught it. The incident's cost was not the wrong answer — it was the absence of a pre-written response: containment took hours, disclosure was improvised, and the trust damage was permanent. **The lesson:** the incident runbook in 4D is a launch artifact, not an ops afterthought.

---

## 4D · The field playbook

### Pilot acceptance criteria (the artifact that prevents every dispute)

Full template: `templates/fde-pilot-acceptance-criteria.md`. Structure:

```
1. BUSINESS OUTCOME            — the one number, with baseline, target, and measurement source
   e.g. "Median handle time for policy questions falls from 11 to ≤7 minutes by 2026-12-01,
         measured from the ticket system's timestamps for the trained cohort (n ≥ 300)."
2. QUALITY THRESHOLDS          — on the client-authored golden set, per slice
   overall ≥ __% · adversarial slice ≥ __% · high-stakes slice: 100% human review (not a score)
   false-answer rate ≤ __% (defined operationally: unsupported claim, wrong policy version, wrong entity)
3. OPERATIONAL THRESHOLDS      — p95 latency ≤ __s · cost per resolution ≤ $__ · escalation path works under load
4. ADOPTION CRITERIA           — ≥ __% of the target team using it weekly by week __, with training complete
5. FAILURE DEFINITIONS         — what counts as a failure, who adjudicates, and the adjudication SLA
6. MEASUREMENT METHOD          — who runs it, on what data, on what dates, with what access
7. SIGN-OFF                    — named client sponsor + named internal owner, dated BEFORE the first demo
8. WHAT HAPPENS BELOW THE BAR  — rework window · paid extension · termination clause
```

**Two disciplines.** First, thresholds are proposed by your side and *agreed* by the client's — a bar you set alone is a bar they can reject later. Second, every threshold names its measurement method; a threshold without a method is a future argument.

### The eval suite plan (one page per project)

```
Owner:                [name — the eval owner owns the quality conversation]
Golden set:           [N cases · source: client cases · version · update rule (≤5 cases/week via review)]
Slices:               [high-stakes · adversarial/injection · rare-language · new-customer · long-tail]
Scorers:              [deterministic checks · LLM-judge with calibration sample of __% · human review slices]
Calibration:          [judge-vs-human agreement target and how it is measured]
Gates:                [overall floor · per-slice floors · who can block]
Change pipeline:      [Blueprint 11, with rollback trigger and time]
Online metrics:       [quality: rolling sample, refusal, escalation, negative feedback]
                      [business: handle time, resolution, error rate, cost per outcome]
Drift triggers:       [threshold → action per signal, from templates/production-eval-plan.md]
Weekly ritual:        [who reads failures, Monday 30 min, decisions recorded]
```

### The ROI model worksheet (do this before the pilot, re-do it after)

Fill Blueprint 12 with client numbers; keep the assumptions block visible; show the three-input sensitivity; state payback as a range. Then **publish the post-hoc delta** — projected vs. actual — including the misses. The teams that publish the misses are the ones invited back.

### The red-team & harm-eval plan

Run before launch and re-run on every model, prompt, retrieval, or guardrail change. The pass criterion is not "nothing got through" — it is that every finding is classified, and the response to each class is defined.

1. **Scope the taxonomy.** Write the harm categories that apply to the client's domain and jurisdiction (a medical client and a consumer client have different taxonomies). Get the client's risk owner to sign it — the taxonomy is a requirements document.
2. **Seed the corpus.** Start from the OWASP list items, the client's own failure modes, and public red-team datasets; add the domain-specific cases your team fears most.
3. **Red-team with humans and models.** Human red-teamers find the novel failures; model red-teamers generate volume. Log every finding against the taxonomy with severity.
4. **Add a "no-harm" slice to the golden set.** Safety behaviors are evaluated, not assumed — refusal correctness, jailbreak resistance, and fairness-by-segment each get slices with thresholds, exactly like accuracy (the `templates/fde-pilot-acceptance-criteria.md` slice table).
5. **Classify severity and define the response per class** (see the incident runbook below). A harmful output in a low-stakes internal tool and one in a member-facing service get different responses — write both.
6. **Publish a system card** before production: intended use, limitations, eval results, safety posture, and the human-review points. It is the artifact a client's risk committee can actually read.

### AI incident response — the short runbook

Pre-written, owned, and rehearsed before launch. The kill switch and rollback are design features (Module 1 Blueprint 2, Module 4 Blueprint 11), not something you improvise during the incident.

| Step | Action | Owner | SLA |
|---|---|---|---|
| **Detect** | Monitoring thresholds, user reports, red-team findings | eval owner / on-call | immediate |
| **Contain** | Kill switch, gate the capability, or rollback to the last known-good version | on-call | ≤ [__] minutes |
| **Notify** | Internal owner + client security/risk owner, with severity and status | PM | ≤ [__] hours |
| **Investigate** | Reconstruct the output — inputs, prompt/model/retrieval versions, permissions, approvals (Module 3 auditability is what makes this possible) | FDE lead | ≤ [__] hours |
| **Remediate** | Patch prompt/guardrail/data; add the case to the golden set so it cannot regress | FDE lead | ≤ [__] days |
| **Disclose** | Client-facing language — what happened, impact, and fix; do not hide it | PM + legal | per policy |
| **Learn** | Weekly review: root cause, what the eval set missed, what the taxonomy should add | PM | weekly |

**Two rules.** Disclosure is a trust decision, not a legal afterthought — a client who learns about a harmful output from you keeps trusting you; one who learns from their own users does not. And an incident is the most valuable eval data you will ever get: every incident should produce at least one new golden-set case and one taxonomy refinement.

---

# Module 5 — The FDE Operational Flywheel & Team Orchestration

> **Gate owned:** 5 (productization). This is the module that separates a deployment business from a product business. Its subject is not tooling but the operating system of an FDE team: the cadence, the triage, the shield, and the machinery that turns the third repeated engagement into a core capability.

---

## 5A · Core PM competencies & mental models

**1. The asset is the pattern, not the revenue.** FDE engagements produce high revenue per head and mediocre gross margin. What compounds is the *repeated* pattern: the same integration, the same eval harness, the same workflow, discovered again at a different client. A team with twenty bespoke deployments and no pattern has twenty maintenance liabilities and zero enterprise value.

**2. Utilization is a trap as a north star.** Maximizing billable deployment time starves exactly the work that creates the platform. The PM's job is to make the trade-off explicit — a deliberate allocation between deployed work, harvesting work, and core building — rather than letting urgency allocate it implicitly to 100% deployment.

**3. The three-client rule.** The third instance of the same request is a market signal; the first two are learning. Test the signal with four questions: how often does it recur, how much does bespoke delivery cost us each time, will the clients pay for a product version, and does the pattern sit close enough to our differentiation to own it?

**4. Measure distance from core.** Every engagement request sits somewhere between "we configure an existing capability" and "we build something new." Score it. Track the distribution. A portfolio drifting toward the custom end is a product strategy failure that will surface as a margin problem two quarters later.

**5. Bespoke work is inventory, not waste.** It is legitimate — it wins the logos, teaches the domain, and pays the bills. But inventory carries cost: maintenance, upgrade burden, onboarding time, and the cognitive load of N variants. The PM manages the carrying cost, not the existence.

**6. The PM is the abstraction engine.** Harvesting means writing down the pattern, naming the configurable axes, defining the core interface, and then *deprecating* the bespoke versions. Deprecation is the step teams skip, and skipping it means the platform grows next to the legacy rather than replacing it.

**7. Shield, don't wall.** Protecting FDEs from scope creep is a process — triage, pricing, change control, cadence — not a personality trait. A PM who simply says no damages the client relationship; a PM who prices and sequences the yes keeps both.

**8. Cadence beats heroics.** Embedded triage daily, demo weekly, client steering monthly, harvest quarterly. Teams without a harvest ritual productize by accident or not at all; the ritual is what makes pattern-spotting a scheduled activity instead of a memory.

**9. Two clocks, published.** The client runs on pilot dates, budget cycles, and executive reviews; the product runs on quarters. The PM owns both and must publish the difference — "this is when you get it, this is when it becomes a product" — because unstated divergence is read as broken promises.

**10. Forks are the enemy; configuration is the answer.** The failure state is a branch per client. The instruments that avoid it: tenant configuration, feature flags, an extension model, and a single trunk with client-specific configuration as data — never a long-lived code fork you must merge forever.

**11. Reuse rate is the team's real KPI — with guardrails.** Measure the share of shipped work that reused core components, and pair it with quality and client-satisfaction guardrails, because a pure reuse target produces shortcuts and resentment.

**12. Say no with a price, not with a policy.** The three-part response: *this is configuration (free, this sprint)*; *this is bespoke (priced, sequenced, and it displaces X)*; *this is a product candidate (here is the decisions memo, here is when you will hear)*. The client can accept any of those; what they cannot accept is silence or a flat no.

**13. Team topology is part of the product.** Stream-aligned engagement teams, a platform team owning the core, enabling engineers who spread expertise, and a small group owning the hard subsystems (retrieval, evals, model infrastructure). Watch Conway's law: your architecture will mirror your team structure, for good or ill.

**14. FDEs are not interchangeable with product engineers.** The distinguishing traits — tolerance for ambiguity, comfort in the client's room, data-detective instinct, willingness to own a system past handoff — need to be hired for, developed, and defended in promotion criteria. A PM who treats the two pools as fungible will lose the FDEs first.

**15. Client trust is an asset that the productization conversation puts at risk.** "We want to turn your bespoke solution into a product we sell to others" must be framed with the client's interests: what they get (maintained code, roadmap influence, a reference architecture, better economics), what they keep (their configuration, their data, their differentiation), and what they must consent to. Raise it early, in writing, and it becomes a partnership. Raise it after they notice, and it becomes a dispute.

**16. The honest harvest.** Some engagements should never be productized: the pattern is too specific, the market too small, the maintenance burden disproportionate. Recording *that* decision — with reasoning — is as valuable as recording the yes, because it stops the same debate recurring every quarter.

---

## 5B · Technical vocabulary & blueprints

### B1 · Operating vocabulary

| Term | What it means | Why the PM must own it |
|---|---|---|
| **Engagement lifecycle** | Land · scope · build · deploy · scale · harvest | The harvest stage is the one that gets cancelled when the next deal lands |
| **Embedded triage** | Short, daily, structured session where the team unblocks client issues and classifies requests | The ritual that converts chaos into a decision record |
| **Cadence** | The fixed rhythm of demos, steering, reviews, harvests | The mechanism that makes abstraction habitual |
| **Leverage vs. utilization** | Revenue per head vs. share of hours billed to clients | The metric pair that reveals whether you are building a product or renting engineers |
| **Scope-creep tax** | The maintenance and upgrade burden created by un-priced one-off work | The number to put in front of leadership when defending the shield |
| **Time to first deploy** | Elapsed time from engagement start to a working system in the client's environment | The best single measure of platform maturity |
| **Reuse rate** | Share of engagement work delivered from core capabilities | The flywheel's output metric, guardrailed by quality and satisfaction |
| **Reference architecture** | The documented, repeatable way this class of solution is built | What converts tribal knowledge into a paved road |
| **Golden path / paved road** | The supported, default way to build and deploy | What new FDEs follow; what the platform team maintains |
| **Exemplar repository** | A working end-to-end example teams copy | Faster and more honest than documentation alone |
| **Config over code; extension points** | Client specifics expressed as configuration or via defined extension interfaces | The structural defense against forks |
| **Feature flag / tenant config** | Runtime toggles scoped to a tenant | How one core serves many clients without branching |
| **Deprecation** | Scheduled removal of bespoke implementations in favour of core | The step that makes productization real |
| **Packaging & licensing; support tiers** | How the productized capability is sold and supported per client | Determines whether productization improves or worsens margin |
| **Design partner** | A client who co-develops in exchange for influence and preferential terms | The legitimate, consented way to fund core development from engagements |
| **Enterprise-ready checklist** | The gate a capability passes to be sellable (security, evals, docs, support) | Prevents "productized" from meaning "works at one client" |
| **RACI** | Responsible, accountable, consulted, informed | Kills the "I thought you owned the client relationship" class of failure |
| **Escalation matrix** | Who is contacted, at what threshold, with what response time | Makes on-call and client escalation survivable |

### B2 · Pricing and monetization

Productization changes the *price*, not just the product. The pricing model is a product decision with engineering consequences (metering, caps, entitlement enforcement) — and it is where the flywheel's value is either captured or leaked.

| Term | What it means | Why the PM must own it |
|---|---|---|
| **Cost-plus vs. value-based** | Price = our cost + margin, vs. price anchored to the cost the client avoids | Anchor to the displaced baseline (Module 4 ROI); a client pays for the outcome, not your compute |
| **Outcome-based pricing** | Charge per resolution / containment / completed outcome, not per seat | Intercom's model for Fin; forces you to prove value every month — which is what a productized capability should want |
| **Seat / license** | Per-user, flat, predictable | Simple and predictable, but decouples price from value and usage — undercharges heavy users, overcharges light ones |
| **Usage / metered** | Per token, call, or query | Aligns to cost, but creates bill anxiety and usage-shifting; pair with caps |
| **Platform fee + usage** | A fixed base plus metered overage | The hybrid that funds the platform team while keeping marginal pricing honest |
| **Usage caps & overage** | A ceiling with defined overage pricing | The client's cost-predictability demand (ties to "unbounded consumption" in Module 3) |
| **Pilot-to-contract pricing** | Price the pilot on outcomes, convert on demonstrated ROI | The acceptance criteria (Module 4) are the pricing evidence; do not re-argue from scratch at conversion |
| **Gross-margin retention / expansion revenue** | The SaaS metrics that reveal whether productization actually helped margin | Proof the flywheel is compounding rather than just accumulating logos (ties to leverage vs. utilization in 5B) |
| **Design-partner discounting** | Reduced price in exchange for co-development and reference | The legitimate way to fund core from an engagement (ties to Module 5 consent) |
| **Price transparency as trust** | A client that understands your unit economics accepts overage; one that doesn't, disputes it | Show the cost drivers, not the whole margin — transparency is the trust instrument |

**Choosing the model — three questions.** (1) *What can the client verify and value?* If the outcome is measurable in their systems and they care about it, price the outcome. (2) *How predictable is usage?* Spiky and unpredictable → metered with caps; stable and role-based → seat or platform fee. (3) *What does the displaced baseline cost them?* That number (from the Module 4 ROI model) is your anchor and your ceiling — never price above the cost you remove without an explicit reason.

**The Intercom lesson.** Outcome pricing makes the vendor re-prove the value every month. For a productized FDE capability that is the point: the same "define done before the demo, measure the business not the model" discipline from Module 4 is what makes the invoice defensible. Price the outcome you can measure, meter the compute you can't avoid, and show the client the sensitivity — not the hope.

Reference: GTMnow — *How Intercom built the highest-performing AI agent with outcome pricing* · [gtmnow.com](https://gtmnow.com/how-intercom-built-the-highest-performing-ai-agent-on-the-market-using-outcome-based-pricing-with-archana-agrawal-president-at-intercom/) · *primary/practitioner*. Pricing economics re-verify with the market each quarter — vendor pricing pages and the displaced-cost baseline both move.

### Blueprint 13 — The FDE flywheel

```
        ┌────────────────────────────────────────────────────────────────────┐
        │                                                                    │
        ▼                                                                    │
  [1] WIN / LAND            [2] DELIVER EMBEDDED        [3] INSTRUMENT       │
  Discovery → SOW           Daily triage, weekly demo    Pattern ledger:      │
  Feasibility, matrix       Client's environment,        what repeated,       │
  Deployment model          client's data, client's      what cost, what      │
  Acceptance criteria       users                          was bespoke        │
        │                          │                            │             │
        │                          ▼                            ▼             │
  [7] REPEAT & EXPAND  ◀── [6] REUSE  ◀────────── [5] SHIP TO CORE ◀── [4] ABSTRACT
  Faster next time:         Next engagement          Platform team builds     Abstraction RFC:
  time-to-first-deploy      starts from the          the capability;          core interface, the
  falls; trust converts     paved road; reuse         docs, evals, security    configurable axes,
  to references and         rate measured             gates pass               what stays bespoke
  expansion                                                                       │
        └────────────────────────────────────────────────────────────────────────┘
   Failure modes per stage:  [1] over-promise  [2] heroics, no record  [3] nobody writes it down
   [4] abstraction by one person, no review  [5] starved for time  [6] bespoke not deprecated
   [7] "every client is different" becomes an excuse
```

**The PM's ownership:** stage 3 (the ledgers exist and are filled weekly), stage 4 (the RFC is written and reviewed), stage 7 (the deprecation plan exists). Stages 2, 5, 6 belong to engineering leadership — but they fail without the PM's inputs.

### Blueprint 14 — The productization pipeline (from pattern to core)

```
 [Pattern observed 3× in the ledger]
        │
        ▼
 [Signal test — all four must hold]
   Frequency:      recurs across ≥3 clients or ≥3 times at one client
   Cost:           bespoke delivery costs ≥ N engineering-days each instance
   Willingness:    ≥2 clients would pay for a configured version
   Differentiation: it sits close enough to our core to defend (not commodity glue)
        │
        ├── fails ──▶ [Written "no" with reasoning] — revisit when the ledger says otherwise
        │
        ▼
 [Abstraction RFC]  core interface · configurable axes · what stays client-specific ·
                    migration path for existing bespoke · eval + security gates · estimate
        │
        ▼
 [Core roadmap slot]  sized against the platform team's capacity; commitment dated
        │
        ▼
 [Ship + document]  golden path updated · exemplar repo updated · enterprise-ready checklist passed
        │
        ▼
 [Migrate & deprecate]  existing clients migrated onto core config · bespoke branch frozen then removed ·
                        reuse rate and support load measured before/after
```

**The gate that matters most is deprecation.** If the bespoke path is not removed, you now maintain two systems per pattern — and your "platform" is a tax rather than a dividend.

### Blueprint 15 — Custom-request triage (the shield, made operational)

```
 Client request arrives (call, email, discovery session, or "can it also…")
        │
        ▼
 Is it required for an agreed acceptance criterion in the current SOW?
   ├─ YES ──▶ [In scope] ──▶ built, tracked, demoed on cadence
   └─ NO ──▶ Is it configuration of an existing core capability?
              ├─ YES ──▶ [Config] ──▶ estimate in hours, done this sprint, logged for reuse
              └─ NO ──▶ Has the pattern appeared ≥3 times in the ledger?
                         ├─ YES ──▶ [Product candidate] ──▶ abstraction RFC; PM commits to a decision date
                         └─ NO ──▶ Is there a paid path?
                                    ├─ YES ──▶ [Bespoke, priced] ──▶ change order; states what it displaces
                                    └─ NO  ──▶ [Decline with a reason + alternative] ──▶ in writing, same week
   Decision owner: PM (with FDE lead on effort). Response SLA: 3 business days. Every decision logged.
```

**The three-day SLA is the whole point.** Most scope-creep damage comes not from the no but from ambiguity — the team starts building while nobody has decided.

### Blueprint 16 — The cadence calendar

| Ritual | Frequency | Duration | Attendees | Outputs (the artifact is the ritual's reason to exist) |
|---|---|---|---|---|
| **Embedded triage** | Daily | 15 min | FDEs, PM | Blocker list with owners; request classifications into the triage tree |
| **Client demo** | Weekly | 30–45 min | Team, client users, client sponsor | Working software; agreed next increment; visible progress (the antidote to trust decay) |
| **Internal review** | Weekly | 30 min | PM, FDE lead, platform rep | Triage decisions; pattern-ledger updates; product-candidate nominations |
| **Client steering** | Monthly | 60 min | Sponsors, PM, FDE lead | Scope decisions, risks, metrics against acceptance criteria, escalation resolution |
| **Harvest session** | Monthly or quarterly | 90 min | PM, FDEs, platform team | Pattern ledger review; one abstraction RFC or one written "no"; deprecation candidates |
| **Portfolio review** | Quarterly | 2 h | Leadership, PM | Distance-from-core distribution; reuse rate; time-to-first-deploy trend; roadmap commitment |
| **Post-handoff retro** | Per engagement | 60 min | Team + client ops owner | Operating manual gaps, eval ownership, what should have been product, reference update |

**The rule:** if a ritual's artifact is not produced, the ritual is a meeting and should be cancelled or redesigned.

### Blueprint 17 — FDE ↔ PM ↔ client RACI (template)

| Activity | PM | FDE lead | Platform team | Client sponsor | Client IT/Security |
|---|---|---|---|---|---|
| Discovery & problem definition | **A/R** | C | I | C | I |
| Instrument decision & feasibility | **A** | R | C | C | I |
| SOW, pricing, change control | **A/R** | C | I | A (signatory) | C |
| Architecture & ADRs | C | **A/R** | C | I | C |
| Deployment model & security review | **A** | R | C | C | **A** (approval) |
| Acceptance criteria & eval suite | **A** | R | C | C | I |
| Delivery cadence & unblocking | **A/R** | R | I | I | I |
| Productization decision | **A/R** | C | R | C | I |
| Handoff & operating manual | A | **R** | C | **A** (acceptance) | C |
| Escalation (technical) | C | **A/R** | C | I | I |
| Escalation (relationship/commercial) | **A/R** | I | I | C | I |

*A = accountable (one name only) · R = responsible · C = consulted · I = informed.*

Fill this in for your own team in week one. Most FDE team dysfunction traces to an activity with two A's or none.

### The shield script (how to say no inside a trusted relationship)

Four sentences, in this order:

1. **Acknowledge the real need:** "That's a real problem, and I can see why it matters to your team."
2. **Place it in the decision frame:** "It isn't in the agreed scope, so here's how I'd handle it…"
3. **Give the options with prices and dates:** "…as configuration, which is free and lands this sprint; as a paid extension, which costs X and displaces Y; or as a product candidate, on which I owe you a decision by [date]."
4. **Commit to the decision date and keep it:** the follow-through is what makes the next three refusals cheap.

What you never do: say yes ambiguously, promise it "soon," or let the team start building before the decision is recorded.

---

## 5C · Reading list & real-world case studies

### Required

| Source | Type | Why |
|---|---|---|
| Palantir — *A Day in the Life of a Forward Deployed Software Engineer* · [blog.palantir.com](https://blog.palantir.com/a-day-in-the-life-of-a-palantir-forward-deployed-software-engineer-45ef2de257b1) | primary | The role's texture: what FDEs actually do all day, and where a PM can add leverage versus interference |
| Palantir — *Dev versus Delta* · [blog.palantir.com](https://blog.palantir.com/dev-versus-delta-demystifying-engineering-roles-at-palantir-ad44c2a6e87) | primary | A two-pool engineering model and its consequences for team topology, promotion, and who owns what |
| Palantir — *The Baseline Team* · [blog.palantir.com](https://blog.palantir.com/the-baseline-team-and-forward-deployed-infrastructure-engineering-at-palantir-efd84e72e40b) | primary | What it takes to operate many client environments: the unglamorous team that makes scale possible |
| Palantir — *Ontology-Oriented Software Development* · [blog.palantir.com](https://blog.palantir.com/ontology-oriented-software-development-68d7353fdb12) · *Foundry Ontology on the front line* · [blog.palantir.com](https://blog.palantir.com/how-palantir-foundrys-ontology-deploys-data-science-to-the-front-line-7a9679bdfd01) | primary | The product thesis behind harvesting: model the enterprise's entities and actions once, then deploy repeatedly |
| Palantir — *Form S-1* (2020) · [sec.gov](https://www.sec.gov/Archives/edgar/data/1321655/000119312520230013/d904406ds1.htm) | primary | How a company describes forward-deployed delivery to public investors — including the risks it discloses about bespoke work, margins, and customer concentration. Read the risk factors; they are a free education in FDE business-model fragility |
| Uber — *Meet Michelangelo* · [uber.com/blog](https://www.uber.com/us/en/blog/michelangelo-machine-learning-platform/) · *From Predictive to Generative* · [uber.com/blog](https://www.uber.com/us/en/blog/from-predictive-to-generative-ai/) | primary | Platformization in the large: one paved road for many teams, then the migration to generative capability |
| Uber — *Domain-Oriented Microservice Architecture* · [uber.com/blog](https://www.uber.com/us/en/blog/microservice-architecture/) | primary | Bounded domains as the answer to unownable sprawl; the same logic applies to engagement code |
| Stripe — *APIs as infrastructure* · [stripe.com/blog/api-versioning](https://stripe.com/blog/api-versioning) | primary | Interfaces as decade-long promises; read it before deciding what to expose to clients |
| Cagan — *Product vs. Feature Teams* · [svpg.com](https://www.svpg.com/product-vs-feature-teams/) | primary | The distinction between delivering requested work and owning outcomes — the precise failure mode an FDE org drifts into |
| *Team Topologies* — key concepts · [teamtopologies.com](https://teamtopologies.com/key-concepts) · Conway's Law · [martinfowler.com](https://martinfowler.com/bliki/ConwaysLaw.html) | primary | The vocabulary for designing engagement, platform, and enabling teams deliberately rather than by accident |
| Fowler — *Technical Debt Quadrant* · [martinfowler.com](https://martinfowler.com/bliki/TechnicalDebtQuadrant.html) · Google SRE — *Eliminating Toil* · [sre.google](https://sre.google/sre-book/eliminating-toil/) | primary | Naming debt and toil precisely is what lets you argue for paying them down |
| The program's own instruments: `templates/pattern-ledger.md` · `templates/productization-memo.md` · `templates/sow.md` · `templates/30-60-90.md` | primary | The artifacts this module produces |
| GTMnow — *How Intercom built the highest-performing AI agent with outcome pricing* (Archana Agrawal, President of Intercom) · [gtmnow.com](https://gtmnow.com/how-intercom-built-the-highest-performing-ai-agent-on-the-market-using-outcome-based-pricing-with-archana-agrawal-president-at-intercom/) | primary/practitioner | The account of restructuring product, pricing, and GTM to be AI-native — the pricing logic in 5B, in the words of someone who ran it |

### Case studies

**1 · Palantir's two engineering pools — the topology decision** · *primary*
Devs build the platform; Deltas deploy into the customer's world. **Extract:** most companies running FDE teams do not have a second pool to absorb generalization work, which means the PM must create the *function* (a rotating harvest role, a platform squad with reserved capacity, or explicit time allocation) even where the org chart does not. **Hold this question:** in my team, who is the named owner of generalization work this quarter?

**2 · Uber Michelangelo — what "platform" means when it works** · *primary*
Data management, training, deployment, and monitoring as shared infrastructure with a paved road. **Extract:** the signs of real platformization — a new use case ships without new infrastructure; monitoring and evaluation are defaults, not per-team projects; the platform team owns the hard, shared problems. Compare your team against those three signs and write down the gaps.

**3 · Stripe API versioning — the cost of a promise** · *primary*
Stripe's approach: version the API, maintain compatibility, and treat breaking changes as a business event. **Extract:** in FDE work, every client-specific interface you expose becomes a promise; the PM should treat one-off client endpoints as liabilities with a deprecation plan, not as free flexibility.

**4 · The composite "third client" case.** Using the pattern ledger from six months of engagements: three clients have asked for the same policy-answer-and-cite assistant; the bespoke implementations differ by ~30% (connectors, prompt, corpus preprocessing) and 70% is identical; each bespoke delivery cost ~25 engineering days; two clients say they would buy a configured version; the capability sits close to the company's core. **Through Blueprint 14:** signal test passes on all four criteria → abstraction RFC → core roadmap slot next quarter → existing clients migrated onto configuration → bespoke branches frozen and removed at the following release → reuse rate and support load compared before and after. **The lesson:** productization is a pipeline with a gate and a deprecation step, not an insight. Write the memo (`templates/productization-memo.md`) or do not claim to have decided.

**5 · The bespoke that should never be productized.** A fourth client asks for an integration with a proprietary, single-installation system used by roughly a dozen organisations worldwide, and it is the only reason this client buys. **Through Blueprint 14:** the frequency test fails at scale, the market is too thin, and the maintenance burden is disproportionate. **The lesson:** record the "no" with reasoning in the ledger. The PM who documents *why not* saves the org from re-litigating it every quarter — and from the more expensive mistake of building it anyway.

---

## 5D · The field playbook

### The pattern ledger (the instrument that makes productization possible)

Full template: `templates/pattern-ledger.md`. One row per repeated request or piece of bespoke work; reviewed monthly; the source of every abstraction RFC.

| ID | Pattern | Clients / instances | Bespoke cost per instance | Core overlap | Requested by | Signal test | Status | Decision date | Owner |
|---|---|---|---|---|---|---|---|---|---|
| P-014 | Policy answer + citation over client corpus | 3 clients, 4 builds | ~25 eng-days | ~70% | Ops leads | Pass (4/4) | Abstraction RFC drafted | 2026-10-01 | PM |
| P-021 | Connector to [legacy system X] | 1 client | ~18 eng-days | ~20% | Client IT | Fail (frequency) | Declined — documented | 2026-09-05 | PM |
| P-009 | Eval harness for client golden sets | 3 clients | ~6 eng-days | ~85% | FDEs | Pass (4/4) | Shipped to core; bespoke frozen | 2026-08-15 | Platform |
| P-022 | Role-based redaction profiles | 2 clients | ~10 eng-days | ~60% | Security leads | Pending (needs 3rd instance) | Watching | 2026-11-15 | PM |

**The three rules of the ledger.** It is filled in *during* engagements, not reconstructed after. Every row has an owner and a decision date. Declines live in it permanently, with reasoning.

### The productization memo (gate document)

Full template: `templates/productization-memo.md`. Structure:

```
1. The pattern                      — what recurs, with ledger evidence (instances, dates, clients)
2. Signal test                      — frequency · bespoke cost · willingness to pay · differentiation. Each with evidence
3. The product, precisely           — core interface · configurable axes · what remains client-specific ·
                                      what we would delete from the bespoke versions
4. The market                       — who buys it, at what price, in what packaging (feature · add-on · module · separate SKU)
5. Migration & deprecation          — how existing bespoke implementations move to core, when branches are removed
6. Cost & return                    — build estimate, run-rate, expected reuse-rate effect, support-load effect,
                                      margin effect at three adoption levels
7. Risks                            — client consent, commercial exposure to one client's specifics, platform-team
                                      capacity, competitive copying
8. Decision requested               — build now / build next quarter / decline (with reasoning) — and by whom, by when
9. If we decline                    — what we tell the clients, and what we do instead
```

**One page of evidence beats ten pages of narrative.** Executives fund the memo that shows the ledger, the numbers, and the deprecation plan.

### Custom-request triage form (three business days, every time)

```
Request:                    [what they asked for, in their words]
Client / stakeholder:       [name, role, decision power]
Date received / SLA:        [date] → respond by [date + 3 business days]
Classification:             in-scope · configuration · product candidate · priced bespoke · decline
Evidence for class:         [SOW line · ledger row · effort estimate]
Effort estimate:            [eng-days, with confidence]
What it displaces:          [the thing that will not happen if we do this]
Commercial treatment:       [no charge / change order $X / product-candidate commitment]
Decision + rationale:       [one paragraph, written to be read by the client]
Communicated to client by:  [name, date, channel]
Ledger updated:             [yes — row ID]
```

### The cadence calendar — your default week

| Day | Ritual | Artifact produced |
|---|---|---|
| Daily 09:15 | Embedded triage (15 min) | Blocker list with owners; request classifications |
| Tue | Client demo prep + internal review | Increment accepted; next increment agreed |
| Wed | Client demo | Visible progress; client feedback captured into the ledger |
| Thu | Deep work block: RFCs, ADRs, memos, evals review | One written decision artifact |
| Fri | Harvest half-hour + week close | Ledger rows updated; one candidate nominated or one "no" written |
| Monthly | Client steering + harvest session | Scope decisions; abstraction RFC or decline memo |
| Quarterly | Portfolio review | Distance-from-core distribution; reuse rate; roadmap commitments |

**The PM's non-negotiable:** the Thursday writing block and the Friday harvest. A PM who is only reacting has no flywheel — they have a queue.

### The FDE hiring scorecard (and why the PM sits on the panel)

The manual has said FDEs are not interchangeable with product engineers (5A-14). This makes that operational, because the biggest lever on the flywheel is *who you hire into it* — and the cost of hiring wrong is a team that ships demos instead of systems, or a team that ships systems and writes down nothing.

**Seven dimensions (score 1–4 each; evidence required; no "impression" scores):**

| Dimension | What it means in an FDE context | Signal question — ask for a story, not an opinion |
|---|---|---|
| Domain immersion | Enters a customer's world fast; asks "walk me through one case" before "what's your API" | "Tell me about a time you learned an unfamiliar domain under a deadline — what did you read, who did you shadow, what did you get wrong?" |
| Data detective instinct | Treats messy client data as the problem to be found, not an obstacle | "Tell me about a case where the data was wrong and the system was right. How did you find it?" |
| Boring-glue pragmatism | Writes the connector, the script, the config — not just the model call | "What's the most boring thing you've built that mattered, and how long did you maintain it?" |
| Client-room communication | Explains trade-offs to non-engineers; holds a line without burning trust | "Describe a time you told a client no, and what you said." |
| Ownership past handoff | Responsible when the spec is wrong and they're on call | "Tell me about a system you owned after launch — what broke at 2am and what did you learn?" |
| Harvest instinct | Sees the repeated pattern; writes it down without being asked | "When did you notice you were building the same thing a second time, and what did you do about it?" |
| Judgment under pressure | Triage — quick fix vs. correct fix vs. escalate — under a client's clock | "Walk me through the hardest production incident you handled alone, and the call you made with incomplete information." |

**Two working exercises (stronger than interviews):**

1. **The data dig.** Hand over a small, messy dataset (a raw export, duplicated records, one bad join) and one real question. Watch whether they (a) explore before coding, (b) name the quality problems, (c) write the boring pipeline. Score the process, not the answer.
2. **The client roleplay.** A stakeholder asks for something that does not need AI and is out of scope. Watch whether they diagnose before proposing, say no with a price, and leave the stakeholder feeling heard.

**Reject signals (any one is disqualifying, documented):** asks who owns the roadmap before who owns the client · cannot name a boring thing they built that mattered · blames the client for a failed deployment · cites only greenfield or personal projects · cannot explain a technical trade-off in plain words · "I don't do support or on-call."

**The PM sits on the panel** because two dimensions — client-room communication and harvest instinct — are the traits the PM depends on daily, and the FDE lead is not the only judge of them. Calibrate per cohort: after 90 days, compare hired candidates' scores against actual performance and re-weight (the `templates/30-60-90.md` plan is the calibration instrument).

**The two-pool warning (from 5A-13).** Hiring only FDEs — no platform pool, no enabling role — stalls the flywheel no matter how good the individuals are. The scorecard serves a topology; it does not replace one.

Fill-in version: `templates/fde-hiring-scorecard.md`.

---

# Appendices

## Appendix A — Suggested pace

About 90 hours in total: Module 1 ~18 h · Module 2 ~16 h · Module 3 ~16 h · Module 4 ~20 h · Module 5 ~12 h · the worked case ~8 h. At 5 hours a week that is roughly 18 weeks; at 8 hours a week, about 11.

There is no schedule to keep and nothing to submit. The useful order: Modules 1–2 before your first client conversation, Module 3 before anyone says the word "data", Module 4 before anyone says "done", Module 5 as engagements accumulate. Read it against live work — every blueprint and template here has a real engagement it can be applied to, and applying one is worth more than reading the module twice.

---

## Appendix B — Reference bank and verification status

All URLs below were checked on **September 12, 2026**. Verification method is stated per group, because "verified" means different things depending on whether a site permits automated fetching. Source types are marked **[P]** primary (the operator's own documentation or engineering writing), **[R]** research, **[V]** vendor, **[S]** standard/regulatory.

**Verified by direct HTTP fetch (status 200, title matched)**

- [P] gRPC — *Introduction* · https://grpc.io/docs/what-is-grpc/introduction/
- [P] Google — *API Design Guide* · https://cloud.google.com/apis/design
- [P] Fowler — *Richardson Maturity Model* · https://martinfowler.com/articles/richardsonMaturityModel.html
- [P] Protocol Buffers · https://protobuf.dev/ · JSON Schema · https://json-schema.org/
- [P] Kafka — *Introduction* · https://kafka.apache.org/intro
- [P] Databricks — *Medallion Architecture* · https://www.databricks.com/glossary/medallion-architecture
- [P] dbt — *What is dbt* · https://docs.getdbt.com/docs/introduction
- [P] C4 model · https://c4model.com/ · ADR resources · https://adr.github.io/ · Fowler — *Architecture Decision Record* · https://martinfowler.com/bliki/ArchitectureDecisionRecord.html
- [P] *Enterprise Integration Patterns* · https://www.enterpriseintegrationpatterns.com/
- [P] Azure Architecture Center — *Cloud Design Patterns* · https://learn.microsoft.com/en-us/azure/architecture/patterns/
- [P] AWS — *Well-Architected Framework* · https://aws.amazon.com/architecture/well-architected/
- [P] OpenTelemetry docs · https://opentelemetry.io/docs/
- [P] pgvector · https://github.com/pgvector/pgvector · tiktoken · https://github.com/openai/tiktoken · MTEB · https://huggingface.co/blog/mteb
- [P] OpenAI — *Structured outputs* · https://platform.openai.com/docs/guides/structured-outputs · *Evaluation best practices* · https://developers.openai.com/api/docs/guides/evaluation-best-practices · *Model optimization (fine-tuning)* · https://platform.openai.com/docs/guides/fine-tuning
- [P] Anthropic — *Prompt caching* · https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching · *Building effective agents* · https://www.anthropic.com/engineering/building-effective-agents · *Effective context engineering* · https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents · *Contextual Retrieval* · https://www.anthropic.com/news/contextual-retrieval
- [P] Wolfram — *What Is ChatGPT Doing…* · https://writings.stephenwolfram.com/2023/02/what-is-chatgpt-doing-and-why-does-it-work
- [R] arXiv, all verified with matching titles: 1603.09320 (HNSW) · 1706.03762 (Transformer) · 2005.11401 (RAG) · 2005.14165 (GPT-3) · 2107.03374 (Codex/HumanEval) · 2202.03629 (hallucination survey) · 2210.03629 (ReAct) · 2211.09110 (HELM) · 2304.09848 (verifiability) · 2305.05176 (FrugalGPT) · 2306.05685 (LLM-as-judge) · 2307.03172 (Lost in the Middle) · 2308.11432 (agent survey) · 2309.15217 (Ragas) · 2310.03714 (DSPy) · 2310.06770 (SWE-bench) · 2403.04132 (Chatbot Arena) · 2404.14618 (Hybrid LLM) · 2404.16130 (GraphRAG) · 2406.12624 (Judging the Judges) · 2406.18665 (RouteLLM) · 2504.20879 (Leaderboard Illusion) · 2509.20353 (Copilot field study)
- [S] OWASP — *Top 10 for LLM Applications* · https://genai.owasp.org/llm-top-10/ (2025 list: LLM01 prompt injection → LLM10 unbounded consumption, titles confirmed)
- [S] NIST — *AI RMF* · https://www.nist.gov/itl/ai-risk-management-framework · *Playbook* · https://www.nist.gov/itl/ai-risk-management-framework/nist-ai-rmf-playbook · *GenAI Profile (NIST AI 600-1)* · https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.600-1.pdf · *SP 800-162 (ABAC)* · https://csrc.nist.gov/pubs/sp/800/162/upd2/final · *SP 800-207 (Zero Trust)* · https://csrc.nist.gov/pubs/sp/800/207/final
- [S] AICPA & CIMA — *SOC suite* · https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2 · GDPR text · https://gdpr-info.eu/ · EU AI Act tracker · https://artificialintelligenceact.eu/ · FedRAMP · https://fedramp.gov/
- [P] AWS — *SOC compliance* · https://aws.amazon.com/compliance/soc-faqs/ · Google Cloud — *SOC 2* · https://cloud.google.com/security/compliance/soc-2
- [P] AWS — *SaaS Tenant Isolation Strategies* · https://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/saas-tenant-isolation-strategies.html · *What is Amazon VPC* · https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html · Azure — *Tenancy models* · https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/considerations/tenancy-models
- [P] OpenID Connect · https://openid.net/connect/ · SCIM protocol (RFC 7644) · https://www.rfc-editor.org/rfc/rfc7644 · Google OAuth 2.0 · https://developers.google.com/identity/protocols/oauth2
- [P] Microsoft Presidio · https://microsoft.github.io/presidio/ · NVIDIA NeMo Guardrails · https://github.com/NVIDIA/NeMo-Guardrails
- [P] Great Expectations · https://docs.greatexpectations.io/docs/
- [P] OpenAI Evals · https://github.com/openai/evals · promptfoo · https://github.com/promptfoo/promptfoo · DeepEval · https://github.com/confident-ai/deepeval · Ragas docs · https://docs.ragas.io/
- [P] Langfuse · https://langfuse.com/docs · LangSmith · https://docs.smith.langchain.com/ · LangGraph Graph API · https://docs.langchain.com/oss/python/langgraph/graph-api
- [P] Evidently AI — *model monitoring* · https://www.evidentlyai.com/ml-in-production/model-monitoring
- [P] Google SRE — *SLOs* · https://sre.google/sre-book/service-level-objectives/ · *Eliminating toil* · https://sre.google/sre-book/eliminating-toil/ · *The Tail at Scale* · https://research.google/pubs/pub40801/ · DORA · https://dora.dev/
- [R/P] Forsgren et al. — *The SPACE of Developer Productivity* · https://queue.acm.org/detail.cfm?id=3454124
- [P] Stanford HAI — *AI Index* · https://hai.stanford.edu/ai-index
- [P] Uber — *Domain-Oriented Microservice Architecture* · https://www.uber.com/us/en/blog/microservice-architecture/ · *Meet Michelangelo* · https://www.uber.com/us/en/blog/michelangelo-machine-learning-platform/ · *From Predictive to Generative* · https://www.uber.com/us/en/blog/from-predictive-to-generative-ai/
- [P] Stripe — *APIs as infrastructure* · https://stripe.com/blog/api-versioning
- [P] SVPG — *Product vs. Feature Teams* · https://www.svpg.com/product-vs-feature-teams/ · Fowler — *Conway's Law* · https://martinfowler.com/bliki/ConwaysLaw.html · *Technical Debt Quadrant* · https://martinfowler.com/bliki/TechnicalDebtQuadrant.html · Team Topologies — *Key concepts* · https://teamtopologies.com/key-concepts
- [P] Kleppmann — *Designing Data-Intensive Applications* · https://dataintensive.net
- [P] *Data Gravity – in the Clouds* (McCrory's original 2010 post) · https://datagravitas.com/2010/12/07/data-gravity-in-the-clouds/ · Dell — *It's Not a Storage Problem, It's Data Gravity* · https://www.dell.com/en-us/blog/its-not-a-storage-problem-its-data-gravity/ (read as vendor positioning on the concept)
- [V] Intercom — *Meet Fin* · https://www.intercom.com/blog/announcing-intercoms-new-ai-chatbot/ · *From resolutions to outcomes* · https://www.intercom.com/blog/from-resolutions-to-outcomes-evolving-how-fin-delivers-value/
- [V] AWS — *Intercom & Anthropic case study* · https://aws.amazon.com/solutions/case-studies/intercom-anthropic/ (average resolution 56% within 30 days, up to 90%, 4,000+ customers — all vendor-reported)
- [V] OpenAI — *Klarna's AI assistant* · https://openai.com/index/klarna/ · Klarna press release · https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/
- [P] GitHub — *Quantifying Copilot's impact* · https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness
- [R] Cui et al. — *The Effects of Generative AI on High-Skilled Work* · https://economics.mit.edu/sites/default/files/inline-files/draft_copilot_experiments.pdf · METR — *Early-2025 AI and experienced OSS developer productivity* · https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
- [S/P] CISA & UK NCSC — *Guidelines for Secure AI System Development* · https://www.cisa.gov/news-events/news/dhs-cisa-and-uk-ncsc-release-joint-guidelines-secure-ai-system-development · HHS — *HIPAA* · https://www.hhs.gov/hipaa/index.html
- [P] Google — *RAG vs. fine-tuning* · https://cloud.google.com/blog/products/ai-machine-learning/rag-vs-fine-tuning (vendor framing of the trade-off)
- [P] Palantir — *Foundry documentation* · https://www.palantir.com/docs/foundry/

**Verified via proxy fetch (site blocks automated clients; page title and content confirmed)**

- [P] Palantir blog — *A Day in the Life of a Forward Deployed Software Engineer* · https://blog.palantir.com/a-day-in-the-life-of-a-palantir-forward-deployed-software-engineer-45ef2de257b1
- [P] Palantir blog — *Dev versus Delta* · https://blog.palantir.com/dev-versus-delta-demystifying-engineering-roles-at-palantir-ad44c2a6e87
- [P] Palantir blog — *The Baseline Team / forward-deployed infrastructure engineering* · https://blog.palantir.com/the-baseline-team-and-forward-deployed-infrastructure-engineering-at-palantir-efd84e72e40b
- [P] Palantir blog — *Ontology-Oriented Software Development* · https://blog.palantir.com/ontology-oriented-software-development-68d7353fdb12
- [P] Palantir blog — *How Foundry's Ontology Deploys Data Science to the Front Line* · https://blog.palantir.com/how-palantir-foundrys-ontology-deploys-data-science-to-the-front-line-7a9679bdfd01
- [P] Palantir — *Form S-1* (2020) · https://www.sec.gov/Archives/edgar/data/1321655/000119312520230013/d904406ds1.htm
- [S] ISO/IEC 42001:2023 · https://www.iso.org/standard/42001
- [P] HBR — Kotter, *Leading Change* · https://hbr.org/1995/03/leading-change-why-transformation-efforts-fail-2 · Christensen et al., *Know Your Customers' Jobs to Be Done* · https://hbr.org/2016/09/know-your-customers-jobs-to-be-done
- [V] Fortune — *Klarna plans to hire humans again* · https://fortune.com/2025/05/09/klarna-ai-humans-return-on-investment

**Verified via search index only (blocks both direct and proxy fetches; title and publisher confirmed, content not read in full)**

- [V/press] Forbes — *Klarna reverses AI push* · https://www.forbes.com/sites/quickerbettertech/2025/05/18/business-tech-news-klarna-reverses-on-ai-says-customers-like-talking-to-people
- [V/report] MIT NANDA — *The GenAI Divide: State of AI in Business 2025* (widely-cited 95% figure; report copy hosted by MLQ) · https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf

**Not included, deliberately.** Palantir's Apollo continuous-delivery blog post (URL now 404 — the Baseline team post covers the same ground), and any "X% of AI pilots fail" statistic quoted without a method. Consulting-blog statistics and vendor benchmark charts were excluded on the same principle the manual teaches: unsourced precision is worse than an honest range.

**Added in v1.2 (all verified 2026-09-12):**

- [P] ggml.ai (llama.cpp, open-weight model runtime) · https://ggml.ai/ — direct fetch
- [P] Hugging Face — quantization overview · https://huggingface.co/docs/transformers/en/quantization/overview — direct fetch
- [R] Ganguli et al. 2022 — *Red Teaming Language Models to Reduce Harms* · https://arxiv.org/abs/2209.07858 — direct fetch (arXiv)
- [R/community] AI Incident Database · https://incidentdatabase.ai/ — direct fetch
- [P/practitioner] GTMnow — Intercom outcome pricing (Archana Agrawal) · https://gtmnow.com/how-intercom-built-the-highest-performing-ai-agent-on-the-market-using-outcome-based-pricing-with-archana-agrawal-president-at-intercom/ — proxy fetch (site 403s to curl)

---

## Appendix C — Template index

| Template | Use it for | Module |
|---|---|---|
| `templates/adr.md` | Architecture Decision Record — the PM's section is Consequences | M1 |
| `templates/fde-discovery-rfc.md` | Internal alignment on the problem before any client promise | M2 |
| `templates/feasibility.md` | Instrument recommendation and expectations before pricing (existing program template) | M2 |
| `templates/sow.md` | Scope in/out, data access, acceptance, metrics, HITL, handoff (existing program template) | M2 |
| `templates/enterprise-security-questionnaire.md` | The 30 questions, answerable from the architecture | M3 |
| `templates/fde-pilot-acceptance-criteria.md` | "Done," defined and signed before the demo | M4 |
| `templates/eval-suite.md`, `templates/production-eval-plan.md` | Golden set, scoring, gates, drift, feedback loop (existing program templates) | M4 |
| `templates/cost-model.md` | Build cost, run-rate, payback, sensitivity (existing program template) | M4 |
| `templates/pattern-ledger.md` | The instrument that makes productization possible | M5 |
| `templates/productization-memo.md` | The gate document: signal test, abstraction, migration, deprecation | M5 |
| `templates/30-60-90.md` | Your own first-90-days plan for the FDE-PM seat (existing program template) | M5 |
| `templates/fde-hiring-scorecard.md` | The 7-dimension FDE hiring instrument: scorecard, signal questions, working exercises, reject signals | M5 |

---

## Appendix D — Worked end-to-end case: remote assistance for distributed field operations

**All figures in this appendix are illustrative**, constructed to show the arithmetic and the decision chain. Substitute your own client's numbers; the structure is the deliverable.

### The situation

A client operates 640 field technicians across 12 regions servicing audiovisual and conferencing installations: 3,000 remote-assistance calls a month, median handling 14 minutes, 28% escalating to engineering, first-time-fix 71%. The knowledge base is three SharePoint sites, two Confluence spaces, four vendor portals, and the senior technicians' memories. The operations director's ask: *"an AI assistant that answers questions so the desk resolves calls faster."*

### Gate 1 — Problem reality (Module 2)

Discovery (half-day workshop + two shadowed shifts + a traffic export) produced:

| Finding | Evidence | Implication |
|---|---|---|
| 41% of calls repeat ~60 known failure signatures | Ticket text clustering, 3 months | A deterministic triage/decision tree covers a large share before any model is involved |
| Median 14 min hides a bimodal distribution: 6 min for known signatures, 38 min for escalations | Ticket timestamps | The cost is the escalation tail, not the average call |
| Technicians don't trust the KB: three conflicting versions of the same procedure | Corpus audit (four documents, two vendors, one internal) | Retrieval without a curation step will surface contradictions and destroy trust |
| The intake form's four free-text fields cause 22% of mis-routing | Sample review by the desk lead | A form change is a prerequisite, not a nice-to-have |
| Client's compliance team requires cited sources for any procedure guidance | Security review meeting | Citation is a hard requirement, not a feature |

**The reframed problem:** *the desk's escalation tail (38-minute calls, 28% of volume) is driven by slow discovery of the right procedure and by conflicting documentation; and the intake form is mis-routing a fifth of calls.*

### Gate 2 — Instrument choice (Module 2)

| Instrument | Verdict | Reasoning |
|---|---|---|
| Deterministic rules / decision tree | **Yes** | Covers the 41% known-signature share exactly, cheaply, and auditably; becomes the fallback path |
| Classic ML | No | No labels for "correct procedure"; the task is retrieval and guidance, not classification |
| Retrieval only (search) | Partial | Improves discovery, but the requirement is cited, phrased guidance for a technician mid-job |
| RAG with citations | **Yes** | Meets the citation requirement; corpus exists; measurable with a golden set |
| Fine-tune | No | Cannot fix the version-conflict problem and cannot cite; would bake in one snapshot of a changing corpus |
| Agentic tool use (auto-remediation) | No — this phase | Irreversible actions on production AV systems; revisit only for read-only diagnostics |
| Human-in-the-loop | **Yes** | Every safety-relevant step reviewed; guidance-only answers auto-returned |
| Process change | **Yes** | Intake form redesign; KB deduplication sprint; both prerequisites |

**Decision:** guided-assist that retrieves the *authoritative* (curated) procedure, returns a cited, stepwise answer, routes known signatures through the deterministic tree, and escalates with a structured diagnostic summary when confidence is low.

### Gate 3 — Integration and compliance (Module 3)

| Question | Answer |
|---|---|
| Where does the data live? | Client's SharePoint/Confluence via read-only connector; nothing copied outside their tenant except retrieved excerpts at query time |
| Deployment model | Dedicated tenant in the client's cloud region; private connectivity; no data residency exception requested |
| Identity | SSO via the client IdP; retrieval filters by the technician's region and entitlement group (no cross-region procedure leakage) |
| PII | Site and asset identifiers only; no customer personal data in scope; redaction boundary nonetheless drawn and tested |
| Auditability | Every answer logged with retrieved chunk IDs, corpus version, model/prompt version, entitlement set |
| Retention | Answers 13 months; traces 90 days; corpus mirrors source permissions nightly |
| Erasure | Source-of-truth deletion propagates to index on the nightly rebuild; documented and tested |
| Injection posture | Retrieved content treated as data; no tools with write access; egress allow-list; step budget on the retrieval loop |

### Gate 4 — Evals, acceptance, and ROI (Module 4)

**Acceptance criteria (agreed before the first demo):**

- *Business:* median handling time for assisted calls ≤ 12 minutes, and escalation share ≤ 21%, measured from ticket system timestamps over 90 days on ≥ 400 assisted calls.
- *Quality:* ≥ 85% correct on a 150-case client-authored golden set; ≥ 95% on the rare-hardware slice; the safety-critical slice (mains power, rigging, live-event procedures) is **never auto-answered** — 100% human review, so it is a design constraint rather than a score.
- *Operational:* p95 ≤ 4 s; cost ≤ $0.30 per assisted call; escalation handoff includes the structured diagnostic summary ≥ 90% of the time.
- *Adoption:* ≥ 70% of desk staff using it weekly by week 8, training complete.
- *Below the bar:* two-week rework window, then a paid extension or termination.

**ROI model (illustrative arithmetic, all inputs sourced in the model):**

| Line | Value |
|---|---|
| Baseline monthly cost | $129,360 (desk $46,200 + escalated engineering $83,160) |
| Measured after pilot (12 min median, 21% escalation, $0.22/call, $2,400/mo run-rate) | $105,030 |
| Gross monthly benefit | **$24,330** |
| One-time build | $180,000 |
| Payback | **7.4 months** |
| Sensitivity: no improvement in handle time or escalation | −$3,060/month — the system is a net cost. *This row is why the pilot exists* |
| Sensitivity: moderate (13 min, 24% escalation) | +$12,120/month, payback 14.9 months |

**The honest framing to the sponsor:** the business case does not depend on the model being impressive. It depends on the *process* changes — intake form, curated KB, deterministic triage — which is why those are in the first increment rather than the backlog.

### Gate 5 — Productization (Module 5)

Pattern ledger entry after the third similar engagement (a manufacturing field-service org, a hospital biomedical team, and this AV operator): *guided diagnostics with cited procedures over fragmented client knowledge bases, with escalation handoff.* Signal test: recurs (3 clients) ✓ · bespoke cost ~25 eng-days each ✓ · two clients indicated willingness to pay for a configured version ✓ · close to core (retrieval + evals + connector framework) ✓.

**Abstraction:** core = connector framework, entitlement-aware retrieval, citation rendering, escalation-summary generation, and the golden-set/eval harness. Configurable axes = corpus sources, procedure taxonomy, safety-slice definition, escalation destination. Stays bespoke = the deterministic decision tree per client. **Deprecation:** the three bespoke implementations migrate to core configuration over two releases; branches frozen at migration and removed at the release after.

**What made it productizable was not the model.** It was the eval harness and the connector framework — the two things that were rebuilt four times.

---

## Appendix E — How this manual connects to the rest of the program, and to interviews

| This manual | Reinforces | New ground it adds |
|---|---|---|
| M1 · Substrate | AI 510 (LLM literacy), AIPM 520 M1–M2 | Interface/streaming architecture, ADRs, diagram protocol, cost-per-outcome |
| M2 · Discovery & scoping | PM 501 (discovery, PRD), FDE 560 M2 | The instrument decision matrix, SOW constraint discipline, the written no |
| M3 · Integration & compliance | RSK 550 (governance), DATA 530 (data) | Deployment models, permission-aware retrieval, the 30-question security interview, injection testing |
| M4 · Evals & ROI | AIPM 520 M3–M4 (evals), DATA 530 (metrics) | Judge calibration, acceptance criteria, ROI model with sensitivity, metrics-that-lie discipline |
| M5 · Flywheel | FDE 560 M4 (productization), STRAT 540 (economics) | Pattern ledger, signal test, triage tree, cadence calendar, RACI, the shield script |

**Using the five gates in an interview case.** For case exercises and interviews (operations, program lead, or platform roles), the gates are a structuring framework that outperforms generic frameworks because it produces a decision, not a list:

1. **Quantify the problem** and name who owns it (Gate 1) — the step most candidates skip.
2. **Choose the instrument** with explicit rejected options and a deterministic baseline (Gate 2).
3. **State the data and compliance constraints** that shape the design (Gate 3).
4. **Define acceptance before proposing the build** — thresholds, methods, sign-off (Gate 4).
5. **Say what becomes reusable**, and what stays bespoke (Gate 5).

Then close with the two sentences that distinguish a senior answer: *what would make me say no*, and *what I would measure in 90 days to know I was wrong.*

---

## Appendix F — Re-verification protocol and changelog

**Every quarter, or before reusing this manual for a new engagement:**

1. Re-run the URL check for Appendix B (a scriptable loop: fetch, compare status and title; the pattern used to build this version is in `tools/verify_links.py`).
2. Re-check the OWASP list version and the NIST AI RMF supplementary documents — both have revision cycles.
3. Re-check the EU AI Act's phased application dates; obligations arrive in stages.
4. Re-check the case-study numbers: vendor pages change quietly (Intercom's own reported average has moved from 56% to 76% as the definition and mix evolved).
5. Re-read the `Metrics that lie` table before quoting any figure from a deck you did not build.

**Changelog**

| Version | Date | Change |
|---|---|---|
| 1.5 | 2026-09-12 | New edition design for the HTML edition: Apple-grade typography and layout — frosted top bar, sticky grouped contents with scroll-spy and filter, display type scale, hairline tables, soft-radius diagram blocks, light/dark appearance, print stylesheet |
| 1.4 | 2026-09-12 | Removed the course scaffolding — per-module exercises, readiness-marker checklists, the assessment explainer, and the 18-week study plan (replaced with a short pacing note). This is a personal reference, not coursework |
| 1.3 | 2026-09-12 | Added the AI product lifecycle (front matter: 12 phases mapped to the gates and modules) and GitHub vocabulary + working surface (M1 B6) |
| 1.2 | 2026-09-12 | Added model selection & routing economics (M1 B5), safety/harm evals & AI incident response (M4 B4 + 4D + 4C), pricing & monetization (M5 B2 + 5C); expanded `templates/productization-memo.md` with a pricing-model row |
| 1.1 | 2026-09-12 | Audit: corrected self-reported counts (17 blueprints, not 12; 6 new templates, not 5); added the FDE hiring scorecard to Module 5 (playbook + `templates/fde-hiring-scorecard.md`) |
| 1.0 | 2026-09-12 | Initial manual: 5 modules, 17 blueprints, 9 field artifacts, 6 new templates, reference bank verified |

**A closing note.** This manual is deliberately more honest about uncertainty than most material of its kind: thresholds are stated as ranges, vendor claims are labelled, and the case that most resembles a success story (Klarna) appears alongside its reversal. That is not hedging — it is the actual skill this role requires. The PM who can say "here is what we know, here is what we don't, here is what would change my mind" is the one clients call first and engineers listen to.
