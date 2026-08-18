# TSM — PIT Forward Expectations, Benchmark Attribution, Upstream Monitor, and Attention-Continuity Validation

**Case ID:** US-TSM-2025-2026  
**Review date:** 2026-08-18  
**Status after review:** research_complete  
**Scope:** Complete the four follow-up validations requested after the initial Investment Case Library migration. This review does not rewrite any historical decision and does not promote the case to decision_grade.

## 1. Founder-level conclusion

The 2025-08-19 TSM opportunity was not primarily a case in which the market was unaware of AI. By that date, AI demand, hyperscaler capital spending, TSMC advanced-node demand and CoWoS expansion were already widely visible. The more important expectation gap was **magnitude and duration**: sell-side FY2026 ADR EPS expectations were still only about $10.95, whereas the current FY2026 consensus is about $16.45. The stock's subsequent move therefore reflected a large earnings-estimate revision plus secondary multiple expansion, with strong semiconductor-sector beta also contributing.

The attention postmortem remains narrower than a generic 'execution failure.' The earliest recovered user-side explicit TSM research record is 2025-08-19. No contemporaneous TSM buy/add/trim/target/stop/size record was recovered. The strongest supported failure classification remains **monitoring continuity + event preparation**, with likely secondary priority-allocation failure.

## 2. Deterministic benchmark attribution — not a formal factor regression

Window uses direct IBKR closing prices from 2025-08-19 through 2026-08-17 (latest complete close available at review time).

| Security | Start | End | Price return |
|---|---:|---:|---:|
| TSM ADR | $232.70 | $430.97 | +85.20% |
| SOXX | $245.15 | $559.12 | +128.07% |
| NVDA | $175.64 | $225.01 | +28.11% |
| QQQ | $569.28 | $729.87 | +28.21% |

Relative wealth results:

- TSM vs QQQ: about +44.5% relative wealth.
- TSM vs NVDA: about +44.6% relative wealth.
- TSM vs SOXX: about -18.8% relative wealth.

Interpretation:

1. TSM's absolute return cannot be described as merely broad-tech beta: it materially outperformed QQQ.
2. It also materially outperformed NVDA over this exact start/end window, so the move was not simply a mechanical proxy for NVIDIA.
3. However, TSM underperformed SOXX. Therefore this deterministic benchmark comparison does **not** establish positive semiconductor-sector alpha. The semiconductor complex itself had an extraordinary year.
4. This is benchmark attribution, not a multivariate regression. It does not separately identify interest-rate beta, Taiwan risk, memory-cycle spillover, factor crowding, options positioning or flow.

## 3. PIT forward earnings history

Historical sell-side figures below are Zacks consensus snapshots published on the stated dates. They are classified as `sell_side_forecast`, not reported company facts. A later snapshot is never backdated across an earnings release.

| Forecast available from | TSM price checkpoint | FY2026 EPS consensus | FY2027 EPS consensus | Implied FY2026 P/E | PIT interpretation |
|---|---:|---:|---:|---:|---|
| 2025-08-12; applied to 2025-08-19 review | $232.70 | $10.95 | n/a | 21.25x | First recovered user research date; AI was known, but FY26 growth expectation was still modest relative to what later emerged. |
| 2025-10-03 | $292.19 | $11.14 | n/a | 26.23x | Earnings expectation had moved only slightly while price had rerated materially. |
| 2025-10-16 pre-event reference | $299.84 | $11.14 | n/a | 26.92x | Uses the latest recovered pre-Q3 snapshot; does not use the post-Q3 estimate. |
| 2025-10-21 post-Q3 | $294.51 | $12.29 | n/a | 23.96x | Q3 evidence caused a large upward estimate revision while price did not rise proportionally. |
| 2025-12-30 / pre-Q4 | $341.64 on 2026-01-15 | $12.20 | n/a | 28.00x | Pre-Q4 expectation state; Q4 actual was not yet known at the Jan-15 open. |
| 2026-01-30 post-Q4 | $330.56 | $14.01 | $17.48 | 23.59x | Major earnings revision with price pullback: a classic re-underwrite opportunity. |
| 2026-04 pre-Q1 | $363.35 on 2026-04-16 | $14.44 | $17.80 | 25.16x | Pre-Q1 consensus before the $3.49 ADR EPS result. |
| 2026-05-12 | $397.28 | $15.25 | $18.97 | 26.05x | Estimates continued to climb after Q1. |
| 2026-06-29 | $455.10 | $15.35 | $19.49-$19.50 | 29.65x | Price moved faster than the estimate revision, raising expectation risk. |
| 2026-07-15 pre-Q2 | $419.48 | ~$15.35 | ~$19.50 | 27.33x | Pre-Q2 reference; do not use the post-Q2 estimate. |
| 2026-07-21 post-Q2 | $424.61 | ~$16.05 | ~$20.42 | 26.45x | Q2 again reset earnings higher. |
| late Jul / 2026-08-17 price | $430.97 | $16.45 | $20.83 | 26.20x | Current consensus snapshot used for the end-state bridge. |

