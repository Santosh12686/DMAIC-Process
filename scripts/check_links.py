#!/usr/bin/env python3
"""Verify that relative Markdown links in the repo point at files that exist.

Keeps the browsable DMAIC package honest: every `[text](relative/path)` link in
a tracked Markdown file must resolve to a real file or directory. External links
(http/https/mailto) and pure in-page anchors (`#section`) are skipped.

Standard library only.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
SKIP_DIRS = {".git"}


def markdown_files() -> list[Path]:
    return [
        p
        for p in REPO_ROOT.rglob("*.md")
        if not any(part in SKIP_DIRS for part in p.relative_to(REPO_ROOT).parts)
    ]


def broken_links() -> list[str]:
    problems: list[str] = []
    for md in markdown_files():
        text = md.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            target = match.group(1).strip()
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            path_part = target.split("#", 1)[0].split("?", 1)[0]
            if not path_part:
                continue
            resolved = (md.parent / path_part).resolve()
            if not resolved.exists():
                rel = md.relative_to(REPO_ROOT)
                problems.append(f"{rel}: broken link -> {target}")
    return problems


def main() -> int:
    problems = broken_links()
    if problems:
        print("Broken Markdown links found:", file=sys.stderr)
        for p in problems:
            print(f"  - {p}", file=sys.stderr)
        return 1
    checked = len(markdown_files())
    print(f"OK: all relative Markdown links resolve ({checked} files checked).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
