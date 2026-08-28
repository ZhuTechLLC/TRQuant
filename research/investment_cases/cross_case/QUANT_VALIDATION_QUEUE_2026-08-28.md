# TRQuant P1-1B Quantitative Validation Queue — 2026-08-28

## Principle

Case Library generates economic hypotheses. QuantConnect validates statistical claims on substantially larger PIT samples. No result in this queue creates trade or capital authority.

QuantConnect Morningstar US Fundamentals are appropriate for broad PIT fundamental research and provide historical fundamental universes and corporate data back to 1998. Use only data available at each signal date and begin forward returns strictly after the signal timestamp.

## QV-01 — Per-share conversion quality

Linked lesson: `CCL-20260828-L02-PER-SHARE-CONVERSION-FIREWALL`

Priority: P1 / first experiment.

### Null
A factor that incorporates FCF/cash conversion, capex/financing burden and share-count change adds no forward-return information beyond headline revenue/earnings growth.

### Required inputs
- historical dynamic US fundamental universe;
- revenue/operating growth;
- operating/free cash flow where available;
- capital expenditure or capital-intensity proxy;
- diluted/basic share-count trend;
- leverage/financial-burden proxy;
- market cap and sector;
- next-session 20D/60D/120D or equivalent forward returns.

### Comparison
A. headline growth score.
B. per-share conversion score.
C. B residualized/controlled versus A and sector.

### Required outputs
- observation count and cross-sections;
- raw and rank IC;
- positive-IC ratio;
- quintile spreads;
- sector-neutral results;
- chronological holdout;
- coverage/missing-data map;
- explicit PIT and look-ahead audit.

### Fail closed
Do not replace missing FCF/share-count/leverage data with future values or current snapshots.

---

## QV-02 — Normalized valuation denominator

Linked lesson: `CCL-20260828-L01-NORMALIZE-VALUATION-DENOMINATOR`

Priority: P1 / second experiment.

### Null
Conditioning valuation on denominator quality, cyclicality and balance-sheet risk does not improve forward-return classification versus raw valuation multiples.

### Required design
Compare raw valuation measures with valuation conditioned on:
- stock/economic type;
- revenue/earnings variability or growth regime;
- cash-flow conversion;
- leverage/liquidity burden;
- capital intensity;
- share-count trend.

At minimum stratify separately for cyclical/distressed/hard-asset/high-yield/slow-growth/growth classifications where the provider taxonomy is PIT available.

### Required outputs
Same audit and metrics as QV-01, plus performance of raw P/E/P/B/EV-style measures by economic category.

### Fail closed
Do not call a proxy `normalized earnings` unless the denominator construction is explicitly reproducible.

---

## QV-03 — Estimate revision versus price rerating

Linked lesson: `CCL-20260828-L04-REVISION-VS-RERATING`

Priority: P2; execute only when PIT analyst-expectation history is available and licensed.

### Null
The relationship between estimate revision and contemporaneous price/multiple rerating has no forward-return information after controlling for surprise, sector and momentum.

### Required event fields
- pre-event PIT revenue/EPS expectations;
- reported result;
- guidance revision;
- post-event PIT expectation revision;
- event return/gap;
- multiple change;
- price acceptance;
- forward +1/+3/+5/+10/+20/+60D returns.

### Fail closed
Never use a later consensus snapshot as if it existed before the event.

---

## QV-04 — Growth persistence mechanism

Linked lesson: `CCL-20260828-L05-GROWTH-PERSISTENCE-MECHANISM`

Priority: P2/P3.

Start with ontology validation, then quantify only observable proxies.

Candidate persistence classes:
- shock pull-forward;
- recurring installed base;
- contracted/backlog-supported;
- second-product S-curve;
- structural value-pool expansion;
- cyclical scarcity.

Do not force every company into exactly one class. Multi-label is allowed.

---

## Non-quantitative regression

`CCL-20260828-L03-REVERSIBLE-INDEPENDENT-STATES` is validated first through Case regression fixtures, not return prediction.

## Execution order

1. QV-01 Per-share conversion.
2. QV-02 Normalized valuation denominator.
3. State-model regression implementation.
4. QV-03 only after PIT expectation data availability is proven.
5. QV-04 after ontology coverage is adequate.

## Promotion gate

A Candidate Lesson can move toward Skill promotion only after:
- cross-case support;
- explicit counterexample search;
- successful applicable validation;
- scope/exception definition;
- review of false-positive and false-negative behavior.
