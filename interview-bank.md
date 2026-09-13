# AI Product Manager Interview Question Bank

Companion to GTH 580 — Career Launch, Module 2 (The Interview Loops). 42 questions across the three loops plus the AI-specific deep dive, each tagged with what the interviewer is testing and the program course that supplies the answer.

**How to use this bank.** Practice protocol per GTH 580 M2: record yourself answering a question, listen back, note where you hedged or rambled, answer again. Every behavioral answer must end in a number. Every framework must land on the specific question — never recite. Reference course codes: AI 510 (AI & LLM Literacy), PM 501 (PM Fundamentals), AIPM 520 (AI Product Craft), DATA 530 (Data, Metrics & Experimentation), STRAT 540 (AI Strategy & Economics), RSK 550 (Responsible AI), AI 570 (LLM Systems), FDE 560 (Forward Deployed Engineering), GTH 580 (Career Launch), CAP 600 (Capstone Studio).

---

## Section 1 — Product Sense (12 questions)

The loop: "design an AI feature for X." Graders want structure, stated assumptions, feasibility judgment, metrics, and risks — in five minutes. Use AIPM 520 M1 for the feasibility call, PM 501 M5 for metrics, RSK 550 M1 for risks.

### 1.1 Design an AI feature for a customer-support tool.

**Scenario variants:**
- Internal support desk for 250 field technicians (parts compatibility, warranty status, fix-it guidance); technicians bill by the job and wait 15–40 minutes on hold.
- Consumer support for a fintech app where a wrong answer about fees or disputes has regulatory weight.
- B2B support for a SaaS onboarding flow where support agents handle 40 concurrent chats and churn correlates with time-to-resolution.

**What they're looking for:** Problem first, evidence second, AI third. A stated feasibility boundary (what the AI should and should not answer, where humans stay in the loop), a north star plus guardrails, and an evaluation design. The field-technician variant is the program midterm scenario — you should be able to reproduce that answer cold.
**Built in:** AIPM 520 M1 (feasibility & system design) · PM 501 M5 (metrics) · DATA 530 M1 (measurement systems) · RSK 550 M1 (risk register) · exams.md midterm Q1.

### 1.2 Design an AI feature for a document-heavy workflow.

**Scenario variants:**
- Contract review for a legal-ops team that spends 6 hours per contract on redlines and missing-clause detection.
- Insurance claims intake: 20-page PDFs, 30% of claims rejected at first pass for missing evidence.
- Procurement/AP: invoice matching against POs and receipts, where the mismatch queue is the bottleneck.

**What they're looking for:** Structured extraction vs. free-form reasoning — knowing when RAG beats raw generation (AI 510). Confusion-matrix thinking about errors (false acceptance vs. false rejection costs differ wildly by domain). A human-in-the-loop checkpoint and an explicit cost of error.
**Built in:** AI 510 M4 (retrieval & RAG) · AIPM 520 M2 (architecture & guardrails) · RSK 550 M1 (risk) · FDE 560 M3 (delivery & evals in the field).

### 1.3 Design an AI feature for a sales team.

**Scenario variants:**
- Pipeline qualification for a mid-market SaaS sales org: 3,000 inbound leads/month, reps spend 20% of the week on discovery calls that go nowhere.
- Account research for enterprise AEs: 40 minutes of prep per account, most of it copy-pasting from six sources.
- Post-call summarization and next-step extraction from Gong/Chorus transcripts, where CRM hygiene is the bottleneck to forecasting.

**What they're looking for:** Clear articulation of where the AI's output is consumed by a human who can override (assistive, not autonomous). A metric that ties to revenue (conversion, prep time, forecast accuracy), not just "productivity." Awareness that summary quality has to be measured on what the rep does with it, not on coherence.
**Built in:** PM 501 M5 (funnels & metrics) · AIPM 520 M4 (evals in production) · DATA 530 M1 (measurement design).

### 1.4 Design an AI feature for a consumer app.

**Scenario variants:**
- Fitness app: a workout/recovery coach that adapts plans to sleep, schedule, and injury constraints logged in natural language.
- Recipe app: meal planning from "what's in my fridge" photos and dietary restrictions.
- Journaling app: a weekly summary that surfaces patterns in mood, energy, and triggers — without feeling like surveillance.

**What they're looking for:** Personalization-loop design (what the app learns and what it forgets), retention metrics as north star (D7/D30, weekly active), and trust/creepiness risk — the journaling variant tests whether you name the emotional downside, not just the technical one. Latency and cost matter at consumer scale.
**Built in:** PM 501 M2 (discovery) · DATA 530 M1 (measurement) · RSK 550 M3 (fairness & trust) · AIPM 520 M5 (cost & latency at scale).

