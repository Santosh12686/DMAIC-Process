#!/usr/bin/env python3
"""Rebuild nab-dmaic-dispute-handling.zip from the browsable sample tree.

The zip is a convenience download of the DMAIC sample package. It contains the
documentation tree (README, LICENSE, CONTRIBUTING, docs/, data/, .github/) under
a top-level `nab-dmaic-dispute-handling/` folder. Repo tooling (scripts/, tests/,
Makefile, .cursor/, the zip itself) is intentionally excluded.

Deterministic (fixed timestamps + sorted entries) so re-running only changes the
zip when the underlying sample files change.
"""

from __future__ import annotations

import zipfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
ZIP_NAME = "nab-dmaic-dispute-handling.zip"
TOP_FOLDER = "nab-dmaic-dispute-handling"

INCLUDE_FILES = ["README.md", "LICENSE", "CONTRIBUTING.md"]
INCLUDE_DIRS = ["docs", "data", ".github"]
FIXED_DATE = (2026, 9, 1, 0, 0, 0)


def collect_files() -> list[Path]:
    files: list[Path] = []
    for name in INCLUDE_FILES:
        path = REPO_ROOT / name
        if path.is_file():
            files.append(path)
    for directory in INCLUDE_DIRS:
        base = REPO_ROOT / directory
        if base.is_dir():
            files.extend(p for p in base.rglob("*") if p.is_file())
    return sorted(files)


def build() -> Path:
    out_path = REPO_ROOT / ZIP_NAME
    files = collect_files()
    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in files:
            arcname = f"{TOP_FOLDER}/{path.relative_to(REPO_ROOT).as_posix()}"
            info = zipfile.ZipInfo(arcname, date_time=FIXED_DATE)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            zf.writestr(info, path.read_bytes())
    return out_path


def main() -> int:
    out_path = build()
    with zipfile.ZipFile(out_path) as zf:
        count = len(zf.namelist())
    print(f"Wrote {out_path.name} ({count} entries).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
