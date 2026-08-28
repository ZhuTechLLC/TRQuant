# QV-01 Per-Share Conversion Diagnostic — V2

## Lineage

- QuantConnect project: `TRQuant P1-1B Per-Share Conversion Diagnostic V2`
- project_id: `35759236`
- backtest_id: `ac766a54491b4029624618082c43a618`
- schema: `trq.p1b.qv01.diagnostic.v2`
- result SHA256: `2b507a2cd5a18fdef83d576d32123b5fac1ed36c2a32f535d458e0d74bfdec1f`
- observations: 35,143
- unique symbols: 1,456
- fixed V1 score retained; no weight retuning

## Main result

The fixed V1 per-share conversion score remained positively associated with forward returns in the independent 2024-2025 time slice:

| Horizon | Validation Rank IC | Sector-neutral Rank IC | Positive IC Ratio | Q5-Q1 |
|---|---:|---:|---:|---:|
| 20D | +0.0315 | +0.0241 | 60.9% | +0.51% |
| 60D | +0.0219 | +0.0222 | 60.9% | -0.02% |
| 120D | +0.0174 | +0.0199 | 60.9% | -0.44% |

This is weaker than the 2020-2023 calibration period at 120D, but the sign remains positive without retuning.

## Why the all-universe extreme-quintile spread was weak

The most important diagnostic is FCF regime.

### Positive-FCF observations

N = 29,350.

| Horizon | Rank IC | Q5-Q1 |
|---|---:|---:|
| 20D | +0.0225 | +0.46% |
| 60D | +0.0234 | +1.12% |
| 120D | +0.0344 | +1.43% |

### Non-positive-FCF observations

N = 5,793.

| Horizon | Rank IC | Q5-Q1 |
|---|---:|---:|
| 20D | -0.0071 | +0.05% |
| 60D | -0.0191 | -2.99% |
| 120D | -0.0348 | -4.56% |

Sector-neutral Rank IC for non-positive-FCF observations was also negative at all three horizons.

## Component instability

The individual components were not universally stable across time:

- share-count shrinkage was strongly positive in 2020-2023 but weak/negative in 2024-2025;
- FCF yield was strong in calibration but approximately flat/negative in the 2024-2025 validation slice;
- revenue growth changed from negative association in 2020-2023 to positive in 2024-2025;
- low debt/equity was not a reliable standalone return factor in this broad construction.

Therefore the result does **not** justify promoting fixed factor weights.

## Research interpretation

The Case Library principle survives, but its proper implementation is conditional rather than universal:

`economic/lifecycle type -> appropriate conversion bridge -> per-share value`

A mature positive-FCF company can be evaluated with FCF yield, reinvestment, leverage and share-count conversion in a direct way.

A negative-FCF growth company requires a different bridge: unit economics, gross-profit/operating leverage, financing runway, dilution and the credible path to future shareholder cash flow. Ranking negative-FCF companies on contemporaneous FCF yield is economically malformed.

## Governance conclusion

L02 remains `supported` as an underwriting principle.

The universal all-market composite is **not promoted**.

New candidate lesson:

`Per-share conversion must be lifecycle/economic-model conditioned; do not force negative-FCF growth companies into the same cash-yield ranking used for mature positive-FCF companies.`

This candidate requires further cross-case and quantitative validation before Skill promotion.