### 1.5 Design an AI feature for an internal enterprise use case.

**Scenario variants:**
- HR helpdesk for a 5,000-person company: benefits, payroll, policy questions; 80% are the same 30 questions.
- IT ticketing triage: classify, route, and pre-fill resolution steps for a 15-person helpdesk drowning in Level 1 tickets.
- Internal knowledge search across wikis, Slack, and drives, where employees can't find the policy they know exists.

**What they're looking for:** Scope discipline — internal tools reward narrow, high-frequency problems over ambitious ones. Change management and rollout (do employees trust it? what's the feedback loop?). Measuring deflection rate honestly, including the "gave up" failure mode (DATA 530 critique).
**Built in:** FDE 560 M1/M2 (operating model, scoping engagements) · DATA 530 M1 (measurement) · PM 501 M6 (delivery with engineers).

### 1.6 Design an AI feature for an e-commerce experience.

**Scenario variants:**
- Personalized shopping: a conversational assistant that narrows 40k SKUs to a shortlist from "I need a gift under $60 for a coffee snob."
- Review summarization across 2,000 product reviews, with the tension between positive bias and genuinely useful signals.
- Returns/refund triage: classify reason codes, detect abuse patterns, and route to the right disposition without gutting the refund policy.

**What they're looking for:** Business-model awareness (does the assistant increase GMV or just engagement?), and the hallucination stakes in commerce — a wrong "we'll refund you" promise has direct financial and legal cost. Guardrails around policy, not just around grammar.
**Built in:** STRAT 540 M1 (unit economics) · AIPM 520 M6 (risk & GTM) · DATA 530 M3 (experimentation).

### 1.7 Design an AI feature for a health-adjacent consumer product.

**Scenario variants:**
- Patient intake assistant for a clinic: collect history, symptoms, and scheduling before the visit.
- Clinician note summarization: turn a 20-minute conversation into SOAP notes.
- Medication adherence: reminders and refill coordination that adapt to the patient's stated barriers.

**What they're looking for:** The discipline to say what you will NOT do — no diagnosis, no dosing advice, no autonomous decisions — and why (scope of practice, liability, trust). Regulatory awareness (HIPAA-adjacent data handling) and the disclaimers-plus-guardrails pattern. The key insight interviewers want: the highest-value features are documentation and logistics, not clinical reasoning.
**Built in:** RSK 550 M4 (policy & governance) · AIPM 520 M6 (risk & GTM) · AI 510 M5 (API & data layer).

### 1.8 Design an AI feature for a creator/content tool.

**Scenario variants:**
- Newsletter writer: turn a 15-minute voice note into a drafted issue in the author's voice.
- Video editor: suggest cuts, b-roll, and captions from raw footage and a rough script.
- Social caption generator for a brand that posts 5x/week and has a strict voice-and-compliance guide.

**What they're looking for:** Voice preservation (how do you keep output on-brand and off-generic?), editing workflows (AI drafts, human owns the publish), and eval on style fit, not just factual correctness. The brand variant tests whether you know the compliance review can't be automated away.
**Built in:** AI 510 M3 (prompting as an interface) · AIPM 520 M4 (evals) · PM 501 M3 (spec & acceptance criteria).

### 1.9 Design an AI feature for a developer tool.

**Scenario variants:**
- Code review assistant: flag bugs, security issues, and style drift before a human reviewer reads the PR.
- Docs Q&A: answer "how do I do X with your SDK" from your docs, changelogs, and GitHub issues.
- On-call incident summarization: turn a paging storm and thread into a timeline the next engineer can act on.

**What they're looking for:** The difference between assistive and autonomous suggestions in high-stakes code paths (a confident wrong code suggestion is worse than none). Precision/recall framing — for a review tool you optimize precision; for a docs bot you can tolerate more recall. Developer trust and the "noise kills adoption" dynamic.
**Built in:** AIPM 520 M2 (guardrails & tool use) · RSK 550 M2 (security & red-teaming) · DATA 530 M1 (measurement design).

### 1.10 Design an AI feature for a mobile app with limited context.

**Scenario variants:**
- Camera-based home inventory: snap shelves, get an itemized list for insurance or moving.
- Voice note organizer: dictation that files, titles, and surfaces action items from a week of brain dumps.
- Photo album search: "find the trip we took with grandma in 2021" from 40,000 local photos.

