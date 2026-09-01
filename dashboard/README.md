# Cursor × DMAIC — Analytics Bridge Dashboard

A single-file, presentable dashboard for the **Cursor × DMAIC Success Plan** pitch
(audience: sponsor / Black Belt). It bridges **leading** Cursor analytics to
**lagging** operational outcomes for a NAB-style transaction-dispute follow-up use case.

> **Demo / training sample only.** Not affiliated with or endorsed by National Australia Bank.
> All figures are **ILLUSTRATIVE / SAMPLE** except the **1.4 measured** follow-up-call
> baseline computed from the sample dataset. No customer data or secrets are included.

## Open it
Just open [`index.html`](index.html) in any browser — it is fully self-contained (no build,
no network, no dependencies). Sample data is embedded so the story is clear from one file.

## The narrative (do not invert)
- **Hero:** Cursor = the agentic DMAIC workspace (repo + rules + human judgment).
- **Proof:** inbound transaction-dispute handling, where status-anxiety drives repeat calls.
- **Improve surface (not the hero):** Brain/Genie-style event-driven status updates.
- **CFO-safe:** `1.4` measured, `−30%` goal shown as **not achieved**, no invented ROI dollars,
  demo numbers marked SAMPLE. Cursor is **not** claimed to have delivered the −30% goal.

## What it shows
- **A · Leading — Cursor analytics:** active users / seats, agent runs & PRs on DMAIC artifacts,
  model / agent cost (investment only), time-to-artifact proxies, rules adoption.
- **B · Lagging — ops outcomes:** 1.4 measured follow-up calls, the −30% goal gauge (clearly not
  achieved), stage TAT, CSAT / transparency, notify accuracy (Improve surface), freed capacity (SAMPLE, no $).
- **C · Mapping panel:** the Success Plan 2×2 (technical goals + business outcomes) mapped to
  metric, source, and leading/lagging.
- **D · Control / DMAIC phase strip:** M0 → M4 (Define → Control). A new data source triggers
  **auto re-measure & alert** against the baseline — not a fully automated DMAIC.

## Sample vs Connected
The header toggle switches between **Sample** (embedded illustrative data) and **Connected**
(stubbed). Connected mode is intentionally not wired: live values would come from the Cursor
Admin Analytics API plus an ops warehouse (dispute case system, contact-centre reason codes, CSAT).
No live credentials ship here.

## Sample data
CSV inputs mirroring the embedded values (for review / re-use):
- [`data/leading_cursor_analytics.csv`](data/leading_cursor_analytics.csv)
- [`data/lagging_ops_outcomes.csv`](data/lagging_ops_outcomes.csv)
- [`data/mapping_success_plan.csv`](data/mapping_success_plan.csv)

The lagging baseline mirrors the DMAIC package dataset (`data/sample_baseline_disputes.csv`),
where follow-up calls average **1.4** per dispute.

## Palette
Cursor Light: `#F7F7F5` background · `#1A1A1A` ink · `#F54E00` accent. Leading is tinted teal,
Lagging is tinted accent-orange, so the two sides read apart in under five seconds.

## Improve-surface context (public)
[BrokerNews — NAB conversational AI data tool](https://www.brokernews.com.au/news/breaking-news/nab-breaks-new-ground-with-conversational-ai-data-tool-289542.aspx)
— cited as context for the Improve surface only, not as the hero of the story.
