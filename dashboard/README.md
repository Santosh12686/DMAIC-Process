# Cursor × DMAIC — Interactive Analytics Bridge Dashboard

A single-file, presentable **interactive** dashboard for the **Cursor × DMAIC Success Plan**
pitch (audience: sponsor / Black Belt). It bridges **leading** Cursor analytics to **lagging**
operational outcomes for a NAB-style transaction-dispute follow-up use case, and lets the
customer **fill in the missing information** so the projected outcome metrics update live.

> **Demo / training sample only.** Not affiliated with or endorsed by National Australia Bank.
> The **1.4 measured** follow-up-call baseline is computed from the sample dataset; every other
> figure is **ILLUSTRATIVE / SAMPLE** or **PROJECTED from your inputs** — a model, not a
> delivered result. No customer data or secrets are included.

## Open it
Just open [`index.html`](index.html) in any browser — it is fully self-contained (no build,
no network, no dependencies). Sample defaults are embedded so the story is clear from one file.

## Interactive: fill in the missing info → outcomes auto-update
The **Inputs** panel ("Fill in the missing information") lets the customer enter their own
assumptions with sliders / number fields. The **projected** outcomes in section B recompute
instantly. A transparent model is shown on-screen and used everywhere:

```
reduction        = status-chasing% × notify-accuracy% × adoption%
projected calls  = baseline × (1 − reduction)
goal met         = projected ≤ baseline × (1 − target%)
avoided / month  = volume × (baseline − projected)
capacity freed   = avoided × minutes ÷ 60
$ benefit        = avoided × cost-per-call     (only when you set a cost-per-call)
```

- **Measured today stays fixed** (1.40, −30% goal not achieved) — the fact never moves with inputs.
- **Projected** cards (goal gauge, avoided calls, capacity, CSAT, break-even) update on every change,
  and the goal gauge flips **met / not met** live.
- **Reset to sample** restores the illustrative defaults. Inputs that differ from sample flip the
  header badge to "Your scenario · projection".
- **CFO-safe:** dollar outputs appear **only** when you supply a cost-per-call assumption (your number),
  so no ROI dollars are invented; Cursor is never claimed to have delivered the −30% goal.

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

## Where live data would come from
Leading Cursor analytics (seats, agent runs, spend) would come from the Cursor Admin Analytics API;
lagging inputs (dispute volume, CSAT, cost-per-call) from an ops warehouse (dispute case system,
contact-centre reason codes). Until then, the Inputs panel lets a customer enter those numbers by hand.
No live credentials ship here.

## Sample data
CSV inputs mirroring the embedded values (for review / re-use):
- [`data/scenario_inputs.csv`](data/scenario_inputs.csv) — the interactive input assumptions + what each drives
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