**What they're looking for:** On-device vs. cloud trade-offs (privacy, latency, cost, capability) stated explicitly; the edge case that the AI sees only what the camera/audio captures; and honest limits — you cannot search what you didn't index, and indexing has its own cost. Preference for small, bounded tasks over open-ended assistants.
**Built in:** AIPM 520 M5 (cost, latency & model selection) · AI 570 M4 (MLOps awareness) · RSK 550 M4 (privacy & governance).

### 1.11 Design an AI feature for a data-heavy internal tool.

**Scenario variants:**
- Analytics assistant: natural-language questions over a company's warehouse ("why did activation drop in the EU last week?"), returning charts, not just SQL.
- Logistics ops: anomaly detection across 10k shipments/day, flagging the 20 that need a human today.
- Board-report generation: draft the exec summary from the quarter's metrics, narratives, and comments.

**What they're looking for:** Text-to-SQL reality (schema grounding, permissioning, and the "confident wrong number" risk), and the eval design that catches it — a golden set of queries with known answers. Understanding that trust in a numbers product is binary: one wrong chart and nobody uses it. The board-report variant tests governance (who reviews before it goes out).
**Built in:** DATA 530 M1/M2 (measurement & instrumentation) · AIPM 520 M3 (data as fuel) · RSK 550 M1 (risk register).

### 1.12 Design an AI feature for a marketplace.

**Scenario variants:**
- Listing optimization for sellers: turn a weak description and three photos into a listing that converts, without misrepresenting the item.
- Buyer search refinement: paraphrase and constraint-match a fuzzy request ("vintage desk under $200, must fit a small car") into structured search.
- Dispute handling: classify and draft resolutions for buyer-seller disputes, with a human owning the final call.

**What they're looking for:** Two-sided thinking (an AI feature that helps one side must not exploit the other — listing polish can drift into misrepresentation), and marketplace metrics (conversion, dispute resolution time, trust score). The dispute variant tests neutrality and escalation design.
**Built in:** STRAT 540 M3 (positioning & strategy) · RSK 550 M3 (fairness & bias) · AIPM 520 M2 (guardrails).

---

## Section 2 — Execution (12 questions)

The loop: "how would you prioritize / measure / de-risk / handle X?" Your portfolio — eval suite, cost model, capstone eval report — is the evidence.

### 2.1 Here are six candidate features for next quarter, including a hallucination fix on tax codes. Rank them. Show the math. Which one would you not ship even if the score says otherwise?

**Scenario variants:**
- The exact RICE table from the program midterm (copilot for accountants, 10k paying customers) — you should be able to recompute it cold.
- Variant: same table, but engineering says the top-scoring item is a 12-week build with 40% confidence, and a competitor just shipped it.

**What they're looking for:** Arithmetic shown out loud, then judgment on top of it: a quality fix (feature D) wins on trust-adjusted value even when reach is lower, and one item (voice dictation) is a theme misalignment. The "wouldn't ship despite the score" call must be defended with AI-specific risk (trust, cost, quality), not vibes.
**Built in:** PM 501 M4 (prioritization & roadmaps) · exams.md midterm Q3 · STRAT 540 M1 (unit economics) · RSK 550 M1 (risk-adjusted value).

### 2.2 Two AI opportunities: one is high-impact but high-risk (autonomous mode), one is incremental but certain (assisted mode). How do you decide?

**Scenario variants:**
- Autonomous vs. assistive version of the same feature, same team, same quarter.
- Variant: the high-risk option is a bet-the-company integration with a new vendor; the safe one ships in two weeks.

**What they're looking for:** A decision rule, not a personality: expected value with confidence weighting, portfolio thinking across the roadmap, and risk capacity of the business (a startup can take the bet; an enterprise client contract can't). Naming the real option value of a small pilot.
**Built in:** PM 501 M4 (prioritization) · STRAT 540 M1 (economics) · RSK 550 M1 (risk registers) · CAP 600 M2 (build & measure).

### 2.3 Your dashboard says 94% accuracy and your VP is celebrating. You suspect it's wrong. What do you do?

**Scenario variants:**
- The program midterm scenario: 60% "resolution" counts users who gave up; 8% rating participation; repeat-contact up 12%; sentiment shows "confident wrong answers."
- Variant: accuracy is computed on a golden set that hasn't been refreshed in nine months and doesn't contain the new failure mode.

