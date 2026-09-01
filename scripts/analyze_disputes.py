#!/usr/bin/env python3
"""Analyze the baseline dispute dataset for the DMAIC Measure/Analyze phases.

Reads the sample dispute CSV, validates its integrity, and reports the core
baseline metrics referenced in docs/02-measure/baseline-metrics.md
(follow-up calls, stage turnaround times, CSAT, outcome mix).

Uses only the Python standard library so it runs with no third-party deps.
"""

from __future__ import annotations

import argparse
import csv
import json
import statistics
import sys
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CSV = REPO_ROOT / "data" / "sample_baseline_disputes.csv"

REQUIRED_COLUMNS = [
    "dispute_id",
    "submit_date",
    "amount_aud",
    "channel",
    "tat_intake_h",
    "tat_docs_h",
    "tat_review_h",
    "tat_decision_h",
    "follow_up_calls",
    "outcome",
    "csat_score",
]
STAGE_COLUMNS = ["tat_intake_h", "tat_docs_h", "tat_review_h", "tat_decision_h"]
ALLOWED_OUTCOMES = {"upheld", "partial", "declined"}


@dataclass
class ValidationResult:
    errors: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors


def load_rows(csv_path: Path) -> list[dict[str, str]]:
    with csv_path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def validate(rows: list[dict[str, str]]) -> ValidationResult:
    """Check the dataset is structurally sound before computing metrics."""
    result = ValidationResult()

    if not rows:
        result.errors.append("dataset is empty")
        return result

    header = list(rows[0].keys())
    missing = [c for c in REQUIRED_COLUMNS if c not in header]
    if missing:
        result.errors.append(f"missing columns: {', '.join(missing)}")
        return result

    seen_ids: set[str] = set()
    for i, row in enumerate(rows, start=2):  # header is line 1
        dispute_id = row["dispute_id"].strip()
        if not dispute_id:
            result.errors.append(f"line {i}: empty dispute_id")
        elif dispute_id in seen_ids:
            result.errors.append(f"line {i}: duplicate dispute_id {dispute_id}")
        else:
            seen_ids.add(dispute_id)

        for col in STAGE_COLUMNS + ["follow_up_calls", "amount_aud", "csat_score"]:
            try:
                value = float(row[col])
            except (TypeError, ValueError):
                result.errors.append(f"line {i}: {col}={row[col]!r} is not numeric")
                continue
            if value < 0:
                result.errors.append(f"line {i}: {col} is negative ({value})")

        outcome = row["outcome"].strip().lower()
        if outcome not in ALLOWED_OUTCOMES:
            result.errors.append(
                f"line {i}: outcome {outcome!r} not in {sorted(ALLOWED_OUTCOMES)}"
            )

        try:
            csat = int(row["csat_score"])
            if not 1 <= csat <= 5:
                result.errors.append(f"line {i}: csat_score {csat} outside 1..5")
        except (TypeError, ValueError):
            pass  # numeric check above already recorded this

    return result


def compute_metrics(rows: list[dict[str, str]]) -> dict:
    """Compute the baseline metrics used across the Measure/Analyze docs."""
    follow_ups = [int(r["follow_up_calls"]) for r in rows]
    csat = [int(r["csat_score"]) for r in rows]
    total = len(rows)

    outcome_counts: dict[str, int] = {}
    for r in rows:
        key = r["outcome"].strip().lower()
        outcome_counts[key] = outcome_counts.get(key, 0) + 1

    channel_counts: dict[str, int] = {}
    for r in rows:
        key = r["channel"].strip().lower()
        channel_counts[key] = channel_counts.get(key, 0) + 1

    metrics = {
        "total_disputes": total,
        "avg_follow_up_calls": round(statistics.mean(follow_ups), 2),
        "pct_with_follow_up_call": round(
            100 * sum(1 for f in follow_ups if f >= 1) / total, 1
        ),
        "avg_csat": round(statistics.mean(csat), 2),
        "median_stage_tat_h": {
            col: statistics.median(float(r[col]) for r in rows)
            for col in STAGE_COLUMNS
        },
        "outcome_distribution": dict(sorted(outcome_counts.items())),
        "channel_distribution": dict(sorted(channel_counts.items())),
    }
    return metrics


def format_report(metrics: dict, csv_path: Path) -> str:
    lines = [
        "NAB DMAIC — Dispute Handling: Baseline Analysis",
        "=" * 48,
        f"Source: {csv_path}",
        f"Total disputes analysed: {metrics['total_disputes']}",
        "",
        "Follow-up calls (visibility gap signal)",
        f"  Avg follow-up calls / dispute : {metrics['avg_follow_up_calls']}",
        f"  Disputes with >=1 chase call  : {metrics['pct_with_follow_up_call']}%",
        "",
        "Stage turnaround (median hours)",
    ]
    labels = {
        "tat_intake_h": "intake",
        "tat_docs_h": "docs",
        "tat_review_h": "review",
        "tat_decision_h": "decision",
    }
    for col in STAGE_COLUMNS:
        lines.append(f"  {labels[col]:<9}: {metrics['median_stage_tat_h'][col]:g} h")
    lines += [
        "",
        f"Dispute journey CSAT (avg): {metrics['avg_csat']} / 5",
        "",
        "Outcome distribution:",
    ]
    for outcome, count in metrics["outcome_distribution"].items():
        lines.append(f"  {outcome:<9}: {count}")
    lines.append("")
    lines.append("Channel distribution:")
    for channel, count in metrics["channel_distribution"].items():
        lines.append(f"  {channel:<9}: {count}")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "csv_path",
        nargs="?",
        default=str(DEFAULT_CSV),
        help="Path to the dispute CSV (default: data/sample_baseline_disputes.csv)",
    )
    parser.add_argument(
        "--json", action="store_true", help="Emit metrics as JSON instead of a report"
    )
    args = parser.parse_args(argv)

    csv_path = Path(args.csv_path)
    if not csv_path.exists():
        print(f"error: dataset not found at {csv_path}", file=sys.stderr)
        return 2

    rows = load_rows(csv_path)
    validation = validate(rows)
    if not validation.ok:
        print("Dataset validation FAILED:", file=sys.stderr)
        for err in validation.errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    metrics = compute_metrics(rows)
    if args.json:
        print(json.dumps(metrics, indent=2))
    else:
        print(format_report(metrics, csv_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
