# PROD 260 — Exam Book

Take-home examinations, rubrics, and grading protocol. All exams are self-graded under the course honor code (see the program guide): complete them in the stated time, with only the allowed materials, and grade yourself honestly. If you cannot defend an answer out loud, it does not count.

**Structure of examination in this program:**
- **Course finals** — every course in the program has a take-home final (~2 hours) specified at the bottom of its syllabus page (courses/). Open-book: the syllabus, your portfolio, the allowed readings.
- **Program midterm** — a cross-course integration exam, sat after Term 2 (after DATA 530). Below.
- **Answer guide** — after writing your midterm answers, grade yourself against the frameworks and the worked RICE model answer in `answer-guide.md` (same folder). Your Q3 ranking must match its arithmetic exactly; your judgment calls may differ only with a defended reason.
- **Final: capstone thesis & defense** — sat after Term 4. Below.

---

# PROGRAM MIDTERM EXAMINATION

**Sits after Term 2 (after DATA 530). Time: ~3 hours, take-home. Open-book: this program's syllabi, your portfolio, the case packets. No web research beyond pricing/API docs.**

Answer all three questions. Each answer: 500–700 words. Grade per the rubric at the end of this section.

---

## Question 1 — Design (product sense)

**Scenario.** FieldService Co., a 4,000-employee HVAC and appliance repair company, has 250 field technicians. Their internal support line fields ~2,000 calls/week from technicians needing: part compatibility checks, warranty status, safety procedures, and "how do I fix X" guidance. Calls average 9 minutes; the 12-person support desk is backlogged; technician wait times run 15–40 minutes, and technicians bill by the job.

The VP of Operations wants an AI assistant for the technicians. The CEO has asked you — the AI PM — for a recommendation.

