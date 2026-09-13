#!/usr/bin/env python3
"""Point hand-authored pages at the rendered HTML instead of raw markdown."""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent

MAP = {
    "ai-pm-training-guide.md": "ai-pm-training-guide.html",
    "case-packets.md": "case-packets.html",
    "exams.md": "exams.html",
    "interview-bank.md": "interview-bank.html",
    "answer-guide.md": "answer-guide.html",
    "audit-report.md": "audit-report.html",
    "templates/README.md": "templates/index.html",
}

targets = [ROOT / "index.html"] + sorted((ROOT / "courses").glob("*.html"))
total = 0
for path in targets:
    text = path.read_text(encoding="utf-8")
    before = text
    for src, out in MAP.items():
        pattern = re.compile(r'href="((?:\.\./)*)' + re.escape(src).replace(r"\.", r"\.") + r'"')
        text, n = pattern.subn(lambda m, o=out: f'href="{m.group(1)}{o}"', text)
        total += n
    if text != before:
        path.write_text(text, encoding="utf-8")
        print(f"  updated {path.relative_to(ROOT)}")
print(f"rewrote {total} links across {len(targets)} pages")
