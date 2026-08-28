# QV-02 Valuation Denominator Validation — V1 Result

## Lineage

- QuantConnect project: `TRQuant P1-1B Valuation Denominator Validation`
- project_id: `35759404`
- backtest_id: `6defddb2f3357eddc476a1eba5a042ed`
- schema: `trq.p1b.qv02.v1`
- result SHA256: `dad1001dc923eb9cb4f2f7934785185be32d3f234bfbb38941bd2e035b55bb24`
- observations: 35,152
- monthly cross-sections: 71
- unique symbols: 1,351
- orders: 0

## Tested hypothesis

Question: does a low positive trailing P/E behave differently when the earnings denominator is supported by stronger contemporaneous free-cash-flow conversion?

Definitions fixed before observing results:

- `cheap_pe`: lower positive trailing P/E ranks higher;
- `earnings_proxy = market_cap / PE`;
- `denominator_quality = FCF / earnings_proxy`;
- high/low denominator quality split at each monthly cross-sectional median;
- no parameter tuning.

## All-sample results

Low P/E itself had positive cross-sectional association with later returns:

| Horizon | Rank IC | Sector-neutral Rank IC | Positive IC Ratio | Q5-Q1 |
|---|---:|---:|---:|---:|
| 20D | +0.0188 | +0.0137 | 53.5% | +0.11% |
| 60D | +0.0331 | +0.0260 | 59.2% | +0.78% |
| 120D | +0.0482 | +0.0386 | 57.7% | +1.74% |

## High versus low FCF/earnings denominator-quality split

The proposed simple quality filter did **not** produce a stable improvement.

### High denominator quality

| Horizon | Rank IC | Q5-Q1 |
|---|---:|---:|
| 20D | +0.0200 | +0.19% |
| 60D | +0.0366 | +1.10% |
| 120D | +0.0513 | +1.40% |

### Low denominator quality

| Horizon | Rank IC | Q5-Q1 |
|---|---:|---:|
| 20D | +0.0200 | +0.16% |
| 60D | +0.0299 | +0.60% |
| 120D | +0.0481 | +2.49% |

The two groups are too similar to claim that the FCF/earnings ratio is a useful universal denominator-quality gate.

## 2024-2025 independent time slice

The failure of the simple quality split is clearer in the later period.

### High denominator quality

- 20D Q5-Q1: -0.07%
- 60D Q5-Q1: -0.19%
- 120D Q5-Q1: -1.85%

### Low denominator quality

- 20D Q5-Q1: +0.46%
- 60D Q5-Q1: +0.65%
- 120D Q5-Q1: +1.05%

Both groups retained positive Rank IC, but the proposed high-quality split did not dominate.

## Interpretation

This is a useful negative result.

The Case Library lesson `normalize the valuation denominator before calling something cheap` is broader than contemporaneous FCF conversion. MU, WBA, OXY, FRC and INTC show different denominator distortions:

- peak-cycle earnings;
- structurally deteriorating cash earnings;
- leverage-driven EV-to-equity convexity;
- liquidity/survival risk;
- capex and dilution before normalized per-share earnings.

A single `FCF / earnings` ratio does not identify these mechanisms.

Therefore:

- the **economic underwriting principle remains supported by Cases**;
- the tested universal quantitative proxy is **REJECTED**;
- no threshold tuning is authorized from this result;
- the next quantitative work should use explicit economic/lifecycle conditioning rather than a single denominator-quality score.

## Governance state

`CCL-20260828-L01-NORMALIZE-VALUATION-DENOMINATOR`

- Case support: `supported`
- QV-02 simple proxy: `rejected`
- universal factor promotion: `not authorized`
- next validation direction: explicit cyclical/financing/lifecycle denominator regimes.
