# Skill: Layer 2 — Inferred TDD (Actor-Critic)

## Purpose

Translate a Layer 1 intent specification into a Python test suite while critically reviewing for logical gaps.

## Inputs

- An intent Markdown file from `01-intent/` containing Business Goal, Done State, Domain Vocabulary, and Acceptance Criteria.

## Actor Role

1. **Parse** every Acceptance Criterion (AC) from the intent file.
2. **Generate** a pytest-based test file in `02-inferred-tdd/tests/test_<topic>.py`.
3. **Map** each AC to at least one test function. Use the naming convention `test_<descriptive_name>`.
4. **Include** docstrings referencing the AC ID (e.g., `"""AC-1: add(2, 3) returns 5"""`).

## Critic Role

After the Actor generates the test suite, switch to Critic mode:

1. **Review** the test suite against the intent for logical gaps:
   - Missing edge cases (boundary values, negative inputs, empty inputs).
   - Untested error paths.
   - Ambiguous acceptance criteria that need clarification.
2. **Add** additional tests for any gaps found.
3. **Document** all findings in the feedback artifact.

## Artifact Output

Create `02-inferred-tdd/feedback/inferred-tdd-feedback-<topic>.md` with this structure:

```markdown
# Inferred TDD Feedback — <Topic>

> **Layer**: 2 (Actor-Critic)
> **Intent Source**: `01-intent/<filename>.md`
> **Date**: <YYYY-MM-DD>

## Actor Analysis

<Table mapping each AC to its test function(s)>

## Critic Review

### Gaps Identified

<Numbered list of gaps. Strike through resolved gaps.>

### Remaining Gaps

<List any unresolved gaps, or state "No Remaining Gaps">

## Gate Decision

<"Approval: Granted" if all gaps are resolved, otherwise explain what's blocking>
```

## Gate Rule

- The **last line** of the feedback artifact must be exactly `Approval: Granted` for the pipeline to proceed to Layer 3.
- If gaps remain unresolved, end with a description of what's needed and enter WAIT STATE.

## Recursive Trigger

If the user modifies the intent file after feedback is generated, **re-run this skill** to update tests and regenerate the feedback artifact.
