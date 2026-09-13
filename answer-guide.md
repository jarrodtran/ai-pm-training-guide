# Midterm Answer Guide — Self-Grading Reference

**Program:** AI-PM Graduate Program · **Exam:** Program Midterm (see `exams.md`)
**Weights:** Q1 35% · Q2 35% · Q3 30% · **Format:** three answers, 500–700 words each

## How to use this guide

Write all three answers first, with only the allowed materials (course syllabi, your portfolio, the case packets). Grade afterward, dimension by dimension, against the midterm rubric:

| Dimension | What it rewards |
|---|---|
| Framework use | Applies course frameworks precisely, by name (feasibility drill, north star + guardrails, eval design, risk register with detection, RICE) |
| Numbers | Correct arithmetic; metrics critiqued with mechanisms, not vibes |
| Judgment | Takes positions; AI-specific risks addressed; assumptions stated |
| Communication | Exec-presentable as-is |

Sections 1 and 2 below are **frameworks** — the skeleton a strong answer is built on. They are not model essays; your answer must be your own words, argued from the scenario. Section 3 is a **fully worked model answer** for the only question with objectively checkable output (RICE arithmetic). Your Q3 ranking must match the worked answer exactly; your judgment call (which feature not to ship) may differ only if you defend it with AI-specific risks.

---

# Question 1 — Design: AI assistant for FieldService Co. technicians

## Model-answer framework

A strong answer makes six moves, roughly one short paragraph each (~100–120 words). If your answer is over 700 words, you are writing an essay instead of a decision document — trim to this skeleton.

**1. Problem and who it serves, with the evidence you'd want before building.**
Do the arithmetic in the scenario: 2,000 calls/week × 9 minutes = 300 desk-hours/week of call handling against 12 agents × 40 hours = 480 capacity hours — the desk is near saturation before callbacks and after-call work, which is why wait times run 15–40 minutes. Technicians bill by the job, so every minute waiting is unbilled revenue. Name the user: the field technician, not the support desk. Then state the evidence you would collect before committing: (a) an intent taxonomy from call transcripts — what share of the 2,000 calls are lookup-type questions (part compatibility, warranty status, safety procedures, "how do I fix X") vs. judgment/dispatch/credits cases; (b) handle time and repeat-call rate by intent; (c) where the knowledge lives — is the parts database, warranty system, and service-manual corpus queryable? (d) a baseline: current resolution rate, cost per call (desk cost + technician idle cost). End with a jobs-to-be-done statement, e.g., "When I'm on a job and need a part spec, I want the answer in under 30 seconds, so I don't leave the customer waiting or call back twice."