**Your task.** Design the feature. Cover, explicitly: (1) the problem and who it serves (evidence you'd want before building); (2) a feasibility judgment — what the AI should and should not do, and where rules or humans stay in the loop; (3) the success metrics (north star + 3 guardrails, including model-quality metrics); (4) the evaluation design you'd stand up before and after launch; (5) the top 3 risks and how you'd detect each. You may make reasonable assumptions about the domain — state them.

**Grading weight: 35% of midterm.**

---

## Question 2 — Measurement (data & metrics)

**Scenario.** Six months after launch, your support bot resolves 60% of conversations and executives are celebrating. Your own data says something else: (1) the reported "accuracy" on the internal dashboard is 94%, computed as the share of bot responses that received no explicit thumbs-down; (2) only 8% of users rate responses at all; (3) repeat-contact rate is up 12% since launch; (4) sentiment analysis on open-ended feedback shows rising frustration with "the bot's confident wrong answers"; (5) the 60% "resolution" figure counts a conversation resolved when the user stops replying — including users who gave up.

**Your task.** Diagnose the measurement failure and fix it. (1) Identify at least three ways the current metrics mislead, with the specific mechanism of each (e.g., selection bias in the rating sample). (2) Redefine the measurement system: what is the real north star for this feature, what are the guardrails, and what instrumentation would you add? (3) Explain how you would communicate the corrected picture to the executives without losing credibility.

**Grading weight: 35% of midterm.**

---

## Question 3 — Prioritization (judgment)

**Scenario.** Your company's AI copilot for accountants has 10,000 paying customers. Candidates for the next quarter (RICE inputs estimated with your team):

| # | Feature | Reach (users/quarter) | Impact (0–3) | Confidence (0–100%) | Effort (person-weeks) |
|---|---|---|---|---|---|
| A | Multi-entity support | 4,000 | 3 | 70% | 8 |
| B | Voice dictation of notes | 6,000 | 1 | 60% | 4 |
| C | AI audit-trail export | 1,500 | 3 | 40% | 12 |
| D | Fix hallucination on tax codes (quality) | 10,000 | 3 | 90% | 3 |
| E | Mobile companion app | 7,000 | 2 | 50% | 20 |
| F | Bulk import from Excel | 5,000 | 2 | 80% | 2 |

**Your task.** (1) Compute RICE for all six (show the arithmetic). (2) Rank, and build a quarter roadmap as themes, not features. (3) Pick the single feature you would *not* ship even if the score says otherwise, and defend that call — consider the AI-specific risks (quality, trust, cost). (4) State the "won't do" list with reasons.

**Grading weight: 30% of midterm.**

---

## Midterm rubric

| Dimension | A | B | C |
|---|---|---|---|
| Framework use | Applies course frameworks precisely (feasibility, guardrails, RICE, risk) | Frameworks present, imprecise | Frameworks absent |
| Numbers | Correct arithmetic; metrics critiqued with mechanisms, not vibes | Mostly correct | Errors or hand-waving |
| Judgment | Takes positions; AI-specific risks addressed; assumptions stated | Position soft | No position |
| Communication | Answer could be shown to an exec as-is | Needs editing | Rambling |

---

# FINAL EXAMINATION — Capstone Thesis & Defense

**Sits after Term 4 (CAP 600). Weight: 30% of program grade. Structure: written thesis + recorded defense + portfolio review.**

---

## Part 1 — Written thesis (10–12 pages)

A proper thesis makes the case that you can run an AI product end-to-end. Structure (each section cites the corresponding portfolio artifact):

1. **Problem & evidence** (1–2 pp) — the problem, who it serves, and the discovery evidence. A stranger must believe the problem is real before you mention AI.
2. **Product design** (1–2 pp) — users, scope in/out, success metrics, PRD v2.
3. **Feasibility & architecture** (1–2 pp) — why AI, why this shape (retrieval, guardrails, human-in-the-loop), and the alternative you rejected.
4. **Evaluation** (2 pp) — the golden set, scoring method, results before/after, failure analysis, drift plan. Include your eval report's headline numbers.
5. **Economics** (1 p) — cost per interaction, monthly model, tiering/caching decisions, sensitivity.
6. **Risk & responsible AI** (1–2 pp) — the risk register with detection mechanisms; the worst case and your mitigation.
7. **Retrospective** (1 p) — what you'd do differently; what you'd do with two more weeks; what this taught you about AI product management.
8. **AI-use declaration** — what AI wrote, what you rewrote, and your defense of every claim.

## Part 2 — Recorded defense (15 minutes)

Record a 15-minute presentation (Loom or screen recording): 5 minutes on the problem and design, 5 on the evaluation and numbers, 5 on risks and what you'd do next. Then answer these five questions out loud, on the recording:

1. "Walk me through how you decided this feature should use AI — and what would have disqualified it."
2. "How do you know it's working? Show me the numbers and the failure cases."
3. "What is the most likely way this product fails in production, and how would you detect it?"
4. "If compute costs doubled, what would you do?"
5. "What did you get wrong, and what did you learn from it?"

## Part 3 — Portfolio review

Submit the portfolio index. The five starred artifacts in the master syllabus (eval suite, feasibility framework, production eval plan, cost model, capstone eval report) are graded for external comprehensibility: *could a stranger understand each without you in the room?* The external reviewer's read (CAP 600 M3) is incorporated here.

---

## Final rubric

| Dimension | A | B | C |
|---|---|---|---|
| Problem & evidence | Real problem, cited evidence, AI earns its place | Problem real, evidence thin | AI-first, problem afterthought |
| Evaluation | Golden set, before/after numbers, honest failure analysis | Eval present, results thin | No measurement |
| Economics | Cost model with tiering and sensitivity | Cost estimate, no depth | No cost math |
| Risk | Register with detection, worst case addressed | Risks listed, no detection | Risk ignored |
| Defense | Frameworked answers, owns mistakes, numbers from memory | Answerable but vague | Defensive or vague |
| External comprehensibility | Stranger understands in 3 minutes | Mostly clear | Requires explanation |

---

# Grading protocol (how to be a fair examiner)

1. **Grade immediately after completing** — memory of effort is freshest; grade the output, not the hours.
2. **Read the rubric dimension by dimension**, not holistically — holistic grading rewards writing quality and punishes honesty about failure, which is backwards for this course.
3. **Be merciless on "evidence."** Any claim without a source in a case memo, or any number in the thesis that isn't traceable to the eval report, drops a full letter band. Fabricating evidence is the one unforgivable error.
4. **Be generous on "judgment."** The goal is a defensible position, not the "right" one — there often isn't one.
5. **Log the score and one sentence of feedback per dimension** in your portfolio tracker — the log is the transcript of your calibration.
6. **An "A" requires external confirmation** (the CAP 600 external reviewer). Until then, the highest honest grade is A−.

*— Exam Book, AI-PM Graduate Program, August 2026.*
