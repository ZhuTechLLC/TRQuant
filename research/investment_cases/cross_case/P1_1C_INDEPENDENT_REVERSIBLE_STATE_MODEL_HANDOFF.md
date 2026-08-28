# P1-1C — Independent Reversible Research-State Model

## Background

P1-1B Cross-Case Pattern Mining is complete for its first cycle.

The 40-Case Library and existing QuantConnect M2/M4 evidence support one process principle strongly enough to implement:

> Economic lifecycle, thesis state, current opportunity state, decision state, and evidence freshness are different concepts. They must not overwrite each other or mechanically create capital authority.

Relevant regression cases:

- HTFL — correct rejection of `New Ignition` did not invalidate the separate continuation opportunity.
- META — a valid historical avoid state had to become re-underwritable after real operating repair.
- NVDA — mature structural winner / prior appreciation must not automatically remove research attention.
- PTON — a large drawdown must not automatically create a turnaround opportunity without economic repair.
- FRC — terminal resolution must not be resurrected as an active listed-equity opportunity.

Existing QuantConnect evidence also shows that WATCH / INVESTIGATE / CONFIRMED-style research labels do not support a deterministic capital-weight function.

## Objective

Implement one canonical independent research-state model used consistently by Opportunity Discovery and Investment Case workflows.

Required independent dimensions:

```text
lifecycle_state
thesis_state
opportunity_state
decision_state
evidence_freshness
```

The implementation must make the meaning and ownership of each state explicit and prevent implicit cross-field overwrites.

## Required semantics

### lifecycle_state

Describes the economic/company lifecycle only.

Examples:

```text
discovery
ignition
confirmation
early_momentum
mature_compounder
cyclical_peak
cyclical_trough
reset
turnaround
re_ignition
thesis_deterioration
terminal_failure
```

It is descriptive, not a buy/sell instruction.

### thesis_state

Describes whether the economic investment thesis is strengthening, intact, uncertain, deteriorating, broken, or repaired based on evidence.

### opportunity_state

Describes the current setup at the present price/expectation state.

Examples may include:

```text
inactive
watch
investigate
conditional_entry
continuation_watch
pullback_watch
reunderwrite
```

Do not hard-code these exact names if an existing canonical enum already exists; preserve one semantic source of truth.

### decision_state

Describes the current research/decision conclusion. It must remain separate from lifecycle and opportunity labels.

No `decision_state` may by itself grant position sizing, order creation, or capital authority.

### evidence_freshness

Describes whether required current evidence is FRESH / STALE / MISSING / UNKNOWN or the current canonical equivalent.

Evidence freshness can block a decision but must not silently rewrite lifecycle history.

## Required invariants

1. Rejecting `New Ignition` must not automatically set opportunity to inactive or false.
2. Historical `AVOID` / negative thesis states must be reversible after documented repair evidence.
3. Prior stock appreciation / mature-winner status must not automatically remove research eligibility.
4. Price decline alone must not promote a deteriorating company into turnaround/opportunity state.
5. Terminal legal/economic resolution may close the active-equity opportunity while preserving the Case as a research analogue.
6. Research-state labels must never map directly to a fixed capital weight.
7. Price zones must not trigger action without a compatible thesis/opportunity/evidence state.
8. State transitions must be attributable to evidence or an explicit reviewed decision, not label propagation.
9. Historical states remain append-only/auditable; current state may change without rewriting prior state.
10. Existing 40 governed US Cases must remain readable and semantically compatible.

## Regression fixtures

Use the existing specification:

`research/investment_cases/cross_case/STATE_MODEL_REGRESSION_SPEC_2026-08-28.md`

At minimum automate these fixtures:

### HTFL

Expected:

```text
false_new_ignition
!=
false_opportunity
```

Lifecycle may be corrected to second-S-curve / confirmation while opportunity remains `continuation_watch` or equivalent if supporting evidence remains valid.

### META

Expected:

```text
historical_avoid
+
verified_operating_repair
->
reunderwrite_allowed
```

Forbidden: permanent exclusion solely because the old state was avoid.

### NVDA

Expected:

```text
mature_structural_winner
+
large_prior_gain/high_consensus
->
research_eligible
```

Forbidden: automatic removal from attention.

### PTON

Expected:

```text
large_drawdown
without_operating_repair
!=
turnaround_opportunity
```

### FRC

Expected:

```text
terminal_resolution
->
no_active_listed_equity_opportunity
```

while the historical Case remains retrievable.

## Existing-system compatibility

Do not rebuild the whole Case system.

First locate existing state definitions/contracts and reuse or minimally extend the canonical source of truth.

Do not create parallel enums or duplicate state stores when a governed source already exists.

Do not restore legacy Equity Research candidate-ranking logic.

Do not change QuantConnect full-US candidate generation.

Do not change capital authorization behavior except to remove any accidental direct dependency on research-state labels if one exists.

## Development responsibility

Cursor should independently:

1. locate the current canonical state contracts and all consumers;
2. identify any state conflation or implicit propagation;
3. choose the smallest coherent architecture;
4. implement;
5. add automated regression tests;
6. run focused + relevant existing tests;
7. deploy/restart the affected production service(s) if required;
8. return exact runtime version/commit and production verification instructions.

Do not stop after identifying a problem. Continue until the acceptance criteria pass or a concrete external blocker is proven.

## Acceptance criteria

### A. Regression

All five fixtures pass:

```text
HTFL PASS
META PASS
NVDA PASS
PTON PASS
FRC PASS
```

### B. State independence

Automated tests prove that changing one dimension does not implicitly overwrite another unless an explicit reviewed transition rule requires it.

### C. No capital leakage

No state label alone creates:

```text
position sizing
capital weight
order instruction
trade authority
```

### D. Backward compatibility

Existing 40 US Cases remain readable.

Research Control remains:

```text
HEALTHY
MATCH
write_eligible = true
integrity_error_cases = 0
```

### E. No regression of upstream discovery

QuantConnect remains the canonical broad/full-US candidate generator.

### F. Auditability

State changes retain provenance/evidence references and do not rewrite prior historical states.

## Return to GPT for independent production acceptance

Return only when implementation is complete, with:

```text
commit SHA
changed paths
services affected
regression test results
relevant existing test results
runtime/deployment commit
production tool calls GPT should use for independent acceptance
remaining blocker = none | exact blocker
```

GPT will independently validate production and return PASS / PARTIAL / FAIL.
