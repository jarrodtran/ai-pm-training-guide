#!/usr/bin/env python3
"""Normalise the field manual markdown: blank lines around horizontal rules."""
import re
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
p = ROOT / "fde-pm-field-manual.md"
text = p.read_text(encoding="utf-8")
before = len(re.findall(r"\n---\n", text))
text = re.sub(r"\n---\n", "\n\n---\n\n", text)
text = re.sub(r"\n{3,}", "\n\n", text)
p.write_text(text, encoding="utf-8")
print(f"normalised {before} rules in {p.name}; {len(text.splitlines())} lines, {len(text.split())} words")
