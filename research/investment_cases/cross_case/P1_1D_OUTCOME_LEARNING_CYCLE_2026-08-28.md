# P1-1D Outcome Learning Cycle — 2026-08-28

## Scope

First bounded learning cycle after the 40-US-Case Foundation and P1-1C Research-State production close.

Decision clock for market outcomes: **2026-08-27 regular-session close**. The still-open 2026-08-28 session is excluded.

This artifact is a cross-case learning record, not capital authority and not a replacement for Case-level evidence or decisions.

## Production basis

- Research Control runtime/source commit: `cbfdd1de748d83a03b5ce6f507cc3255b85e1ea3`
- US Cases: 40
- V1 Native: 40
- Integrity errors: 0
- `research_state_v1` production projection: PASS

## Cycle A — Price zone + evidence state

| Case | Case reference | 2026-08-27 close | Move | Production research state | Interpretation |
|---|---:|---:|---:|---|---|
| ALNY | $224.39 (2026-08-18) | $236.56 | +5.4% | reunderwrite_required / underwrite_in_progress / reunderwrite | Price moved into the prior $230–260 wait zone. The move does not create a chase instruction; stronger evidence is still required. |
| CRWV | $96.52 (2026-08-18) | $86.80 | -10.1% | reunderwrite_required / underwrite_in_progress / reunderwrite | Price fell through the prior $90–95 starter zone. Lower price alone does not create an automatic buy; capital-conversion evidence and price stabilization remain required. |
| MU | $932.97 (2026-08-25) | $935.39 | +0.3% | reunderwrite_required / underwrite_in_progress / reunderwrite | Remains near the original $900–950 hurdle zone. No new action follows from price alone. |
| VRT | $256.03 (2026-08-25) | $269.28 | +5.2% | monitoring / intact / continuation | Remains inside the prior $250–275 starter/hold zone. The move does not justify chasing; estimate and delivery evidence remain load-bearing. |
| CEG | $278.42 (2026-08-25) | $282.41 | +1.4% | reunderwrite_required / underwrite_in_progress / reunderwrite | Remains in the prior $270–290 re-underwrite zone. The zone is a research trigger, not an automatic entry. |

### Cycle A conclusion

Across biotech, AI infrastructure, semiconductors, industrial power/cooling and power generation, a price-zone crossing did **not** have a consistent directional implication. The stable process rule is that price zones identify where to re-underwrite; thesis/opportunity/evidence state determines whether action is justified.

This supports `CCL-20260828-L06-PRICE-ZONE-REQUIRES-EVIDENCE-STATE` as a **supported process rule**, not an alpha rule.

## Cycle B — Per-share conversion / lifecycle conditioning

QV-01 V2 was independently re-read from the persisted QuantConnect result:

- 35,143 PIT observations / 71 monthly cross-sections / 1,456 symbols.
- Composite conversion-score rank IC: about +0.028 / +0.028 / +0.041 at 20D / 60D / 120D.
- 2024–2025 validation split retained positive composite rank IC: about +0.031 / +0.022 / +0.017.
- Positive-FCF subset Q5-Q1: +0.46% / +1.12% / +1.43% at 20D / 60D / 120D.
- Non-positive-FCF subset: 60D -2.99%, 120D -4.56%, with negative rank-IC behavior.

### Cycle B conclusion

The underwriting principle is supported, but a universal contemporaneous FCF-yield factor is rejected. Lifecycle/economic-model conditioning is required.

This upgrades `CCL-20260828-L07-LIFECYCLE-CONDITIONED-CONVERSION` from **candidate** to **supported**.

## Cycle C — Valuation denominator

QV-02 was independently re-read from the persisted QuantConnect result:

- 35,152 PIT observations / 71 monthly cross-sections / 1,351 symbols.
- Cheap positive trailing P/E had positive cross-sectional rank IC.
- Splitting by the simple `FCF / earnings_proxy` denominator-quality measure did **not** create stable improvement.
- In the 2024–2025 validation split, the low-quality bucket was not consistently worse and in several return comparisons was better.

