# Case-Library Review -> Skill Evolution Specification — 2026-08-23

**Source:** 21-case decision-grade review across US / CN_A / HK.  
**Status:** implementation specification, not an automatic core-Skill rewrite.

## 1. Supported lesson to retain by default

### Supplier evidence conversion ladder

**Status:** Supported in the case-learning layer.  
**Cases:** 飞荣达, 领益智造, 雷赛智能, 同星科技, 绿的谐波, 奥比中光, 拓普集团, 双环传动, 卧龙电驱, 飞龙股份, 中大力德, 日发精机; with broader analogy to capital-conversion cases such as CRWV.

**Principle:**

`capability -> named design-in/cooperation -> validation -> small batch -> stable batch -> material recognized revenue -> margin contribution -> CFO/FCF -> EPS revision`

Do not skip economic layers. A company may be strong at one stage and weak at the next.

**Research behavior changed:**
- A theme scan may use capability/partnership evidence to allocate attention.
- A security-level thesis must identify the highest verified rung and the missing next rung.
- “Can make”, “partner”, “supplier list”, “capacity”, “order”, and “batch delivery” must not be collapsed into revenue/profit/cash-flow evidence.
- When the verified rung is below material revenue/margin/cash conversion, valuation should treat the exposure as an option or early-stage contribution rather than as mature earnings unless an explicit scenario bridge is provided.

## 2. No new core rule for points already covered

Do **not** add redundant core rules for:
- business/theme quality vs stock attractiveness;
- order/backlog/capacity vs recognized revenue and shareholder cash flow;
- reverse valuation / price-implied expectations;
- deliberate no-action as a valid decision;
- events as re-underwrite triggers rather than automatic trade signals;
- sizing from expected return/downside/correlation rather than confirmation count.

These are already represented in the existing Equity Investment Case protocol.

## 3. Candidate lessons — retain, do not promote yet

### A. Fast-changing BOM claims require versioned identity
`robot platform + model + year/version + component + evidence date + supplier role` should be the default identity for load-bearing BOM claims.

Reason: TianGong 2025/2026 transmission and thermal architectures changed, and exclusivity claims decayed quickly.

**Promotion evidence needed:** additional fast-iteration hardware ecosystems beyond humanoid robotics.

### B. Listed-parent value capture must be ownership adjusted
When the attractive business sits in a subsidiary/JV, translate subsidiary value to the listed parent through ownership, dilution, minority interest, capital requirements and cash-remittance economics.

**Promotion evidence needed:** test across robotics, semiconductors, biotech subsidiaries/JVs and infrastructure SPVs.

### C. Same operating company may justify different security actions
Dual-listed A/H or ADR/local securities can have materially different price-implied expectations, liquidity, investor base, currency and corporate-action risk. Operating evidence may be shared; security actions must remain separate.

**Promotion evidence needed:** additional A/H and ADR/local cases with actual return/flow history.

### D. Active-cooling convergence is an opportunity-discovery map, not a stock rule
AI compute and high-power humanoid robotics both increasingly require active thermal management, but this only identifies a cross-theme research map. It does not prove that a specific supplier captures economics in both markets.

**Promotion evidence needed:** verified cross-market customer revenue/margin evidence across multiple suppliers and end markets.

## 4. Decision-grade gate integration

Future case reviews should reference:
`research/investment_cases/library_reviews/decision_grade_gate_v1.md`

A case is eligible for promotion only after evidence integrity, economic underwrite, valuation/expectations, decision logic, risk/invalidation, capital/exit and freshness gates pass.

Important: `decision_grade` is not synonymous with `BUY`. A well-supported `AVOID` with `size=0` and explicit reopen conditions can qualify.

## 5. What should not be automated

Do not automatically:
- promote a case because all JSON fields are populated;
- turn a high evidence rung into a Buy;
- convert an event date into an order;
- change size because a case receives more confirmations;
- promote a candidate lesson to a core Skill rule from one industry cluster.

## 6. Recommended future implementation

At case creation/review time, expose deterministic metadata fields such as:
- `highest_verified_evidence_rung`;
- `next_missing_economic_rung`;
- `decision_grade_gate_status`;
- `event_blocker`;
- `promotion_blockers`.

These fields should support retrieval/audit only. Final investment judgment remains in the reasoning/review layer rather than a fixed composite score.
