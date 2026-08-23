# US Investment Case Migration Status — 2026-08-23

## Active-stack canonical cases
- `US/CRWV` — existing `research_complete` golden case candidate.
- `US/TSM` — existing `research_complete` case with decision-grade candidate review.
- `US/HTFL` — migrated into the current stack from the previously isolated `case-library/htfl-migration-20260818` branch using the original verified Git blobs; no research content was rewritten.
- `US/NVDA` — migrated 2026-08-23; `research_complete`, event-ready for 2026-08-26 earnings.
- `US/MU` — migrated 2026-08-23; `research_complete`, conditional start-small/buy review.
- `US/ALNY` — migrated 2026-08-23; `research_complete`, post-guidance-reset conditional start-small/buy review.

## Superseded migration PR
PR #3 (`Migrate HTFL into Investment Case Library`) preserved the original HTFL work but became non-mergeable as the Case Library base evolved. Its case/review/skill-update blobs have now been ported unchanged into the current US migration stack. PR #3 can therefore be closed as superseded rather than merged or duplicated.

## Integrity rule
A prior conversation or recommendation is not treated as a canonical case until it has case/evidence/timeline/valuation/decision artifacts in Git. If historical trade provenance cannot be recovered, the migration states that explicitly instead of reconstructing a hindsight trade.
