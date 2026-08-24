# M6.2-P1 Current State

Updated: 2026-08-23

## Status

**Stage 1 mechanical eligibility audit: COMPLETE**  
**Stage P1.5 PIT provenance & timestamp integrity audit: COMPLETE**  
**Stage P2 H1 outcome protocol: FROZEN**  
**Stage P2 execution: BLOCKED BY QUANTCONNECT NODE CAPACITY — NO H1 RESULT YET**

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

Non-primary records:
- `E3-GOOGL-20240426` — `PIT_AMBIGUOUS`: same-day Google primary source is date-only; pre-10:00 ET public availability was not established. Also flagged `CONCURRENT_EARNINGS_PRIOR_EVENING`.
- `E4-META-20240418` — `PIT_FAIL`: frozen 10:00 ET decision precedes the earliest independently verified contemporaneous dissemination found in the audit (~12:00 ET). The record is not rescued by shifting its entry time.

### P2 frozen protocol

Protocol artifact:

`M6.2_P2_OUTCOME_EXTRACTION_PROTOCOL_V0_1.md`

Primary H1 endpoint:

> Cross-event mean of T+3 net directional SPY-excess return using a frozen 25 bps round-trip implementation-cost assumption.

Secondary/frozen robustness diagnostics include T+1/T+5, median, 10% trimmed mean, issuer-clustered bootstrap 95% CI, hit rate, direction counts, contribution concentration, and 10/50 bps cost sensitivities.

No GPT catalyst grade, semantic score, analyst-revision overlay, RVOL threshold, PROBE/CONFIRM state logic, support/resistance, RSI/MACD, or category-selection layer is permitted before H1 is adjudicated.

### P2 implementation and execution status

Corrected event-driven QuantConnect source:

`quantconnect/M6.2_P2_V0_1R_MAIN.py`

Implementation tag:

`v0.1R_EVENT_DRIVEN_NO_FUTURE_HISTORY`

Planned QuantConnect project:

`M6.2 P2 Catalyst Outcome Extraction V01`

Planned authoritative backtest:

`M6.2-P2 H1 Outcome Extraction v0.1R - 46 PIT PASS - NO ORDERS`

The corrected implementation removes future-event history calls from initialization while preserving the frozen research protocol. The DevOps two-step confirmation guard was completed, but QuantConnect rejected backtest creation because no spare Cloud backtest node was available. A second attempt returned the same capacity condition.

Execution detail artifact:

`M6.2_P2_EXECUTION_STATUS.md`

**H1 remains `NOT RUN / NOT CALIBRATED`. No alpha or profitability conclusion is permitted from the capacity error.**

## Locked methodological decisions

1. The 46 `PIT_PASS` IDs are the **frozen primary H1 sample** for M6.2-P2.
2. Do not add replacement events for the two non-primary records.
3. Do not alter the $5 price gate, $20M prior-20 median daily dollar-volume gate, or ticker-frequency cap based on outcomes.
4. Do not alter any frozen decision timestamp after seeing returns.
5. `E3-GOOGL-20240426` stays in the audit trail and remains excluded from primary labels unless its timestamp is independently resolved without using subsequent price behavior.
6. `E4-META-20240418` stays `PIT_FAIL` in this sample; a future protocol may define a different event-relative entry rule only on a newly frozen sample.
7. No post-entry return, MFE/MAE, win/loss label, or outcome-dependent sample choice was used in P1/P1.5.
8. Do not change P2 methodology merely because QuantConnect compute capacity is temporarily unavailable.

## Next gate

`M6.2-P2 — Execute exact v0.1R and adjudicate H1`

When a Cloud backtest node is available, rerun the exact persisted v0.1R source. First verify extraction integrity (`Expected=46`, exact data-limited IDs, zero orders, entry timing), then evaluate the frozen H1 metrics.

- `GO` → broader out-of-sample replication before H2.
- `INCONCLUSIVE` → only one pre-specified sample-expansion step; no feature mining.
- `NO-GO` → stop H2/H3.

## Research boundary

P1.5 establishes point-in-time admissibility for 46 events. The frozen P2 protocol defines how H1 will be tested. **Neither establishes alpha, profitability, win rate, expected return, or a validated trading strategy until the corrected P2 run completes.**