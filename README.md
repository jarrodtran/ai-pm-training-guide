# AI-PM Training Guide

A self-paced program in AI product management — course syllabi, case packets, an exam book, and a technical field manual for forward-deployed product work.

**Start here:** open [`index.html`](index.html) in a browser.

## Contents

| Path | What it is |
|---|---|
| `index.html` | Program hub — courses, documents, resources |
| `field-manual.html` | **FDE-PM Field Manual** — HTML edition |
| `fde-pm-field-manual.md` | Field manual source: 5 modules, ~90 hours, 17 blueprints |
| `courses/` | Ten course syllabi — AI 510 → CAP 600, plus electives |
| `ai-pm-training-guide.md` | Master syllabus — 20 modules |
| `case-packets.md` | Four case studies with exhibits and teaching notes |
| `exams.md` | Midterm, capstone thesis, defense, rubrics |
| `templates/` | 21 fill-in-the-blank templates for the program's deliverables |
| `glossary.html` | Searchable glossary, tagged by course |
| `schedule.html` | Generates a dated week-by-week schedule |
| `tracker.html` | Progress tracker (saved in the browser) |
| `interview-bank.md` | Interview questions, each mapped to the course that builds the answer |
| `audit-report.md` | Read-only audit of the program files |
| `tools/` | Build and verification scripts |

## The field manual

Markdown is the source of truth; the HTML edition is generated from it.

```bash
python3 tools/build_field_manual_html.py   # render field-manual.html from the markdown
python3 tools/check_manual.py              # verify local links, count reference URLs
python3 tools/verify_links.py              # check reference URLs (batch 1)
python3 tools/verify_links2.py             # check reference URLs (batch 2)
```

Requires `markdown` (`pip install markdown`).

## Notes

- Personal, self-paced reference — no assessments, no grading, nothing to submit.
- Every external reference in the field manual was verified by direct fetch; the method and status per URL are recorded in Appendix B of the manual.
- All pages are self-contained HTML with no build step and no external dependencies.
