# TSM Review — Investment Case Library Migration and Attention-Continuity Postmortem

**Date:** 2026-08-18  
**Case:** US-TSM-2025-2026  
**Review type:** migration / missed-opportunity audit / process design  

## Review purpose

This review does not claim that a TSM buy recommendation existed in 2025. It reconstructs what was knowable at the first recovered user-side research date, separates that from later outcomes, and asks which process controls could have converted awareness into persistent research and an explicit action/no-action decision.

## PIT finding: the long AI-capex cycle was already researchable before 2025-08-19

By 2025-04-17, TSMC management had publicly stated that:

- AI-accelerator revenue was expected to double in 2025;
- CoWoS capacity was being doubled in 2025;
- based on customer and customers' customer demand, TSMC's planning framework expected AI-accelerator revenue growth to approach a mid-40s percentage CAGR for five years starting in 2024;
- 2025 capex remained $38-42B, around 70% allocated to advanced process technologies;
- the expanded Arizona plan was intended to support strong multi-year customer demand.

By 2025-07-17, Q2 revenue was $30.07B, +44.4% YoY in USD, with 58.6% gross margin and 49.6% operating margin, and Q3 revenue guidance was $31.8-33.0B.

Before 2025-08-19, upstream customers also strengthened the evidence set. Alphabet raised 2025 capex to about $85B and expected another increase in 2026 while describing a tight cloud demand-supply environment into 2026. Meta guided to $66-72B of 2025 capex and expected another year of similarly significant dollar growth in 2026 to bring additional AI capacity online. Microsoft's FY2025 property/equipment additions were $64.55B.

The ex-ante conclusion is therefore not that the later stock appreciation was obvious. It is narrower: **there was already enough primary-source evidence to justify persistent monitoring and event preparation.**

## Failure classification

### Awareness

Not the main failure. TSM was explicitly inside the research universe by 2025-08-19.

### Recognition

Not the main failure. The company was recognized as an important semiconductor/AI beneficiary.

### Research

Partial failure. The record does not show a fully documented valuation/expectation-gap case at the first research date.

### Preparation

Material failure. No recovered pre-event matrix defined what monthly revenue, earnings, hyperscaler capex, N2/CoWoS progress or valuation state would cause an action.

### Priority/resource allocation

Likely secondary failure. Later recollection indicates attention moved to other work/A-shares. A legitimate higher-priority task can interrupt research, but it should not silently remove a core case from the monitoring queue.

### Monitoring

Primary failure. The case lacked a persistence mechanism linking `thesis -> next evidence node -> review -> action/no action -> next evidence node`.

### Execution

Not established. No verified contemporaneous buy decision or position record was recovered. Calling this an execution failure would use hindsight to invent a decision that may not have existed.

## Price/result attribution from first recovered research date

TSM closed $232.70 on 2025-08-19 and was about $420 at the 2026-08-18 review, a price increase of about 80.5% excluding dividends.

Over the same period, TTM ADR EPS rose from about $8.77 to $13.86, roughly +58%, while TTM P/E rose from about 26.5x to 30.3x. A simple logarithmic decomposition attributes roughly three-quarters to four-fifths of the price move to earnings growth and roughly one-quarter to multiple expansion. This is a valuation bridge, not a causal trading-flow regression.

Capital structure contributed little to the rerating: TSMC remained net cash and share count was essentially flat. The migration does not assign a precise residual to SOX/market beta, FX, Taiwan risk premium or positioning without a dedicated factor regression.

## Counterfactual event-ready process

Had today's discipline existed, the process would not have said 'buy TSM because AI is strong.' It would have created the following recurring triggers:

