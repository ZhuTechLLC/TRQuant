# HTFL Evidence-Backed Skill Update Specification — 2026-08-18

**Source case:** `US-HTFL-2025-2026`  
**Status:** implementation specification  
**Evidence threshold:** only durable conclusions supported by SEC filings, direct IBKR market data, explicit management guidance, or reproducible valuation math are eligible for immediate Skill refinement. Single-case trading hypotheses remain candidate lessons.

## 1. `trquant-market-opportunity-discovery`

### A. Add a two-axis state model

Do not force `lifecycle` and `opportunity_setup` into one label.

**Lifecycle axis** describes the economic/company stage:

- Discovery
- Confirmation
- Momentum
- Harvest
- Reset
- Re-ignition
- Second S-Curve / platform expansion where applicable

**Opportunity-setup axis** describes the current actionable research setup:

- fundamental_mispricing
- event_confirmation
- post_event_continuation_candidate
- pullback_reunderwrite
- failed_breakout
- no_action

A candidate may fail a strict `New Ignition` lifecycle test while still deserving P0/P1 attention as a separately underwritten opportunity setup.

### B. Add the `False New Ignition != False Opportunity` guardrail

When a candidate is demoted from strict New Ignition after diluted-EV / prior-lifecycle / reverse-return review:

1. preserve the lifecycle correction;
2. do **not** automatically remove it from the active research queue;
3. independently test whether the catalyst created an event-confirmation or continuation setup;
4. require a separate risk/reward and evidence threshold for that setup.

This is a research-routing rule, **not** a trade rule.

### C. Post-event re-underwrite sequence

After a material earnings/FDA/contract/guide event and material gap, require:

`new evidence -> current price -> economic diluted EV -> price-implied expectations -> lifecycle -> opportunity setup -> handoff`

Do not preserve the pre-event lifecycle or valuation label mechanically.

### D. Evidence discipline for price formation

When interpreting large moves:

- true VWAP requires intraday `price x volume`; HLC/3 or typical price is not VWAP;
- volume alone does not identify institutional buyers;
- do not attribute CTA, gamma, short covering, ETF flow, forced flow or algorithmic activity without direct sign/scale/timing evidence;
- use direct market data when available and quarantine conflicting secondary OHLCV.

### E. Historical-analog promotion threshold

Do not turn one successful follow-through case into a continuation strategy.

Before promoting a post-earnings continuation rule, require a PIT event study controlling where feasible for:

- IPO age;
- market capitalization / economic diluted EV;
- revenue growth;
- revenue surprise;
- guidance revision magnitude;
- margin revision;
- profitability state;
- forward valuation;
- gap size;
- close location;
- relative volume;
- short/float context;
- market regime.

Evaluate at least T+1, T+2, T+5, T+10, T+20 and T+60, plus gap-fill probability, maximum drawdown and maximum run-up.

## 2. `trquant-equity-investment-case`

### A. Economic diluted valuation convention

For post-IPO / high-SBC / option-heavy growth companies, do not rely on basic market capitalization when current valuation is decision-critical.

Record explicitly:

- basic shares and as-of date;
- options, exercise price and treasury-stock convention;
- RSUs / ESPP / warrants where relevant;
- economic diluted shares;
- equity value;
- cash / investments;
- funded debt;
- lease treatment;
- enterprise value;
- denominator date / forecast status.

Label the result `reported`, `reconstructed` or `inferred`.

### B. Gross-margin leverage versus operating leverage

Do not describe gross-margin expansion as `operating leverage` by itself.

Use this sequence:

`revenue -> gross margin -> OpEx growth -> operating margin -> cash flow -> dilution -> FCF/share`

- `gross_margin_leverage`: revenue grows materially faster than cost of revenue / gross margin expands.
- `operating_leverage`: requires evidence that operating expenses grow slower than revenue and/or operating margin improves on a sustainable basis.
- `shareholder_operating_leverage`: ultimately requires per-share cash-flow / FCF improvement after SBC and dilution.

HTFL Q2 2026 is the canonical caution: gross-margin leverage was strong, but GAAP OpEx grew faster than revenue and GAAP operating loss widened YoY.

### C. Lifecycle versus trade setup

Preserve the existing principle `business thesis != stock attractiveness` and add:

`economic lifecycle != current opportunity setup`

A strong Confirmation/Momentum company can present a valid event setup even when it is no longer Discovery/New Ignition. Conversely, an early lifecycle company can have poor current risk/reward.

### D. Forward valuation evidence quality

When NTM/FY+1/FY+2 estimates are material:

- distinguish verified sell-side consensus from management guidance and internal model inference;
- do not label an internally constructed NTM/FY27/FY28 revenue as `consensus`;
- if PIT consensus cannot be verified, use `Unavailable` and keep model scenarios separately labeled.

## 3. `trquant-investment-case-library`

No core contract rewrite is required from HTFL alone. Existing append-only / immutable-decision / candidate-lesson promotion discipline is appropriate.

Implementation refinement only:

- reviews may add an `opportunity_setup` state without rewriting the historical lifecycle;
- candidate lessons must include `counterexample_or_limitation` and `promotion_evidence_needed` before Skill promotion;
- weak or conflicting vendor-generated outputs should be preserved only as leads/audit notes, not promoted into canonical evidence.

## 4. What is **not** promoted from HTFL

The following remain hypotheses pending broader validation:

- `gap hold -> add`;
- `strong close after earnings -> positive expected return`;
- exact PEAD persistence for recent IPO growth equities;
- a fixed starter-position percentage;
- any universal price level or anchored-VWAP trading rule;
- institutional/CTA/gamma/short-covering attribution based on volume alone.

## 5. Regression cases

Use these as regression anchors when implementing the update:

- **HTFL** — false New Ignition, genuine second S-curve, large rerating, possible separate opportunity setup.
- **CRWV** — strong business thesis but capital-intensity / financing / entry-price discipline.
- **TSM** — proven winner where market consensus does not imply first Discovery; attention continuity matters.
- **ALNY** — false-positive / launch-normalization / prior-winner reset diagnostic where relevant.

The intended outcome is fewer false-stage labels **without filtering out genuine post-event opportunities that belong to a different workflow.**
