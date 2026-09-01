# NAB DMAIC — Transaction Dispute Handling (Sample)

> **Demo / training sample only.** Inspired by public reporting on NAB conversational AI data tools. Not official NAB documentation, and not affiliated with or endorsed by National Australia Bank. Metrics and case data are **illustrative**.

## Problem in one line
Customers chase dispute status by phone because of a visibility gap — not because investigations are inherently slow.

## Goal
- Reduce repeat customer phone calls by **30%**
- Improve transparency across the dispute resolution lifecycle

## Scope
Inbound customer transaction dispute workflows handled by support and operations teams. **Out of scope:** changing investigation/fraud policy rules themselves.

## DMAIC map

| Phase | Folder | Focus |
|-------|--------|--------|
| **D**efine | [`docs/01-define/`](docs/01-define/) | [Problem statement](docs/01-define/problem-statement.md) · [Project charter](docs/01-define/project-charter.md) |
| **M**easure | [`docs/02-measure/`](docs/02-measure/) | [Data collection plan](docs/02-measure/data-collection-plan.md) · [Baseline metrics](docs/02-measure/baseline-metrics.md) |
| **A**nalyze | [`docs/03-analyze/`](docs/03-analyze/) | [Process map](docs/03-analyze/process-map.md) · [Root-cause analysis](docs/03-analyze/root-cause-analysis.md) |
| **I**mprove | [`docs/04-improve/`](docs/04-improve/) | [Solution design](docs/04-improve/solution-design.md) · [Pilot plan](docs/04-improve/pilot-plan.md) |
| **C**ontrol | [`docs/05-control/`](docs/05-control/) | [Control plan](docs/05-control/control-plan.md) · [SOP event triggers](docs/05-control/sop-event-triggers.md) |

## Two ways to browse this package
- **Read it in place:** open the [`docs/`](docs/) tree above directly on GitHub.
- **Download it:** grab [`nab-dmaic-dispute-handling.zip`](nab-dmaic-dispute-handling.zip) for the full sample tree (docs, data, and `.github/` templates) as a single download. Rebuild it any time with `make zip`.

## Sample data
[`data/sample_baseline_disputes.csv`](data/sample_baseline_disputes.csv) — 25 fictional baseline rows (AUD banking flavour) with per-stage TATs, follow-up calls, outcomes, and CSAT.

## Baseline highlight (illustrative)
Customers call an average of **1.4 times** post-submission due to lack of visibility (docs received / under review / resolved). Reproduce it from the sample data with `make analyze`.

## Solution sketch
Integrate conversational AI data capabilities (Customer Brain / Genie-style) to auto-trigger proactive status updates at milestones: info needed, under review, finalized. See [Solution design](docs/04-improve/solution-design.md).

## Repository tooling
A small, dependency-light validation layer keeps the sample honest (this tooling lives in the repo, not in the downloadable zip):

| Command | What it does |
|---------|--------------|
| `make install` | Install test dependencies (`pytest`) |
| `make analyze` | Print the baseline analysis report from the CSV |
| `make analyze-json` | Emit the baseline metrics as JSON |
| `make test` | Run the pytest suite (metric + validation + link checks) |
| `make lint` | Verify every internal Markdown link resolves |
| `make zip` | Rebuild `nab-dmaic-dispute-handling.zip` from the sample tree |
| `make validate` | Run lint + tests + analysis end to end |

The analysis app ([`scripts/analyze_disputes.py`](scripts/analyze_disputes.py)) uses only the Python standard library and validates the dataset before computing the DMAIC Measure baseline.

## Reference (public)
[BrokerNews — NAB conversational AI data tool](https://www.brokernews.com.au/news/breaking-news/nab-breaks-new-ground-with-conversational-ai-data-tool-289542.aspx)

## License
See [LICENSE](LICENSE). MIT. Sample materials; no claim of NAB endorsement.
