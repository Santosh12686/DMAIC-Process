# SOP — Event-Driven Dispute Status Triggers

## Purpose
Make proactive, automated status updates the standard operating procedure for all in-scope dispute categories.

## Rules
1. Every eligible milestone **must** emit a domain event within SLA (e.g. 15 minutes of stage change).  
2. Customers receive a channel-appropriate ping; outcomes prefer authenticated channels.  
3. Agents do not rely on outbound manual “we’re looking at it” calls as the primary mechanism.  
4. Failed sends retry then escalate to ops queue.  
5. Changes to copy or events go through PR + privacy checklist in this repo’s templates.

## Categories
Applies to standard inbound transaction disputes; exclusions listed in pilot/control docs must stay explicit.
