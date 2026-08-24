# TRQuant Investment Case Library

This directory is the authoritative, versioned research-case layer between raw evidence and reusable investment Skills.

## Design principle

`raw data -> evidence -> decision-grade case -> cross-case pattern -> reusable Skill principle`

Do not treat raw data, scanner labels, or model scores as decision-grade research. A case earns higher status only after provenance, point-in-time integrity, valuation reconstruction, counter-evidence, and decision logic are reviewed.

## Case states

1. `draft` — exploratory research; not reliable as precedent.
2. `evidence_verified` — load-bearing facts and dates checked against primary/authoritative sources.
3. `research_complete` — dominant variable, valuation/expectations, risks, scenarios, and trade state completed.
4. `decision_grade` — includes as-of decision, entry/wait conditions, valuation, expected-return logic, kill criteria, sizing/exit framework, and evidence traceability.
5. `postmortem_complete` — original decision is compared with later outcomes without rewriting history.

Promotion is explicit. Automation may create/update drafts and evidence records, but must not silently promote a case to `decision_grade`.

## Layout

- `registry.json` — compact catalog used to build downstream indexes.
- `schema/` — deterministic contracts for case/evidence/review objects.
- `<MARKET>/<TICKER>/case.md` — human-readable decision case.
- `<MARKET>/<TICKER>/case.json` — structured research state.
- `<MARKET>/<TICKER>/evidence.jsonl` — evidence ledger with provenance and PIT fields.
- `<MARKET>/<TICKER>/timeline.json` — dated lifecycle/research/trade-state events.
- `<MARKET>/<TICKER>/valuation_history.csv` — reproducible valuation checkpoints.
- `<MARKET>/<TICKER>/decisions.jsonl` — immutable ex-ante decisions and later updates.
- `<MARKET>/<TICKER>/reviews/` — later re-underwrites/postmortems.

## Non-negotiable rules

- Preserve original decisions; later reviews append rather than overwrite.
- Keep `reported`, `guidance`, `forecast`, `market_expectation`, and `inference` distinct.
- Historical analysis must use information available at that date. Mark availability timestamps when known.
- Revenue, ARR/run-rate, bookings, backlog/RPO, capacity, utilization, cash receipts, EBITDA, operating income, and FCF are distinct metrics.
- Valuation checkpoints must state the share-count convention, debt/cash convention, and whether figures are reported or inferred.
- A historical analogue is a research prompt, never an automatic buy/sell label.

## Downstream use

GitHub is the source of truth. TRQuant may compile validated cases into SQLite/DuckDB/Parquet/vector indexes for retrieval, but those indexes are derived artifacts and must remain traceable to repository paths and commits.
