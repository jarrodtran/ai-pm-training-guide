# PROD 260 — Case Packet

## How to use this packet (HBS case method)

For each case: (1) read the packet and the assigned primary sources; (2) form a view on the decision or judgment the case centers; (3) **write your 1-page decision memo before reading the teaching note** at the end of that case; (4) then read the teaching note and grade your memo against it. Memos are 5% of the course grade each.

All facts and figures below were verified against the cited primary sources, August 2026. Where a number is *vendor-published* (company or partner claims), it is labeled as such — treating that distinction is part of the exercise.

---

# CASE A — GitHub Copilot: "Measuring the Unmeasurable"

**Prepared for PROD 260 · Module 6 (Measurement)**
**Sources:** GitHub Research blog (2022); Chen et al. 2021 (arXiv:2107.03374); GitHub public statistics pages (2024–2025); independent replication study (arXiv:2509.20353).

## Background

In June 2022, GitHub shipped Copilot — an AI pair programmer that suggests code as developers type — as a generally available product. It is powered by Codex, a GPT model fine-tuned on public code, described in the research paper *Evaluating Large Language Models Trained on Code* (Chen et al., 2021). The paper introduced **HumanEval**, an evaluation set of 164 programming problems that tests *functional correctness* — does the generated code pass the test? Codex solved 28.8% of HumanEval problems on its first sample; with 100 samples per problem, 70.2%. The paper's authors themselves noted limitations: difficulty with long chains of operations, and "the potential broader impacts of deploying powerful code generation technologies, covering safety, security, and economics."

## Timeline

| Date | Event |
|---|---|
| Jul 2021 | Codex paper published (arXiv:2107.03374) |
| Jun 2021 | Copilot technical preview announced (VS Code extension) |
| Jun 2022 | Copilot general availability |
| Sep 2022 | GitHub publishes its productivity experiment (below) |
| 2023–2024 | GitHub reports rising share of AI-written code; claims reach 46% of code in enabled files, up from 27% in 2022 (GitHub statistics pages — *vendor-published*) |
| Jul 2025 | GitHub reports 20M all-time users; claims 90% of Fortune 100 companies have deployed Copilot (*vendor-published*) |

## The measurement problem

Copilot is the canonical "hard to measure" AI feature: its output is open-ended code, its value is partly subjective (developer satisfaction, focus, learning), and its failures (subtle bugs, security vulnerabilities, plausible-looking nonsense) may not surface for months. GitHub's own research (Sep 2022) ran a controlled experiment with 95 professional developers: those using Copilot completed an HTTP-server task **55% faster** (1h11m vs. 2h41m; P=0.0017; 95% CI [21%, 73%]) — a real, statistically significant result on a narrow task.

But the picture is contested at field scale. A later independent longitudinal study of a company's engineering team (arXiv:2509.20353, 2025) found **no statistically significant difference** in developers' weekly activity after adopting Copilot, while noting participants *felt* faster. Meanwhile vendor statistics emphasize adoption and share-of-code, not business outcomes.

**Exhibit A — the numbers in play:**

| Metric | Value | Source type |
|---|---|---|
| HumanEval solve rate (Codex, first sample) | 28.8% | Research paper |
| HumanEval solve rate (100 samples) | 70.2% | Research paper |
| Task completion speedup (controlled, n=95) | 55% faster | Vendor research (GitHub) |
| Speedup 95% confidence interval | [21%, 73%] | Vendor research (GitHub) |
| Share of code written by Copilot (2022 → 2024) | 27% → 46% | Vendor statistics |
| Weekly-activity effect in field study | Not statistically significant | Independent study |
| All-time users (Jul 2025) | 20M | Vendor statistics |

## The decision

You are the PM who must convince the company (and customers) that Copilot delivers measurable value. Your choices of metric will determine what the company optimizes: **developer speed** (controlled experiments), **developer satisfaction** (surveys — GitHub reported >90% agreement that it accelerates repetitive work), **code quality** (bug rates, security findings, review times), **business outcomes** (merge time, time-to-ship features, retention), or some combination. Each metric has a trap: speed experiments don't generalize; satisfaction is subjective; quality is confounded by the very code the AI wrote; business outcomes take quarters.

**Your memo (1 page):** Define how you would *measure* Copilot's value. What is the north star for a developer-tool AI? What are the guardrails? Which claims in Exhibit A would you trust, which would you discount, and how would you design your own evaluation? Where does the capability/reliability gap show up in this product?

## Discussion questions

1. What does the gap between GitHub's controlled experiment and the independent field study teach you about AI measurement in general?
2. If you optimized for "share of code written by AI," what would you accidentally optimize against? (Consider learning, code review load, security.)
3. HumanEval tests functional correctness. What does it *not* test — and what would you add for a production developer tool?

