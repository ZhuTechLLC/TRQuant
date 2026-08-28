# TRQuant Case Library Completeness Standard

Version: 2026-08-28

## Purpose

Case Library completeness is not defined by raw case count. A dataset is considered sufficiently complete only when it has adequate coverage across investment archetypes, economic mechanisms, lifecycle states, positive and negative outcomes, time horizons, and research maturity.

The Case Library is used to generate and test research hypotheses. It is not, by itself, statistical proof of a trading or capital-allocation rule.

## 1. Required multi-axis taxonomy

Every Case should be classifiable on the following independent axes.

### A. Lynch category

- Slow Grower
- Stalwart
- Fast Grower
- Cyclical
- Turnaround
- Asset Play

A Case may carry more than one tag, but one primary category should be stated where meaningful.

### B. Investment style / research approach

Minimum core set:

- structural growth
- quality compounder
- classic value
- deep value / distressed
- cyclical
- turnaround
- income / dividend compounder
- capital-allocation compounder
- event / earnings revision
- special situation / merger arbitrage
- asset unlock / SOTP / spin-off
- contrarian / expectation reset
- re-ignition
- momentum / price-acceptance study

### C. Economic mechanism

Examples include:

- capital intensity
- financing dependence
- leverage / deleveraging
- customer concentration
- installed-base / recurring revenue
- regulated rate base
- real asset / cap rate / NAV
- bank funding and credit
- insurance underwriting cycle
- commodity price cycle
- semiconductor scarcity / supply response
- clinical / regulatory binary risk
- product adoption / second S-curve
- membership economics
- share-count shrinkage / buyback accretion
- conglomerate discount / separation
- merger completion probability

Analogue retrieval should prefer these economic mechanisms over ticker or sector similarity.

### D. Lifecycle

- discovery
- ignition
- confirmation
- early momentum
- mature compounder
- cyclical peak / trough
- reset
- turnaround
- re-ignition
- thesis deterioration
- terminal failure

Lifecycle and opportunity state must remain separate.

### E. Outcome class

- successful thesis
- failed thesis
- value trap
- correct avoid
- wrong chase
- missed winner
- missed opportunity
- classification error
- successful turnaround
- failed turnaround
- re-ignition
- terminal failure
- successful special situation
- broken special situation

### F. Time horizon

Evidence and review state should distinguish:

- event: 1-20 trading sessions
- short: 1-3 months
- medium: 6-12 months
- long: 24+ months
- full-cycle: from thesis formation through a material economic cycle or terminal event

A short-window outcome must not be treated as long-horizon validation.

### G. Research maturity

- draft
- evidence_verified
- research_complete
- decision_grade
- outcome_reviewed
- outcome_complete

`outcome_complete` requires an original or explicitly reconstructed decision state, later evidence, attribution, counterfactual analysis, and a sufficient observation horizon. It is not inferred from elapsed time or price direction alone.

## 2. Dataset completeness gates

### Gate 1 — Foundation Ready

Required before Cross-Case development begins:

- Research Control health = HEALTHY
- integrity errors = 0
- all active US cases readable through V1
- all six Lynch categories represented
- all core investment styles represented or explicitly marked as non-material
- major economic mechanisms represented
- both positive and negative examples present
- historical cases span more than one market regime
- historical reconstruction is clearly separated from contemporaneous decisions

Raw count is secondary. As a practical floor, roughly 30-40 high-quality US Cases is sufficient when the above coverage conditions are met.

### Gate 2 — Pattern Mining Ready

Required before promoting observations from individual Cases into supported cross-case lessons:

- Foundation Ready passed
- core archetypes have both confirming and disconfirming examples where economically possible
- multiple Reference Cases contain decisions, valuation history, timeline and repeated reviews
- outcome evidence exists across event, short, medium and long horizons
- at least several cases predate the current market regime
- candidate lessons are tested against counterexamples
- no single Case is treated as sufficient proof of a reusable rule

### Gate 3 — Rule Promotion Ready

Required before a lesson changes screening, execution or capital-allocation logic:

- Pattern Mining Ready passed
- candidate lesson supported by materially different Cases
- scope and exceptions explicitly defined
- point-in-time evidence integrity verified
- counterexamples searched and retained
- quantitative validation performed on a substantially larger independent sample when the claim is statistical
- implementation tested for false positives and false negatives
- no promotion based solely on a successful recent price outcome

## 3. Minimum coverage matrix

The dataset should maintain at least one strong anchor for each of the following mechanisms, and preferably a positive/negative pair where meaningful:

- Fast Grower / structural winner
- Slow Grower / income compounder
- Stalwart / quality compounder
- Cyclical
- Turnaround success
- Turnaround failure / value trap
- Asset Play / asset unlock
- Deep value / distressed recovery
- Capital allocation / buyback compounding
- Special situation / merger arbitrage
- Re-ignition
- Wrong chase / demand pull-forward
- Correct avoid / terminal failure
- Missed winner / missed opportunity
- Capital-intensive growth
- Regulated utility
- REIT / real asset
- Bank / funding model
- Insurance underwriting
- Commodity / energy cycle
- Healthcare payer
- Biotech / clinical-regulatory
- Product adoption / second S-curve

## 4. Current 2026-08-28 anchor additions

The following historical anchors were added specifically to close structural coverage gaps:

- KO — Slow Grower / income compounder
- AZO — capital allocation / per-share compounding
- BBY — successful operational turnaround
- OXY — distressed cyclical / deleveraging / deep-value recovery
- GE — asset unlock / corporate separation / SOTP
- ATVI — special situation / merger arbitrage

These complement existing negative and modern-growth Cases rather than replace them.

## 5. Current dataset interpretation

As of 2026-08-28, Research Control reports 40 US Cases, all V1-native, with zero integrity errors.

This is sufficient for Foundation Ready and for beginning Cross-Case / Outcome Review development.

It is not sufficient to declare mature universal investment rules. The main remaining limitation is natural time depth: many governed decisions are recent, so medium-, long-, and full-cycle outcomes must accumulate over time.

## 6. Continuous improvement rule

Use the loop:

Case -> Cross-Case Pattern -> Candidate Lesson -> Counterexample Search -> Quantitative Validation -> Investment Result Review -> Case Update

After every approximately 5 material outcome reviews or whenever a new failure mode appears:

1. rerun the coverage audit;
2. identify empty or one-sided cells;
3. add only the smallest number of Cases needed to close a real structural gap;
4. do not increase Case count merely to make the library look larger.

## 7. Naming convention

Use professional investment-research terminology:

- Outcome Review
- Investment Result Review
- Decision Review
- Outcome Complete

Avoid non-financial forensic terminology in user-facing research and future schema design.