**What they're looking for:** Metric literacy with mechanisms, not vibes — selection bias in rating samples, "resolution" as an artifact of silence, dashboard accuracy that measures the easy sample. Then the harder skill: telling an exec the good number is a lie without losing credibility — you bring the corrected system, not just the critique.
**Built in:** DATA 530 M1 (measurement systems design) · exams.md midterm Q2 · AIPM 520 M4 (evals in production).

### 2.4 Define success for a new AI feature before a line of code is written. What do you instrument?

**Scenario variants:**
- The support bot from Section 1 (you pick the domain) — north star, guardrails, and model-quality metrics.
- Variant: a summarization feature where the user rarely reads the output closely — how do you know it's good?

**What they're looking for:** A layered metric system: product north star (e.g., resolution rate), guardrails (hallucination rate, refusal rate, latency percentile), and model-quality metrics (golden-set accuracy, failure-class distribution). Instrumentation must be planned pre-launch — you can't backfill what you didn't log. For summarization: downstream action metrics, not readability.
**Built in:** DATA 530 M1/M2 (measurement & instrumentation) · AIPM 520 M4 (evals in production) · PM 501 M5 (metrics).

### 2.5 How do you run an experiment on an AI feature when the model can't be cleanly A/B tested?

**Scenario variants:**
- A model upgrade that changes behavior across the whole product at once — no per-user assignment.
- Variant: the change is a prompt tweak that affects every session; your guardrail metric says neutral, your revenue metric says down 2%.

**What they're looking for:** The standard tools — holdouts, staggered rollout (5% → 25% → 100%), pre/post with controls, synthetic or shadow eval — and the honest limits: for system-wide changes you lean on offline eval plus guardrail monitoring, not a classic experiment. Knowing that a 2% revenue drop can be real at high volume even if not "significant" in a week.
**Built in:** DATA 530 M3 (experimentation for AI) · AIPM 520 M4 (evals) · PM 501 M5 (funnels).

### 2.6 De-risk a feature whose model quality is completely unproven. You have one quarter.

**Scenario variants:**
- A support bot that must hit 80% resolution or the project is canceled — the model has never been tested on your domain.
- Variant: a compliance-adjacent feature where the failure case is a fine, and the team has never built an eval suite.

**What they're looking for:** Eval-first sequencing — build the golden set and baseline the model before committing to the product build; kill criteria written down ("below X, we stop"); and a fallback (human-in-the-loop, narrower scope) that preserves the user value even if the model underperforms. The demo-first instinct ("it worked in my prompt") is the failure mode.
**Built in:** AIPM 520 M4 (evals in production) · CAP 600 M2 (build & measure) · DATA 530 M1 (measurement design) · GTH 580 M1 (case study packaging of exactly this arc).

### 2.7 You have eight weeks and a team that has never shipped an LLM feature. What's the plan?

**Scenario variants:**
- Greenfield internal tool, two engineers, no ML background, no existing eval infrastructure.
- Variant: six weeks to a pilot with one enterprise customer who has already paid.

**What they're looking for:** Scoping a small, completable, measurable slice (the FDE move: one workflow, one user class, one metric); using hosted APIs and proven patterns before custom anything; standing up a minimal golden set in week one; and a launch gate defined by eval results, not by the calendar. Realism about what an eight-week team can and can't do.
**Built in:** FDE 560 M1/M2 (operating model, scoping) · AIPM 520 M1/M4 (feasibility, evals) · PM 501 M3 (PRD & acceptance criteria) · GTH 580 M4 (30/60/90 — this is the 60-day feature).

### 2.8 You're at 92% on the golden set. Leadership wants to ship. You're worried about the failure cases. What happens in the launch conversation?

**Scenario variants:**
- The 8% failures include a class of confidently-wrong answers in a domain where users can't tell (the midterm "confident wrong answers" pattern).
- Variant: the failure cases are rare but individually expensive (a refund promise, a legal citation).

**What they're looking for:** You can defend a launch decision with a risk posture, not a vibe: show the failure breakdown, the severity-weighted cost, the guardrails that catch the worst class, the rollback plan, and a staged rollout. The interviewer wants to see you hold a position ("ship at 50% with a classifier in front") while respecting the exec's constraints.
**Built in:** RSK 550 M1 (risk registers with detection) · DATA 530 M1 (guardrail metrics) · AIPM 520 M4 (failure analysis) · exams.md final Q3 (how does it fail in production).

### 2.9 Sales committed a capability to a customer that the model can't reliably deliver. Engineering wants to say no. The deal is in the balance. What do you do?

