# AI-PM Training Guide

**Live site:** https://jarrodtran.github.io/ai-pm-training-guide/

A self-paced program in AI product management — course syllabi, case packets, an exam book, and a technical field manual for forward-deployed product work.

Open [`index.html`](index.html) locally, or browse the published site.

## Contents

| Path | What it is |
|---|---|
| `index.html` | Program hub — courses, documents, resources |
| `field-manual.html` | **FDE-PM Field Manual** — 5 modules, 17 blueprints |
| `ai-pm-training-guide.html` | Master syllabus — 20 modules |
| `case-packets.html` | Four case studies with exhibits and teaching notes |
| `exams.html` | Midterm, capstone thesis, defense, rubrics |
| `interview-bank.html` | Interview questions, each mapped to the course that builds the answer |
| `answer-guide.html` | Midterm answer guide and worked models |
| `audit-report.html` | Read-only audit of the program files |
| `templates/index.html` | Template library — 21 fill-in-the-blank templates |
| `courses/` | Ten course syllabi — AI 510 → CAP 600, plus electives |
| `glossary.html` | Searchable glossary, tagged by course |
| `schedule.html` | Generates a dated week-by-week schedule |
| `tracker.html` | Progress tracker (saved in the browser) |
| `assets/apple.css` | The design system, inlined into every page at build time |
| `tools/` | Build and verification scripts |

Markdown is the source of truth; each `*.md` sits beside its rendered `*.html`.

## Building

Every page is self-contained — CSS is inlined and there are no external
dependencies, so the site works offline and needs nothing at runtime.

```bash
python3 tools/build_field_manual_html.py   # field-manual.html from fde-pm-field-manual.md
python3 tools/build_docs.py                # the seven rendered documents
python3 tools/rewrite_doc_links.py         # point hub/course links at rendered pages
python3 tools/check_manual.py              # verify local links, count reference URLs
python3 tools/verify_links.py              # check reference URLs (batch 1)
python3 tools/verify_links2.py             # check reference URLs (batch 2)
```

Requires `markdown` (`pip install markdown`).

## Notes

- Personal, self-paced reference — no assessments, no grading, nothing to submit.
- Every external reference in the field manual was verified by direct fetch; the method and status for each URL are recorded in Appendix B of the manual.
- `assets/apple.css` is the single source of truth for the design; each builder inlines it so the output stays a standalone file.