**2. Feasibility judgment — what the AI should and should not do, and where rules or humans stay in the loop.**
Run the Module 12 feasibility drill (AI vs. rules vs. human, scored on input/output clarity, error tolerance, data availability, cost, latency) per top intent, not once in general:
- *AI, retrieval-grounded:* part compatibility checks, warranty status, how-to guidance from service manuals. RAG over the parts/warranty/manual corpus (Module 4); the model answers from retrieved context, never from training memory (Case B: Fin's retrieval-first constraint).
- *Rules:* anything that is a deterministic lookup (warranty eligibility = date + contract → status). AI is the wrong instrument where a query can be answered exactly (Module 12: AI loses when answers must be deterministic).
- *Humans stay:* exceptions, credits, and anything that binds the company to a customer commitment; and the escalation layer for low-confidence answers. The 12-person desk is not eliminated — it becomes the review/escalation tier.
- *What AI must not do:* improvise procedures not in retrieval, make commitments, override safety steps, answer out-of-scope queries (out-of-scope refusal is a feature, not a bug).
- *Architecture (one or two lines):* query → retrieve top-k → answer with citations → separate policy/verification model call (Case B's composition) → confidence gate → answer with sources or escalate. State a latency budget (<5 s) and a cost-per-interaction cap (Module 15), and note model tiering: cheap model for lookups, verification gate on top.

**3. Success metrics: north star + 3 guardrails, including model-quality metrics.**
North star (Module 10): one outcome number, not activity. A strong candidate: *share of technician questions answered correctly at first attempt* (first-contact resolution for technicians). Explicitly reject "% of calls deflected" as a north star — deflection without correctness is cost-shifting. Then three guardrails with thresholds, one of which must be a model-quality metric:
- (g1) *Model quality:* answer accuracy ≥ 95% on the golden set for lookup intents; ungrounded-answer/hallucination rate ≤ 1% on safety and warranty content; every safety answer must pass a citation-grounding check.
- (g2) *Trust:* escalation rate and repeat-contact rate within defined bounds; repeat contact must not rise.
- (g3) *Economics:* cost per interaction ≤ a pre-set cap (model the 2,000 calls/week bill before launch — Module 15's "budget for your own success").

**4. Evaluation design, before and after launch.**
*Before:* build a golden set of 200–500 real questions sampled from call transcripts across the top intents (easy / edge / adversarial / out-of-scope cells, Module 6); score with a human rubric for correctness + grounding; use LLM-as-judge for volume with human spot-checks (judges are biased — check them); set a regression gate: no model version ships below the threshold (Module 14). Phase the rollout (Case B: Rocket Money started at 10% of conversations with scoped workflows): start with one intent family or 10–20% of call volume, with an explicit decision rule to expand, e.g., ≥ 90% correct on the slice for 4 weeks and escalation rate ≤ X.
*After:* drift monitoring on live signals (thumbs-down, "I don't know"/escalation rate, cost per session, rolling eval score), a feedback loop where production failures become new eval cases, and retrieval-corpus freshness checks (new parts, warranty rule changes) — "it worked in the demo is not it works in production."

**5. Top 3 risks, each with detection (risk register, Module 16).**
For each risk: likelihood, impact, mitigation, detection. At minimum:
- (r1) *Hallucinated answer on safety or warranty content.* Detection: mandatory citation-grounding check on every response; golden-set accuracy on the safety slice; weekly sampled human audit of safety answers; hard rule — no retrieval match means escalate, never improvise.
- (r2) *Trust collapse after one confident wrong answer.* Detection: escalation rate, repeat-contact rate, thumbs-down rate, sentiment on feedback, "answer challenged" rate; pre-commit to an intervention threshold (e.g., repeat contact up > 10% → pause expansion).
- (r3) *Cost/latency blowup or model drift at scale.* Detection: cost per interaction, p95 latency, and rolling eval score with alert thresholds; retrieval-freshness audit.

**6. Assumptions, stated explicitly.**
Examples: technicians have a phone/tablet in the field; call transcripts are available to build the eval set; parts/warranty/safety data is in queryable systems; the desk can absorb escalation volume; union or operational rules permit the tool. Also state what you deliberately excluded (e.g., dispatch/scheduling) and why. If you made a domain assumption (e.g., safety procedures are digital), say so — the scenario rewards stated assumptions and punishes silent ones.

## What separates A from B from C

- **A:** All six moves present; feasibility scored *per intent* with an explicit rules-vs-AI boundary; north star + guardrails with numeric thresholds including a model-quality metric; eval design with golden set, regression gate, and a phased rollout with a decision rule; every risk has a detection mechanism, not just a mitigation; assumptions stated; arithmetic traceable to the scenario (2,000 × 9 min, capacity math); could be shown to the VP of Operations as-is.
- **B:** The same skeleton, filled generically — "use RAG," "monitor hallucination," "keep humans in the loop" — without per-intent feasibility, thresholds, detection mechanisms, or assumptions. Numbers soft or absent.
- **C:** AI-first enthusiasm ("the assistant will handle 2,000 calls/week") with no problem evidence, no feasibility (no rules/human boundary), "accuracy" as the only metric, risks as a sentence ("we'll monitor it"), no assumptions, no numbers.

## Common failure modes (Q1)

- **AI-first framing** — solution in search of a problem; the problem paragraph doesn't exist or is one sentence.
- **No evidence plan** — no intent taxonomy, no transcript analysis, no baseline, no data-availability check.
- **No stated assumptions** — domain guesses (device availability, digital safety docs, system access) made silently.
- **Trusting the model's trained knowledge** — proposing answers from the model's memory instead of retrieval over the parts/warranty/manual corpus.
- **No rules-vs-AI boundary** — proposing AI for deterministic lookups (warranty status is a query, not an inference).
- **No human in the loop** — no escalation layer for high-stakes or low-confidence answers; the desk treated as an expense to eliminate rather than a resource to re-tool.
- **North star = activity** — "% of calls deflected" or "adoption" as the success metric; no outcome measure, no correctness measure.
- **Guardrails without model-quality metrics** — the AI feature's quality is unmeasured, which is the exact failure Q2 is about.
- **Risks without detection** — "we'll monitor closely" is not a risk register; each risk needs a measurable detection signal and a pre-committed threshold.
- **No eval before launch, no rollout decision rule** — "we'll test in beta" instead of a golden set, regression gate, and a defined expansion rule.
- **No cost/latency modeling** — 2,000 calls/week × tokens with no cost-per-interaction cap; the bill scales with success (Module 15).
- **Ignoring the safety-critical intent class** — safety procedures get the same treatment as part lookups, with no grounding requirement or escalation.

---

# Question 2 — Measurement: the misleading support-bot metrics

## Model-answer framework

**1. Diagnosis: identify at least three ways the metrics mislead, each with a specific mechanism.**
Name the mechanism, the direction of the bias (every one here inflates), and the evidence in the scenario that it is happening. The strongest set:
- (m1) *Selection (non-response) bias in the ratings.* "94% accuracy" = share of responses with no explicit thumbs-down, but only 8% of users rate at all. The denominator is a tiny, self-selected, polarized sample; non-raters are censored, and absence of a thumbs-down is absence of a signal, not approval. The instrument measures nothing about the 92% who don't rate.
- (m2) *Construct error in "resolution."* "Resolved" = user stopped replying. Silence is a behavioral proxy, not the construct (the problem is actually solved); users who gave up — exactly the segment the sentiment data describes — count as resolved. A proxy must be validated against outcomes before it can stand in for them; this one was never validated, and the scenario shows it is inversely correlated with the truth.
- (m3) *Contradictory signals with no governance.* Repeat-contact rate is up 12% and sentiment shows rising frustration with "confident wrong answers" — both directly falsify "resolved." Reporting a metric system with no guardrail structure lets the flattering numbers win by default; a single metric cannot be the truth when its own correlates contradict it (a resolved customer doesn't call back — Case D: repeat inquiries down 25% was the credible quality signal).
- (m4, optional fourth) *Instrumentation gap.* No event log links a conversation to a later repeat contact by the same user on the same issue, so even the claims that exist can't be verified. "If you didn't log it, it didn't happen" (Module 10).

**2. Redefine the measurement system: real north star, guardrails, instrumentation.**
- *North star:* first-contact resolution (FCR) measured by outcome, not silence — e.g., share of conversations resolved at first contact, where "resolved" means the user's issue was actually addressed: explicit confirmation on a designed sample **and** no repeat contact within 7 days on the same issue (matched by user + issue fingerprint) **and** no escalation.
- *Guardrails:* (g1) *Model quality* — golden-set accuracy on a rolling production sample, plus a direct hallucination/"confident wrong answer" rate. The sentiment data literally reports this failure; measure it directly (Module 14: golden set, regression gate, drift monitoring). (g2) *Trust* — repeat-contact rate (target: declining, back to at-or-below baseline), escalation rate, sentiment trend. (g3) *Economics* — cost per resolved conversation (Module 15); a cheap "resolution" that isn't one is the worst kind of savings. (g4) *Sample health* — rating coverage: instrument ratings on a stratified random sample of conversations so the 8% problem becomes a governed, measured guardrail instead of a silent selection filter.
- *Instrumentation to add (Module 10):* event log for every conversation (intent, outcome, escalation, repeat-contact linkage, rating); a post-contact micro-survey on a stratified random sample rather than voluntary opt-in; issue-fingerprint matching so repeat contacts are attributable; a sentiment pipeline on open-ended feedback; a weekly human audit of a random sample of "resolved-by-silence" conversations to calibrate the proxy; a golden-set regression run on production traffic with alert thresholds; and the feedback loop (production failures → new eval cases).

**3. Communicating the corrected picture to executives without losing credibility.**
- Lead with the mechanism, not just the number: "We counted every conversation the user walked away from as resolved — that's why 60% coexisted with repeat contact up 12%." A corrected number without the mechanism reads as an excuse; the mechanism reads as rigor.
- Quantify the correction: audit the silent-end conversations and report a true-FCR band, not a false-precision point estimate (sampled estimates get confidence intervals). Show old metric vs. new metric side by side with the definitional fix annotated on the dashboard.
- Frame it as an instrumentation and definition failure, not deception: "We defined resolution wrong, and we weren't sampling ratings representatively. Here's the corrected definition, here's what the real number is, and here's how we'll track it from now on." Owning the miss is what preserves credibility — defensiveness destroys it.
- Don't overcorrect into doom: the bot may be delivering real value; the honest statement is "we don't know yet, and here's the instrument that will tell us." Executives can act on "we don't know, measured properly" — they can't act on theater.
- Commit to a timeline and a single source of truth: one dashboard, corrected definitions, next review date, and the decision rule (what we'll do if the true FCR is below target).

## What separates A from B from C

- **A:** Three or more mechanisms, each with a named bias and its direction; a redesigned system with an outcome-based north star, guardrails including direct model-quality measurement, and a concrete instrumentation list; a communication plan that owns the miss, quantifies the correction (band, not false precision), and stays decision-relevant; connects diagnosis to fix (sentiment says "confident wrong answers" → measure hallucination rate directly).
- **B:** Lists the problems ("the metrics are misleading") without mechanisms; proposes "better metrics" without instrumentation or thresholds; communication advice is generic ("be transparent").
- **C:** Defends the numbers or shrugs ("that's what the dashboard says"); proposes a vanity replacement ("we need CSAT"); or no redesign and no communication plan at all. Treating the dashboard figures as fact is a C-level error in this program.

## Common failure modes (Q2)

- **Accepting the dashboard numbers at face value** — the 94% and 60% are quoted as facts to be explained, not as claims to be interrogated.
- **No mechanism** — "the metrics feel misleading" without naming selection bias, construct error, or proxy invalidity.
- **"Just ask more users to rate"** — raising the rating rate doesn't fix selection bias; the fix is instrumented random sampling, not volume.
- **Treating absence of a thumbs-down as approval** — silence is not a signal; the 8% rating rate proves the sample is unrepresentative.
- **Silence-as-resolution accepted as a proxy without validation** — no calibration audit, no repeat-contact linkage, no acknowledgment that "user stopped replying" includes "user gave up."
- **Ignoring contradictions between metrics** — repeat contact +12% and rising frustration are the story; the dashboard's own correlates falsify it.
- **No instrumentation plan** — "we'll compute the right metrics" with no event log, no sampling design, no linkage.
- **No model-quality metrics** — this is an AI feature failing on AI quality ("confident wrong answers"); the fix must measure the model (golden set, hallucination rate), not just the funnel.
- **No communication plan** — how the correction lands with executives is part of the job, not an afterthought.
- **False precision** — quoting a corrected number as exact when it comes from a sample; give the band and the confidence.
- **Defensive framing** — "the numbers were right, executives just misunderstood" is the opposite of credibility.

---

# Question 3 — Prioritization: RICE for the accounting copilot

This is the fully worked model answer. Your arithmetic and ranking must match exactly. **RICE = Reach × Impact × Confidence ÷ Effort**, where Confidence is the percentage divided by 100 (70% → 0.70).

## 1. The arithmetic (verified)

| # | Feature | R | × | I | × | C | ÷ | E | = | RICE |
|---|---|---|---|---|---|---|---|---|---|---|
| D | Fix hallucination on tax codes | 10,000 | × | 3 | × | 0.90 | ÷ | 3 | = | (30,000 × 0.90) ÷ 3 = 27,000 ÷ 3 = **9,000** |
| F | Bulk import from Excel | 5,000 | × | 2 | × | 0.80 | ÷ | 2 | = | (10,000 × 0.80) ÷ 2 = 8,000 ÷ 2 = **4,000** |
| A | Multi-entity support | 4,000 | × | 3 | × | 0.70 | ÷ | 8 | = | (12,000 × 0.70) ÷ 8 = 8,400 ÷ 8 = **1,050** |
| B | Voice dictation of notes | 6,000 | × | 1 | × | 0.60 | ÷ | 4 | = | (6,000 × 0.60) ÷ 4 = 3,600 ÷ 4 = **900** |
| E | Mobile companion app | 7,000 | × | 2 | × | 0.50 | ÷ | 20 | = | (14,000 × 0.50) ÷ 20 = 7,000 ÷ 20 = **350** |
| C | AI audit-trail export | 1,500 | × | 3 | × | 0.40 | ÷ | 12 | = | (4,500 × 0.40) ÷ 12 = 1,800 ÷ 12 = **150** |

## 2. Ranking and the quarter roadmap

**Ranking:** D (9,000) → F (4,000) → A (1,050) → B (900) → E (350) → C (150).

**Sanity checks worth stating:** D's reach (10,000) is the entire paying base — a quality fix that touches every customer and is the single most defensible AI move (it is the same "confident wrong answers" failure Q2 diagnoses, fixed at the source). The top two are robust to input wobble: D stays #1 even at 50% confidence (10,000 × 3 × 0.50 ÷ 3 = 5,000), and F stays #2 even at 60% (5,000 × 2 × 0.60 ÷ 2 = 3,000). Confidence is a confession of uncertainty; note where the team is confident (D, F) and where it is guessing (C, E).

**Roadmap by themes, not features (Module 9):**

| Quarter | Theme (outcome) | Features | Effort |
|---|---|---|---|
| Q1 | **Earn trust through correctness** — stop the bot from being wrong about money | D (3 pw) + F (2 pw) | 5 person-weeks |
| Q2 | **Grow with the firm** — expand from one accountant to the entities they serve | A (8 pw) | 8 person-weeks |

- Q1's theme pairs the trust fix (D) with the highest-confidence activation feature (F); both are small, high-confidence, and load-bearing for retention.
- The remaining quarter capacity is not "free" — it is budgeted to the production eval system, regression gates, and cost-per-interaction monitoring (Module 14/15). Quality infrastructure is roadmap work, especially for an accounting product.
- Q2's theme carries A alone; B and E are excluded by the decisions below, freeing 36 person-weeks (B 4 + E 20 + C 12) for what actually matters.

## 3. The single feature I would NOT ship despite its score: B — voice dictation of notes

Raw RICE says B (900, rank 4) is a respectable Q2 candidate: reachable, cheap to build (4 person-weeks). I would not ship it. RICE prices reach, impact, confidence, and effort — it does not price the AI-specific risks, and for voice dictation in an accounting product those risks are fatal:

- **Quality.** Dictation runs speech-to-text plus LLM summarization over the most error-hostile vocabulary in the product: numbers, tax-code identifiers, entity names, invoice references. Transcription errors on a dictated figure are not cosmetic — they become the note, and the note becomes the record the accountant relies on. A "confident wrong number" in a note is the same failure class Q2 measures, written directly into the books.
- **Trust.** One wrong dictated figure — a client name, a deduction amount — poisons trust in the entire copilot, not just the dictation feature. For a product whose core promise (per feature D) is *not being wrong about money*, shipping a feature with a structurally high error rate on financial content undermines the brand of everything else. Trust is a stock that this feature draws down on day one.
- **Cost.** Unlike one-time build effort, dictation carries recurring per-session compute (STT + LLM) that scales with usage and prices no offset — notes are an input, not billable value. That is the Duolingo Max lesson (Module 15/Case C): success compresses margins when compute scales with usage and revenue doesn't. The RICE "Effort" column (4 pw) hides this ongoing cost entirely.
- **Compliance.** In accounting, dictated notes become records: they must be accurate, complete, and attributable. A generative transcription of financial facts is a liability, not a feature — and audio of client financials is PII with storage and retention obligations (Module 13/16). The company would be engineering a records-integrity risk into its most sensitive data.
- **The team's own inputs agree.** Impact 1 with 60% confidence is the team saying it does not believe this matters much, and is not sure. When the score's own components confess low expected value *and* the un-priced risks are severe, the judgment call is no-ship — this is precisely the case where the PM's job is to say no despite the number (Module 9: the won't-do list is the difference between a strategy and an aspiration).

*(Note for grading: a defensible alternative is to pick E — mobile companion app — on cost-of-uncertainty grounds (20 pw for 50% confidence). Accept either pick if the defense uses specific AI-specific risks; reject any pick that cites only the score.)*

## 4. The "won't do" list, with reasons

- **C — AI audit-trail export: permanent won't-do.** Two independent reasons. (1) It scores last (150): lowest reach, lowest confidence (40%), highest effort of the six. (2) It is the wrong instrument — the program's feasibility drill (Module 12) says AI loses when answers must be deterministic and complete. An audit trail is a non-fabricable, complete, attributable record of what actually happened; a generative model producing the trail is a compliance catastrophe (a fabricated trail is worse than no trail). If customers need export, ship a deterministic rules-based export of logged events — no LLM involved. This is the "AI toaster" of the list: an AI feature where the problem is actually about process and determinism.
- **E — Mobile companion app: deferred, not permanently won't-do.** 20 person-weeks (half a quarter for a small pod) at 50% confidence for a platform bet whose value rests on unvalidated assumptions about accountants' mobile workflows. Defer with a re-evaluation trigger: re-score after D ships and we have retention evidence, and validate the mobile job-to-be-done with discovery (Module 7) before any build. A platform bet is a bet you make with evidence, not hope.
- **B — Voice dictation: not shipped (see above), regardless of score.** Restate it in the won't-do list so the roadmap is explicit: the score is overridden by quality, trust, cost, and compliance risk.

The discipline of the list is that it is written, explicit, and reasoned — not a silent "we didn't get to it." If a future quarter produces evidence (better STT accuracy on financial vocabulary, validated demand, a compliant records design), B and E may be re-scored; C's reason (determinism) is structural and does not change with evidence.

---

# How to grade yourself honestly

- **Grade dimension by dimension, within 48 hours of writing, and grade the output — not the hours.** Score Framework use, Numbers, Judgment, and Communication separately per the midterm rubric; a beautiful Q1 answer with no detection mechanisms is a C on framework use no matter how well it reads, and an A on communication doesn't rescue it.
- **Apply the "defend it out loud" test:** could you stand in front of a skeptical VP and deliver this answer in five minutes, with the numbers from memory — including explaining *why* RICE ranks D first and defending why you won't ship B? If you couldn't, the answer is not an A, regardless of what is on the page.
- **Be merciless on numbers and evidence, generous on judgment.** Recompute every RICE figure by hand (they must equal the worked answer exactly); trace every claim in Q1/Q2 to the scenario text or the case packets — a claim with no traceable basis drops a band (per the exam book's grading protocol). But on judgment, reward any position that is specific, defended with AI-specific risks, and built on stated assumptions — even if you would have chosen differently. If you caught yourself hand-waving anywhere ("we'll monitor it," "the metrics are misleading" with no mechanism), that section is a C regardless of the prose around it.