**Scenario variants:**
- A "guaranteed accuracy" clause in an enterprise deal for a feature you know fails 15% of the time.
- Variant: sales demoed a prompt that worked once in the demo room; the real data looks nothing like it.

**What they're looking for:** You broker, you don't pick sides: restate the actual capability with evidence (eval numbers beat demo vibes), offer the scoped alternative that satisfies the customer's job-to-be-done, and take the conflict to a decision with the data in the room. Willingness to make sales uncomfortable with truth — and to stand behind the engineering read when it's right.
**Built in:** PM 501 M6 (delivery with engineers) · STRAT 540 M3 (positioning — sell what it does) · AIPM 520 M4 (the evidence) · FDE 560 M2 (scoping client work).

### 2.10 Your CEO wants an AI feature because a competitor shipped it. You believe it's the wrong problem. How do you handle it?

**Scenario variants:**
- A "me-too" AI assistant for a product whose real churn driver is onboarding complexity, not missing AI.
- Variant: the competitor's feature is getting press but you have evidence of low engagement in your own user research.

**What they're looking for:** How you disagree without being disagreeable: bring the customer evidence, offer a frame (competitive features vs. product strategy), and a path to test the CEO's hypothesis cheaply before the full build. You don't need to win — you need a decision made on evidence, and the courage to say "this is a strategy question, not a feature question."
**Built in:** STRAT 540 M3 (positioning & competitive strategy) · PM 501 M2 (discovery) · PM 501 M4 (prioritization) · AIPM 520 M1 (feasibility — and when to say no to AI).

### 2.11 Legal and security are blocking your launch over data handling. The feature is done. How do you get to yes?

**Scenario variants:**
- Customer data going to a third-party model API, and security wants on-prem or nothing.
- Variant: retention policy conflicts — your fine-tuning data includes PII you didn't plan to scrub, and legal found out at the last minute.

**What they're looking for:** You treat legal/security as stakeholders with legitimate constraints, not obstacles: understand the specific concern (data residency, retention, consent, export), engineer options (data scrubbing, PII redaction, on-prem/private endpoints, no-retention agreements), and bring options + trade-offs to the table rather than asking them to fold. Owning that data governance is a product decision, not an afterthought.
**Built in:** RSK 550 M4 (policy & governance) · DATA 530 M4 (data governance & the flywheel) · AIPM 520 M2 (architecture choices that satisfy security).

### 2.12 Your feature is live and model cost just blew up the unit economics. Finance wants numbers. What do you present, and what do you change?

**Scenario variants:**
- Cost per resolution is 3x the plan because users re-prompt and the model re-reads long contexts; usage grew faster than the caching plan.
- Variant: the vendor raised prices 20% and your contract auto-renews in 60 days.

**What they're looking for:** You know your cost model cold: cost per interaction, the monthly burn at current volume, the levers (prompt compression, caching, model tiering, smaller model for easy cases, rate limits) with their expected savings, and a sensitivity table (cost doubles → what breaks). You present a plan, not a problem, and you already know whether the next decision is re-tiering, re-pricing, or re-scoping.
**Built in:** STRAT 540 M1 (unit economics of AI) · AIPM 520 M5 (cost, latency & model selection) · exams.md final Q4 (compute costs doubled — answer from memory).

---

## Section 3 — Behavioral (10 STAR prompts)

Every answer: Situation, Task, Action, Result — translated into PM vocabulary, ending in a number. Mine stories from your strategist/operator career using the PM 501 M1 asset map, then stress-test them against the GTH 580 rubric (one story without a number is a C). Deliver in 90–120 seconds.

### 3.1 Tell me about a time you had to make a high-stakes decision with incomplete information.

**What they're looking for:** How you bound the uncertainty, what evidence you insisted on vs. accepted, the decision rule, and the outcome with a number. They want to hear you name what you didn't know without hiding behind it.
**Built in:** PM 501 M1 (asset map → narrative) · GTH 580 M2 (STAR discipline) · CAP 600 M2 (decide under uncertainty and measure).

### 3.2 Tell me about a time you influenced someone without authority.

**What they're looking for:** Influence mechanics — evidence, allies, framing to their incentives, persistence without escalation. A PM has no direct reports; this is the job. The number should be the thing that moved because you influenced.
**Built in:** PM 501 M1 (asset map) · PM 501 M6 (working with engineers) · GTH 580 M2 (STAR).

### 3.3 Tell me about a time you shipped something that didn't work, or a project that failed.