---

### Teaching note — Case A

**What to look for in a strong memo:** (1) A recognition that no single metric suffices — the best memos define a metric *system*: a north star (e.g., time-to-merge or developer-reported value), quality guardrails (bug rate, security findings), and satisfaction measures. (2) Explicit skepticism of vendor numbers — 55% is a narrow task; 46% share-of-code is an input, not an outcome. (3) A designed evaluation: the memo proposes its own controlled or quasi-experiment rather than accepting any published number. (4) Naming the capability/reliability gap: the demo (solves a task fast) vs. production reality (subtle bugs, security risk).

**The recurring lesson (module-level):** when the artifact is open-ended, measurement is a *design* problem first. Copilot forced the industry to invent measurement; the PM who defines the metric system controls the strategy conversation. Red flags: accepting any single number, especially a vendor one; proposing "accuracy" or "speed" as if self-evident; no mention of what could go wrong.

---

# CASE B — Intercom Fin: "The Retrieval-First Support Agent"

**Prepared for PROD 260 · Module 12 (Feasibility & System Design)**
**Sources:** Intercom launch post (Mar 2023); AWS × Anthropic × Intercom case study (2024–2025); Fin customer case studies (Rocket Money, Consensys — vendor-published).

## Background

In March 2023 — days after GPT-4's release — Intercom announced **Fin**, an AI customer-support agent. The founding design constraint is stated plainly in the launch post: Fin "is designed to only provide answers based on content in your existing help center," because "large language models currently have a different failure mode than previous bots: while a rules bot may deliver an irrelevant answer, our AI bot may deliver an *incorrect* answer." Fin links to its source articles so users can verify; when help content updates, answers update with it. The launch post also flags the era's constraints: cost ("large language models are currently expensive to run") and latency ("10 or more seconds of latency is not uncommon").

Intercom later rebuilt Fin on Anthropic's Claude via AWS Bedrock. The architecture (per the AWS case study) is **15–20 subcomponents, each paired with a specific model** — answer verification, policy-compliance checking, response generation — rather than one giant prompt. Intercom reports average resolution rates of **56% within 30 days of deployment**, with some customers reaching **80–90%**; **4,000+ customers** and "tens of millions of dollars" in revenue since launch (*vendor-published*). Anthropic itself became a Fin customer.

**Exhibit B — customer results (vendor-published, fin.ai):**

| Customer | Fin involvement | Resolution rate | Notes |
|---|---|---|---|
| Rocket Money | 54% of conversations | 68% | ~$1M annual efficiency gain; human CSAT +6 points; phased rollout (started at 10% of conversations, scoped workflows: billing, troubleshooting, account access) |
| Consensys | 90% of conversations | >70% | ~20k resolutions/month; ran a live "bake-off" vs. two competitors; pays per resolution |

## The decision

Fin is a feasibility and design case. Intercom made a series of architectural bets: retrieval-only answers (no improvisation from training knowledge), source-link transparency, per-task models (verify → generate → policy-check) instead of one monolithic prompt, explicit human handoff for high-stakes actions (e.g., cancellations), and phasing — customers like Rocket Money started at 10% of conversations with tightly scoped workflows. You are the PM at a company building a similar agent for a *different* domain (pick one: healthcare scheduling, field-service support, or a B2B software help desk). Which of Fin's bets transfer? Which don't? What does your feasibility assessment say?

**Your memo (1 page):** For your chosen domain: (1) feasibility — AI vs. rules vs. human for each of the top 5 support intents; (2) architecture — where retrieval, guardrails, policy checks, and human handoff sit; (3) the eval design you'd use before letting it touch real customers; (4) the rollout path (how you'd phase, like Rocket Money's 10% start).

## Discussion questions

