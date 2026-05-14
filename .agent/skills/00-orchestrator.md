# Skill: Art of Intent — Pipeline Orchestrator

## Trigger

User says: "Run the Art of Intent pipeline on `<intent-file>`"

## Behavior

Execute the 5-layer pipeline in strict sequential order. Each layer must complete before the next begins. Adjacent layers may interact (e.g., Layer 4 feeding failure telemetry back to Layer 3).

### Execution Order

1. **Read** the intent file from `01-intent/`.
2. **Execute Layer 2** — Inferred TDD (Actor-Critic). See `01-inferred-tdd.md`.
3. **Enforce the Recursive Gate** — Do NOT proceed until the feedback artifact ends with `Approval: Granted`.
4. **Execute Layer 3** — Implementation. See `02-implementation.md`.
5. **Execute Layer 4** — Validation. See `03-validation.md`.
6. **Execute Layer 5** — Audit. See `04-audit.md`.

### Gate Logic (Layer 2 → Layer 3)

```text
IF intent markdown is modified AND feedback artifact does NOT end with "Approval: Granted":
    → RE-RUN Layer 2

ELSE IF feedback artifact ends with "Approval: Granted":
    → PROCEED to Layer 3

OTHERWISE:
    → WAIT STATE (ask user for direction)
```

### Artifact Locations

| Layer | Output Directory |
| ----- | ---------------- |
| 2 — Tests | `02-inferred-tdd/tests/` |
| 2 — Feedback | `02-inferred-tdd/feedback/` |
| 3 — Code | `03-implementation/src/` |
| 4 — Reports | `04-validation/reports/` |
| 5 — Audit | `05-audit/` |

### Completion

Report a summary table showing each layer's status and any artifacts generated.
