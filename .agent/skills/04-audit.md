# Skill: Layer 5 — Audit (Auditor)

## Purpose

Generate a transparent evidence chain mapping final implementation results back to the original intent specification.

## Precondition

- Layer 4 validation report must show a PASS verdict.

## Process

### Step 1 — Gather Evidence

Collect artifacts from all prior layers:

1. **Layer 1**: Intent file (`01-intent/<topic>.md`) — extract all Acceptance Criteria and Done State conditions.
2. **Layer 2**: Feedback artifact (`02-inferred-tdd/feedback/inferred-tdd-feedback-<topic>.md`) — confirm gate was passed.
3. **Layer 2**: Test suite (`02-inferred-tdd/tests/test_<topic>.py`) — list all test functions.
4. **Layer 3**: Implementation (`03-implementation/src/`) — list all source files.
5. **Layer 4**: Validation report (`04-validation/reports/`) — extract test results.

### Step 2 — Build Traceability Matrix

Map every Acceptance Criterion through the pipeline:

```text
AC-N → test_function(s) → implementation_function(s) → PASSED/FAILED
```

### Step 3 — Verify Done State

Cross-reference each Done State condition with the test results to confirm all conditions are met.

## Artifact Output

Create `05-audit/audit-<YYYY-MM-DDTHH-MM-SS>.md` with:

```markdown
# Audit Report — <Topic>

> **Layer**: 5 (Auditor)
> **Date**: <ISO 8601 timestamp>
> **Intent Source**: `01-intent/<filename>.md`

## Evidence Chain

### Layer 1 → Layer 2 Traceability

<Table: AC → Test Function → Covered?>

### Layer 2 Gate

- Feedback artifact: <path>
- Gate status: Approval: Granted
- Critic gaps resolved: <N/N>

### Layer 3 → Layer 4 Results

<Table: Test → Result>

### Done State Verification

<Checklist of Done State conditions with pass/fail>

## Final Verdict

<✅ PASS or ❌ FAIL with explanation>
```

## Completion Criteria

- Audit report generated with full traceability.
- Every AC maps to at least one passing test.
- Every Done State condition is verified.
- The audit file is the final deliverable of the pipeline.
