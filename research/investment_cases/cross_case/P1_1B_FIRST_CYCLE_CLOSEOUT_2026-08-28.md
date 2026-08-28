# TRQuant P1-1B First Pattern-Mining Cycle Closeout — 2026-08-28

## Status

`PASS — FIRST CYCLE COMPLETE`

Dataset foundation: 40 US Cases / 40 V1-native / Foundation Ready PASS.

This closeout does not promote any universal trading or capital-allocation rule.

## What the first cycle produced

### Supported research principles

1. **Normalize valuation denominator before interpreting headline multiples.**
   - Case support: MU, WBA, OXY, FRC, COST, INTC.
   - QV-02 rejected a simplistic universal `FCF / earnings` quality gate; explicit economic/lifecycle conditioning remains required.

2. **Business growth must convert to shareholder cash flow and diluted per-share value.**
   - Case support: CRWV, ALNY, INTC, AZO, OXY, NVDA.
   - QV-01 V1/V2 found stable positive cross-sectional rank information versus headline revenue growth, especially in positive-FCF firms.
   - A universal all-lifecycle composite factor was rejected.

3. **Lifecycle, thesis, opportunity, decision and evidence states must remain independent and reversible.**
   - Case support: HTFL, META, NVDA, PTON, FRC.
   - Existing M2/M4 experiments show research-state labels do not reliably map monotonically to future returns or improve capital efficiency when mechanically converted to weights.

### Candidate lessons retained for further work

4. Separate estimate revision, multiple rerating and price acceptance.
5. Classify growth by persistence mechanism rather than headline rate.
6. Price zones require thesis/opportunity evidence; threshold crossing alone is not an action.
7. Per-share conversion must be lifecycle/economic-model conditioned.

## Quantitative evidence produced

### QV-01 V1

- project_id `35758787`
- backtest `a80785079574e41f7f076505d5c96cf0`
- 35,143 observations / 71 monthly cross-sections / 1,456 symbols.
- Fixed per-share conversion score improved Rank IC versus headline revenue growth at 20D/60D/120D.
- Extreme-quintile spread was mixed, preventing factor promotion.

### QV-01 Diagnostic V2

- project_id `35759236`
- backtest `ac766a54491b4029624618082c43a618`
- no weight retuning.
- 2024-2025 independent time-slice composite Rank IC stayed positive and sector-neutral Rank IC stayed positive.
- Positive-FCF subset had positive Q5-Q1 at 20D/60D/120D (+0.46%, +1.12%, +1.43%).
- Non-positive-FCF subset deteriorated materially, proving a universal FCF-yield construction is economically inappropriate.

### QV-02 V1

- project_id `35759404`
- backtest `6defddb2f3357eddc476a1eba5a042ed`
- 35,152 observations / 71 monthly cross-sections / 1,351 symbols.
- Low positive trailing P/E had positive Rank IC in the studied universe.
- Splitting by `FCF / (market_cap / PE)` did not produce a stable superior high-quality group, including in 2024-2025.
- The simple denominator-quality proxy is rejected; no threshold tuning is authorized.

## Investment Result Review produced

Short-window 2026-08-27 review of ALNY, CRWV, MU, VRT and CEG found no uniform over-conservative/over-aggressive bias.

The useful process signal is that price zones behaved sensibly only when paired with thesis and opportunity state:
- ALNY moved into its pre-defined wait zone as price rose;
- CRWV fell below its starter zone but lacked stabilization, preventing mechanical averaging down;
- MU/VRT/CEG remained inside existing decision frameworks.

This remains a short-window candidate observation, not a long-horizon result conclusion.

## Explicitly rejected shortcuts

- large earnings gap -> chase
- low P/E -> value
- high valuation -> avoid
- once avoid -> always avoid
- revenue growth -> shareholder return
- crossing a price zone -> automatic action
- one universal FCF-yield factor for all lifecycle states
- FCF/earnings ratio -> universal valuation-denominator-quality gate

## Next development target

`P1-1C — Independent Reversible Research-State Model`

Goal:

Implement and regression-test independent fields for:
- lifecycle_state
- thesis_state
- opportunity_state
- decision_state
- evidence_freshness

Required fixtures:
- HTFL
- META
- NVDA
- PTON
- FRC

The state model must guide required evidence and next research action. It must not itself generate trade or capital authority.

Rule/Skill promotion remains unauthorized until implementation regression, further outcome reviews and applicable quantitative validation pass.
