# PROD 260 — AI PRODUCT MANAGEMENT
## From First Principles to Production Judgment

> **Program note:** This file is the core syllabus of the **AI-PM Graduate Program** (Graduate Certificate in AI Product Management) — 10 courses, 23–27 credits, four terms. Its 20 modules map to the program's courses as follows:
>
> | Course | Modules (this file) |
> |---|---|
> | AI 510 — AI & LLM Literacy | 2–6 |
> | PM 501 — Product Management Fundamentals | 1, 7–11 |
> | AIPM 520 — AI Product Craft | 12–16 |
> | DATA 530 — Data, Metrics & Experimentation | 10, 13, 14 deepened |
> | STRAT 540 — AI Strategy, Economics & GTM | 15–16 deepened |
> | RSK 550 — Responsible AI, Safety & Governance | 16 deepened |
> | CAP 600 — Capstone Studio | 17–20 |
> | FDE 560 / AI 570 / GTH 580 (electives) | new content in the HTML syllabi |
>
> **Program site:** `index.html` · schedule generator: `schedule.html` · progress tracker: `tracker.html` · glossary: `glossary.html` · case packet: `case-packets.md` · exam book: `exams.md`. Each course's full syllabus (lectures, problem sets, seminars, self-checks, course final, rubric, key terms) lives in `courses/`. This file remains the authoritative deep syllabus; the HTML is the navigation and operating layer.

**Course format:** Self-paced graduate-style seminar · 20 modules · 5–10 hrs/week · ~150–180 total hours (~2.5 credit-hours equivalent)
**Designed in the tradition of:** the Harvard Business School case method and the Stanford graduate seminar — a reading-intensive, artifact-producing, case-driven course. Not affiliated with either institution.
**Instructor:** You. This course is taught by the student to the student; every module ends with a graded self-assessment, and the portfolio you build is the grade the world will see.
**Prerequisites:** None technical. Significant professional experience recommended (strategy, operations, client delivery — the transferable half of the PM job).
**Materials cost:** Under $50 (three used paperbacks; everything else free — full packet in Appendix A).
**All readings, papers, and case facts verified against primary sources, August 2026.**

---

## Catalog description

This course builds a product manager from zero technical and PM background, with working fluency in modern AI systems. Students develop, in order: (1) a first-principles mental model of how large language models work and fail; (2) the core craft of product management — discovery, specification, prioritization, metrics, and delivery; and (3) the judgment that defines an AI PM — feasibility, evaluation, cost/latency trade-offs, and risk. The course is case-driven (GitHub Copilot, Intercom Fin, Duolingo Max, Klarna), paper-grounded (Vaswani et al. 2017; Brown et al. 2020; Lewis et al. 2020; Liu et al. 2023; Chen et al. 2021), and practice-first: every module produces a portfolio artifact, culminating in a capstone product with a full evaluation suite and a written thesis defended orally. By the end, students can walk into an AI PM role — or lead AI product work in their current organization — and operate on day one.

**Why this course exists for you:** You are a strategist/operator launching a Forward Deployed Engineering team, moving toward AI product management. You are not starting from nothing — you are adding product craft and AI literacy to an existing operating core. The course is built to that profile: your FDE launch is your live lab ("FDE twist" callouts throughout), and the capstone can be a prototype your team could genuinely show a client.

---

## How this course works

**The contract.** You are the student and the grader. The course is honest about this: no one will check your work, so the course is designed so that *skipping the work is self-evidently worse* — every deliverable is a real artifact you will want (a prompt library, an eval suite, a cost model, a case study). The grade matters only insofar as it calibrates you.

**The weekly rhythm (5–10 hrs):**
- **Pre-class preparation** (~2.5 hrs) — the required readings and videos, in order
- **Problem set** (~2 hrs) — the hands-on exercise
- **Deliverable** (~2 hrs) — the portfolio artifact (every one is examinable; see Appendix B)
- **Self-assessment** (~0.5–1 hr) — the module's "you can now" checklist, graded honestly

**The case method.** Four cases (Appendix: *case-packets.md*) are taught HBS-style: you read the case packet, form a view, then write a one-page decision memo *before* reading the teaching note at the end of each packet. The memo is the point — it forces a position. Discussion questions are provided for study-group or written reflection.

**Examinations.** A take-home midterm after Module 10 and a capstone thesis + oral defense at the end. Full exam book: *exams.md*.

**Honor code (self-paced adaptation).** You may use AI for *everything* — drafting, coding, reviewing, critiquing — because supervising AI output is the skill this course teaches. Two obligations: (1) every deliverable carries an **AI-use declaration** ("drafted by AI, rewritten by me," "AI-reviewed, claims verified," or "entirely mine"), and (2) you must be able to defend every claim in every deliverable under questioning. If you cannot explain a paragraph, it does not count as learned — regardless of who wrote it.

**Office hours.** In a solo course, "office hours" means study groups. Recruit one peer (or an AI in a separate session) to review deliverables and to answer seminar questions out loud. Verbalizing judgment is half the training.

---

## Learning objectives

By the end of this course, the student can — organized by Bloom's taxonomy:

| Level | Objective |
|---|---|
| **Remember** | Define the core vocabulary: token, context window, hallucination, RAG, embedding, eval, drift, precision/recall, latency, prompt injection, and the PM toolkit (PRD, RICE, north star, JTBD, double diamond). |
| **Understand** | Explain how LLMs work from first principles — training as lossy compression, attention, next-token inference — and why that implies both capability and failure modes. Explain the AI PM's core insight: *capability is not reliability*. |
| **Apply** | Run a discovery interview; write a PRD with testable acceptance criteria; score with RICE; build a no-code AI product; call an LLM API; build and run an eval suite; estimate cost per interaction. |
| **Analyze** | Decompose any product idea into feasibility (AI vs. rules vs. human), data requirements, evaluation design, and cost/latency constraints. Analyze case studies — including separating vendor-published claims from verifiable evidence. |
| **Evaluate** | Judge model quality with evals and metrics; design production eval systems (golden sets, regression gates, drift monitoring); weigh model-selection and packaging trade-offs; assess bias, privacy, security, and compliance risk; decide when *not* to use AI. |
| **Create** | Ship a capstone AI product end-to-end with a PRD, eval suite, metrics plan, cost model, and risk register; write a case study; defend the whole in a recorded presentation; produce a 30/60/90 plan for a first AI PM role. |

---

## Assessment & grading

| Component | Weight | What it is |
|---|---|---|
| Problem sets | 25% | Weekly exercises; graded on completion + evident learning (see rubric) |
| Case memos | 20% | Four 1-page decision memos (5% each), one per case |
| Self-assessments | 10% | Weekly "you can now" checklists, honestly scored |
| Midterm examination | 15% | Take-home, ~3 hours, after Module 10 (*exams.md*) |
| Final: capstone thesis + defense | 30% | Written thesis, recorded defense, portfolio review (*exams.md*) |

