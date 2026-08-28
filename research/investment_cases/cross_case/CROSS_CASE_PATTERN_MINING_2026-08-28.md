# TRQuant P1-1B Cross-Case Pattern Mining — 2026-08-28

## Scope

Source of truth: TRQuant Research Control V1.

Research Control source commit used for the cross-case read: `f2bc6efa61180e24a0b3b82c3a136d484b4554b1`.

Dataset state at start: 40 US Cases, 40 V1-native, Foundation Ready PASS.

This review does not promote any universal trading or capital-allocation rule. It identifies cross-case lessons, searches for disconfirming cases, and defines falsifiable validation work.

## Method

Use the ladder:

`case observation -> cross-case comparison -> counterexample -> candidate/supported lesson -> quantitative or regression validation -> later promotion decision`

Cases were compared by economic mechanism rather than ticker/sector similarity. Representative reads included HTFL, COST, WBA, OXY, MU, AZO, FRC, CRWV, META, BBY, NVDA, PTON, INTC and ALNY.

---

## L01 — Normalize the valuation denominator before calling something cheap or expensive

**State:** SUPPORTED

**Claim:** A headline valuation multiple is unreliable when the denominator is cyclically extreme, economically incomplete, structurally deteriorating, or not the relevant residual claim. First normalize the earnings/cash-flow denominator and capital structure; then judge valuation.

**Cross-case support**

- MU: a very low forward P/E can be an optical peak-cycle earnings trap; normalized EPS and the durability of the memory/HBM floor matter more.
- WBA: low P/E/high yield did not establish value because normalized FCF, reinvestment needs, healthcare losses, leases/debt and dividend sustainability were deteriorating.
- OXY: deep value depended on survival and debt repayment transferring enterprise value to common equity; a simple earnings multiple missed the leverage convexity.
- FRC: P/B and accounting capital became secondary once runnable uninsured funding and forced-sale asset values dominated survival.
- COST: the denominator is comparatively durable, but a great business can still have weak expected return when the starting premium multiple capitalizes too much future compounding.
- INTC: a large drawdown and strategic narrative did not make the stock conventionally cheap; normalized future per-share earnings after foundry losses, capex and dilution remained the key denominator.

**Disconfirming boundary:** In stable, asset-light, mature businesses with durable cash conversion and limited balance-sheet distortion, conventional forward valuation measures may be more informative. Even there, starting expectations still matter.

**Implementation consequence:** Every Investment Case should identify `valuation_denominator_quality` before applying headline P/E, EV/EBITDA, P/B or EV/Sales.

**Quant test:** Compare forward-return ranking from raw valuation multiples with versions conditioned on earnings cyclicality, FCF conversion, leverage/liquidity, share-count change and capex intensity. Test 6/12/24-month excess return and drawdown.

---

## L02 — Per-share conversion is the common economic firewall

**State:** SUPPORTED

**Claim:** Revenue growth, backlog, assets, policy support or operating profit are not sufficient investment outcomes. The common endpoint is durable per-share value after capex, financing, debt/leases, interest, taxes, royalties and dilution/buybacks.

**Cross-case support**

- CRWV: contracted AI demand must become active capacity, utilization, operating profit and shareholder cash flow faster than debt, leases, interest and dilution expand.
- ALNY: strong revenue growth can still produce modest expected return if royalties, interest, opex and other claims keep FCFE-like conversion weak.
- INTC: process/foundry success must survive manufacturing capex and diluted-share growth to create per-share value.
- AZO: modest business growth can create much stronger per-share compounding when durable FCF is used to retire shares at sensible prices.
- OXY: debt reduction shifts value from creditors toward common equity even without requiring extraordinary permanent business growth.
- NVDA: the relevant endpoint remains core operating earnings/FCF and per-share value, not AI capex or revenue growth alone.

**Disconfirming boundary:** The conversion bridge can be short in asset-light businesses with low reinvestment and little financing complexity, but it should still be explicit.

**Implementation consequence:** Standard value-driver chains should terminate at `shareholder_fcf -> diluted_share_count -> per_share_value`, not at revenue/EBITDA.

**Quant test:** Build a cross-sectional `per_share_conversion` factor using revenue/EBIT growth, OCF/FCF growth, capex intensity, net-debt change and diluted-share-count change. Compare it with headline growth alone.

---

## L03 — Lifecycle, thesis, opportunity and decision state must be independent and reversible

**State:** SUPPORTED as a research-process principle; NOT a trading rule.

**Claim:** A lifecycle label or prior decision must not permanently determine opportunity status. Re-underwrite when dominant variables change. Conversely, genuine deterioration must be allowed to remain terminal when evidence does not repair.

**Cross-case support**

- HTFL: `False New Ignition` was a valid lifecycle correction, but the opportunity remained active; lifecycle classification and opportunity state were not equivalent.
- META: a valid 2022 avoid state should not become permanent after cost discipline, revenue growth and operating margin materially repaired.
- NVDA: a mature, widely recognized structural winner should not be automatically removed from research attention because it has already appreciated or consensus is high.
- PTON: demand pull-forward and fixed-cost/inventory overbuild show that some deterioration is economically real and should not be reversed without repair evidence.
- FRC: a runnable funding model can become terminal; reversibility is evidence-dependent, not automatic optimism.