**What they're looking for:** Honest ownership of failure, the detection mechanism that caught it, the metric that proved it, and what you changed. Interviewers penalize defensive answers more than failure itself — this program grades the same way.
**Built in:** GTH 580 M2 (failures translated, numbers included) · CAP 600 M2 (retrospective discipline) · exams.md final Q5 (what did you get wrong).

### 3.4 Tell me about a time you dealt with a difficult stakeholder.

**Scenario variants (pick the one that matches your story):**
- A stakeholder who kept changing requirements.
- A stakeholder with veto power who didn't believe your numbers.

**What they're looking for:** You diagnosed the stakeholder's actual constraint, changed your approach, and kept the working relationship. The result should show something moving (deadline met, scope protected, relationship repaired) with a number.
**Built in:** PM 501 M6 (delivery) · GTH 580 M2 (STAR) · STRAT 540 M3 (stakeholder strategy).

### 3.5 Tell me about a time you said no to your boss or to leadership.

**What they're looking for:** You can push back with evidence and still be seen as a team player — you brought an alternative, not just a refusal. The number is what you saved or what the alternative gained.
**Built in:** PM 501 M4 (prioritization — saying no is the job) · GTH 580 M2 (STAR) · AIPM 520 M1 (saying no to AI is a feature).

### 3.6 Tell me about a time you took a risk that paid off — or one that didn't.

**What they're looking for:** A risk posture that is deliberate, not reckless: what you bet, what you capped the downside at, and what you learned either way. A "didn't pay off" story told well scores higher than a safe story.
**Built in:** RSK 550 M1 (risk registers — apply the same discipline to yourself) · GTH 580 M2 (STAR) · CAP 600 M2.

### 3.7 Tell me about a time you had to learn something technical quickly to make a decision.

**What they're looking for:** Your learning loop under time pressure — what you read, who you asked, what you tested, and how you converted "I don't know" into "I can decide." For an AI PM transition story this is gold: it's the AI 510 → AIPM 520 arc in miniature.
**Built in:** AI 510 (LLM literacy) · GTH 580 M2 (STAR) · AI 570 M4 (staying current).

### 3.8 Tell me about a time you resolved a conflict inside a team.

**Scenario variants (pick one):**
- Engineering and design deadlocked on an approach.
- Two senior people competing for the same resources.

**What they're looking for:** You surfaced the real disagreement under the stated one, got both sides' constraints on the table, and produced a decision the team could execute. Number = what shipped or what was saved.
**Built in:** PM 501 M6 (delivery) · GTH 580 M2 (STAR) · FDE 560 M1 (operating across functions).

### 3.9 Tell me about a time the data said something different from the consensus — and what you did.

**What they're looking for:** The guts to trust evidence over the room, and the communication skill to bring the room with you. The number is the gap between the consensus belief and what the data showed.
**Built in:** DATA 530 M1 (measurement systems — trust the mechanism, not the number) · GTH 580 M2 (STAR) · exams.md midterm Q2.

### 3.10 Tell me about a time you managed a vendor or an external partner.

**What they're looking for:** Contracting, expectation-setting, and verification — did you accept their claims or test them? The number is what you negotiated, saved, or validated. Maps directly to the model-vendor relationship you'll own as an AI PM.
**Built in:** STRAT 540 M4 (vendor risk) · AIPM 520 M4 (evals — verify claims) · GTH 580 M2 (STAR).

---

## Section 4 — AI-Specific Deep Dives (8 questions)

The loop that separates AI PMs from classic PMs. These are the "what do you actually know" questions. Answer with frameworks and numbers, not enthusiasm.

### 4.1 Walk me through how you'd decide whether a feature should use AI.

**What they're looking for:** The two-minute killer question answer — comparative feasibility → data check → evaluation design → cost/latency → risk — delivered as a framework applied to the specific feature, ending in a yes/no/condition. Full fillable script in the Killer Question Framework section below.
**Built in:** AIPM 520 M1 (feasibility) · GTH 580 M2 (the killer question) · GTH 580 final Q1.

### 4.2 How do you handle hallucination in production?

**Scenario variants:**
- A support bot that gives confident wrong answers about policies.
- A text-to-SQL tool that fabricates a plausible but wrong number.
- A summarizer whose output can't be checked against the source by the reader.

**What they're looking for:** You don't say "we fix it with better prompting." You name the layered defense: retrieval grounding with source citations, guardrails/classifiers on high-risk outputs, confidence thresholds that route to human or refusal, eval sets built specifically from the failure class, and monitoring that catches drift into new hallucination families. And you can say when the right answer is "don't use the model for this."
**Built in:** AIPM 520 M2 (retrieval & guardrails) · AIPM 520 M4 (evals & failure analysis) · RSK 550 M1 (risk with detection) · DATA 530 M1 (guardrail metrics).

