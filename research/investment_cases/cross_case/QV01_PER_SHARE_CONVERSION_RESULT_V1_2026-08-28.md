# QV-01 Per-Share Conversion Validation — V1 Result

## Lineage

- QuantConnect project: `TRQuant P1-1B Per-Share Conversion Validation`
- project_id: `35758787`
- backtest_id: `a80785079574e41f7f076505d5c96cf0`
- result schema: `trq.p1b.qv01.v1`
- result SHA256: `c0488bd0ca40119978a6df05ef8c3f1d15121d30b14da8c8bca2d89878f950c5`
- research period: 2020-01-01 through 2025-12-31 signals
- observations: 35,143
- monthly cross-sections: 71
- unique symbols: 1,456
- orders: 0

## Tested comparison

Headline baseline:
- cross-sectional rank of 1Y revenue growth.

Per-share conversion score:
- 40% revenue-growth rank
- 30% FCF-yield rank
- 15% share-count shrinkage rank
- 15% low debt/equity rank

The weights were specified before observing the result and are not claimed to be optimal.

## Results

| Horizon | Headline Revenue Growth Rank IC | Per-share Conversion Rank IC | Conversion Positive Rank-IC Ratio | Conversion Q5-Q1 Return Spread |
|---|---:|---:|---:|---:|
| 20D | 0.0034 | 0.0277 | 64.8% | +0.14% |
| 60D | -0.0108 | 0.0284 | 66.2% | -0.46% |
| 120D | -0.0210 | 0.0413 | 70.4% | -0.17% |

Headline revenue-growth positive-IC ratios were 53.5%, 46.5%, and 46.5% at 20D/60D/120D respectively.

## Interpretation

The experiment supports the underwriting hypothesis that business growth should be evaluated through a per-share conversion bridge rather than headline revenue growth alone:

- conversion-score Rank IC is positive at all three horizons;
- Rank IC improves materially versus headline growth at every horizon;
- directional consistency rises with horizon, reaching ~70% positive monthly Rank IC at 120D.

However, V1 does **not** validate a production long-short or top-quintile trading rule:

- Q5-Q1 return spread is only slightly positive at 20D;
- Q5-Q1 is slightly negative at 60D and 120D;
- V1 did not persist full quintile-shape diagnostics, sector-neutral IC, or a chronological holdout split in the compact payload.

The coexistence of positive Rank IC and weak/negative extreme-quintile spread suggests possible nonlinearity, tail contamination, sector effects, or a score-construction problem. That must be diagnosed rather than ignored.

## Governance conclusion

Linked lesson `CCL-20260828-L02-PER-SHARE-CONVERSION-FIREWALL` remains:

- `supported` as an underwriting / research principle;
- `not promoted` as a screening or capital-allocation rule;
- quantitative factor status: `PARTIAL_VALIDATION_REQUIRES_DIAGNOSTIC_V2`.

## Required V2

Without parameter optimization, preserve the original score and add:

1. Q1-Q5 mean returns and excess returns;
2. each component's standalone Rank IC;
3. sector-neutral Rank IC;
4. chronological validation split;
5. tail diagnostics for negative-FCF / extreme leverage / extreme revenue-growth observations;
6. no weight tuning based on V1 outcomes.
