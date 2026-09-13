# Feasibility Template

Fill-in-the-blank template for the AIPM 520 feasibility drill (5 cases) and the FDE 560 client feasibility memo (one page, client-room ready). Comparative feasibility is the AI PM's signature judgment: **AI vs. a rules-based system vs. a human vs. nothing**, scored on input/output clarity, error tolerance, data availability, cost per interaction, and latency.

---

## Part 1 — The 5-Case Feasibility Drill

Pick 5 product ideas: **3 real, 2 deliberately bad** (an "AI-powered toaster" is a gimmick with a transformer inside — include one or two of those on purpose, so the class learns to say no). Fill one row per idea. Be concrete: if you cannot write the input and output as definite types, the case fails the drill.

| # | Idea | What AI would do | Input / Output | Error tolerance | Data needs | Cost | Non-AI alternative |
|---|---|---|---|---|---|---|---|
| 1 | [IDEA — ONE-LINE DESCRIPTION] | [TASK THE MODEL WOULD PERFORM] | [INPUT: e.g. free-text query → OUTPUT: e.g. structured reply + source links] | [WHAT HAPPENS WHEN IT IS WRONG — is that acceptable, and why?] | [WHAT DATA EXISTS / WHAT IS MISSING] | [ESTIMATE COST PER INTERACTION] | [RULES / HUMAN / NOTHING — and why that alternative wins or loses] |
| 2 | [IDEA — ONE-LINE DESCRIPTION] | [TASK THE MODEL WOULD PERFORM] | [INPUT → OUTPUT] | [WHAT HAPPENS WHEN IT IS WRONG] | [DATA EXISTS / MISSING] | [ESTIMATE COST PER INTERACTION] | [RULES / HUMAN / NOTHING — and why] |
| 3 | [IDEA — ONE-LINE DESCRIPTION] | [TASK THE MODEL WOULD PERFORM] | [INPUT → OUTPUT] | [WHAT HAPPENS WHEN IT IS WRONG] | [DATA EXISTS / MISSING] | [ESTIMATE COST PER INTERACTION] | [RULES / HUMAN / NOTHING — and why] |
| 4 | [IDEA — ONE-LINE DESCRIPTION — make this one deliberately bad] | [TASK THE MODEL WOULD PERFORM] | [INPUT → OUTPUT] | [WHAT HAPPENS WHEN IT IS WRONG] | [DATA EXISTS / MISSING] | [ESTIMATE COST PER INTERACTION] | [RULES / HUMAN / NOTHING — and why] |
| 5 | [IDEA — ONE-LINE DESCRIPTION — make this one deliberately bad] | [TASK THE MODEL WOULD PERFORM] | [INPUT → OUTPUT] | [WHAT HAPPENS WHEN IT IS WRONG] | [DATA EXISTS / MISSING] | [ESTIMATE COST PER INTERACTION] | [RULES / HUMAN / NOTHING — and why] |

**Verdict per case** (write below each row or in a notes column):

- AI wins when the task is **high-volume, language-shaped, and error-tolerant**.
- AI loses when answers must be **deterministic**, when the **cost of being wrong is catastrophic**, or when the problem is actually **about process, not intelligence**.

**Worked example** (model answer, for calibration — delete before submitting):

| — | AI-powered toaster | Vision model classifies bread doneness and adjusts heating | INPUT: camera frame → OUTPUT: heat-level adjustment | Wrong = burnt or raw toast; low stakes, retryable | Labeled toast images — don't exist, expensive to collect per appliance | High: camera + model per unit | A timer costs $0.50 and never fails. Verdict: **AI loses** — process, not intelligence. |

---

## Part 2 — One-Page Client Feasibility Memo (FDE 560)

Reusable template for client work. Written **before the SOW** so expectations are set before the price is. Usable in a client room as-is. One page.

**Memo for:** [CLIENT — NAME] · **Prepared by:** [YOU — NAME] · **Date:** [DATE]

### 1. The problem
[THE ACTUAL PROBLEM BEHIND THE ASK — not the ask itself. "We want an AI assistant" is a request; the problem is the thing it costs the client money to do today. **Quantify it with client numbers:** volume, time spent, error rate, cost per incident. If you cannot write the number, discovery is not done.]

### 2. The AI-vs-alternative judgment
[COMPARATIVE FEASIBILITY, ARGUED: AI vs. a rules-based system vs. a human vs. nothing — with the client's numbers attached. Score input/output clarity, error tolerance, data availability, cost per interaction, and latency. State the verdict plainly: AI is the right instrument here because ___, or AI is not the right instrument because ___. Say no in the room, with the evidence, when that is the honest answer — the no is the deliverable that builds trust.]

### 3. What AI will and will not do
- **Will do:** [SCOPE — THE TASKS THE SYSTEM HANDLES, EACH STATED AS INPUT → OUTPUT, WITH THE SOURCE OF TRUTH (e.g. retrieval over the client's docs, never the model's memory)]
- **Will not do:** [EXPLICIT WON'T-LIST — DETERMINISTIC ACTIONS, HIGH-STAKES DECISIONS, OUT-OF-VOCABULARY TOPICS, ANYTHING THAT NEEDS A HUMAN. If this list is empty, the scope is not defined.]

### 4. Risks
[THE RISKS THAT MATTER FOR THIS CLIENT, EACH WITH A DETECTION MECHANISM — hallucination, bias, privacy (PII), security, compliance. "We mitigate hallucinations with retrieval" is a plan; "we sample 2% of sessions weekly against the golden set" is a system. Name the risk, the mitigation, and how you will know it is happening.]

**Recommended next step:** [SCOPE THE ENGAGEMENT / SOW / KILL THE DEAL — WITH THE REASON]

---

## Done when

- [ ] All 5 drill rows are filled; 2 of the 5 are deliberately bad ideas, and each row states a verdict (AI wins / loses) with the reason
- [ ] Every input and output is written as a concrete type (no "intelligent answers")
- [ ] The client memo is one page, fits the client room, and quantifies the problem with client numbers
- [ ] "What AI will not do" has at least one line, and the AI-vs-alternative judgment names the loser (rules / human / nothing) and why
- [ ] Risks each have a detection mechanism, not just a mitigation
- [ ] The memo is written before any SOW is discussed
