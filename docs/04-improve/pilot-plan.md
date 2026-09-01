# Pilot Plan

## Cohort
- Inbound card transaction disputes, 1–2 product lines  
- Exclude high-risk fraud hold cases if legally restricted from auto-notify  
- Sample size: enough closed cases to detect ~30% drop in follow-up calls (power analysis TBD)

## Success gates
| Gate | Criteria |
|------|----------|
| G1 Technical | ≥ 95% eligible events produce a notify attempt |
| G2 Behaviour | Avg follow-up calls ≤ baseline × 0.70 |
| G3 Experience | CSAT stable or improved vs control |
| G4 Risk | Zero critical privacy / wrong-party send incidents |

## Rollback
Feature flag off event publishers; revert to manual notify SOP within one change window.

## Risks & controls
- Misdirected SMS → prefer authenticated app / secure message for outcomes  
- Message tone / APP compliance → legal/privacy review of templates  
- Alert fatigue → coalesce events; quiet hours policy
