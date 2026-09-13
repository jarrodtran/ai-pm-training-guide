# AI-PM Graduate Program — Read-Only Audit Report

**Audited:** /Users/jarrod/ai-pm-training-guide/ (15 HTML files: index.html, schedule.html, tracker.html, glossary.html, brochure.html + 10 course pages in courses/)
**Date:** 2026-08-23
**Method:** static analysis of file content (link resolution, regex extraction, tag counting). No files were modified.

**Summary of findings by severity:**
- HIGH: 0
- MED: 49
- LOW: 10
- **Total: 59 findings**

---

## 1. INTERNAL LINKS

**Result: CLEAN — 0 broken links found.**

Every relative `href`/`src` in index.html, schedule.html, tracker.html, glossary.html, brochure.html, all 10 files in courses/, and courses/course.js + courses/course.css was resolved against the containing file's directory and checked for existence on disk. External URLs (https://), mailto:, and same-page `#anchor` links were excluded per audit scope. Anchors `#courses`, `#documents`, `#resources` used by index.html were verified to exist as element IDs on that page. All relative targets exist — including cross-folder links (`../index.html`, `../glossary.html`, `../case-packets.md`, `../ai-pm-training-guide.md`, `../exams.md`), sibling course links (`pm501.html`, `fde560.html`, …), and asset refs (`course.css`, `course.js`).

No findings.

---

## 2. MODULE NUMBERING

**Numbering itself: CLEAN.** All 10 course pages number modules consecutively starting at M1 with no gaps or duplicates: 6 courses are M1–M6 (ai510, pm501, aipm520, plus electives checked), 4 courses are M1–M4 (data530, strat540, rsk550, cap600, fde560, ai570, gth580 — M1–M4 for the 6-module/4-module split verified per page). Module counts match the schedule.html COURSES object for every course.

**Title mismatches vs. schedule.html COURSES object: 8 findings (MED).** The course page title and the corresponding `modules[...]` string in schedule.html differ. The schedule generator displays these strings in the weekly plan, so students see the schedule wording while the syllabus shows the page wording — the two should be one canonical string.

