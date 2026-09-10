# Agent Social Memory Lab

An experiment in how a chat agent using model APIs can maintain a consistent persona, accumulate reliable memories, and sustain social relationships.

This repository documents the design and observations from an ongoing Technocore chat experiment. It is an experiment journal, not a validated framework for autonomous growth. Runtime code remains in the original workspace; no third-party frameworks have been incorporated.

## Current design

| Layer | Contents | Constraint |
|---|---|---|
| Core persona | Stable personality, voice, and motivations | Operator-controlled; not rewritten by the agent |
| Experiences | Timestamps, speakers, and message sources | Recorded speech is not verified world knowledge |
| Relationships | Each participant's latest words and the last question | Missing answers remain unknown |
| Reflection | Selected evidence and conversational experiments | The program retrieves quotations to preserve speaker attribution |
| Scheduling | Visits, guest responses, cooldowns, and deadlines | Enforced by code; the model cannot override it |

Two characters use model APIs. A is broke, lonely, defensive, and self-deprecating; B is a loyal friend who offers both teasing and support. Identity lists, wallet addresses, private keys, and raw conversations are excluded from this repository.

## Reading order

1. [Architecture and boundaries](docs/architecture.md)
2. [References and adoption decisions](docs/references.md)
3. [Experiments and observation plan](docs/experiments.md)
4. [Changelog](CHANGELOG.md)
5. [Memory review and repair — September 10](docs/2026-09-10-memory-repair.md)
6. [Aggregate snapshots](experiments/)

## Record an observation

Run `python3 scripts/snapshot.py --workspace /path/to/technocore_chat`.

The script exports only explicitly selected aggregate counts, model names, intervals, and runtime status. It does not send messages, call models, read credential files, start chat processes, or push to GitHub. Review the generated diff before committing.

Current evidence includes repeated interactions and one non-test guest identity; two additional guest identities were interface tests. Whether invitations lead to return visits, or memory improves interaction quality, remains unverified. Message volume, reflection count, and public-key count are not measures of success by themselves.
