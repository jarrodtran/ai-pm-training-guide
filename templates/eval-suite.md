# Eval Suite Template — 25-Case Golden Set

Fill-in-the-blank template for the AIPM 520 production eval system (M4). The golden set is the fixed set of cases that **never changes**, so you can compare across model versions and catch regressions. A golden set that grows without discipline stops being a golden set.

**Product / feature:** [NAME — WHAT IS BEING EVALUATED]
**Model version under test:** [MODEL + VERSION]
**Set version:** [v1.0 — BUMP ONLY WHEN CASES ARE ADDED OR REWRITTEN, NEVER SILENTLY]
**Curator / owner:** [NAME — ONE PERSON OWNS THE SET]

---

## 1. The 25 Cases

Category mix to aim for: **~12 easy, ~6 edge, ~4 adversarial, ~3 out-of-scope** (adjust deliberately, and say why in the notes). Fill 25 rows. "Expected behavior" is the pass condition — write it so that a human and an LLM-as-judge would agree on it.

| # | Category (easy / edge / adversarial / out-of-scope) | Case | Expected behavior | Pass / Fail |
|---|---|---|---|---|
| 1 | [CATEGORY] | [THE EXACT INPUT — QUOTE IT] | [THE EXACT OUTPUT BEHAVIOR THAT COUNTS AS CORRECT] | [PASS / FAIL] |
| 2 | [CATEGORY] | [THE EXACT INPUT] | [EXPECTED BEHAVIOR] | [PASS / FAIL] |
| 3 | [CATEGORY] | [THE EXACT INPUT] | [EXPECTED BEHAVIOR] | [PASS / FAIL] |
| 4 | [CATEGORY] | [THE EXACT INPUT] | [EXPECTED BEHAVIOR] | [PASS / FAIL] |
| 5 | [CATEGORY] | [THE EXACT INPUT] | [EXPECTED BEHAVIOR] | [PASS / FAIL] |
| 6 | [CATEGORY] | [THE EXACT INPUT] | [EXPECTED BEHAVIOR] | [PASS / FAIL] |
| 7 | [CATEGORY] | [THE EXACT INPUT] | [EXPECTED BEHAVIOR] | [PASS / FAIL] |
| 8 | [CATEGORY] | [THE EXACT INPUT] | [EXPECTED BEHAVIOR] | [PASS / FAIL] |
| 9 | [CATEGORY] | [THE EXACT INPUT] | [EXPECTED BEHAVIOR] | [PASS / FAIL] |
| 10 | [CATEGORY] | [THE EXACT INPUT] | [EXPECTED BEHAVIOR] | [PASS / FAIL] |
| 11 | [CATEGORY] | [THE EXACT INPUT] | [EXPECTED BEHAVIOR] | [PASS / FAIL] |
| 12 | [CATEGORY] | [THE EXACT INPUT] | [EXPECTED BEHAVIOR] | [PASS / FAIL] |
| 13 | [CATEGORY] | [THE EXACT INPUT] | [EXPECTED BEHAVIOR] | [PASS / FAIL] |
| 14 | [CATEGORY] | [THE EXACT INPUT] | [EXPECTED BEHAVIOR] | [PASS / FAIL] |
| 15 | [CATEGORY] | [THE EXACT INPUT] | [EXPECTED BEHAVIOR] | [PASS / FAIL] |
| 16 | [CATEGORY] | [THE EXACT INPUT] | [EXPECTED BEHAVIOR] | [PASS / FAIL] |
| 17 | [CATEGORY] | [THE EXACT INPUT] | [EXPECTED BEHAVIOR] | [PASS / FAIL] |
| 18 | [CATEGORY] | [THE EXACT INPUT] | [EXPECTED BEHAVIOR] | [PASS / FAIL] |
| 19 | [CATEGORY] | [THE EXACT INPUT] | [EXPECTED BEHAVIOR] | [PASS / FAIL] |
| 20 | [CATEGORY] | [THE EXACT INPUT] | [EXPECTED BEHAVIOR] | [PASS / FAIL] |
| 21 | [CATEGORY] | [THE EXACT INPUT] | [EXPECTED BEHAVIOR] | [PASS / FAIL] |
| 22 | [CATEGORY] | [THE EXACT INPUT] | [EXPECTED BEHAVIOR] | [PASS / FAIL] |
| 23 | [CATEGORY] | [THE EXACT INPUT] | [EXPECTED BEHAVIOR] | [PASS / FAIL] |
| 24 | [CATEGORY] | [THE EXACT INPUT] | [EXPECTED BEHAVIOR] | [PASS / FAIL] |
| 25 | [CATEGORY] | [THE EXACT INPUT] | [EXPECTED BEHAVIOR] | [PASS / FAIL] |

**Notes on the mix:** [WHY THESE CATEGORY COUNTS — AND WHICH CASE IS THE ONE YOU MOST EXPECT TO FAIL]

---

## 2. Scoring Method

- **Score:** [NUMBER OF PASSES] / 25 = **___% pass rate**. A case passes only if the actual behavior matches the expected behavior; partial credit is a decision, not a default — if you use it, define it here: [PARTIAL CREDIT RULE — e.g. "0.5 for correct intent with a wrong format"]
- **Who scores:** [HUMAN REVIEW / LLM-AS-JUDGE] for [WHICH SLICES — e.g. "humans score the adversarial set; LLM-as-judge scores easy + edge at volume"]. Judges have biases too — see the spot-check note in `production-eval-plan.md`.
- **Per-category floor:** the overall pass rate is not enough; a model can ace the easy set and fail the adversarial set. Report the pass rate **per category** and hold each to its floor (below).

## 3. Regression Gate

> **We do not ship a version scoring below ___% overall** on the golden set, and we do not ship a version scoring below ___% on the adversarial category (floor), ___% on the edge category (floor), or ___% on the out-of-scope category (floor — where the requirement is usually that the system refuse or escalate, not answer).

The gate is the mechanism that turns evals into governance. Numbers must be written before the version under test is picked — the gate is not negotiable after a demo looks good. "It worked in the demo" is not "it works in production": the demo is a single sample; production is a distribution.

---

## Done when

- [ ] All 25 cases are filled with quoted inputs and behavior-level expected outputs
- [ ] Every case has a category from the four (easy / edge / adversarial / out-of-scope), and the mix is deliberate
- [ ] At least 4 adversarial and 3 out-of-scope cases exist (the sets where models actually fail)
- [ ] Scoring method is defined, including who scores which slice and any partial-credit rule
- [ ] The regression gate sentence is completed with numbers — overall floor plus per-category floors
- [ ] One owner is named for the set, and the version is stamped
