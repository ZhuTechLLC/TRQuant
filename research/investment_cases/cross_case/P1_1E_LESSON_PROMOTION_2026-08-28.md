# P1-1E Lesson Promotion / Research Protocol Integration — 2026-08-28

## Verdict

**PASS / CLOSED**

P1-1E promotes only the two lessons that cleared the P1-1D evidence and governance gate. No other lesson is upgraded in this phase.

## Promoted principles

### L03 — Independent and reversible research states

Promoted into `trquant-equity-investment-case` as a standing research-control principle:

- keep lifecycle, thesis, opportunity, decision, and evidence-freshness states separate;
- update only the state dimension supported by new evidence;
- allow evidence-driven state reversal or repair;
- never let a research-state label mechanically create position size, capital weight, an order, or trade authority.

Load-bearing lineage: M2 state/capital evidence plus P1-1C production `research_state_v1` regression. M4 remains explicitly non-load-bearing because its replication checksum failed and `decision_eligible=false`.

### L02 — Lifecycle-conditioned per-share conversion firewall

Promoted into `trquant-equity-investment-case` as a standing underwriting principle:

- bridge business growth through reinvestment/capex, working capital, financing/interest/lease burden, shareholder cash generation, dilution/buybacks/capital allocation, and finally diluted per-share value;
- choose the conversion bridge according to lifecycle and economic model;
- do not impose one contemporaneous FCF-yield framework on mature positive-FCF companies and negative-FCF growth companies without separate validation.

Load-bearing lineage: QV-01 V1 and diagnostic V2. The universal FCF-yield interpretation is explicitly rejected.

## Skill changes

Updated package: `trquant-equity-investment-case`

Files changed:

- `SKILL.md`
- `references/research-protocol.md`
- `references/investment-epistemology.md`
- `references/case-lessons.md`

Core changes are intentionally compact and non-duplicative. Case-specific evidence remains in `case-lessons.md` rather than being copied into the Skill control plane.

Official Skill validator/package workflow: **PASS**.

Package SHA256: `6cfc5da7872af61fe35f6cf1c9b19962b6c7a3589bffbba30bcef8a1546068d0`

The packaged Skill is the promotion deliverable. Activation in a ChatGPT environment requires installing/replacing the existing Skill with that validated package; this closeout does not claim an unavailable live Skill-install API was invoked.

## Lesson registry state

- L02: `promoted`
- L03: `promoted`
- L01: remains `supported`
- L04: remains `candidate`
- L05: remains `candidate`
- L06: remains `supported` process rule
- L07: remains `supported`
- promotion queue: empty

## Boundaries preserved

- No capital authority added.
- No order/execution behavior added.
- No mechanical state-to-position sizing rule added.
- No universal FCF factor added.
- No Case history rewritten.
- No change to QuantConnect full-US discovery, Research Control governance, or Capital Authorization architecture.

## Continuing validation

Use the promoted protocol prospectively in new and updated Investment Cases. Continue Investment Result Reviews at material evidence horizons. If future counterexamples invalidate the scope, revise or retire the principle through the same governed lesson lifecycle rather than silently rewriting the Skill.