### 4.3 How do you choose a model for a feature?

**Scenario variants:**
- Open vs. closed models for a B2B product where customers ask about data.
- Frontier model vs. small fine-tuned model for a high-volume, narrow task.
- A task where the best model wins by 2 points on your golden set but costs 10x.

**What they're looking for:** A decision process, not a favorite model: define the task's requirements (capability, latency, cost, data residency, controllability), test candidates on your golden set with your scoring rubric, and make the trade-off decision on your metrics — including when 2 eval points aren't worth 10x cost. Naming the shift left ("try the small model first, escalate only when the eval says so").
**Built in:** AIPM 520 M5 (cost, latency & model selection) · AI 570 M4 (MLOps awareness) · STRAT 540 M4 (vendor dependence).

### 4.4 How do you think about cost and pricing for an AI feature?

**Scenario variants:**
- A free consumer feature whose marginal cost is real money at scale — do you keep it free?
- A B2B copilot: per-seat, usage-based, or bundled? What happens when a customer's usage is 20x the median?
- Pricing after a 3x cost blowup (see 2.12).

**What they're looking for:** Unit economics fluency: cost per interaction, the margin math, tiering and caching as cost levers, and the pricing decision tied to value delivered, not cost incurred — with the guts to set usage limits or raise prices and the sensitivity thinking to know what breaks. You should be able to sketch a cost-per-month model out loud.
**Built in:** STRAT 540 M1/M2 (unit economics, pricing & packaging) · AIPM 520 M5 (cost model) · CAP 600 M2 (your cost model artifact).

### 4.5 What is prompt injection, and how would you defend a product against it?

**Scenario variants:**
- An internal support bot that reads documents — one of which contains "ignore previous instructions."
- A customer-facing chat that can see other users' data through tool calls.

**What they're looking for:** You can explain the mechanism (instruction vs. data boundary, indirect injection through retrieved content), the attacker's goal (exfiltration, jailbreak, reputation damage), and a defense stack: least-privilege tool permissions, output filtering, delimiters and system-boundary hygiene, red-teaming the eval set with adversarial inputs, and — critically — not trusting the model as the only boundary. Awareness that injection is a design problem (what can the model do?) more than a prompt problem.
**Built in:** RSK 550 M2 (injection, red-teaming, threat models) · AI 570 M2 (tools & function calling) · AIPM 520 M2 (guardrails).

### 4.6 How would you design the evaluation for a new LLM feature?

**Scenario variants:**
- A summarization feature with no ground-truth labels available.
- A classification feature where you have 500 labeled examples and the failure cost is high.
- An agentic feature with multi-step tool use (see 4.6 variant in AI 570).

**What they're looking for:** The full eval stack, named in order: golden set construction (representative + adversarial + edge cases), scoring method (exact match vs. rubric-based human rating vs. LLM-as-judge with its own validation), inter-rater reliability, pre-launch gate thresholds, in-production monitoring (drift, guardrail metrics, sampling for human review), and failure analysis that feeds the next iteration. For no-ground-truth tasks: rubric-based evals and downstream behavioral proxies, with their limits stated.
**Built in:** AIPM 520 M4 (evals in production — the flagship module) · DATA 530 M1 (measurement design) · AI 570 M3 (evals for agentic systems) · CAP 600 M2 (your eval suite artifact).

### 4.7 A vendor claims their model is "98% accurate" and your CEO wants to buy it. How do you verify the claim?

**Scenario variants:**
- The claim is a marketing number with no eval methodology disclosed.
- The vendor's eval was on a benchmark you suspect doesn't match your domain (e.g., legal text vs. general web text).

**What they're looking for:** You treat the claim as a hypothesis: ask for the eval methodology (data, split, rubric, inter-rater agreement), run the model on your own golden set of real domain cases — including the hard 20% — and compare against your baseline with your scoring method. You know a benchmark score is not a deployment decision, and you can tell the CEO exactly what you'd test before signing.
**Built in:** AIPM 520 M4 (evals — your golden set is the referee) · STRAT 540 M4 (vendor risk) · DATA 530 M1 (measurement hygiene) · GTH 580 M2 (land the framework on the specific claim).

### 4.8 How do you stay current in AI — and how do you filter signal from hype?

