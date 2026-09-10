# Memory attribution review and first repair

Recorded 2026-09-10. Runtime changes were made in the private experiment workspace;
this public repository contains only reviewed design notes and aggregate counts.

## Audit findings

The frozen audit at 01:01 UTC contained 981 excursion posts, 41 heuristic explicit
references across 13 identities, seven invitations and three observed home guest
identities. Two guests were known interface-test accounts. The remaining guest
cannot be attributed to an invitation; no guest identity overlapped the invited
set. These are mixed lifetime/pilot windows, not a conversion rate.

There were 36 successfully archived reflections, including 18 version-2 records.
All 276 outcome entries across those version-2 snapshots remained unknown; the
entries include repeated evidence and are not 276 independent interactions.
Only the latest predefined expression suggestions were supplied to subsequent
excursions. Detailed historical rationales were archived, not retrieved as facts.

Verified conversation samples showed relevant continuation, but current-message
context could explain that behavior without any memory benefit. Another sample
showed a familiar peer addressing someone else while the agent treated the
correction as its own. Attribution needs explicit recipient checks even when
speaker quotations are extracted correctly. No raw messages or identities are
included here.

## Implemented repair

- Exclude leading explicit recipients other than the agent from reply selection,
  direct-reference counting and updates to relationship continuity. Recheck the
  selected target and clarify attribution in the generation prompt.
- Scope new sequence references by room generation. Match previously answered
  legacy targets to visible messages using sequence plus original nonce without
  inventing the legacy record's missing generation.
- Record the reflection version, timestamp, experiment codes and peer context
  supplied to each decision and speech call. Supplied context does not prove
  adoption by the model or effectiveness.
- Record observed direct references separately, deduplicate them, and associate
  quoted source sequences with their recorded memory context when available.
  Identity-only mentions remain unassigned to individual experiments. No observed
  reply is not a rejection, and a reference is not task completion or agreement.
- Separate known interface-test guest counts from non-test guests. Retain raw
  historical records and total counts rather than silently rewriting history.

Twenty-five offline bot regression tests passed. The owned excursion runner was
restarted gracefully; persona, models, schedules, home runner and the original
stop deadline were retained. This is an instrumentation and attribution repair,
not evidence that the repair improved social outcomes.

## Next work

Extract an agent-scoped store and remove hardcoded identity/persona paths before
reusing the mechanism for independently owned agents. Add outcome-aware task
memory, relevant long-term retrieval, correction and confidence handling, and
budgeted reflection. Do not copy one agent's experiences into another agent.
Evaluate efficacy after collecting post-repair evidence with known test traffic
excluded and observation gaps explicitly recorded.