1. **TSMC quarterly earnings:** update revenue, HPC share, advanced-node mix, margin, EPS, CFO, capex, FCF and guidance.
2. **TSMC monthly revenue:** mandatory quarter-guidance bridge, even when no human analyst is actively working on TSM.
3. **Hyperscaler capex changes:** Meta/Alphabet/Microsoft/Amazon material increases or cuts automatically reopen the TSM case.
4. **Technology/capacity:** N2/A16, CoWoS/advanced packaging and major design/customer changes reopen the case.
5. **Valuation:** material price reset with intact evidence creates an add review; material price expansion without estimate revision creates a trim/no-chase review.
6. **Staleness:** passing a scheduled evidence node without review creates `stale_attention`, not silent disappearance.

## Golden Case comparison

### CRWV — same capital-intensity question, different capital structure

**Similarity:** both require a conversion chain from AI demand through physical capacity to shareholder economics.  
**Difference:** CRWV's chain is constrained by financing, interest, debt/leases and unproven shareholder FCF; TSMC's financing burden is small, balance sheet is net cash and operating profitability is proven.  
**Transferred question:** incremental capex must be judged by productivity and shareholder cash conversion, not by headline demand alone.  
**Failure mode:** not the same. CRWV is primarily a capital-conversion/valuation risk case; TSM is primarily an expectations/attention-continuity case.

### SNDK — event readiness is the common process variable

**Similarity:** both show that a known future evidence event should be prepared before it happens rather than researched after the move.  
**Difference:** SNDK centered on a discrete Investor Day; TSM has a richer recurring information stream, including monthly sales plus quarterly results and upstream customer capex.  
**New variable exposed by TSM:** `evidence cadence density` — securities with frequent, high-quality evidence deserve persistent automated attention even if the analyst's manual focus moves elsewhere.

### ALNY — thesis confidence versus expectation state

**Similarity:** both require business quality, expectations and trade setup to be separated.  
**Difference:** ALNY is useful as an expectation-reset/re-ignition analogue; TSM is a high-consensus compounder where the investor usually needs either a price reset or another earnings-revision wave.  
**Transferred question:** what exact evidence would cause the market's earnings path to change from today's already-known thesis?

## Candidate reusable lessons

### A. Case-specific observation

TSM was known and researched, but the investment process did not maintain a persistent evidence queue as attention moved elsewhere.

### B. Candidate reusable lesson

For a thesis-ready core security, **attention continuity should be explicit state**. If a scheduled material evidence node passes without review, the system should mark `stale_attention` and surface the case rather than allowing it to disappear.

### C. Counterexample / limitation

Not every watched security deserves permanent monitoring. A low-conviction idea, structurally impaired thesis or consciously deprioritized opportunity may correctly leave the active queue. Persistent monitoring must therefore require an explicit case priority and next evidence node, otherwise it becomes alert overload.

### D. Promotion evidence needed

Before making `stale_attention` a promoted Skill rule, validate it across additional cases where the security was already understood but later missed because attention shifted. SNDK is supportive on event readiness; NVDA/MU or another long-duration monitored case would provide stronger cross-case evidence.

## Skill-update recommendation

**Do not modify the core Skill solely because of TSM.** The existing equity-investment-case Skill already states that attention allocation, event readiness and missed-opportunity stage diagnosis matter. TSM supports those principles rather than contradicting them.

A future Skill update may be justified after cross-case validation to add a more operational contract:

`core_case_priority + next_evidence_node + due_review + stale_attention_state + explicit_deprioritization_reason`

This belongs first as a candidate process extension in the Case Library, not as an immediate universal rule.

## Next questions worth validating

1. Canonicalize quarter-end FX and recompute TSM EV/Operating Income and FCF yield history deterministically.
2. Retrieve any other brokerage/account records before concluding there was definitively no 2025 TSM trade outside the connected IBKR account.
3. Run a TSM vs semiconductor benchmark attribution from 2025-08-19 to 2026-08-18 to separate sector beta from idiosyncratic earnings/multiple rerating.
4. Reconstruct archival sell-side consensus, if available, at 2025-08-19 and 2025-10-16; otherwise retain the current price-implied expectation methodology.
5. Test `stale_attention` against SNDK, NVDA and MU before promoting it to core protocol.