**What they're looking for:** A system, not a vibe: a reading diet (primary sources — model cards, papers, release notes — over hot takes), a practice loop (build and eval something small when a new capability appears, per AI 510/AI 570), a trusted filter (people whose claims you check, benchmarks you re-run yourself), and the discipline to ignore the 90% that doesn't change your products' unit economics. They want to see you treat staying current as a process you manage, like any other workstream.
**Built in:** AI 510 (foundation) · AI 570 M4 (staying current as a module) · AIPM 520 M4 (your eval suite is how you test new claims) · GTH 580 M2 (interview prep = staying current in practice).

---

## Killer Question Framework — "Walk me through how you'd decide whether a feature should use AI"

The two-minute answer, timed. This is GTH 580 M2's killer question and GTH 580 final Q1 — practice it out loud until it is fluent, then re-record it. Structure: **comparative feasibility → data check → evaluation design → cost/latency → risk**. Fill the brackets with the specific feature's facts; the sentences are your script.

### The script (fill in the blanks, aim for ~2 minutes total)

**Opener — :00–:10 (frame the decision, one sentence)**
> "I'd decide whether [FEATURE] should use AI the same way I'd decide anything: does it beat the alternative on evidence, and can we know that before we build? Five checks."

**1. Comparative feasibility — :10–:35**
> "First, the baseline. For [USER] doing [TASK], the current solution is [RULES / PEOPLE / NOTHING], and it costs [CURRENT COST OR FAILURE RATE]. AI wins this when the task needs [PATTERN RECOGNITION OVER MESSY INPUT / NATURAL LANGUAGE / PERSONALIZATION AT SCALE]. It loses when the task is [DETERMINISTIC / HIGH-STAKES WITH NO HUMAN CHECK / CHEAP TO DO WITH RULES]. For this feature, I'd judge the AI approach is [FEASIBLE / NOT FEASIBLE] because [ONE-SENTENCE REASON] — and the honest non-AI alternative is [NAME IT], which is a real option, not a fallback."

**2. Data check — :35–:60**
> "Second, the data. To build and evaluate this I need [LABELED EXAMPLES / GROUND TRUTH / LOGS], and I need it to cover the [HARD 20%] — the edge cases, not just the happy path. Today we have [WHAT EXISTS] and we're missing [WHAT'S MISSING]. If the data isn't there, no model choice fixes it — so this check either passes, or the answer is no."

**3. Evaluation design — :60–:85**
> "Third, how we'd know it works. I'd build a golden set of [N] real cases scored on [PRIMARY METRIC], with guardrails on [HALLUCINATION / REFUSAL / LATENCY], and I'd hold out [ADVERSARIAL / RED-TEAM SET] for the failure classes. The launch gate is [THRESHOLD], measured on our data — not a vendor benchmark and not a demo."

**4. Cost / latency — :85–:105**
> "Fourth, the economics. At [VOLUME] calls per month and [$ PER CALL], that's [$ PER MONTH] — and with [CACHING / TIERING / SMALL MODEL FOR EASY CASES] we'd get it to [TARGET]. Latency of [X SECONDS] [FITS / DOESN'T FIT] the user moment. If the unit economics don't hold at scale, the feature doesn't either."

**5. Risk — :105–:120**
> "Finally, the risk register. The top risks are [FAILURE MODE 1 — e.g., confident wrong answers], [FAILURE MODE 2 — e.g., data/privacy], and [FAILURE MODE 3 — e.g., vendor dependence], each with a detection mechanism: [DETECTION FOR EACH]. If the worst case is unacceptable and we can't detect it early, the answer is no."

**Closer — last 10 seconds (commit)**
> "So: yes, if AI beats the baseline on data we actually have, we can evaluate it honestly, the unit economics hold, and the risks have detection. If any of those fail, I'd ship the [RULES / HUMAN] alternative instead — and that's a win too."

### Delivery rules

- **Time-box to 2 minutes.** Practice with a timer; the opener and closer are non-negotiable, the middle four checks flex by 5 seconds each.
- **Land it on the specific.** Never recite the skeleton — every check names the feature's real users, real numbers, real failure classes. A framework without specifics is a recitation (GTH 580 M2).
- **State your assumption once, then go.** "I'm assuming [X] — if that's wrong, my answer changes at check 2."
- **A "no" is a great answer.** The question tests whether you know when AI doesn't earn its place; a disciplined no with a named alternative scores higher than an enthusiastic yes.
- **End with the decision.** Interviewers remember the verdict. If the checks are mixed, say "conditional yes — ship at 50% with a guardrail in front," and name the condition.