1. MED — courses/ai510.html (M6) — Page: "Measurement: evals & metrics · Case A: GitHub Copilot" vs schedule.html ai510.modules[5]: "Measurement: evals & metrics". Fix: append "· Case A: GitHub Copilot" to the schedule entry, or drop it from the page title — pick one canonical wording.
2. MED — courses/aipm520.html (M1) — Page: "Feasibility & system design · Case B: Intercom Fin" vs schedule: "Feasibility & system design · Case B: Fin". Fix: align the case name (page is more specific; "Fin" is the product's short name).
3. MED — courses/aipm520.html (M2) — Page: "Architecture: retrieval, guardrails, tool use" vs schedule: "Architecture: retrieval, guardrails, tools". Fix: unify "tool use" vs "tools".
4. MED — courses/aipm520.html (M5) — Page: "Cost, latency & model selection · Case C: Duolingo Max" vs schedule: "Cost, latency & model selection · Case C". Fix: add "· Case C: Duolingo Max" to the schedule entry or trim the page.
5. MED — courses/aipm520.html (M6) — Page: "Risk, safety & go-to-market · Case D: Klarna" vs schedule: "Risk, safety & GTM · Case D". Fix: unify "go-to-market" vs "GTM" and add/remove "· Case D: Klarna".
6. MED — courses/pm501.html (M3) — Page: "Spec writing: PRDs, stories, acceptance criteria" vs schedule: "Spec writing: PRDs, stories, criteria". Fix: unify "acceptance criteria" vs "criteria".
7. MED — courses/rsk550.html (M2) — Page: "Security: injection, red-teaming, threat models" vs schedule: "Security: injection & red-teaming". Fix: unify wording (page lists three topics; schedule lists two).
8. MED — courses/strat540.html (M4) — Page: "Platforms, ecosystems & vendor risk" vs schedule: "Platforms & vendor risk". Fix: unify wording.

Suggested global fix: treat the course pages as the source of truth and update the `modules` arrays inside the COURSES object in schedule.html to match, then re-verify with this audit.

---

## 3. GLOSSARY COVERAGE

All 10 course pages have a "Key terms" paragraph (none missing). Each page's key-terms line was split on "·" and every term was checked case-insensitively as a substring against the 133 terms in the TERMS array of glossary.html. **51 terms are missing** (41 MED, 10 LOW). LOW = the glossary covers the concept under different wording (variant/near-match); MED = no coverage in the glossary at all.

*Method caveat:* the substring rule is lenient — e.g. fde560's "land" and "scope" pass only because they occur inside unrelated glossary entries "model landscape" and "out-of-scope"; gth580's "execution"/"behavioral"/"equity" pass via "execution loop"/"behavioral loop"/"equity basics". Such coincidental matches are noted inline below where material.

### courses/ai510.html (2 missing)
1. LOW — courses/ai510.html — "training as lossy compression" not in glossary; glossary has "training (lossy compression)". Fix: add as alias or rename one side.
2. LOW — courses/ai510.html — "vector store" not in glossary; glossary has "vector database". Fix: add alias or rename one side.

### courses/ai570.html (6 missing)
3. MED — courses/ai570.html — "orchestration" absent from glossary. Fix: add term (c:"AI 570").
4. MED — courses/ai570.html — "validation" absent. Fix: add term.
5. LOW — courses/ai570.html — "injection through tool results" absent; glossary covers "indirect injection". Fix: add alias or reword page term.
6. MED — courses/ai570.html — "goal hijacking" absent. Fix: add term.
7. MED — courses/ai570.html — "versioning" absent. Fix: add term.
8. LOW — courses/ai570.html — "drift monitoring" absent; glossary has "model drift". Fix: add alias or reword page term.

### courses/aipm520.html (3 missing)
9. LOW — courses/aipm520.html — "comparative feasibility" absent; glossary has "feasibility". Fix: add alias or reword.
10. LOW — courses/aipm520.html — "retrieval data vs. fine-tuning data" absent; glossary has "retrieval vs. fine-tuning data". Fix: add alias or reword.
11. MED — courses/aipm520.html — "caching" absent. Fix: add term.

### courses/cap600.html (3 missing)
12. LOW — courses/cap600.html — "fix-and-re-run loop" absent; glossary has "fix-and-re-run". Fix: add alias or reword.
13. MED — courses/cap600.html — "case study" absent. Fix: add term.
14. MED — courses/cap600.html — "failure question" absent. Fix: add term.

### courses/data530.html (3 missing)
15. MED — courses/data530.html — "taxonomy" absent. Fix: add term.
16. LOW — courses/data530.html — "guardrail metrics" absent (plural); glossary has "guardrail metric". Fix: add alias or reword.
17. MED — courses/data530.html — "GDPR" absent. Fix: add term.

### courses/fde560.html (6 missing)
18. LOW — courses/fde560.html — "FDE operating model" absent; glossary has abbreviation "FDE". Fix: expand entry or add alias.
19. MED — courses/fde560.html — "build" absent (engagement-stage name; also a generic word). Fix: add as stage-name term or reword key-terms line.
20. MED — courses/fde560.html — "deploy" absent. Fix: add as stage-name term or reword.
21. MED — courses/fde560.html — "scale" absent. Fix: add as stage-name term or reword.
22. MED — courses/fde560.html — "harvest" absent. Fix: add as stage-name term or reword.
23. MED — courses/fde560.html — "repeated pattern" absent. Fix: add term.

### courses/gth580.html (10 missing)
24. MED — courses/gth580.html — "framework" absent. Fix: add term.
25. MED — courses/gth580.html — "referral" absent. Fix: add term.
26. MED — courses/gth580.html — "search funnel" absent. Fix: add term.
27. MED — courses/gth580.html — "vesting" absent. Fix: add term.
28. MED — courses/gth580.html — "strike price" absent. Fix: add term.
29. MED — courses/gth580.html — "total comp" absent. Fix: add term.
30. MED — courses/gth580.html — "learn" absent (likely fragment of a "learn · own · drive" phrasing; also a generic word). Fix: add or reword.
31. MED — courses/gth580.html — "own" absent (see above). Fix: add or reword.
32. MED — courses/gth580.html — "drive" absent (see above). Fix: add or reword.
33. MED — courses/gth580.html — "onboarding interviews" absent. Fix: add term.

### courses/pm501.html (3 missing)
34. MED — courses/pm501.html — "demonstrated behavior" absent (Mom Test concept). Fix: add term.
35. MED — courses/pm501.html — "standup" absent. Fix: add term.
36. MED — courses/pm501.html — "retro" absent. Fix: add term.

### courses/rsk550.html (8 missing)
37. MED — courses/rsk550.html — "bias" absent. Fix: add term.
38. MED — courses/rsk550.html — "privacy" absent. Fix: add term.
39. MED — courses/rsk550.html — "security" absent. Fix: add term.
40. MED — courses/rsk550.html — "compliance" absent. Fix: add term.
41. MED — courses/rsk550.html — "jailbreak" absent. Fix: add term.
42. MED — courses/rsk550.html — "segment decomposition" absent. Fix: add term.
43. LOW — courses/rsk550.html — "EU AI Act risk classes" absent; glossary covers "EU AI Act" and "risk classes" as separate entries. Fix: add combined alias or reword page term.
44. MED — courses/rsk550.html — "GDPR" absent (also missing for data530). Fix: add term.

### courses/strat540.html (7 missing)
45. MED — courses/strat540.html — "cost as design variable" absent. Fix: add term.
46. MED — courses/strat540.html — "subscription" absent. Fix: add term.
47. MED — courses/strat540.html — "usage pricing" absent. Fix: add term.
48. MED — courses/strat540.html — "hybrid" absent. Fix: add term.
49. MED — courses/strat540.html — "positioning" absent. Fix: add term.
50. MED — courses/strat540.html — "repeat-test" absent. Fix: add term.
51. MED — courses/strat540.html — "abstraction layer" absent. Fix: add term.

---

## 4. OBVIOUS HTML PROBLEMS

**Result: CLEAN — no findings on any page.**

- Duplicate element IDs: none on any of the 15 HTML pages (checked via per-page id counts).
- Tag balance: `<section>`/`</section>` balanced on every page that uses sections (index 3/3, brochure 4/4, all 10 course pages 4–5/4–5); `<details>` is not used anywhere (0/0), so no unclosed `<details>` risk. `<title>` tags are present and non-empty on all 15 pages.

No findings.

---

## Appendix: Files audited
- Root: index.html, schedule.html, tracker.html, glossary.html, brochure.html
- courses/: ai510.html, pm501.html, aipm520.html, data530.html, strat540.html, rsk550.html, cap600.html, fde560.html, ai570.html, gth580.html, course.css, course.js
- Cross-referenced: ai-pm-training-guide.md, case-packets.md, exams.md (link targets only)