**Implementation consequence:** Keep at least these independent fields:

`lifecycle_state`, `thesis_state`, `opportunity_state`, `decision_state`, `evidence_freshness`.

Transitions require evidence; no label is permanent merely because it was once correct.

**Validation:** Use regression fixtures HTFL, META, NVDA, PTON and FRC. This is primarily a state-machine/governance validation, not a return backtest.

---

## L04 — Separate estimate revision from multiple rerating and price acceptance

**State:** SUPPORTED conceptually; quantitative edge still unvalidated.

**Claim:** After a catalyst, decompose the stock move into (1) fundamental/estimate revision, (2) valuation/multiple rerating and (3) price acceptance. A large positive price move is not equivalent to an equally large improvement in the forward economic path.

**Cross-case support**

- HTFL: FY2026/FY2027 revenue consensus rose about 8–9%, while the stock rose about 47% through 2026-08-19; reconstructed forward EV/Sales expanded materially. Business improvement and multiple expansion were both real and had to be separated.
- MU: FY2027 EPS expectations rose sharply, but the low headline P/E still required normalized-cycle analysis; revision velocity and valuation denominator were distinct variables.
- NVDA: the prospective add rule explicitly prefers situations where forward revenue/EPS expectations rise faster than price rerates.
- COST: near-zero positive estimate revision means the investment case is mainly quality compounding plus multiple duration, not an expectation-reset trade.
- ALNY: long-run revenue opportunity can coexist with modest expected return when cash conversion and current price already embed substantial success.

**Implementation consequence:** Catalyst reviews should record `estimate_revision`, `price_change`, `multiple_change`, and `price_acceptance` separately.

**Quant test:** For earnings/guidance events, test whether forward returns differ when estimate revisions exceed price rerating versus when price rerating materially exceeds estimate revisions. Preserve PIT expectations.

---

## L05 — Growth quality requires persistence evidence, not headline growth

**State:** SUPPORTED as an underwriting principle; statistical thresholds remain CANDIDATE.

**Claim:** High growth should be classified by persistence mechanism. Distinguish externally pulled-forward demand from installed-base/recurring economics, contractual demand, second-product adoption, and structural value-pool expansion.

**Cross-case support**

- PTON: pandemic demand was partially pulled forward; hardware growth plus fixed-capacity expansion did not represent a durable growth rate.
- HTFL: Q2 acceleration was real, but it was a second-product S-curve on top of an established FFRCT franchise, not first-company ignition.
- MU: HBM demand and strategic customer agreements may raise the normalized floor, but the commodity supply response still matters.
- NVDA: AI-compute growth must be supported by customer monetization, system-level economic share and durable demand quality rather than capex headlines alone.
- CRWV: backlog must convert through deployment/utilization and financing economics before it proves durable shareholder growth.

**Implementation consequence:** Growth cases should tag the persistence mechanism explicitly: `shock_pullforward`, `recurring_installed_base`, `contracted`, `second_s_curve`, `structural_value_pool`, or `cyclical_scarcity` where appropriate.

**Quant test:** Compare forward outcomes for high-growth firms stratified by persistence proxies: recurring revenue share, contract/backlog conversion, capex/fixed-cost response, inventory build, and post-event revenue persistence.

---

## What did NOT qualify as a cross-case rule

1. `Big earnings gaps should be chased` — rejected as unsupported. HTFL is one short-window case and explicitly does not establish this rule.
2. `Low P/E means value` — contradicted by MU/WBA/INTC and incomplete without normalization.
3. `High valuation means avoid` — contradicted by the need to compare price with revision/compounding path; NVDA/COST illustrate different high-expectation states.
4. `Once avoid, always avoid` — contradicted by META and the required reversible state model.
5. `Strong revenue growth means strong shareholder return` — contradicted by CRWV/ALNY/INTC conversion mechanics.

---

## Validation priority

### P1 — Per-share conversion quality
Highest priority because it spans growth, cyclical, biotech, turnaround and capital-allocation cases and can be tested with broad fundamental data.

### P2 — Normalized valuation denominator
High priority because it directly addresses value traps, peak-cycle P/E traps and leverage/liquidity distortions.

### P3 — Estimate revision versus price rerating
High potential value, but requires reliable PIT analyst-expectation history. Do not substitute current consensus for historical PIT expectations.

### P4 — Growth persistence classification
Important but data ontology is harder; begin with smaller validated datasets before full-universe automation.

### Process regression — Reversible independent state model
Implement/test as governance logic using case fixtures rather than treating it as an alpha factor.

---

## Readiness after this review

- Foundation Ready: PASS / CLOSED.
- Pattern Mining: ACTIVE and producing cross-case lessons.
- L01/L02/L03: supported enough to proceed to formal validation/design work.
- L04/L05: supported conceptually but still require quantitative threshold validation.
- No lesson is promoted into universal screening, execution or capital-allocation authority from this review alone.
