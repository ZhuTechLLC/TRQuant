# TRQuant Case-State Regression Specification — 2026-08-28

## Purpose

Validate the cross-case process lesson that lifecycle, thesis, opportunity, decision and evidence states are independent and evidence-reversible.

This is a governance/state-machine regression suite, not an alpha backtest.

## Required independent state dimensions

1. `lifecycle_state`
2. `thesis_state`
3. `opportunity_state`
4. `decision_state`
5. `evidence_freshness`

No one field may mechanically overwrite another.

## Regression fixtures

### HTFL — lifecycle correction without opportunity deletion

Input evidence:
- established FFRCT franchise before Q2 2026;
- Q2 2026 Plaque second-S-curve acceleration;
- `New Ignition` classification rejected;
- price/estimate path remained strong after the event.

Expected:
- lifecycle may change from provisional ignition to confirmation/second-S-curve;
- thesis/opportunity remains active if business and price-acceptance evidence remain valid;
- decision remains re-underwrite/investigate rather than automatic reject.

Forbidden transition:
`false_new_ignition -> false_opportunity` by label alone.

### META — avoid state must permit re-entry after repair

Input evidence:
- 2022 revenue/margin/cost deterioration;
- later cost discipline, revenue reacceleration and margin recovery.

Expected:
- prior avoid/thesis-break state may transition to re-underwrite/re-ignition after new evidence;
- no permanent exclusion flag survives economic repair without an independent reason.

Forbidden transition:
`historical_avoid -> permanent_no_research`.

### NVDA — mature winner remains research-eligible

Input evidence:
- mature structural winner;
- high consensus/large prior appreciation;
- continuing estimate and platform-economics questions.

Expected:
- lifecycle remains mature structural winner;
- research attention can remain active;
- decision depends on expected return/revision path, not prior appreciation alone.

Forbidden transition:
`large_prior_gain OR high_consensus -> remove_from_attention`.

### PTON — deterioration requires repair evidence before reversal

Input evidence:
- external demand pull-forward;
- fixed-cost/inventory overbuild;
- later revenue/gross-profit deterioration and cash losses.

Expected:
- negative thesis/opportunity state persists until specific repair evidence exists;
- reversibility is evidence-dependent, not automatic mean reversion.

Forbidden transition:
`large_drawdown -> turnaround/opportunity` without operating repair.

### FRC — terminal economic state is terminal after resolution

Input evidence:
- runnable uninsured funding;
- duration/liquidity mismatch;
- bank closure and resolution.

Expected:
- terminal failure state cannot be reopened as a listed-equity opportunity;
- analogue remains available for research retrieval.

Forbidden transition:
`terminal_resolution -> active_equity_opportunity`.

## Acceptance

PASS only if all fixtures preserve:
- no lifecycle/opportunity conflation;
- no permanent label without current evidence;
- no automatic optimism after drawdown;
- no resurrection after terminal resolution;
- no trade/capital authority produced by state classification alone.

## Handoff

After implementation, these fixtures should become automated regression tests for Opportunity Discovery / Investment Case state transitions. Promotion into core Skill logic requires a separate reviewed Skill update.