### Expectation-revision bridge

The most decision-relevant comparison is 2025-08-19 versus 2026-08-17:

- Price: $232.70 -> $430.97 = **+85.20%**.
- FY2026 sell-side EPS expectation: about $10.95 -> $16.45 = **+50.23%**.
- Price / FY2026 EPS multiple: about 21.25x -> 26.20x = **+23.28%**.

Because `Price = forward EPS × forward P/E`, the multiplicative bridge approximately reconciles the stock move. The dominant component was **earnings estimate revision**, with meaningful secondary multiple expansion.

This is more informative than saying 'AI became popular.' AI was already popular. The missed edge was that the market still materially underestimated how much of the AI capital-spending cycle would flow into TSMC earnings.

## 4. FX and ADR-basis decomposition

A TSM ADS represents five common shares. For 2025-08-19:

- 2330 Taiwan close: about NT$1,185.
- Central Bank of Taiwan USD/TWD close: about 30.120.
- ADR parity = 1,185 × 5 / 30.12 ≈ $196.71.
- ADR close = $232.70.
- Implied ADR premium ≈ **18.3%**.

For 2026-08-17, direct IBKR local-share close was about NT$2,400. Exact official Aug-17 USD/TWD was not yet indexed in the source set; using the verified low-32s current range (~32.3-32.5) gives parity around $369-$372 and an ADR premium in roughly the mid-16% range.

Thus local TSMC shares rose about +102.5% from NT$1,185 to NT$2,400, versus about +85.2% for the ADR over the matched US-close window. Most of the gap is consistent with TWD weakening versus USD, plus modest ADR-premium compression. Because the ending FX is approximate, this component remains **provisional**, not production-grade factor attribution.

## 5. Upstream AI-capex evidence graph

The monitor is designed to detect changes in **real AI compute demand**, not merely nominal capital spending.

`Hyperscaler demand / AI monetization`

-> `GOOGL / META / MSFT / AMZN real infrastructure commitments`

-> `GPU / custom ASIC / CPU design demand (NVDA and hyperscaler silicon)`

-> `TSMC advanced-node + CoWoS / advanced-packaging workload`

-> `TSMC monthly revenue + HPC share + N2/A16 mix`

-> `utilization / gross margin / operating margin`

-> `CFO / capex / FCF`

-> `EPS revisions / forward valuation / decision state`

### Historical PIT evidence already available before 2025-08-19

- Alphabet Q2 2025: Q2 capex $22.4B; FY2025 capex raised from ~$75B to ~$85B; management expected a further increase in 2026 and said Cloud would remain in a tight demand-supply environment going into 2026.
- Meta Q2 2025: FY2025 capex guided to $66-72B and management expected similarly significant dollar growth in 2026.
- Microsoft FY2025: property/equipment additions were about $64.6B, consistent with large-scale cloud/AI infrastructure buildout.
- TSMC Q1/Q2 2025 had already tied advanced-node/CoWoS planning to multi-year customer and customer-of-customer AI demand.

Therefore, by the earliest recovered TSM research date, a **multi-year AI capex cycle** was a defensible PIT research thesis, not hindsight.

### Current upstream evidence as of 2026-08-18

**Meta:** Q2 2026 maintained/raised the floor of 2026 capex guidance to $130-145B including finance-lease principal.

**Microsoft:** FY26 Q3 capex was $31.9B; roughly two-thirds was short-lived assets, primarily GPUs/CPUs. Management expected Q4 capex above $40B, calendar-2026 capex around $190B including about $25B of component-price impact, and continued capacity constraints through at least 2026. This is why nominal capex must be split into real capacity versus component inflation.

**Amazon:** Q2 2026 AWS grew 37% YoY to a $169B annualized run-rate; AWS AI and chips businesses each exceeded $25B annual run-rates and were growing triple digits. This is a strong real-demand/custom-silicon evidence node.

**Alphabet:** official 2025 Q4 guidance had already put 2026 capex at $175-185B; current Q2-2026 management guidance was subsequently reported at $195-205B. Because the latest capex figure is presently sourced through contemporaneous Reuters reporting of management's earnings-call statement rather than an indexed primary transcript in this ledger, classify it as `secondary_reported_management_guidance` until the issuer transcript is archived.

**NVIDIA:** Q1 FY2027 revenue was $81.6B (+85% YoY), Data Center $75.2B (+92%), and Q2 revenue guidance was $91B ±2%, excluding China Data Center compute. This remains a strong accelerator-side demand signal; the next earnings event is 2026-08-26.

## 6. Monitor ontology: nominal capex is not real compute capacity

Do not use a one-variable rule such as `hyperscaler capex up -> buy TSM`.

Track separately:

