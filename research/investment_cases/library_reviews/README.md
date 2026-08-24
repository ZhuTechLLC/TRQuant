# Investment Case Library Reviews

This directory stores library-wide governance artifacts rather than single-ticker research.

## Current canonical review gate
- `decision_grade_gate_v1.md` — non-scoring promotion gate from `research_complete` to `decision_grade`.

## Current library review
- `2026-08-23_case_library_decision_grade_review.md` — human-readable 21-case review.
- `2026-08-23_case_library_decision_grade_review.json` — machine-readable promotion/blocker state.

## Workflow

`case research -> case status research_complete -> library/case-specific decision-grade gate -> remediation or event wait -> explicit approval -> immutable promotion commit`

Do not use library review classifications as trading signals. `EVENT_BLOCKED`, `EVIDENCE_BLOCKED`, or `READY_FOR_DECISION_GRADE_APPROVAL` describe research/governance state only.
