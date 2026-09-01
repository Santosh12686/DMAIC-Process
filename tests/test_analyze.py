"""Tests for the dispute baseline analysis app.

These lock in the metrics computed from the committed sample dataset so the
DMAIC Measure baseline stays reproducible.
"""

from __future__ import annotations

import copy
from pathlib import Path

import pytest

from scripts.analyze_disputes import (
    DEFAULT_CSV,
    compute_metrics,
    load_rows,
    validate,
)


@pytest.fixture(scope="module")
def rows() -> list[dict[str, str]]:
    return load_rows(DEFAULT_CSV)


def test_sample_dataset_is_valid(rows: list[dict[str, str]]) -> None:
    result = validate(rows)
    assert result.ok, f"unexpected validation errors: {result.errors}"


def test_row_count_in_expected_range(rows: list[dict[str, str]]) -> None:
    assert 20 <= len(rows) <= 30


def test_baseline_metrics_match_docs(rows: list[dict[str, str]]) -> None:
    metrics = compute_metrics(rows)
    assert metrics["total_disputes"] == 25
    # DMAIC baseline headline: customers call ~1.4 times post-submission.
    assert metrics["avg_follow_up_calls"] == 1.4
    assert metrics["pct_with_follow_up_call"] == 76.0
    assert metrics["avg_csat"] == 3.4
    assert metrics["median_stage_tat_h"] == {
        "tat_intake_h": 4.0,
        "tat_docs_h": 25.0,
        "tat_review_h": 70.0,
        "tat_decision_h": 7.0,
    }
    assert metrics["outcome_distribution"] == {
        "declined": 5,
        "partial": 4,
        "upheld": 16,
    }
    assert sum(metrics["channel_distribution"].values()) == 25


def test_validation_flags_bad_outcome(rows: list[dict[str, str]]) -> None:
    bad = copy.deepcopy(rows)
    bad[0]["outcome"] = "mystery"
    result = validate(bad)
    assert not result.ok
    assert any("outcome" in e for e in result.errors)


def test_validation_flags_negative_and_nonnumeric(rows: list[dict[str, str]]) -> None:
    bad = copy.deepcopy(rows)
    bad[1]["follow_up_calls"] = "-2"
    bad[2]["tat_review_h"] = "n/a"
    result = validate(bad)
    assert not result.ok
    assert any("negative" in e for e in result.errors)
    assert any("not numeric" in e for e in result.errors)


def test_validation_flags_duplicate_id(rows: list[dict[str, str]]) -> None:
    bad = copy.deepcopy(rows)
    bad[1]["dispute_id"] = bad[0]["dispute_id"]
    result = validate(bad)
    assert not result.ok
    assert any("duplicate" in e for e in result.errors)


def test_validation_flags_csat_out_of_range(rows: list[dict[str, str]]) -> None:
    bad = copy.deepcopy(rows)
    bad[0]["csat_score"] = "9"
    result = validate(bad)
    assert not result.ok
    assert any("csat" in e.lower() for e in result.errors)


def test_default_csv_path_exists() -> None:
    assert Path(DEFAULT_CSV).exists()
