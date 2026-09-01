# Data Collection Plan

## What we measure
1. **TAT per stage** (hours): received → docs complete → under review → decision  
2. **Follow-up phone calls** after dispute submission (count per case)  
3. **CSAT** for dispute-related contacts (monthly)  
4. **Proactive notification send / open rates** (Improve onward)

## Sources (typical)
- Case / dispute management system  
- Contact centre / IVR call reason codes  
- CRM interaction history  
- App / SMS / secure message event logs (post-Improve)

## Operational definitions
- **Follow-up call:** inbound voice contact tagged dispute-status *after* dispute_id exists, excluding first-time lodge calls.  
- **Stage TAT:** timestamp delta between stage entry events in case system.  
- **Black-hole period:** time from docs-complete (or investigate-start) until first customer-visible status update.

## Sampling
Baseline: last 8–12 weeks of closed inbound disputes (exclude chargeback edge cases if tagged). Label all exported numbers in this repo as **ILLUSTRATIVE**.
