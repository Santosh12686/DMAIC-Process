# Solution Design — Proactive Status via Conversational AI Data Tools

## Concept
Integrate conversational AI / customer-data capabilities (styled after public **Customer Brain** / **Genie** narratives) so dispute milestones **automatically** trigger customer-visible updates.

## Event catalogue
| Event | Customer message intent | Channel preference |
|-------|-------------------------|-------------------|
| `dispute.received` | We have your dispute | App push + secure inbox |
| `docs.received` | Documents received | App / SMS (low sensitivity) |
| `info.needed` | Please provide X | Secure message + push |
| `case.under_review` | Under review — no action needed | App push |
| `case.finalized` | Outcome available — view in app | App + secure message |

## Workflow change
**Before:** Wait for manual updates → customer phones.  
**After:** System pings at info-needed / under-review / finalized.

## Architecture sketch (logical)
Case system emits domain events → rules / orchestration → conversational AI data layer personalises copy → channel adapters (app, SMS, secure msg) → interaction log feeds Measure/Control.

## Non-goals
Do not auto-decide disputes; do not expose investigation internals beyond approved status codes.
