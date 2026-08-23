# HTFL Review — False New Ignition Re-underwrite

**Date:** 2026-08-18  
**Case:** US-HTFL-2025-2026  
**Review type:** lifecycle correction / scanner regression case

## What changed

The original scanner escalation was useful: HTFL deserved P0 attention after Q2 2026 showed revenue acceleration, Plaque adoption, guidance revision, gross-margin expansion and a major price/volume response. The error was the next step: treating those signals as sufficient evidence for `New Ignition`.

Deep research showed that Heartflow was already an established public growth company with a mature FFRCT franchise. FFRCT represented 98% of 2025 revenue. Q2 2026 is better understood as **Plaque second-S-curve confirmation plus a major valuation rerating**, not a first-company ignition.

## False-stage root cause

The scanner effectively passed:

- structural relevance;
- fundamental acceleration;
- catalyst significance;
- price/volume confirmation.

It did not adequately complete four gates before assigning lifecycle state:

1. **Prior lifecycle history:** IPO and prior 40% growth were already known; the core company was not at first discovery.
2. **Metric ontology:** +74% revenue cases did not mean +74% unique patient/procedure volume because FFRCT + Plaque on one CCTA count as two cases.
3. **Current diluted valuation:** after the gap, economic diluted equity value was about $4.05B and EV about $3.80B.
4. **Reverse mathematical room:** at about 15.3x FY2026 EV/Sales, a 3x/5x outcome over a four-year window required very demanding revenue growth and terminal multiples.

The corrected state is:

`P0 Active Case + Confirmation / Early Momentum + second-product S-curve optionality`

not:

`Confirmed New Ignition`.

## Why the business thesis actually improved

The lifecycle downgrade is not a business downgrade. Q2 2026 strengthened the case:

- revenue $64.1M, +48% YoY;
- revenue cases 84,491, +74%;
- GAAP gross margin about 83%;
- Plaque revenue $7.8M management commentary;
- FY2026 revenue guide $246-250M;
- Plaque guide $29-31M;
- FFRCT utilization remained durable;
- management continued to target ~85% mid-term non-GAAP gross margin and mid-2028 cash-flow profitability.

The important change is that **thesis confidence rose while price-implied expectations also rose sharply**. Those two variables must not be collapsed.

## Reverse-return implication

At the 2026-08-14 close of $42.08, approximate economic diluted shares were 96.24M and EV approximately $3.80B. Against $248M FY2026 revenue guidance midpoint, EV/Sales was ~15.3x.

Using an illustrative 105M diluted shares in 2030 and $150M net cash:

- at a 10x terminal sales multiple, a 3x stock outcome requires roughly $1.31B revenue in 2030, ~52% CAGR from the FY2026 midpoint;
- a 5x outcome requires roughly $2.19B, ~72% CAGR;
- a 10x outcome requires roughly $4.40B, ~105% CAGR.

These calculations do not say HTFL cannot be a long-run multibagger. They say **the current post-gap state does not satisfy a strict near/medium-horizon first-ignition mathematical-room test**.

## Scanner/Skill candidate changes

Do not change the core principles from one case. Add implementation guardrails:

- Make `P0 priority` and `lifecycle state` separate required output fields.
- Scanner `new_ignition` is provisional until current economic diluted EV is available.
- Require reverse 3x/5x/10x math or equivalent right-tail feasibility test before confirmed New Ignition.
- Require prior-lifecycle check: first ignition vs second S-curve vs reset/re-ignition.
- Require metric ontology before comparing growth metrics across candidates.
- A >20% catalyst gap should automatically trigger `reunderwrite_at_new_price`.
- Maintain HTFL as a canonical `false_stage` regression example.

## Cross-case support

CRWV already supports the broader principle that a correct high-growth business thesis can coexist with a poor or demanding entry after multiple expansion. TSM supports the distinction between a widely recognized structural winner and an early discovery-stage opportunity. HTFL adds a new implementation-specific failure mode: **a second-product S-curve plus a huge event gap can look like New Ignition unless lifecycle history and diluted-EV math are forced into the classifier.**

## Promotion status

Lesson state remains `candidate`. Promote only after testing against true early winners, false-positive post-IPO growth names and second-S-curve platform cases using PIT data.