- total nominal capex;
- servers / GPUs / CPUs / accelerators;
- data-center buildings and networking;
- finance leases;
- component-price inflation;
- custom silicon versus merchant GPU mix;
- cloud/AI revenue and backlog;
- capacity constraints;
- AI ROI / monetization evidence.

### Green upstream state

At least two major hyperscalers maintain/raise real AI-infrastructure commitments **and** cloud/AI demand remains strong, while NVDA/custom-ASIC evidence and TSM monthly revenue/guidance remain intact.

### Yellow

Nominal capex stays high but incremental growth is increasingly driven by component prices or buildings; cloud growth slows; supply constraints ease; ROI scrutiny rises; TSM revenue remains intact.

### Red / mandatory re-underwrite

At least two hyperscalers materially cut **real** AI compute build plans, combined with deterioration in cloud/AI demand and either TSM three-month revenue/guidance or NVDA/custom-ASIC demand signals. One company's project timing alone is not sufficient.

## 7. Known next evidence nodes

- 2026-08-26 — NVIDIA earnings: accelerator demand / guidance evidence node.
- 2026-09-10 — TSMC August monthly revenue.
- 2026-10-08 — TSMC September monthly revenue.
- Each GOOGL/META/MSFT/AMZN earnings event is an upstream re-underwrite node when capex, cloud growth, AI monetization, supply constraints or custom-silicon plans materially change.

## 8. `stale_attention` cross-case validation

### TSM — direct support

Strongest case. A thesis-ready security entered the user's research universe by 2025-08-19, recurring high-quality public evidence existed, but no persistent event-review chain or documented investment action was recovered. This supports the candidate process concept.

### NVDA — partial supporting analogue

Recovered prior research history indicates that the user had followed the AI revolution/NVDA early, then at one point stopped following because the thesis appeared to have become fully recognized by the market. This is economically similar to TSM: **market awareness was mistaken for complete price discovery / no remaining research edge**. However, a timestamped historical `next_evidence_node` and decision-ready state were not recovered, so it does not fully validate the exact stale-attention rule.

### SNDK — adjacent but distinct

The SNDK 2026 Investor Day review is better classified as **event-readiness / preparation failure**: the important event was knowable in advance and the decisive questions could have been prepared. This supports the broader attention/event discipline but is not the same as a long-duration thesis disappearing from monitoring.

### MU — insufficient evidence

The current archive does not establish a comparable MU historical attention failure. Do not use MU to inflate cross-case support.

## 9. Lesson-promotion decision

`stale_attention` remains **candidate**, not `supported` or `promoted`.

Proposed operational metadata can nevertheless be used immediately at the Case Library level:

- `attention_state`
- `next_evidence_node`
- `review_due`
- `deprioritization_reason`
- `stale_attention`

Suggested deterministic workflow:

`thesis_ready / P0`
-> assign `next_evidence_node`
-> pre-event questions
-> event date passes
-> if review recorded: assign next node
-> if intentionally deprioritized: require reason
-> otherwise: mark `stale_attention=true` and return case to research/decision queue

This is an operational guardrail, not a buy/sell rule.

### Counterexample / limitation

Not every ignored stock represents a process failure. Deliberate deprioritization can be correct when expected return is poor, downside is unacceptable, evidence quality falls, portfolio exposure is already excessive, or a superior opportunity consumes scarce research time. `stale_attention` should only fire when a case was explicitly P0/thesis-ready, a material evidence node was scheduled, and no review or explicit deprioritization reason exists.

### Promotion evidence still needed

Require at least one additional case with timestamped evidence of:

1. thesis-ready/P0 state;
2. an explicit next evidence node;
3. the node passing without review;
4. no documented intentional deprioritization;
5. a later material opportunity or risk that the missed review would reasonably have surfaced.

Also require at least one counterexample where deliberate deprioritization was correct.

## 10. Decision implications for TSM today

This review strengthens the **business/earnings-duration thesis** but does not automatically strengthen today's entry because market expectations have risen substantially.

The investment state therefore remains:

- Business thesis: **strong / validated**.
- Market consensus: **high**.
- Dominant variable: AI/HPC capacity capital productivity versus high expectations.
- Trade state: **confirmation / momentum continuation / quality compounder**.
- Action: **watch / hold / selective start-small or add only when price and evidence align**.

Most important change from the initial migration: the historical opportunity can now be stated more precisely as **persistent earnings underestimation inside an already-known AI narrative**, not merely a failure to notice AI.

## 11. Promotion status

Keep `research_complete`.

Do not promote to `decision_grade` until:

- ending FX / ADR basis is validated with an authoritative same-date rate and historical EV rows use a canonical FX convention;
- benchmark attribution is upgraded to a formal factor model if factor-alpha claims are needed;
- current sizing / action / kill criteria are explicitly approved by founder/reviewer;
- absence of other historical transaction records is either checked or accepted as an explicit unknown.
