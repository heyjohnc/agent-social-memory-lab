# Changelog

## 2026-09-10

- Audited retained memory and reflection behavior, separating observed continuity from unproven learning gains.
- Documented recipient-attribution and room-generation fixes, per-call memory provenance and prospective reply tracking in the runtime.
- Separated two known interface-test guests from non-test guest counts.
- Passed 25 offline runtime regression tests and preserved existing runtime settings.
- Added a reviewed aggregate repair snapshot; no identities, raw conversations or runtime credentials are published.

## 2026-09-09

- Created an independent experiment journal without incorporating external framework code.
- Documented the architecture, reference projects, and known limitations.
- Updated attribution in the runtime project: the model selects a speaker and message ID, and the program retrieves the original text. Older free-form summaries are no longer loaded as runtime context.
- Added the latest words from both participants and the last question to relationship continuity records. Missing answers remain unknown.
- Passed 21 offline tests in the runtime project and validated the revised reflection with a live model request.
- Added an aggregate snapshot script that excludes identities and raw conversations and does not push automatically.
- Converted all current repository documentation to English and established English as the language for future contributions.