1. Fin's launch post says the failure mode changed from "irrelevant" to "incorrect." Why is that a *harder* product problem? What does it imply for UX design (source links, disclosure)?
2. Why build 15–20 subcomponents with separate models instead of one long prompt? (Relate to Anthropic's "simple, composable patterns.")
3. Rocket Money started at 10% of conversations with billing/troubleshooting scope. What made that a good first slice? What would you add last, and why?

---

### Teaching note — Case B

**What to look for in a strong memo:** (1) Feasibility scored per intent, with high-stakes intents (account actions, health, money) reserved for humans or heavily guarded AI — not a blanket "AI for everything." (2) Architecture borrowing Fin's composition: retrieval + generation + a separate verification/policy step, plus escalation. (3) An eval design *before* customer exposure (golden set of the top intents, resolution correctness, hallucination rate on out-of-scope). (4) A phased rollout with a defined expansion order and a decision rule for expanding ("resolve ≥X% correctly on slice 1 for 4 weeks, then add slice 2"). Red flags: no human handoff; trusting the model's own knowledge; proposing to "just fine-tune" instead of retrieval; no measurement plan.

**The recurring lesson (module-level):** Fin is the reference architecture for production LLM products: *compose small, verified pieces; ground everything in retrieval; keep a human in the loop where stakes are high; measure before you scale.* The best memos also notice the business-model echo — outcome pricing (pay per resolution) aligns vendor and customer, a preview of Module 15's packaging discussion.

---

# CASE C — Duolingo Max: "When AI Succeeds, Margins Compress"

**Prepared for PROD 260 · Module 15 (Cost, Latency & Model Selection)**
**Sources:** Duolingo public announcements and SEC filings; press coverage of Q4/FY25 shareholder communications (as reported, 2025–2026).

## Background

Duolingo runs a two-layer AI system. The first layer is **Birdbrain**, a proprietary model refined over years that estimates, for every exercise, both its difficulty across the user base and the individual learner's proficiency — powering personalization at ~1 billion exercises per day. The second layer is generative: **Duolingo Max**, launched **March 14, 2023**, powered by GPT-4, adding Roleplay (conversations with AI characters) and Explain My Answer. Earlier experiments with GPT-3 had failed — the model couldn't sustain unscripted conversation.

The company then went all-in: an "AI-first" mandate in early 2024 (CEO memo; AI proficiency factored into hiring and reviews), ~10% of contract workforce cut, and content generation automated to nearly 100%. By end of 2025: **~50M daily active users**, **$1B+ in annual bookings**.

But the financials tell the other half of the story. **Gross margin compressed from 73.0% to 71.1%**, attributed in SEC filings to generative-AI compute costs. Analysts responded harshly — Morgan Stanley cut its price target from $245 to $100, flagging growth-vs-revenue prioritization. Max penetration stayed low (~5% of paid subscribers at end of 2025, on a ~$30/month tier, vs. the cheaper Super tier), and Duolingo began moving features down-tier (Video Call moving from Max to Super).

**Exhibit C — the tension:**

| Signal | Value |
|---|---|
| Birdbrain scale | ~1B exercises/day |
| Max launch | Mar 14, 2023 (GPT-4; Roleplay + Explain My Answer) |
| DAU (end 2025) | ~50M |
| Annual bookings (FY25) | $1B+ |
| Gross margin change | 73.0% → 71.1% (GenAI compute costs, per SEC filings) |
| Max share of paid subs | ~5% |
| Wall Street reaction | Price target cut $245 → $100 (Morgan Stanley) |

## The decision

You are the PM for Duolingo's generative-AI features. The classical trade-off has arrived with force: **AI features succeed, usage grows, and the compute bill grows with success — compressing margins that a subscription business was built to protect.** Your decisions: (1) *Model selection* — frontier (GPT-4-class) for Roleplay/Video Call vs. cheaper models elsewhere; what's the cost/quality/latency frontier, and where does Birdbrain (classical ML) remain the right tool? (2) *Packaging & pricing* — Max at ~$30/month with ~5% penetration; what pricing/feature structure aligns revenue with cost? (3) *The margin conversation* — how do you defend AI investment to a board watching margins compress and the stock fall?

**Your memo (1 page):** A cost and packaging strategy for Duolingo's generative features. Build a token-cost model for one feature (Roleplay: speech-to-text + LLM + text-to-speech per session — estimate tokens and cost per session using current pricing), recommend a model tiering strategy (which features get frontier models, which get cheap ones), and propose a pricing/packaging change with a rationale. Address the margin conversation head-on.

## Discussion questions

1. "If your AI features succeed, your compute bill grows with them." What pricing structures survive that reality, and which break?
2. Why is Birdbrain — not GPT-4 — still the engine of the core product? What does that say about when to use frontier models at all?
3. Analysts punished margin compression despite growth. Is the market wrong, or is there a real strategy problem in AI-era economics?

---

### Teaching note — Case C

**What to look for in a strong memo:** (1) A real cost model — tokens per session (Roleplay is a long multi-turn session with STT/TTS on top), cost per session, monthly cost at scale, and a tiering recommendation that keeps frontier models only where the experience demands them. (2) Recognition that classical ML (Birdbrain) carries the core experience at near-zero marginal cost — the lesson that "AI" isn't one technology and the cheapest model is often the right one. (3) A packaging proposal with logic: e.g., outcome-based value (language outcomes), tiered features by cost profile, or hybrid pricing — and an acknowledgment that the ~5% penetration suggests the $30 tier is mispriced or mispositioned. (4) A board-level framing: margin compression as an investment in a defensible data/moats flywheel vs. as a structural cost disease — the memo should take a side. Red flags: no cost math; "use the best model everywhere"; ignoring Birdbrain; no pricing proposal.

**The recurring lesson (module-level):** success has a cost curve. Budget for your own success before launch — model tiering, caching, and packaging that aligns revenue with compute are not optimizations, they are the product strategy.

---

# CASE D — Klarna AI Assistant: "Vendor Claims as Data"

**Prepared for PROD 260 · Module 16 (Risk, Safety & Go-to-Market)**
**Sources:** Klarna press release (Feb 2024); OpenAI customer story (2024). *Both are vendor-published — that is the case.*

## Background

In February 2024, Klarna — a global payments and shopping network with ~150M consumers — launched an OpenAI-powered customer-service assistant inside its app. The numbers, published by Klarna and OpenAI within the first month:

**Exhibit D — the claims:**

| Claim | Value | Source |
|---|---|---|
| Conversations handled (month 1) | 2.3M — two-thirds of all customer-service chats | Klarna press release / OpenAI story |
| Agent-equivalent work | 700 full-time agents | Same |
| Customer satisfaction | "On par with human agents" | Same |
| Repeat inquiries | −25% | Same |
| Resolution time | <2 min vs. 11 min previously | Same |
| Markets / languages | 23 markets, 35+ languages, 24/7 | Same |
| Projected profit improvement (2024) | ~$40M | Same |

## The decision

You are (a) the PM at a fintech reviewing this case to decide whether to replicate it; or (b) the PM at Klarna defending the numbers to a skeptical board. Both readings are the same exercise: **separate signal from marketing.** The claims are vendor-published — Klarna has an incentive to frame aggressively (and a history of AI-forward PR), and OpenAI has an incentive to showcase customers. The metrics themselves are a mixed bag: resolution time (an *efficiency* metric) and repeat inquiries (a *quality* metric) are the strongest; "on par with human agents" on CSAT is plausible but under-specified (sample, selection, survey mechanics); "work of 700 agents" is a rhetorical unit, not a measurement; the $40M is a projection. And this is *fintech*: refunds, account access, PII, regulated markets — the risk surface is severe. What would you verify, how, and what would you build to keep this safe at scale?

**Your memo (1 page):** A verification and risk plan. (1) For each headline claim: what would you need to see to believe it, and what would you measure yourself? (2) A risk register for a fintech support agent: hallucination, bias, privacy, security (prompt injection on a financial chatbot), compliance — with mitigations and *detection* mechanisms. (3) The human-in-the-loop design: which actions may the agent take unassisted, which require escalation, and how do you make that legible to customers?

## Discussion questions

1. "Resolution time down from 11 to 2 minutes" — what could make that number flattering beyond reality? (Routing of easy queries to AI, definition of "resolution," cherry-picked markets…)
2. If you were Klarna's CTO, which of your own numbers would you refuse to repeat externally?
3. What is the prompt-injection risk profile of a chatbot that can process refunds? What is the worst case you can construct?

---

### Teaching note — Case D

**What to look for in a strong memo:** (1) Epistemological discipline: the memo classifies each claim by verifiability — efficiency metrics (resolution time) are most credible; equivalence claims (CSAT) need methodology; "700 agents" is rhetoric; $40M is a projection — and proposes its own measurement for each. (2) A fintech-grade risk register: hallucinated refund policies, PII exposure in prompts, prompt injection with financial consequences, bias in credit/collections-adjacent content, GDPR/regulatory exposure — each with detection (sampled human review, injection test suites, red-team drills) not just mitigation. (3) Escalation design: an explicit list of actions the agent may and may not take, and the UX of handing off. Red flags: quoting the vendor numbers as fact; no injection threat model; agent allowed to perform irreversible actions without a human gate; no compliance mention in a regulated industry.

**The recurring lesson (module-level):** the AI PM's relationship to numbers is adversarial-by-default and constructive-by-design. Every vendor-published metric is a hypothesis until you can reproduce it; the risk register is the deliverable that turns "this is risky" into "here is how we detect it."

---

## Case grading rubric (applies to memos 1–4)

| Dimension | A (18–20) | B (15–17) | C (12–14) |
|---|---|---|---|
| Position | Clear, specific decision; no hedging | Position present, somewhat general | No clear position |
| Evidence | Uses case data correctly; separates vendor claims from verified facts; cites sources | Mostly correct use of data | Ignores or misreads data |
| Framework | Applies course frameworks (feasibility, evals, RICE, risk register) explicitly | Frameworks implied | No frameworks |
| AI-use declaration | Present and honest | Present | Missing |

*Each memo: 1 page, ~500 words. Grade yourself before reading the teaching note; the delta between your grade and the note's assessment is the learning.*
