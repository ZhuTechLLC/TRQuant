# M6.2-P1 Current State

Updated: 2026-08-23

## Status

**Stage 1 mechanical eligibility audit: COMPLETE**

Authoritative QuantConnect run:
- Project ID: `35534302`
- Backtest ID: `3234d66296959b8e4d1c68590ed5745b`
- Candidates: 50
- Mechanical pass: 48
- Mechanical fail: 2
- Data limited: 0
- Outcome fields calculated: false
- Orders: 0

Frozen accepted sample by category:
- E1 Clinical / Regulatory: 10
- E2 Earnings / Guidance: 11
- E3 Contract / Capacity: 10
- E4 Strategic / Product: 10
- E5 M&A / Policy: 7

Mechanical exclusions:
- `E3-RKLB-20231221`: prior-20 median daily dollar volume below $20M.
- `E5-IRBT-20220805`: prior-20 median daily dollar volume below $20M.

## Locked methodological decision

Do not calculate or inspect post-entry returns until the 48 accepted event IDs, source provenance and admissible decision timestamps have been audited. Eligibility thresholds must not be modified based on subsequent performance.

## Next gate

`M6.2-P1.5 — PIT Catalyst Provenance & Timestamp Integrity Audit`

For every accepted event record:
1. primary source / document;
2. publication date and timestamp where available;
3. timezone;
4. session classification;
5. admissible decision timestamp;
6. proof that decision time is after public availability;
7. confounder flags;
8. source quality / timestamp ambiguity status.

Required output status per event:
- `PIT_PASS`
- `PIT_AMBIGUOUS`
- `PIT_FAIL`

Only `PIT_PASS` events are eligible for M6.2-P2 outcome extraction. `PIT_AMBIGUOUS` is retained for audit and excluded from primary labels until resolved.

## Research boundary

The 48-event result establishes only mechanical tradability and sample balance. It is not evidence of alpha, profitability, win rate, or expected return.
