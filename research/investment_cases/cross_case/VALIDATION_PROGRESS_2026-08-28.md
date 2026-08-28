# TRQuant P1-1B Validation Progress — 2026-08-28

## Cross-case mining status

Pattern Mining has produced five governed lessons:

- L01 normalized valuation denominator — supported
- L02 per-share conversion firewall — supported
- L03 independent reversible research states — supported as governance principle
- L04 estimate revision versus price rerating — candidate pending PIT event validation
- L05 growth persistence mechanism — candidate pending ontology/quant validation

No lesson has trade or capital authority.

## L03 independent-state validation from prior QuantConnect experiments

### M2 fresh PIT capital allocation

Source:
- project `TRQuant M2 Capital Allocation Validation`
- project_id `35478113`
- backtest_id `26799faa3f56a4fb29940dabf20f2a3a`
- period 2023-01-01 through 2026-08-20

Relevant result:
- WATCH, INVESTIGATE and CONFIRMED did not show stable monotonic forward-return separation.
- CONFIRMED minus INVESTIGATE confidence intervals crossed zero at 20D, 60D and 120D.
- INVESTIGATE minus WATCH was positive at 60D in this reconstruction but negative/indeterminate at 20D and 120D.
- Therefore a research-state label is not sufficient evidence for a deterministic capital-weight function.

### M4 strict OOS technology-lane capital validation

Source:
- project `TRQuant M4 Technology Capital Validation`
- project_id `35478581`
- backtest_id `9c1913333c05d11a00a35401cdf03d8e`
- decision slice: 2025 strict OOS

Relevant result:
- adding 10% INVESTIGATE weight increased annualized return only from ~14.11% to ~14.34% in the inspected slice;
- Sharpe declined from ~1.73 to ~1.58;
- return/drawdown efficiency declined from ~2.97 to ~2.67;
- max drawdown worsened from about -4.76% to -5.37%;
- replication checksum failed and `decision_eligible=false`.

Interpretation:

This does not prove that INVESTIGATE should always receive zero capital. It supports a narrower governance principle: `research_state` describes evidence maturity and required next action; it must not mechanically create trade or capital authority.

## QV-01 field-coverage probe — PASS

Project:
- `TRQuant P1-1B Fundamental Coverage Probe`
- project_id `35758683`
- backtest_id `4ca3be8f890c3575c33990822f3af115`
- actual PIT fundamental slice: 2025-07-01
- top 1000 contemporaneous dollar-volume universe, price >= $5

Coverage:
- Revenue Growth 1Y: 99.9%
- Free Cash Flow TTM: 99.9%
- Capex TTM: 99.0%
- Basic Average Shares 3M: 99.8%
- Basic Average Shares 12M: 99.8%
- Long-Term Debt/Equity 3M: 99.0%
- P/E: 93.8%
- Stock Type: 100%

Conclusion:

QV-01 can use direct PIT fundamental fields. There is no need to substitute weak current-state proxies for FCF, share count or leverage.

## QV-01 full validation — READY, EXECUTION BLOCKED BY QC CAPACITY

Prepared project:
- `TRQuant P1-1B Per-Share Conversion Validation`
- backtest name `QV-01 per-share conversion PIT 2020-2025`

Prepared design:
- historical dynamic fundamental universe;
- top 500 by contemporaneous dollar volume;
- signal years 2020-2025;
- 20D / 60D / 120D forward returns;
- compare headline revenue-growth rank against a per-share conversion score built from revenue growth, FCF yield, share-count shrinkage and low leverage;
- output rank IC, positive-rank-IC ratio and Q5-Q1 spread.

Preflight passed.

Execution attempt failed before launch because QuantConnect reported:
`There are no spare nodes available in your cluster.`

This is a compute-capacity blocker, not a code, schema, PIT or data-coverage failure.

## Current stage assessment

- Foundation Ready: PASS / CLOSED
- Pattern Mining: PASS for first cross-case lesson set
- State-model governance principle: supported and strengthened by M2/M4 evidence
- QV-01 data feasibility: PASS
- QV-01 quantitative result: PENDING compute availability
- Rule Promotion: NOT AUTHORIZED
