# Skill: Layer 3 — Implementation

## Purpose

Write the production code that satisfies all tests from Layer 2, driving the Delta (Δ) between code and verified intent to exactly zero.

## Precondition

- Layer 2 feedback artifact must end with `Approval: Granted`.
- Test suite must exist in `02-inferred-tdd/tests/`.

## Process

Execute an iterative Red-Green-Refactor loop:

### Step 1 — Red (Confirm Failing Tests)

1. Run the test suite: `python -m pytest 02-inferred-tdd/tests/test_<topic>.py -v`
2. Confirm all tests fail (no implementation exists yet).
3. Record the initial failure count as the starting Δ.

### Step 2 — Green (Make Tests Pass)

1. Create implementation files in `03-implementation/src/`.
2. Write the minimum code to make each test pass.
3. Run tests after each significant change.
4. Track Δ (number of failing tests) — it must decrease monotonically.

### Step 3 — Refactor (Clean Up)

1. Once all tests pass (Δ = 0), refactor for:
   - Code clarity and readability.
   - Elimination of duplication.
   - Proper error handling and docstrings.
2. Re-run tests to confirm Δ remains 0 after refactoring.

## Artifact Output

- Implementation files in `03-implementation/src/`.
- Ensure `sys.path` or package structure allows the test suite to import the implementation.

## Completion Criteria

- All tests pass: `Δ = 0`.
- Code is clean and documented.
- Ready for Layer 4 validation.

## Adjacent Layer Interaction

- **From Layer 4**: If validation reveals failures, accept telemetry and re-enter the Green/Refactor loop to fix regressions.