**Letter scale (self-graded):** A ≥ 90 · A− ≥ 85 · B+ ≥ 80 · B ≥ 75 · B− ≥ 70 · C+ ≥ 65 · below 65: repeat the deficient modules. An "A" requires the capstone to be externally demonstrable (see below).

**External review (the honest grade).** The portfolio's true examination happens when a hiring manager, mentor, or recruiter reads it. After Module 19, send the portfolio index to one experienced PM or hiring manager for review. Their read is the grade that matters; treat it as a final exam with an external examiner.

**Audit track vs. credit track.** Audit: read + watch only, no deliverables, no grade. Credit track (recommended): everything. Audit-tracking a course like this produces knowledge without judgment; the deliverables are where judgment is built.

---

## Course calendar

| Mod | Module | Theme | Deliverable | Case | Milestone |
|---|---|---|---|---|---|
| 1 | Orientation: The PM's Instrument | Foundations | Skill map + portfolio system | — | — |
| 2 | The Transformer: How LLMs Work | AI literacy | "AI 101" explainer | — | — |
| 3 | Prompting as an Interface | AI literacy | Prompt library | — | — |
| 4 | Retrieval & No-Code Building (RAG) | AI literacy | Working RAG bot + write-up | — | — |
| 5 | Python & the API Layer | AI literacy | Scripts + API README | — | — |
| 6 | Measurement: Evals & Metrics | AI literacy | Eval suite + report | **Case A: Copilot** | Case memo 1 |
| 7 | Discovery: The Double Diamond | PM craft | Discovery notes | — | — |
| 8 | The PRD & Spec Writing | PM craft | PRD v1 | — | — |
| 9 | Prioritization & Roadmaps | PM craft | RICE + roadmap | — | — |
| 10 | Metrics, Funnels & Instrumentation | PM craft | Metrics tree | — | **Midterm** |
| 11 | Delivery: Working with Engineers | PM craft | Sprint plan | — | — |
| 12 | Feasibility & System Design | AI PM craft | Feasibility doc + template | **Case B: Fin** | Case memo 2 |
| 13 | Data: The Fuel | AI PM craft | Data plan | — | — |
| 14 | Evals in Production | AI PM craft | Production eval plan | — | — |
| 15 | Cost, Latency & Model Selection | AI PM craft | Cost model | **Case C: Duolingo** | Case memo 3 |
| 16 | Risk, Safety & Go-to-Market | AI PM craft | Risk register + GTM | **Case D: Klarna** | Case memo 4 |
| 17 | Capstone: Proposal | Capstone | Capstone brief + PRD v2 | — | — |
| 18 | Capstone: Build & Measure | Capstone | Working product + eval report | — | — |
| 19 | Portfolio & Packaging | Capstone | Case study, demo, index | — | External review |
| 20 | The Defense & Transition | Capstone | STAR stories, résumé, 30/60/90 | — | **Final** |

---

# MODULES

---

## Module 1 — Orientation: The Product Manager's Instrument

**Objectives:** Explain what an AI PM does in two minutes · map your transferable skills to PM competencies · stand up the portfolio system.

