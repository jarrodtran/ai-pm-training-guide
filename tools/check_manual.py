#!/usr/bin/env python3
"""Consistency check for the field manual: local links resolve, remote links counted."""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
md = (ROOT / "fde-pm-field-manual.md").read_text(encoding="utf-8")

# local references written as `path` or [text](path) or bare filenames in backticks
candidates = set()
for m in re.finditer(r"\]\((?!https?:)([^)#]+)\)", md):
    candidates.add(m.group(1).strip())
for m in re.finditer(r"`([a-zA-Z0-9_\-/]+\.(?:md|html|py|css|js))`", md):
    candidates.add(m.group(1).strip())

missing = []
for c in sorted(candidates):
    for base in (ROOT, ROOT / "templates"):
        p = (base / c).resolve()
        if p.exists():
            break
    else:
        missing.append(c)

remote = sorted(set(re.findall(r"https?://[^\s\)\]|,]+", md)))
domains = sorted({re.sub(r"^https?://([^/]+).*", r"\1", u) for u in remote})

print(f"local links checked: {len(candidates)} · missing: {missing or 'none'}")
print(f"remote URLs: {len(remote)} across {len(domains)} domains")
print("domains:", ", ".join(domains))
