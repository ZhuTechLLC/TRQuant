# US Investment Case Migration Status — 2026-08-23

## Active-stack canonical cases
- `US/CRWV` — existing `research_complete` golden case candidate.
- `US/TSM` — existing `research_complete` case with decision-grade candidate review on separate follow-up PR.
- `US/NVDA` — migrated 2026-08-23; `research_complete`, event-ready for 2026-08-26 earnings.
- `US/MU` — migrated 2026-08-23; `research_complete`, conditional start-small/buy review.
- `US/ALNY` — migrated 2026-08-23; `research_complete`, post-guidance-reset conditional start-small/buy review.

## Existing separate migration — do not duplicate
- `US/HTFL` already exists on branch `case-library/htfl-migration-20260818` and PR #3 (`Migrate HTFL into Investment Case Library`). It contains a full `research_complete` case and should be rebased/merged through that PR rather than copied into a second artifact.

## Integrity rule
A prior conversation or recommendation is not treated as a canonical case until it has case/evidence/timeline/valuation/decision artifacts in Git. If historical trade provenance cannot be recovered, the migration states that explicitly instead of reconstructing a hindsight trade.
