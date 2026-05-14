# Skill: Layer 4 — Validation (Diagnostic)

## Purpose

Orchestrate the full test suite (unit, integration, regression, E2E) and provide operational diagnostics to ensure global system integrity.

## Precondition

- Layer 3 must report Δ = 0 (all unit tests passing).

## Process

### Step 1 — Full Test Suite Execution

1. Run all tests with verbose output and coverage:

   ```bash
   python -m pytest 02-inferred-tdd/tests/ -v --tb=long
   ```

2. If coverage tooling is available:

   ```bash
   python -m pytest 02-inferred-tdd/tests/ --cov=03-implementation/src --cov-report=term-missing
   ```

### Step 2 — Diagnostic Analysis

Analyze test results for:

- **Failures**: Any test that was passing in Layer 3 but fails here indicates a regression.
- **Warnings**: Deprecation warnings, unclosed resources, or other diagnostic signals.
- **Coverage gaps**: Uncovered lines or branches in the implementation.
- **Performance**: Note any tests with unusually long execution times.

### Step 3 — Telemetry Feedback

If failures are found:

1. Generate a diagnostic report with failure details, stack traces, and suggested fixes.
2. **Feed telemetry back to Layer 3** — provide the failure information so the implementation can be corrected.
3. Layer 3 re-enters its refactor loop and signals back when Δ = 0 again.
4. Re-run this validation step.

## Artifact Output

Create `04-validation/reports/validation-<topic>-<date>.md` with:

```markdown
# Validation Report — <Topic>

> **Layer**: 4 (Diagnostic)
> **Date**: <YYYY-MM-DD>

## Test Results

<Full test output summary>

## Coverage

<Coverage report if available>

## Diagnostics

<Any warnings, regressions, or performance notes>

## Verdict

<PASS or FAIL with explanation>
```

## Completion Criteria

- All tests pass across the full suite.
- No regressions detected.
- Validation report generated.
- Ready for Layer 5 audit.
