# TRQuant Case Library Coverage Audit — 2026-08-28

## Production state

Research Control independently verified after the PIT metadata correction:

- US Cases: 40
- V1-native US Cases: 40
- legacy-compatible: 0
- legacy-partial: 0
- registry/case integrity-error Cases: 0
- Case Library dirty: false
- Research Control: HEALTHY
- runtime drift: MATCH
- write eligible: true
- transaction journals: 0
- initial-case journals: 0

Targeted PIT timeline audits passed for all six newly added historical anchors:

- KO — AUDITED, warnings = [], integrity_errors = []
- AZO — AUDITED, warnings = [], integrity_errors = []
- BBY — AUDITED, warnings = [], integrity_errors = []
- OXY — AUDITED, warnings = [], integrity_errors = []
- GE — AUDITED, warnings = [], integrity_errors = []
- ATVI — AUDITED, warnings = [], integrity_errors = []

The earlier same-day creation-time metadata defects in KO-E003, AZO-E003, OXY-E004 and GE-E004 were corrected to the canonical first-recorded timestamps. Historical company/regulatory source availability was not changed.

## 1. Lynch coverage

| Lynch category | Representative anchors | Coverage |
|---|---|---|
| Slow Grower | KO, SO | PASS |
| Stalwart | COST, JPM, JNJ, UNH | PASS |
| Fast Grower | NVDA, VRT, CRWV, HTFL, ALNY | PASS |
| Cyclical | MU, CAT, XOM, OXY | PASS |
| Turnaround | BBY, META, INTC, WBA | PASS |
| Asset Play | GE, PLD | PASS |

## 2. Investment-style coverage

| Style / approach | Representative anchors | Coverage |
|---|---|---|
| Structural growth | NVDA, VRT, GEV | PASS |
| Quality compounder | COST, JPM, JNJ | PASS |
| Slow-growth income | KO, SO | PASS |
| Cyclical | MU, CAT, XOM | PASS |
| Deep value / distressed | OXY positive; WBA negative/value-trap contrast | PASS |
| Turnaround | BBY positive; WBA negative; INTC unresolved; META re-ignition | PASS |
| Capital allocation | AZO | PASS |
| Asset unlock / SOTP | GE | PASS |
| Real asset / REIT | PLD | PASS |
| Special situation / merger arbitrage | ATVI | PASS for Foundation; negative pair desirable for later Pattern Mining |
| Event / earnings revision | HTFL, MU | PASS for research; longer Outcome horizon still developing |
| Re-ignition | META | PASS |
| Capital-intensive growth | CRWV | PASS |
| Regulated utility | SO | PASS |
| Bank / funding model | JPM, FRC | PASS |
| Insurance underwriting | PGR | PASS |
| Healthcare payer | UNH | PASS |
| Biotech / clinical-regulatory | ALNY and additional healthcare Cases | PASS |
| Product adoption / second S-curve | HTFL | PASS |

## 3. Positive / negative balance

Positive / successful mechanism anchors include NVDA, BBY, OXY, GE, ATVI, META, AZO and KO.

Negative / failure / avoid anchors include PTON, WBA, FRC and unresolved value-trap/turnaround risk in INTC.

Process-error / missed-opportunity anchors include HTFL and NVDA-related attention-allocation work.

The whole-library positive/negative balance is adequate. Narrow mechanisms should still seek specific counterexamples during Pattern Mining.

## 4. Historical span / regime coverage

Representative anchors cover materially different periods:

- 2012-2017: BBY turnaround
- long-duration pre-2020 mechanism history: KO dividend compounding; AZO share-repurchase compounding
- 2020-2022: PTON demand pull-forward; OXY distressed deleveraging; META thesis break; GE separation plan
- 2022-2023: ATVI special situation / regulatory path
- 2023: FRC funding failure
- 2024-2025: WBA value/dividend-trap outcome
- 2025-2026: HTFL and current governed Cases

Historical-regime diversity is adequate for Foundation-level development.

The main structural weakness is the natural age of governed ex-ante TRQuant decisions: many current decision records began in August 2026, so 6-, 12-, and 24-month Outcome Reviews must accumulate naturally.

## 5. Research maturity

Do not treat all 40 V1-native Cases as equally mature.

Reference-grade Cases such as COST, MU and INTC contain richer decision ledgers, timelines, valuation histories, monitoring and repeated reviews.

KO, AZO, BBY, OXY, GE and ATVI are intentionally `research_complete` historical mechanism anchors. They do not imply contemporaneous historical TRQuant recommendations.

## 6. Readiness conclusion

### Classification / mechanism coverage — PASS

The 40-Case dataset covers the required major archetypes and styles.

### Foundation Ready — PASS / CLOSED

All six targeted historical anchors pass PIT timeline audit. Research Control is HEALTHY/MATCH, all 40 US Cases are V1-native, there are zero integrity errors, no dirty library state and no leftover transaction journals.

The Case Library is now sufficiently complete to serve as the foundation for Cross-Case Pattern development, Multi-Axis analogue retrieval, Investment Result Review development, candidate-lesson generation and quantitative-validation design.

### Pattern Mining — READY TO START / MATURITY STILL ACCUMULATING

Pattern Mining may begin now. Candidate lessons must continue to be tested against disconfirming Cases and should remain scoped until they survive cross-case review.

### Rule Promotion — NOT YET GLOBAL

No universal screening, execution or capital-allocation rule should be promoted from the Case Library alone. Statistical claims require substantially larger independent samples and explicit false-positive/false-negative validation.

## 7. Remaining non-blocking gaps

1. Negative merger-arbitrage / broken-special-situation pair for ATVI.
2. More 6-12 month governed Outcome Reviews.
3. More 24+ month governed Outcome Reviews.
4. More full-cycle governed decisions across regime change.
5. Narrow mechanism-specific counterexamples discovered during Pattern Mining.

Add a new Case only when one of these gaps materially limits a research conclusion.

## Governing loop

`Coverage gap -> smallest sufficient Case addition -> Outcome Review -> cross-case comparison -> quantitative validation -> coverage re-audit`
