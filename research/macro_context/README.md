# TRQuant Macro & Cross-Asset Context Library

## Purpose

Store reusable macro, cross-asset, policy, geopolitical and supply-chain states once, then link them to individual Investment Cases through explicit company-specific transmission paths.

The Macro Library does **not** answer whether a stock is a buy. It answers what external state changed, how reliable that evidence is, and which economic transmission channels may affect company cash flows, capital costs, risk premia or tail risks.

## Architecture

```text
Macro & Cross-Asset Context Library
        |
        +-- rates / inflation / growth / liquidity / credit
        +-- FX / commodities
        +-- industry-capex / semiconductor-cycle
        +-- trade / export-control / industrial-policy
        +-- geopolitics / supply-chain / operational-resilience
        |
        +--> company-specific macro_links.json
                 |
                 +--> Investment Case decision state
```

## Evidence rules

1. Store **Observed Macro Fact** separately from **Company Transmission Inference**.
2. Preserve `available_from`, `as_of`, source type and URL when possible.
3. Prefer central banks, statistical agencies, regulators, issuer IR and direct market data for load-bearing evidence.
4. Never turn a macro threshold into an automatic buy/sell rule; it is a re-underwrite trigger.
5. Do not duplicate the same macro event into every company case. Link the shared context instead.
6. Classify company relevance by channel rather than one blended macro score:
   - `direct_operating_demand`
   - `margin_fx_cost`
   - `capital_cost_valuation`
   - `policy_market_access`
   - `geopolitical_operational_tail`
7. For AI infrastructure, separate nominal CapEx from real compute capacity: accelerators/CPU/server spend, data-center buildings/networking, finance leases, component-price inflation, custom silicon, cloud demand and monetization.

## Status vocabulary

- `green`: supportive / strengthening
- `yellow_green`: supportive but with meaningful caveats
- `yellow`: mixed or material watch item
- `yellow_red`: adverse but not thesis-breaking
- `red_tail`: low-frequency/high-severity tail risk requiring explicit monitoring
- `unknown`: evidence insufficient; do not infer

## Governance

Macro state can change a valuation hurdle, scenario probability, required return, portfolio risk budget or the urgency of re-underwriting. It cannot by itself promote an Investment Case to `decision_grade`, change position sizing, or create an order without explicit review.
