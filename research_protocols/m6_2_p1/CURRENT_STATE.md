# M6.2-P1 Current State

Updated: 2026-08-23

## Status

**Stage 1 mechanical eligibility audit: COMPLETE**  
**Stage P1.5 PIT provenance & timestamp integrity audit: COMPLETE**

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

## Locked methodological decisions

1. The 46 `PIT_PASS` IDs are now the **frozen primary H1 sample** for M6.2-P2.
2. Do not add replacement events for the two non-primary records.
3. Do not alter the $5 price gate, $20M prior-20 median daily dollar-volume gate, or ticker-frequency cap based on outcomes.
4. Do not alter any frozen decision timestamp after seeing returns.
5. `E3-GOOGL-20240426` stays in the audit trail and remains excluded from primary labels unless its timestamp is independently resolved without using subsequent price behavior.
6. `E4-META-20240418` stays `PIT_FAIL` in this sample; a future protocol may define a different event-relative entry rule only on a newly frozen sample.
7. No post-entry return, MFE/MAE, win/loss label, or outcome-dependent sample choice was used in P1/P1.5.

## Next gate

`M6.2-P2 — Outcome / Path Extraction for H1`

P2 is now permitted **only for the 46 frozen PIT_PASS events**.

Minimum P2 extraction should remain hypothesis-focused:
- frozen decision price / first valid tradable observation;
- T+1, T+3, T+5 returns;
- market/sector-adjusted return where the benchmark mapping is defined ex ante;
- MFE / MAE over the same frozen horizons;
- initial repricing measure observable by the decision timestamp;
- contemporaneous participation measure such as RVOL if it can be calculated strictly PIT;
- explicit transaction-cost / slippage assumptions;
- halt or missing-data flags.

Primary H1 question remains:

> Do complex, verified catalysts exhibit tradable 1–5 day conditional drift after an accessible point-in-time entry, net of realistic costs?

P2 must first estimate the **simple unconditional/low-complexity event baseline**. It must not introduce Catalyst Grade, GPT semantic scoring, PROBE/CONFIRM state logic, support/resistance, RSI/MACD, or other feature mining before the primary H1 result is known.

## Research boundary

The P1.5 result establishes point-in-time admissibility for 46 events. It is **not evidence of alpha, profitability, win rate, expected return, or a validated trading strategy**.