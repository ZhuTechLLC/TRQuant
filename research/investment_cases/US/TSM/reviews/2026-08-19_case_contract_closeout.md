# TSM Case Contract Closeout — 2026-08-19

## Purpose

Close the TSM migration into the standard Investment Case Library contract before merge. This review does not promote the case beyond `research_complete`.

## Canonical market-state correction

The earlier 2026-08-18 morning IBKR snapshot near $420 is retained in `evidence.jsonl` as a superseded intraday observation. The canonical current-state price is the 2026-08-18 IBKR regular-session close:

- Open: $416.84
- High: $419.63
- Low: $410.76
- Close: **$413.41**
- Prior close: $430.97
- 52-week high: $478.89
- One-day move: approximately -4.07%
- Drawdown from 52-week high: approximately -13.67%

The close entered the predefined `$395-$420` first-accumulation / buy-review zone and exceeded the `>=12%` drawdown re-underwrite trigger. These are research triggers, not automatic trade instructions.

## Synchronized canonical state

The following files were synchronized to the regular-session close:

- `case.json`
- `case.md`
- `timeline.json`
- `valuation_history.csv`
- `decisions.jsonl`
- `registry.json`

Current action is consistently represented as:

`START SMALL / BUY REVIEW — CONDITIONAL`

The action remains conditional on intact company fundamentals, forward expectations, upstream AI-demand evidence, macro/geopolitical state and portfolio concentration.

## Recomputed current valuation

At $413.41:

- Equity value: ~ $2.144T
- Provisional EV: ~ $2.060T
- TTM P/E: ~29.83x
- FY2026 forward P/E: ~25.13x using $16.45 sell-side ADR EPS consensus
- FY2027 forward P/E: ~19.85x using $20.83 sell-side ADR EPS consensus
- EV/Sales: ~14.41x
- EV/Operating Income: ~25.73x

EV remains provisional because the stored historical FX convention is not yet fully deterministic.

## Evidence-ledger closeout

`evidence.jsonl` now carries `retrieved_at` for the migrated evidence set. Because exact historical retrieval timestamps were not preserved for every source, legacy migrated records use date-level retrieval granularity rather than invented times.

The regular-session close is stored as new canonical market evidence (`TSM-E027`). The earlier intraday market record (`TSM-E018`) is retained and marked superseded, preserving audit history rather than overwriting it.

## Case Contract validation

Validated concepts:

- identity / status / as-of
- dominant variable
- value-driver chain
- current decision state
- point-in-time historical checkpoints
- evidence classification and provenance
- `period_end` vs `available_from` vs `retrieved_at`
- immutable retrospective decision reconstructions vs current decision
- reproducible valuation checkpoints with provisional-status disclosure
- explicit unknowns
- kill criteria and monitoring handoff
- candidate lessons remain candidate-level

## Status

- Case status: `research_complete`
- Golden case: `false`
- Decision grade: **not promoted**
- Postmortem complete: **not applicable / not promoted**

## Remaining decision-grade blockers

1. Deterministic historical balance-sheet-date FX / EV convention.
2. Same-date authoritative FX if production-grade ADR/local-share attribution is required.
3. No verified original 2025 TSM trade-decision record across all possible accounts.
4. Explicit founder/reviewer approval of current sizing, action and kill criteria.

Formal factor regression is not a general blocker; it is required only if the research claims positive semiconductor-sector alpha.
