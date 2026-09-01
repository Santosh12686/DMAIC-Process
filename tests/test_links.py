"""Ensure the browsable package has no broken internal Markdown links."""

from __future__ import annotations

from scripts.check_links import broken_links


def test_no_broken_internal_markdown_links() -> None:
    problems = broken_links()
    assert problems == [], "broken links:\n" + "\n".join(problems)