### Cycle C conclusion

`CCL-20260828-L01-NORMALIZE-VALUATION-DENOMINATOR` remains economically supported by heterogeneous Cases, but the simple FCF/Earnings quality proxy is **rejected**. No parameter retuning is authorized to rescue it. Future validation must explicitly condition on cycle, financing structure and lifecycle.

## Cycle D — Reversible independent states

P1-1C production reads expose machine-readable `research_state_v1`:

- HTFL: `reunderwrite_required / underwrite_in_progress / continuation / INVESTIGATE / mixed`
- NVDA: `monitoring / intact / continuation / INVESTIGATE / mixed`
- FRC: `terminal_resolution / historical / none / NO_ACTION / not_applicable`
- PTON and META remain readable historical analogues without becoming active capital signals.

M2 was independently re-read and shows that WATCH / INVESTIGATE / CONFIRMED do not provide a stable monotonic capital-weight mapping: several state-return differences have 95% confidence intervals crossing zero and transition errors remain economically material.

M4 is **not load-bearing evidence** because its replication checksum failed and `decision_eligible=false`. Its correct role is a governance example: a failed reproducibility gate must block capital-rule promotion even when a headline return delta appears favorable.

### Cycle D conclusion

Together, M2 plus the production P1-1C state regressions support separation of lifecycle, thesis, opportunity, decision, freshness and capital authority.

`CCL-20260828-L03-REVERSIBLE-INDEPENDENT-STATES` is **supported and protocol-promotion eligible**, but is not marked `promoted` until a reusable Skill protocol update is separately approved and completed.

## Lesson-state decisions

| Lesson | Result after P1-1D cycle 1 |
|---|---|
| L01 Normalize valuation denominator | SUPPORTED; simple FCF/Earnings quality proxy rejected; not promotion-ready |
| L02 Per-share conversion firewall | SUPPORTED; quantitative evidence strong; protocol-promotion eligible with lifecycle scope |
| L03 Reversible independent states | SUPPORTED; M2 + production state regression support; protocol-promotion eligible |
| L04 Revision vs rerating | CANDIDATE; requires PIT estimate-revision event study |
| L05 Growth persistence mechanism | CANDIDATE; ontology and historical validation still required |
| L06 Price zone requires evidence state | **SUPPORTED PROCESS RULE**; not an alpha claim |
| L07 Lifecycle-conditioned conversion | **SUPPORTED**; universal FCF factor rejected |

## Explicit non-lessons retained

- Large earnings gap implies chase.
- Low P/E implies value.
- High valuation implies avoid.
- Once avoid, always avoid.
- Headline revenue growth implies shareholder return.
- Crossing an entry-price zone implies automatic buy.
- One universal FCF-yield factor works across lifecycles.
- FCF/Earnings ratio is a universal valuation-denominator-quality gate.

## Promotion gate

No lesson is silently marked `promoted` in this cycle.

Promotion requires a separate protocol change that preserves scope, counterexamples and the Case/Quant evidence lineage. Current promotion queue:

1. **L03** — independent/reversible states and no state-to-capital shortcut.
2. **L02** — business growth must bridge to shareholder cash flow and diluted per-share value; lifecycle-specific implementation required.

## Next outcome checkpoints

Continue append-only Investment Result Reviews at meaningful information horizons, not daily price noise:

- ALNY: next material guidance/launch evidence or ~1–3 month checkpoint.
- CRWV: capital-conversion/debt/lease/utilization evidence and stabilization checkpoint.
- MU: earnings/ASP/HBM/SCA evidence and normalized-EPS floor.
- VRT: delivery conversion + FY2027/FY2028 estimate revisions.
- CEG: contracted/Base earnings, Calpine integration, deleveraging and fleet availability.

Do not upgrade short-window results into long-horizon investment rules.