**Pre-class preparation**
- *Required:* This course's catalog description and assessment sections (above). Skim 2–3 real "AI product manager" job descriptions on LinkedIn/Indeed — read them as specifications: what *outcomes* do they demand?
- *Required:* [Lenny's Newsletter — "A guide to AI prototyping for product managers"](https://lennysnewsletter.com) (free tier; search the archive)
- *Recommended:* [LaunchNotes — "AI Product Manager: Responsibilities & Skills"](https://www.launchnotes.com/blog/ai-product-manager-job-description-key-responsibilities-and-skills)

**Lecture.** A product manager is the person who owns the answer to three questions: *what problem are we solving, for whom, and how will we know it worked?* Everything else — PRDs, roadmaps, standups — is instrumentation around those three questions. Classic PMs sit between users, engineers, and the business; the AI PM adds a fourth party: *the model*, which has capabilities, failure modes, and a per-token price. The AI PM's distinctive job is judging when AI is the right instrument, designing how it will be measured, and owning the risks it introduces. Note what is *not* in the job: training models. Technical literacy — enough to judge feasibility, read metrics, and argue trade-offs — is the requirement, and it is exactly what this course builds.

**FDE twist.** You have run most of a PM's job inside client engagements: scoping, stakeholders, risk, delivery. The gap this course closes is vocabulary and instrument: how to *write* the product down, how to *measure* the AI, and how to *argue* the trade-offs with engineers.

**Seminar questions.** Where does an AI PM's job differ from a classic PM's? Where is it identical? What does "AI for everything" thinking cost a company?

**Problem set.** The asset map: translate your strategist/operator experience into PM terms on paper (stakeholder alignment → stakeholder management; engagement scoping → prioritization & trade-offs; risk on engagements → risk management; ambiguity → discovery). Add four rows of your own.

**Deliverable.** Portfolio system: folder structure (`portfolio/`, `prompts/`, `evals/`, `capstone/`) plus `portfolio/README.md` — a tracker table (Week, Artifact, Date done, One-line value pitch, Link) with this module as row one.

**Self-assessment.** ☐ I can explain what an AI PM does in two minutes ☐ I've mapped 6+ transferable skills ☐ My tracker exists and I know what "done" means for me this week.

---

## Module 2 — The Transformer: How LLMs Work

**Objectives:** Explain, in plain English, how an LLM works: training, tokens, context window, inference · articulate why "predicting the next word" produces intelligence-like behavior · state what AI can and cannot do.

**Pre-class preparation**
- *Required:* [Karpathy — "Intro to Large Language Models" (1 hr)](https://www.youtube.com/watch?v=zjkBMFhNj_g)
- *Required:* [Wolfram — "What Is ChatGPT Doing … and Why Does It Work?"](https://writings.stephenwolfram.com/2023/02/what-is-chatgpt-doing-and-why-does-it-work) — read the first third
- *Required:* [3Blue1Brown — "Attention in transformers, step-by-step"](https://www.3blue1brown.com/lessons/attention/)
- *Required paper:* Vaswani et al., *Attention Is All You Need* (2017) — [arXiv:1706.03762](https://arxiv.org/abs/1706.03762). Read the abstract and introduction; skim the architecture figure. This is the paper that created the transformer. You are not expected to follow the math — you are expected to be able to say what the paper *did*.
- *Recommended paper:* Brown et al., *Language Models are Few-Shot Learners* (2020) — [arXiv:2005.14165](https://arxiv.org/abs/2005.14165). Read the abstract only.

**Lecture.** The mental model to internalize: a language model is a giant statistical machine trained to predict the next token (a word fragment) given everything before it. Training is lossy compression — the model absorbs patterns from internet-scale text into its parameters, not the text itself. That is why it "knows" things (patterns, it compressed) and why it hallucinates (patterns it confidently mis-assembles). Attention is the mechanism that lets each token weigh the relevance of every other token in the context — it is what makes long-range meaning possible. Inference is the cheap operation: feed tokens in, sample the next, repeat. Two properties follow directly and will recur all course: **capability** (what it can do in a demo) is not **reliability** (what it will do in production), and the **context window** is the only working memory the model has — what is not in context does not exist for it. "It's just predicting the next word" is true, and it is not a put-down: the discipline of an AI PM is designing around a system that is probabilistic, not deterministic.

**Seminar questions.** If an LLM "knows" only what it compressed, what does that imply about building a product on a model's internal knowledge vs. on retrieved documents? What does the capability/reliability gap mean for a product that must never be wrong?

**Problem set.** Write the first 15 glossary terms (Appendix C) in your own words from memory; check against the glossary.

**Deliverable.** The "AI 101" explainer: a 2-page plain-English document — *how an LLM works, for a smart non-technical person* — covering training as lossy compression, tokens, context window, probabilistic output, hallucination. You will reuse this document for interviews, exec briefings, and onboarding your FDE team.

**Self-assessment.** ☐ I can define: token, context window, hallucination, inference, fine-tuning ☐ I can explain why a model confidently states false facts ☐ I can say what the 2017 transformer paper did and why it mattered ☐ I can explain capability vs. reliability.

---

## Module 3 — Prompting as an Interface

**Objectives:** Use frontier models systematically · design prompts (role, context, task, format; few-shot; structured output) · build a reusable prompt library.

**Pre-class preparation**
- *Required:* [DeepLearning.AI — "ChatGPT Prompt Engineering for Developers" (free)](https://www.deeplearning.ai/courses/chatgpt-prompt-eng) — or, if you prefer zero code, [AI Prompting for Everyone](https://www.deeplearning.ai/courses/ai-prompting-for-everyone)
- *Recommended:* [Simon Willison's blog](https://simonwillison.net/) — 30 minutes on the *llms* tag. He is the field's clearest practical writer; subscribe for the rest of your career.

**Lecture.** The prompt is the product's interface to the model — which makes prompt design interface design. The core pattern: **role** (who the model is), **context** (the situation), **task** (what to do), **format** (how to output). Add **few-shot** examples when behavior matters more than prose, and **structured output** (JSON, schemas) when a machine will consume the result — every serious product forces structure. Temperature is the creativity knob; products that need determinism turn it down or fix the seed. Two deeper truths: (1) prompt engineering is *shifting* the model's behavior, not rebuilding it — when the prompt grows past a page, you are fighting the model and should reconsider the design; (2) prompts are attack surface — the model will follow instructions it finds in user-supplied text, which is the security hole called prompt injection (full treatment in Module 16). Treat the prompt as a spec: version it, test it, and measure it like any interface.

**Seminar questions.** Where does prompt engineering end and product design begin? What breaks first when a prompt library grows to 200 prompts?

**Problem set.** The 20-prompt challenge: pick one high-value use case (client status updates, vendor proposal summaries, FDE scoping questions), build 20 prompts, test each, record what worked. Include at least one "ask me clarifying questions first" prompt and one structured-output prompt.

**Deliverable.** `prompts/` library: winning prompts with (a) why it works, (b) one bad variant and why it fails. A hiring manager will ask "how do you prompt?" — this is the evidence.

**Self-assessment.** ☐ I can explain system vs. user prompts, few-shot, temperature, structured output ☐ 15+ tested prompts saved ☐ I can explain prompt injection in one sentence.

---

## Module 4 — Retrieval & No-Code Building (RAG)

**Objectives:** Build a working document-Q&A product without code · explain RAG at the architectural level · articulate why grounding reduces hallucination.

**Pre-class preparation**
- *Required paper:* Lewis et al., *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks* (2020) — [arXiv:2005.11401](https://arxiv.org/abs/2005.11401). Read the abstract and the conclusion; the core idea is parametric memory (the model) + non-parametric memory (a retrieval index).
- *Required paper:* Liu et al., *Lost in the Middle: How Language Models Use Long Contexts* (2023) — [arXiv:2307.03172](https://arxiv.org/abs/2307.03172). Read the abstract and skim the findings: models use information at the *ends* of long contexts far better than the middle. This one finding shapes real product decisions (where you place retrieved content, how you chunk documents).
- *Required:* 30 minutes on [Simon Willison's blog](https://simonwillison.net/) on retrieval/search.
- *Recommended:* A YouTube walkthrough of your chosen builder (search "build a document Q&A bot with [tool] 2026").

**Lecture.** A model's parameters are its *trained* knowledge — frozen at training time, unreliable for your specific documents. Retrieval-augmented generation fixes this by giving the model a working memory: chunk your documents, embed them into vectors, and at query time fetch the most relevant chunks into the context window. The model then answers from what is in front of it, not from memory — which is why RAG reduces hallucination and keeps answers current (update the documents, and the answers update). The architecture you should be able to draw from memory: documents → chunking → embeddings → vector store → (query → retrieve top-k → stuff into context) → model → grounded answer. Now the failure modes: bad retrieval (the right chunk didn't make top-k), bad chunking (the answer straddled two chunks), and *Lost in the Middle* — the model under-uses the middle of its context, so where you place retrieved content is a design decision. Retrieval quality is a product-quality problem: it is measurable, and it is yours to own.

**Seminar questions.** Why does RAG beat fine-tuning for most products? (Answer by Module 13.) What happens to a RAG system when the underlying documents contain contradictions?

**Problem set.** Build a document Q&A bot with a free-tier builder (Claude/Google AI Studio projects, Flowise, or n8n). Upload 3–5 real documents; test 25 questions; note the failure cases.

**Deliverable.** The working bot + a 1-page architecture write-up (draw the pipeline) + 3 documented failure cases with hypotheses about *why* they failed.

**Self-assessment.** ☐ I can explain RAG and draw its pipeline ☐ I can explain what "Lost in the Middle" means for design ☐ I can list 3 failure modes of my bot and diagnose each.

---

## Module 5 — Python & the API Layer

**Objectives:** Run Python · make a real LLM API call · read a small script · estimate what a call costs · explain the request/response pattern.

**Pre-class preparation**
- *Required:* [freeCodeCamp — "Learn Python – Full Course for Beginners"](https://www.youtube.com/watch?v=rfscVS0vtbw) — watch through ~2.5 hrs (functions, lists, dictionaries). You will finish the rest in Module 13 downtime.
- *Reference:* [The Python Handbook](https://www.freecodecamp.org/news/the-python-handbook/)
- *Recommended:* [Kaggle Learn — Python](https://www.kaggle.com/learn/python) (browser-based, free) as an alternative or supplement.

**Lecture.** Why does an AI PM learn Python? Not to ship production code — to *verify, evaluate, and estimate*. Three uses recur: (1) run evaluation scripts that score model outputs; (2) read the code engineers and data scientists write, well enough to ask good questions; (3) build prototypes and cost estimates. The API pattern you must internalize: an **endpoint** is a URL that accepts a **request** (your prompt + parameters, authenticated by an **API key**) and returns a **response** (the model's output + **usage** — tokens in/out). Everything about cost flows from usage: price per million input tokens + price per million output tokens (output is typically 3–5× input price — check current pricing). A chain — call 1 summarizes, call 2 extracts, call 3 grades — is the seed of every agent architecture. Your first scripts will feel magical; by Module 18 they will feel like furniture. That shift is the point of this module.

**Problem set.** Make the call. Free path: [Ollama](https://ollama.com) locally (zero cost). Hosted path: ~$5 of credits at OpenAI or Anthropic. Script 1: prompt → response → token usage. Script 2: a 3-call chain (summarize → bullets → grade). Comment every line yourself — the commenting is the learning.

**Deliverable.** Both scripts in `portfolio/` + README: API key, endpoint, request/response, token, rough cost of one call.

**Self-assessment.** ☐ I can run a `.py` file ☐ I can explain endpoint/request/response/API key ☐ I can read a 30-line script and say what it does ☐ I can estimate one API call's cost.

---

## Module 6 — Measurement: Evals & Metrics
*Case A: GitHub Copilot — "Measuring the Unmeasurable" (case-packets.md)*

**Objectives:** Build and run an eval suite · explain the accuracy trap and precision/recall · measure an AI feature's quality · write a case decision memo.

**Pre-class preparation**
- *Required:* 2–3 Simon Willison posts on LLM evals/testing ([simonwillison.net](https://simonwillison.net), *machine-learning* or *llms* tags)
- *Required:* **Case A** in *case-packets.md* — read the packet, form a view, write memo 1 *before* reading its teaching note.
- *Required paper (background for Case A):* Chen et al., *Evaluating Large Language Models Trained on Code* (2021) — [arXiv:2107.03374](https://arxiv.org/abs/2107.03374). Read the abstract and the HumanEval discussion: Codex solves 28.8% of HumanEval problems; with 100 samples per problem, 70.2%. The birth of "evaluate by functional test."

**Lecture.** The accuracy trap: a model that answers "yes" to everything scores 90% "accuracy" on skewed data while being useless. The discipline of evals exists to defeat this. An **eval set** is a fixed collection of cases with expected behaviors; an eval *run* scores the model against it. For classification, precision = of the things flagged, how many were right; recall = of the things that should be flagged, how many were caught — and they trade off; the threshold you choose is a *product* decision (in a medical app you want recall; in a spam filter, precision). For generative output, scoring is fuzzier: rubric-based human review, LLM-as-judge (fast, cheap, biased — spot-check), or functional tests (does the code pass the test suite — the HumanEval insight). The deeper lesson, via Copilot: when the artifact is open-ended (code, prose), measurement is a *design* problem — you must define what "good" means before you can argue about whether the AI is good. That definition is the AI PM's job.

**FDE twist.** Your FDE team will be asked "does this AI actually work?" by clients. This module gives you the instrument that answers it — before you've even met the client.

**Problem set.** Build an eval suite for your Module 4 bot: 25 cases (easy, edge, adversarial, out-of-scope) with expected behaviors; run, score, find failure patterns; fix the worst; re-run.

**Deliverable.** `evals/week6-eval-suite.md` (suite + results + what you learned) **and Case memo 1** (1 page, per *case-packets.md*).

**Self-assessment.** ☐ I can define precision, recall, accuracy, hallucination rate ☐ I can explain why accuracy alone misleads ☐ I ran a fix-and-re-run eval cycle ☐ My case memo takes a position.

---

## Module 7 — Discovery: The Double Diamond

**Objectives:** Run the discovery half of the double diamond · conduct non-leading user interviews · write JTBD statements · capture evidence, not opinions.

**Pre-class preparation**
- *Required:* [Lenny's Newsletter](https://lennysnewsletter.com) — search "what do product managers do"
- *Required:* *The Mom Test* (Appendix D), chapters 1–2 — how to interview without being lied to
- *Recommended:* A "double diamond" explainer and a JTBD primer (search either term; pick one well-cited source)

**Lecture.** Product work is two diamonds: *discover* the right problem (divergent) → *define* it (convergent) → *develop* the right solution (divergent) → *deliver* it (convergent). Most failures happen in the first diamond, where speed feels like progress. Discovery is an evidence-gathering discipline: you are looking for *demonstrated* behavior, not *stated* desire — what people did, how they solve it today, what it costs them. The Mom Test's core move: talk about their past, never pitch your idea, never ask "would you use this?" (people lie to be polite). The output is jobs-to-be-done — "when ___, I want ___, so I can ___" — and a set of quotes you can show, not a feature list. A problem statement without interview evidence is a hypothesis wearing a costume; your PRD in Module 8 will cite this evidence, which is what separates product management from opinion.

**Problem set.** Pick a real problem space (FDE twist: a service clients keep requesting, or a recurring client pain). Write a one-paragraph problem statement. Interview 3–5 people Mom-Test style. Capture quotes, pains, current workarounds, frequency.

**Deliverable.** `portfolio/discovery-notes.md` — problem statement, interview notes, 5+ direct quotes, 3 JTBD statements, and a "surprises" section (what contradicted your assumption — the gold).

**Self-assessment.** ☐ I can explain the double diamond ☐ I can interview without leading ☐ I can write a JTBD statement ☐ My notes contain demonstrated behavior, not stated desires.

---

## Module 8 — The PRD & Spec Writing

**Objectives:** Write a PRD with evidence, scope discipline, user stories, and *testable* acceptance criteria.

**Pre-class preparation**
- *Required:* Two real PRD examples (search "PRD example"; or Lenny's PRD template on lennysnewsletter.com)
- *Required:* A user stories + acceptance criteria guide (Atlassian's is good and free)

**Lecture.** The PRD is a *decision document*, not a wish list: it records the problem (with evidence), the users, the success metrics, the scope, and the requirements in a form engineers can build from. The unit of requirements is the **user story** — "as a ___, I want ___, so ___" — with **acceptance criteria** written as given/when/then ("Given a question outside scope, when asked, the bot responds with the out-of-scope message"). Testable acceptance criteria are the difference between a spec and a vibe. Scope is the PRD's spine: an explicit out-of-scope section is a promise to stakeholders about what you are *not* doing, which is harder and more valuable than listing what you are. A good test for the whole document: *could an engineer build this without asking me ten questions?* If not, tighten.

**Problem set.** Write PRD v1 for one AI feature of your capstone idea: problem & evidence (cite Module 7), users, success metrics (deepened in Module 10), scope in/out, user stories, acceptance criteria, risks, open questions.

**Deliverable.** `portfolio/prd-v1.md`.

**Self-assessment.** ☐ I can define PRD, user story, acceptance criteria, out-of-scope ☐ My acceptance criteria are given/when/then ☐ My PRD cites evidence ☐ An engineer could build from it without ten questions.

---

## Module 9 — Prioritization & Roadmaps

**Objectives:** Score with RICE · apply MoSCoW · build a theme-based roadmap with an explicit "won't do" list · defend a prioritization decision.

**Pre-class preparation**
- *Required:* RICE (search "RICE scoring model Intercom") and MoSCoW (one article each)
- *Required:* Roadmapping basics (search "product roadmap themes vs features")

**Lecture.** Prioritization is where PMs earn their keep, because saying yes to everything is free and worthless. RICE makes the trade explicit: **R**each × **I**mpact × **C**onfidence ÷ **E**ffort — a single number that forces you to write down assumptions (confidence is a confession of uncertainty, which is its point). MoSCoW handles the *shape* of a release (must/should/could/won't). The modern roadmap is organized by **themes with outcomes** — "improve activation for new users" — not by dated features, because themes survive contact with reality and dates don't. The single most valuable artifact on any roadmap is the **"won't do" list**: written, explicit, with reasons. It is the difference between a strategy and an aspiration. Note the AI-specific wrinkle: AI features often win on RICE *impact* but carry hidden cost and risk (Modules 15–16); a good prioritization accounts for them.

**Problem set.** Take 8 candidate features (from discovery + your own ideas), score with RICE showing your work, group winners into themes, lay out a 2-quarter roadmap (theme → outcome → candidate features), and write the "won't do" list with reasons.

**Deliverable.** `portfolio/roadmap.md`.

**Self-assessment.** ☐ I can explain RICE and MoSCoW ☐ I can defend one decision against pushback ☐ My roadmap is themes + outcomes, not dated features ☐ My "won't do" list has reasons.

---

## Module 10 — Metrics, Funnels & Instrumentation

**Objectives:** Define north star + guardrail metrics · build a funnel · specify instrumentation (events) · explain leading vs. lagging measures.

**Pre-class preparation**
- *Required:* North star metric (search "north star metric" on lennysnewsletter.com), AARRR ("pirate metrics"), and A/B testing basics (one explainer each)

**Lecture.** A metric is a contract about what success means; choose it badly and everything downstream is theater. The **north star** is the one number that best captures delivered value ("weekly active learners," not "downloads"). **Guardrails** are the numbers that must not silently degrade — for AI features, always include model-quality metrics: hallucination rate, eval score, cost per session. The **funnel** shows where value leaks (acquisition → activation → retention → referral); **instrumentation** is the event log that makes the funnel visible — if you didn't log it, it didn't happen. Leading indicators predict the future (activation rate), lagging ones confirm it (retention); a north star needs both. The AI-specific trap: AI features change *quality*, not just *clicks* — an A/B test that shows +10% clicks while hallucination doubles is a loss dressed as a win. Your metrics tree (north star at top, drivers below, guardrails at the side) is the document that makes this legible to everyone.

**Problem set.** For your capstone idea: north star, 3 guardrails with thresholds, the funnel, the event list (every event you'd log), and the model-quality metrics you'd merge in from Module 14.

**Deliverable.** `portfolio/metrics-tree.md`.

**Self-assessment.** ☐ I can define north star, activation, retention, guardrail, A/B test ☐ My metrics tree has leading and lagging measures ☐ I can list the events a simple AI feature must log.

> ### MIDTERM EXAMINATION (take-home, ~3 hrs)
> Sit after completing this module. See **exams.md** — three essay questions on design, measurement, and prioritization. Closed-notes except: this course guide, your portfolio, and the case packets. Grade against the rubric in the exam book.

---

## Module 11 — Delivery: Working with Engineers

**Objectives:** Turn a PRD into a sprint plan · run the delivery rituals (standup, retro, definition of done) · unblock with evidence.

**Pre-class preparation**
- *Required:* Agile/scrum basics (search "scrum roles sprint standup retrospective"; Atlassian's guide is free and good)
- *Required:* One PM–engineering collaboration essay on [First Round Review](https://firstround.com/review) (search "how product managers work with engineers")

**Lecture.** Discovery wins the problem; delivery wins the trust. The delivery machinery: **sprints** (time-boxed iterations), **standups** (daily sync: what I did, what's blocked, what's next), **retros** (what to keep/change), **definition of done** (the shared bar for "finished"). The PM's job *during* a sprint is not to manage people — it is to manage *information*: unblock ambiguity ("the spec is unclear here" → "I'll clarify by Thursday"), cut scope with evidence when reality bites, and protect the team from whiplash. Two disciplines matter most. First, tickets: slice work small enough to finish in days, each with acceptance criteria — a ticket without criteria is a hope. Second, saying no: engineers will propose technical debt and scope creep with good reasons; the PM's answer is "show me the impact" — the same RICE discipline from Module 9, now at ticket scale. Treat engineers as expert collaborators, not order-takers: the best spec conversations change the spec.

**Problem set.** Convert your PRD into a sprint plan: tickets with acceptance criteria and a definition of done. Record a 5-minute mock standup (voice memo). Write 3 ways you'd unblock an engineer this sprint.

**Deliverable.** `portfolio/sprint-plan.md` + communication plan (who you update, how often).

**Self-assessment.** ☐ I can explain sprint, standup, retro, DoD ☐ I can turn a PRD into tickets ☐ I know what a PM does *during* a sprint.

---

## Module 12 — Feasibility & System Design
*Case B: Intercom Fin — "The Retrieval-First Support Agent" (case-packets.md)*

**Objectives:** Decide when AI is the right tool · sketch a simple AI system architecture · design guardrails and human-in-the-loop · write case memo 2.

**Pre-class preparation**
- *Required:* [Anthropic — "Building effective agents"](https://www.anthropic.com/engineering/building-effective-agents) — read fully. The most-cited engineering post in the field: the best AI systems are *simple, composable patterns*, not complex frameworks.
- *Required:* **Case B** in *case-packets.md* — read, form a view, write memo 2 *before* the teaching note.
- *Required:* One a16z essay on AI products (search "a16z how to think about AI products" or "a16z LLM app stack")

**Lecture.** Feasibility is the AI PM's signature judgment: *should this use AI at all?* The test is comparative — AI vs. a rules-based system vs. a human vs. nothing — scored on input/output clarity, error tolerance, data availability, cost, and latency. AI wins when the task is high-volume, language-shaped, and error-tolerant; it loses when answers must be deterministic, when the cost of being wrong is catastrophic, or when the problem is actually about process, not intelligence. (An "AI-powered toaster" is not a product; it's a gimmick with a transformer inside.) When AI is right, the architecture should be boring: model + retrieval + tools + guardrails + a human in the loop where stakes demand it. The Fin case is the masterclass: retrieval-only answers (no training-knowledge improvisation), source links (verifiable answers), policy checks as a separate model call (composition over one giant prompt), and an explicit human handoff for high-stakes actions. **Simple and composable** is not an aesthetic — it's how you keep a probabilistic system debuggable.

**Seminar questions.** What does Fin's architecture tell you about when *not* to trust the model's own knowledge? Where should the human-in-the-loop sit in a support product?

**Problem set.** The feasibility drill: 5 product ideas (3 real, 2 deliberately bad) × (what AI would do, input/output, error tolerance, data needs, cost, and the non-AI alternative). Sketch one architecture in boxes-and-arrows.

**Deliverable.** `portfolio/feasibility.md` — the drill + a reusable one-page feasibility template **and Case memo 2**.

**Self-assessment.** ☐ I can name 3 cases where AI is the wrong tool ☐ I can sketch model + retrieval + tools + guardrails + HITL ☐ I can explain "simple, composable" ☐ My case memo takes a position on Fin's design.

---

## Module 13 — Data: The Fuel

**Objectives:** Map data requirements · distinguish retrieval data from fine-tuning data · apply privacy fundamentals (PII, GDPR, EU AI Act vocabulary) · explain the data flywheel.

**Pre-class preparation**
- *Required:* One explainer each on: data quality vs. quantity, the data flywheel, and PII/GDPR basics (search the terms; pick well-cited sources)

**Lecture.** Every AI product runs on data, and most product failures trace back to a data assumption. Three distinctions organize the subject. (1) **Quality vs. quantity**: 1,000 clean, labeled examples beat 100,000 messy ones; the model learns the pattern, not the noise. (2) **Retrieval data vs. fine-tuning data**: retrieval data is the corpus your RAG system looks up — you maintain it like documentation; fine-tuning data changes the model itself — expensive, risky, and rarely the right lever when retrieval works. The default architecture is retrieval; the burden of proof is on fine-tuning. (3) **The data flywheel**: product usage generates data (queries, corrections, ratings) that improves the model/eval set, which improves the product — the strategic asset that compounds. Privacy is the constraint that shapes all of it: know what PII is, know that user data is *not* yours to train on without consent, and know the vocabulary of GDPR and the EU AI Act even if you're not in Europe — they govern what global products may do. An AI PM who says "we'll figure out data later" has already failed; this module's deliverable is the figure-it-out-now document.

**Problem set.** Finish the freeCodeCamp Python course (remaining ~2 hrs). Then map your capstone's data plan: what exists, what's missing, quality issues, collection method, PII exposure and what it means for design.

**Deliverable.** `portfolio/data-plan.md`.

**Self-assessment.** ☐ I can explain why clean beats big ☐ I can distinguish retrieval vs. fine-tuning data and argue for the default ☐ I can name privacy red flags in a feature idea.

---

## Module 14 — Evals in Production

**Objectives:** Design a production eval system — golden set, scoring method, regression gates, drift monitoring, feedback loop.

**Pre-class preparation**
- *Required:* One eval-in-production guide each from the labs (search "OpenAI evals" and "Anthropic evaluating AI systems"; both publish free, current guides)
- *Required:* One explainer on model drift and monitoring (search "model drift monitoring machine learning")

**Lecture.** Module 6 taught you to measure; this module teaches you to *operate*. A shipped AI product degrades — the world changes, users find new edge cases, the model's distribution drifts — so quality is an ongoing operating problem, not a launch-day checkbox. The production system has five parts: (1) a **golden set** — fixed cases that never change, so you can compare across model versions; (2) a **scoring method** — human review for high-stakes slices, LLM-as-judge for volume, and the discipline to spot-check the judge (judges have biases too); (3) **regression gates** — "we do not ship a model version that scores below X" — the mechanism that turns evals into governance; (4) **drift monitoring** — live signals (thumbs-down rate, "I don't know" rate, cost per session, eval score on a rolling sample) that trigger a re-eval; (5) the **feedback loop** — bad answers from production become new eval cases, so the eval set learns. The lesson to internalize and repeat to executives: *"it worked in the demo" is not "it works in production."* The demo is a single sample; production is a distribution.

**Problem set.** Design the production eval system for your capstone: golden set (start from Module 6's 25 cases), scoring method with trade-offs, regression thresholds, drift signals with triggers, and the feedback loop.

**Deliverable.** `portfolio/production-eval-plan.md`.

**Self-assessment.** ☐ I can design an eval pipeline for a live feature ☐ I can explain golden set, LLM-as-judge and when it lies, regression, drift, feedback loop ☐ I can give the "demo vs. production" speech.

---

## Module 15 — Cost, Latency & Model Selection
*Case C: Duolingo Max — "When AI Succeeds, Margins Compress" (case-packets.md)*

**Objectives:** Build a cost model · set a latency budget · select a model with explicit trade-offs · write case memo 3.

**Pre-class preparation**
- *Required:* Current pricing pages for OpenAI and Anthropic (search "OpenAI pricing" / "Anthropic API pricing"); note price per million tokens and the input/output price gap
- *Required:* One model-selection guide (search "how to choose an LLM cost latency quality")
- *Required:* **Case C** in *case-packets.md* — read, form a view, write memo 3 *before* the teaching note.

**Lecture.** AI breaks the software-economics assumption that marginal cost is ~zero: every interaction burns tokens, and your bill scales with success. The AI PM's toolkit: **cost per interaction** = (input tokens × input price + output tokens × output price) + retrieval/storage; then × usage = monthly bill. **Latency** is a product constraint — a "personal assistant" that takes 10 seconds to respond is not a personal assistant; set the budget before choosing the model. **Model tiers** are the trade-off engine: frontier models (better, slower, dearer) vs. small/cheap models (fast, cheap, good-enough on most cases) — and the professional move is to find where the cheap model is good enough, using *your* eval set (Module 6/14), not the leaderboard. **Caching** and prompt/cost engineering (shorter contexts, cheaper models for routine calls) are the levers. **Fine-tuning** is the expensive last resort. The Duolingo case is the cautionary tale that defines the module: AI features *worked* — and gross margin compressed because compute scaled with success, while the market punished the stock anyway. Budget for your own success before you launch, not after.

**Problem set.** Build the cost model for your capstone: tokens per action, cost per interaction, monthly bill at projected usage, 2–3 model tiers compared, latency budget, and a sensitivity ("if usage doubles…; if we switch models…").

**Deliverable.** `portfolio/cost-model.md` **and Case memo 3**.

**Self-assessment.** ☐ I can estimate cost per interaction and per month ☐ I can compare models on cost/latency/quality and make a call ☐ I can explain the "AI success compresses margins" dynamic.

---

## Module 16 — Risk, Safety & Go-to-Market
*Case D: Klarna AI Assistant — "Vendor Claims as Data" (case-packets.md)*

**Objectives:** Build a risk register · explain prompt injection and its mitigations · apply responsible-AI and compliance vocabulary · position and price an AI product · write case memo 4.

**Pre-class preparation**
- *Required:* One explainer on prompt injection (search "prompt injection explained")
- *Required:* One responsible-AI primer (Anthropic or Google publish good free ones)
- *Required:* One EU AI Act primer (search "EU AI Act explained")
- *Recommended:* Wilson & Daugherty, *Collaborative Intelligence: Humans and AI Are Joining Forces*, HBR July–August 2018 — [hbr.org/2018/07/collaborative-intelligence-humans-and-ai-are-joining-forces](https://hbr.org/2018/07/collaborative-intelligence-humans-and-ai-are-joining-forces) (free summary; full PDF is subscriber-only)
- *Required:* **Case D** in *case-packets.md* — read, form a view, write memo 4 *before* the teaching note.

**Lecture.** The risk taxonomy for AI products: **hallucination** (wrong confident output), **bias** (skewed training data producing skewed outcomes), **privacy** (PII leakage in prompts and training), **security** (prompt injection — attacker text hijacking the model's instructions; a real, demonstrated vulnerability class), and **compliance** (GDPR, EU AI Act, sector rules). The AI PM's instrument is the **risk register**: for each risk — likelihood, impact, mitigation, detection, owner. The universal mitigations recur: retrieval over improvisation (Module 4), evals as gates (Module 14), human-in-the-loop where stakes are high (Module 12), and transparency (source links, "this is AI" disclosure). Go-to-market completes the picture: positioning ("the fastest way to resolve a refund" beats "AI-powered refund agent"), and pricing — where AI breaks subscription assumptions, because usage-based cost (Module 15) argues for usage-based price, hybrid tiers, or outcome pricing (Fin's "pay per resolution"). Finally, the Klarna case teaches *epistemology*: the numbers are vendor-published. Your job as a PM is to know which claims are verified, which are marketing, and what you would measure yourself.

**Seminar questions.** How would you verify Klarna's numbers if you were their CTO? If you were their competitor? Where does "does the work of 700 agents" break down as a framing?

**Problem set.** Risk register for your capstone (the five risks above, each with likelihood/impact/mitigation/detection) + a GTM one-pager (who it's for, positioning, pricing logic, three expected objections and answers).

**Deliverable.** `portfolio/risk-register.md` + `portfolio/gtm-onepager.md` **and Case memo 4**.

**Self-assessment.** ☐ I can explain prompt injection and one mitigation ☐ My risk register has five risks, each with detection ☐ I can position without saying "AI-powered" four times ☐ I can explain why per-token pricing creates a packaging problem.

---

## Module 17 — Capstone: Proposal

**Objectives:** Scope a 15–20-hour build · write the capstone brief integrating every prior module · set evaluation design before code.

**Pre-class preparation**
- *Required:* Re-read your discovery notes (Module 7), PRD v1 (Module 8), metrics tree (Module 10), and production eval plan (Module 14) — the capstone integrates them.

**Lecture.** A capstone is a demonstration of judgment, not of engineering. The scoping rule: **narrow enough to finish, deep enough to show**. A document-Q&A assistant, a meeting-notes summarizer with action extraction, a support-triage bot — all are sufficient. The brief must be one page and must cite earlier modules: problem (M7 evidence), users, scope in/out, success metrics (M10), eval plan (M14), cost model (M15), risks (M16). Evaluation design comes *before* code: define the golden set and the success bar before you write a line, so "done" means "measured," not "demoed." **FDE twist:** the strongest capstone is a real FDE-shaped problem — a working prototype your team could show a client. That is not extra credit; it is the point.

**Problem set.** Write the capstone brief (one page) + PRD v2 (everything you now know that v1 didn't). Pre-register your golden set (25+ cases).

**Deliverable.** `capstone/brief.md` + `capstone/prd-v2.md`.

**Self-assessment.** ☐ My capstone is scoped to 15–20 hours ☐ Every brief section cites an earlier module ☐ My eval set is defined before code ☐ I can state success in one sentence.

---

## Module 18 — Capstone: Build & Measure

**Objectives:** Ship the product · run the eval cycle · report before/after with real numbers.

**Pre-class preparation:** None required — this is a build week.

**Lecture.** The build discipline: no-code + API scripts (or Python with heavy AI assistance — using an LLM to write code is what modern PMs do; reading every line it writes is what makes them PMs). Then the loop: run the golden set → score → fix the worst failure mode → re-run. Record everything: eval before/after, cost per interaction, latency, three user-visible examples of the improvement. The eval report is the capstone's center of gravity — a working product without measured results is a hobby.

**Problem set.** Build + eval loop (as above).

**Deliverable.** The working product + `capstone/eval-report.md` (before/after table, failure analysis, "what I'd do with 2 more weeks").

**Self-assessment.** ☐ The product works end-to-end ☐ My report shows a real before/after ☐ I can demo in 2 minutes without a script failure ☐ I know exactly what I'd improve next and why.

---

## Module 19 — Portfolio & Packaging

**Objectives:** Package the work for external judgment — case study, demo, index, LinkedIn.

**Pre-class preparation:** None required — packaging week.

**Lecture.** Hiring managers don't read résumés; they read evidence. The packaging stack: (1) **case study** — problem → process → solution → results (real numbers from M18) → what you'd do differently, written in STAR discipline; (2) **demo video** — 3 minutes, no dead air, talking through your own product (a job interview in miniature); (3) **portfolio index** — one page, who you are, the M1 asset map, five best artifacts with one-line pitches; (4) **LinkedIn** — headline with PM intent, post the case study. The test of packaging: *a stranger understands the case study in three minutes.*

**Deliverable.** `portfolio/case-study.md`, demo video, portfolio index, LinkedIn refresh. Then send the index to one experienced PM or hiring manager — the external review is part of the grade.

**Self-assessment.** ☐ A stranger can understand my case study in 3 minutes ☐ My demo has no dead air ☐ My index has 5+ artifacts with one-line pitches ☐ External review requested.

---

## Module 20 — The Defense & Transition

**Objectives:** Defend the work · answer AI-PM interview questions with frameworks · produce the transition kit (STAR stories, résumé, 30/60/90).

**Pre-class preparation**
- *Required:* *Cracking the PM Interview* (Appendix D), Part III — interview prep
- *Required:* Collect 10 real "AI product manager interview questions" (search); note the pattern — they test judgment ("should this feature use AI?"), measurement ("how would you know it's working?"), and risk ("how do you handle hallucination?") — you built answers in Modules 12, 14, 16.

**Lecture.** The AI PM interview tests three loops: **product sense** ("design an AI feature for X"), **execution** ("how would you prioritize / measure / de-risk?"), and **behavioral** ("tell me about a time…" — STAR: situation, task, action, result, ending in numbers). The killer question — "walk me through how you'd decide whether a feature should use AI" — now has a two-minute answer with a real framework, because you have one: comparative feasibility (M12), data check (M13), evaluation design (M14), cost/latency (M15), risk (M16). Your capstone is the proof. The transition kit: three STAR stories mined from your strategist/operator career and translated into PM vocabulary (the M1 asset map, turned into narrative), a résumé written in outcomes ("led X, defined success as Y, shipped Z"), and the **30/60/90** — 30 days learning the business and users, 60 days owning a feature end-to-end, 90 days driving a measured outcome. The 30/60/90 gets you hired because it shows you arrive already doing the job.

**Problem set.** Mock interviews: record yourself answering 10 questions (4 behavioral STAR, 3 product sense, 3 execution). Listen back. Answer the killer question out loud for two minutes.

**Deliverable.** `portfolio/star-stories.md`, `portfolio/resume.md`, `portfolio/90-day-plan.md` — then sit the **Final** (*exams.md*).

**Self-assessment.** ☐ I can answer "should this feature use AI?" with a framework in 2 minutes ☐ 3 STAR stories ending in numbers ☐ I can explain the capstone in 2 minutes ☐ My 90-day plan fits on one page.

---

# APPENDIX A — Reading packet

**Papers (all free, all verified August 2026; read the assigned portions only — you are a PM, not a researcher):**
1. Vaswani et al. (2017). *Attention Is All You Need*. arXiv:1706.03762 — [link](https://arxiv.org/abs/1706.03762)
2. Brown et al. (2020). *Language Models are Few-Shot Learners* (GPT-3). arXiv:2005.14165 — [link](https://arxiv.org/abs/2005.14165)
3. Lewis et al. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. arXiv:2005.11401 — [link](https://arxiv.org/abs/2005.11401)
4. Liu et al. (2023). *Lost in the Middle: How Language Models Use Long Contexts*. arXiv:2307.03172 — [link](https://arxiv.org/abs/2307.03172)
5. Chen et al. (2021). *Evaluating Large Language Models Trained on Code* (Codex/HumanEval). arXiv:2107.03374 — [link](https://arxiv.org/abs/2107.03374)
6. Wilson & Daugherty (2018). *Collaborative Intelligence: Humans and AI Are Joining Forces*. Harvard Business Review, July–August 2018 — [link](https://hbr.org/2018/07/collaborative-intelligence-humans-and-ai-are-joining-forces) (summary free; PDF gated)

**Video lectures:**
- Karpathy, *Intro to Large Language Models* — [YouTube](https://www.youtube.com/watch?v=zjkBMFhNj_g)
- 3Blue1Brown, *Neural networks* and *Attention in transformers* — [3blue1brown.com/lessons](https://www.3blue1brown.com/lessons/)
- DeepLearning.AI short courses (free): *ChatGPT Prompt Engineering for Developers*, *AI Prompting for Everyone* — [deeplearning.ai/courses](https://www.deeplearning.ai/courses)

**Practitioner canon (free):**
- Simon Willison's blog — [simonwillison.net](https://simonwillison.net)
- Anthropic, *Building effective agents* — [anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents)
- Wolfram, *What Is ChatGPT Doing… and Why Does It Work?* — [writings.stephenwolfram.com](https://writings.stephenwolfram.com/2023/02/what-is-chatgpt-doing-and-why-does-it-work)
- Lenny's Newsletter — [lennysnewsletter.com](https://lennysnewsletter.com)
- First Round Review — [firstround.com/review](https://firstround.com/review)
- Kaggle Learn (Python, Intro to ML) — [kaggle.com/learn](https://www.kaggle.com/learn)

**Case sources (primary, for *case-packets.md*):**
- Intercom Fin launch post — [intercom.com/blog](https://www.intercom.com/blog/announcing-intercoms-new-ai-chatbot/)
- Intercom × Anthropic × AWS case study — [aws.amazon.com/solutions/case-studies/intercom-anthropic](https://aws.amazon.com/solutions/case-studies/intercom-anthropic/)
- GitHub research, *Quantifying Copilot's impact* — [github.blog](https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness)
- OpenAI customer story, *Klarna's AI assistant* — [openai.com/index/klarna](https://openai.com/index/klarna/)
- Klarna press release — [klarna.com/international/press](https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/)

**Books (the entire materials budget, <$50):** see Appendix D.

**Newsletters (free):** The Batch (deeplearning.ai) · Lenny's Newsletter · Simon Willison (RSS).

---

# APPENDIX B — Examined deliverable checklist

Every deliverable is examinable; the five starred ones carry the most weight in interviews and in the final. All must be linked from `portfolio/README.md`:

- [ ] M1 Skill map & portfolio system
- [ ] M2 "AI 101" explainer
- [ ] M3 Prompt library (15+)
- [ ] M4 RAG bot + architecture write-up
- [ ] M5 Python scripts + API README
- [ ] M6 Eval suite + report ★
- [ ] M7 Discovery notes
- [ ] M8 PRD v1
- [ ] M9 RICE + roadmap + won't-do
- [ ] M10 Metrics tree
- [ ] M11 Sprint plan + DoD
- [ ] M12 Feasibility drill + template ★
- [ ] M13 Data plan
- [ ] M14 Production eval plan ★
- [ ] M15 Cost & latency model ★
- [ ] M16 Risk register + GTM one-pager
- [ ] M17 Capstone brief + PRD v2
- [ ] M18 Capstone + eval report ★
- [ ] M19 Case study + demo + index
- [ ] M20 STAR stories + résumé + 30/60/90
- [ ] Case memos 1–4 (1 page each)
- [ ] Midterm (exams.md)
- [ ] Final: thesis + defense (exams.md)

---

# APPENDIX C — Key terms (examinable)

**AI literacy (Modules 2–6):** model · LLM · token · context window · training · inference · fine-tuning · prompt (system/user/few-shot) · temperature · hallucination · RAG · embedding · vector database · agent · eval · golden set · LLM-as-judge · precision/recall · accuracy trap · latency · throughput · structured output · tool use · distillation · benchmark · RLHF · jailbreak · capability vs. reliability

**PM craft (Modules 7–11):** double diamond · JTBD · discovery · Mom Test · PRD · user story · acceptance criteria · out-of-scope · RICE · MoSCoW · roadmap themes · north star · guardrail metric · funnel · activation · retention · instrumentation · A/B test · sprint · standup · retro · definition of done

**AI PM craft (Modules 12–16):** feasibility · human-in-the-loop · composable architecture · parametric vs. non-parametric memory · data flywheel · PII · GDPR · EU AI Act · model drift · regression gate · feedback loop · cost per interaction · token economics · caching · model tiers · prompt injection · bias · risk register · positioning · usage-based pricing · outcome pricing

---

# APPENDIX D — The book budget (<$50)

1. **The Mom Test** (Fitzpatrick, used ~$10) — Module 7. Smallest, highest-leverage book in the course.
2. **Cracking the PM Interview** (McDowell & Bavaro, used ~$15) — Modules 1, 20. The frameworks + interview bible.
3. **Inspired** (Cagan, used ~$15) — Modules 7–11. The PM craft canon; read alongside the modules.

Everything else is free. Resist paid courses; the free packet above is what working PMs themselves read.

---

## Closing note

This course teaches a stack that survives model turnover: **judgment about problems, literacy about models, discipline about measurement, and courage about risk.** The models will be replaced annually; the PM won't be. Sit the midterm honestly, defend the capstone proudly, and treat every "A" as provisional until an external reviewer agrees.

*— PROD 260 syllabus, built August 2026 from a two-round interview with the student. Re-verify Appendix A annually.*
