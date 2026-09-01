# Root Cause Analysis

## 5 Whys (status-chase calls)
1. Why do customers call after lodging? → They want case status.  
2. Why don’t they already know status? → No proactive update on their channel.  
3. Why no proactive update? → Status lives in back-end case tools, not pushed to CX channels.  
4. Why isn’t it pushed? → No event-driven bridge from investigation milestones to messaging.  
5. Why no bridge? → Process designed for *agent-led* updates; digital/AI triggers not standardised.  

**Root cause:** Communication gap (“black hole”) between internal investigations and customer-facing channels.

## Fishbone (summary)
- **Process:** Manual notify; milestone ownership unclear  
- **People:** Agents interrupted by status-only calls  
- **Systems:** Case events not published to conversational / notify layer  
- **Measurement:** Follow-up call volume not tied to missing notify events  
- **Environment:** Privacy-correct channels required (authenticated)

## Implication for Improve
Fix **visibility** with automated milestone pings (Customer Brain / Genie-style), not only shorten investigation TAT.
