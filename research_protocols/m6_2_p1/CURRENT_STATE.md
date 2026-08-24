# M6.2-P1 Current State

Updated: 2026-08-24

## Status

**Stage 1 mechanical eligibility audit: COMPLETE**  
**Stage P1.5 PIT provenance & timestamp integrity audit: COMPLETE**  
**Stage P2 H1 pilot: COMPLETE — `INCONCLUSIVE`**  
**Stage P2E single permitted H1 expansion: PROTOCOL + SOURCE POPULATION FROZEN — MANIFEST BUILD NEXT**

### Stage 1 authoritative QuantConnect run

- Project ID: `35534302`
- Backtest ID: `3234d66296959b8e4d1c68590ed5745b`
- Candidates: 50
- Mechanical pass: 48
- Mechanical fail: 2
- Data limited: 0
- Outcome fields calculated: false
- Orders: 0

Mechanical exclusions remain unchanged:
- `E3-RKLB-20231221`: prior-20 median daily dollar volume below $20M.
- `E5-IRBT-20220805`: prior-20 median daily dollar volume below $20M.

### P1.5 PIT audit result

Audit artifact: `M6.2_P1_5_PIT_PROVENANCE_AUDIT_V0_1.md`

- Mechanically eligible entering P1.5: **48**
- `PIT_PASS`: **46**
- `PIT_AMBIGUOUS`: **1**
- `PIT_FAIL`: **1**
- Primary P2-eligible sample: **46**

Non-primary records remain in the audit trail:
- `E3-GOOGL-20240426` — `PIT_AMBIGUOUS`
- `E4-META-20240418` — `PIT_FAIL`

## P2 H1 pilot — completed

Protocol:

`M6.2_P2_OUTCOME_EXTRACTION_PROTOCOL_V0_1.md`

Results:

`M6.2_P2_H1_RESULTS_V0_1.md`

Corrected event-driven source:

`quantconnect/M6.2_P2_V0_1R_MAIN.py`

Authoritative QuantConnect run:

- Project: `M6.2 P2 Catalyst Outcome Extraction V01`
- Project ID: `35546834`
- Backtest: `M6.2-P2 H1 Outcome Extraction v0.1R - 46 PIT PASS - NO ORDERS`
- Backtest ID: `08399f885022cd3c77d612b0e7b3f195`
- Status: `Completed.`
- Expected: **46**
- Extracted: **46**
- Data limited: **0**
- Delayed entry: **0**
- Orders: **0**

Primary T+3 result at 25 bps round-trip cost:

- mean net directional SPY-excess: **+1.7035%**
- median: **-0.6438%**
- 10% trimmed mean: **+0.6244%**
- hit rate: **47.83%**
- issuer-clustered 95% bootstrap CI: **[-0.6331%, +4.3043%]**
- top-3 positive contribution share: **45.08%**

Frozen H1 pilot gate: **`INCONCLUSIVE`**.

Interpretation: the simple continuation hypothesis remains plausible and positively skewed, but the pilot does not establish a statistically defensible positive mean because the clustered confidence interval crosses zero. H2/H3 remain closed.

## P2E — single permitted expansion

Frozen protocol:

`M6.2_P2E_SAMPLE_EXPANSION_PROTOCOL_V0_1.md`

Frozen manifest schema:

`M6.2_P2E_EXPANSION_MANIFEST_SCHEMA_V0_1.md`

Frozen source-population specification:

`M6.2_P2E_SOURCE_POPULATION_SPEC_V0_1.md`

The source-population spec fixes SEC EDGAR 8-K/8-K-A/6-K as the primary discovery backbone, defines allowed official FDA/government supplements, freezes category admission terms, deduplication, timestamp handling, and deterministic SHA-256 selection. It explicitly prohibits stopping after finding five attractive events; the category-year source population must be enumerated before hash ranking.

### Locked expansion design

P2E adds exactly **125 candidate events** before mechanical/PIT exclusions:

- 25 E1 Clinical / Regulatory
- 25 E2 Earnings / Guidance
- 25 E3 Contract / Capacity
- 25 E4 Strategic / Product
- 25 E5 M&A / Policy

Each category contributes exactly 5 candidates for each calendar year 2021–2025. Candidate identity is selected from source-defined populations by deterministic SHA-256 ranking, not from remembered winners or price screens.

Across the combined pilot + expansion candidate manifest, one ticker may contribute at most 2 events.

The same $5 price gate, prior-20 median $20M daily-dollar-volume gate, PIT provenance rules, SPY benchmark, direction rule, T+1/T+3/T+5 horizons and 10/25/50 bps cost assumptions remain unchanged.

### Critical replication rule

The final H1 decision is based on the **new P2E expansion cohort only**. The 46 pilot observations may be pooled afterward for a secondary precision estimate but cannot determine the final gate.

A valid empirical expansion adjudication requires at least **90 new `PIT_PASS` events**.

After a valid P2E run, only two research conclusions are permitted:

- `FINAL_GO` — expansion-only T+3 mean > 0, trimmed mean > 0, issuer-clustered 95% CI excludes zero positively, and horizon/concentration diagnostics do not contradict continuation.
- `FINAL_NO_GO` — execution-integrity minimum is met but any required `FINAL_GO` condition fails.

There is no second `INCONCLUSIVE` expansion round. If fewer than 90 new events are PIT-valid/data-complete, classify `DESIGN_NOT_EXECUTABLE_AT_REQUIRED_COVERAGE`; H2/H3 remain closed and no hand-picked rescue sample is allowed.

## Locked methodological decisions

1. Do not change the pilot sample after seeing P2 outcomes.
2. Do not promote Clinical/Regulatory or any other category because a few pilot events contributed large gains.
3. Do not introduce GPT catalyst grade, semantic score, RVOL, analyst revision, technical indicators, PROBE/CONFIRM or category-return filters before final H1 adjudication.
4. Do not select P2E candidates from known winners or from post-event price screens.
5. Do not reuse pilot outcomes as the primary validation cohort.
6. Do not conduct a second sample expansion if P2E fails the final gate.
7. Mechanical/PIT failures remain in the audit trail and are not replaced after outcomes are known.
8. Do not change the source-population definition or hash-selection rule after candidate returns are available.

## Next gate

`M6.2-P2E-A — Enumerate source populations and freeze the 125-event expansion candidate manifest`

The next work item is candidate discovery only. It must populate the frozen manifest fields and the full/hash-reconstructable category-year source populations without calculating any post-entry return, MFE/MAE, win/loss or strategy PnL.

Only after the 125-event candidate manifest is frozen may the existing QuantConnect mechanical eligibility gate and PIT provenance audit be applied.

## Research boundary

The 46-event P2 result is a pilot with an `INCONCLUSIVE` H1 classification. The P2E research design and source universe are now fixed before any new-event outcome extraction. **No production-alpha, position-sizing or live-trading claim is established at this stage.**