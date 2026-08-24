# TRQuant Decision-Grade Review Gate v1

**Effective date:** 2026-08-23  
**Purpose:** Provide a non-scoring promotion gate from `research_complete` to `decision_grade`.

A case is not promoted because it is long, bullish, popular, or well researched. Promotion means the current security-level decision is sufficiently specified and auditable to guide capital allocation or deliberate no-action.

## Required gates

### G1 — Evidence integrity
- Load-bearing reported facts are traceable to primary/authoritative sources whenever reasonably available.
- Availability/PIT dates are valid and semantically compatible.
- Reported fact, management guidance, sell-side forecast, market expectation and inference remain distinct.
- Material source conflicts are resolved or explicitly non-load-bearing.

### G2 — Economic underwrite
- The dominant variable is explicit.
- The value-driver chain reaches shareholder economics rather than stopping at theme, orders, backlog, capacity or revenue.
- Material counter-evidence and the weakest link are visible.

### G3 — Valuation and expectations
- A current completed-session price or equivalent decision-date price is recorded.
- Share-count, cash/debt/lease and currency conventions are reproducible when load-bearing.
- The case contains an expected-return, reverse-valuation or other explicit price-to-operating-outcome bridge.
- Good business quality is not used as a substitute for security attractiveness.

### G4 — Decision logic
- The case states a current action: investigate, watch, start small, buy/add, hold, trim, exit or avoid.
- Entry/wait/add/trim/reopen conditions are explicit where applicable.
- A known material near-term event is either incorporated into the decision or treated as an event blocker.

### G5 — Risk / invalidation
- Thesis-kill criteria are explicit and economically causal.
- Volatility risk is distinguished from thesis risk.
- A material adverse condition triggers re-underwriting or exit rather than an undefined request for more confirmation.

### G6 — Capital and exit framework
- Positive-capital decisions specify a provisional sizing envelope or a clear rule for deriving size from confidence, expected return, downside, liquidity, correlation and portfolio exposure.
- `AVOID` / zero-capital decisions may pass with `size = 0`, but must define the evidence required to reopen the case.
- Exit/trim/review triggers are explicit where relevant.

### G7 — Freshness / decision stability
- No known imminent event is likely to make the current underwrite obsolete before capital can rationally be deployed, unless the case is explicitly event-ready and the decision already accounts for that event.
- The current action is supported by evidence available as of the stated decision date.

## Promotion outcomes

Promotion uses **gates, not a weighted score**:

- `READY_FOR_DECISION_GRADE_APPROVAL` — all analytical/technical gates pass; only explicit reviewer/founder approval remains if required by the case.
- `NEAR_READY_REMEDIATION` — the full decision architecture exists, but one or more narrow deterministic/evidence gaps remain.
- `EVENT_BLOCKED` — a known near-term event is likely to materially change the underwrite.
- `EVIDENCE_BLOCKED` — a load-bearing commercial, financial, ownership, valuation or source-quality gap remains.
- `REFERENCE_COUNTEREXAMPLE` — useful for cross-case learning but not currently worth promotion work.
- `DECISION_GRADE` — explicitly promoted after the relevant approval/review; may be bullish, neutral or `AVOID`.

## Important asymmetry

`decision_grade` does **not** mean `BUY`.

A zero-capital `AVOID` can be decision-grade when evidence is sufficient to justify no exposure, the decision is robust to remaining unknowns, and reopen conditions are explicit. Conversely, an exciting positive thesis should remain `research_complete` when valuation, sizing, cash conversion, customer economics or an imminent event is not yet underwritten.

## Governance

- Promotion is explicit and must be recorded in a review/promotion artifact; never silently change status.
- Preserve prior decisions; later evidence appends a review rather than rewriting history.
- Founder/reviewer approval is required when a case-specific promotion review says so.
- No promotion creates an order.
