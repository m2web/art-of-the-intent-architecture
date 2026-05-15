# Art of the Intent Architecture

A 5-layer agentic development pipeline that enforces rigorous intent-to-implementation traceability.

## How It Works

```text
┌─────────────────────────────────────────────────────────────┐
│  Layer 1: INTENT          Human spec (Markdown)             │
│           ↓                                                 │
│  Layer 2: INFERRED TDD    Actor generates tests,            │
│           ↕ (gate)        Critic reviews for gaps            │
│           ↓                                                 │
│  Layer 3: IMPLEMENTATION  Code → Test → Fail → Refactor     │
│           ↕                                                 │
│  Layer 4: VALIDATION      Integration / Regression / E2E    │
│           ↓                                                 │
│  Layer 5: AUDIT           Evidence chain → audit report      │
└─────────────────────────────────────────────────────────────┘
```

## Quick Start

1. **Write your intent** — Copy `01-intent/_template.md` and rename it to something identifiable for your specific project (e.g., `01-intent_my-code-project.md`). Fill out the business goal, done state, and domain vocabulary.
2. **Run the pipeline** — Ask Antigravity: *"Run the Art of Intent pipeline on `01-intent/my-code-project.md`"* (replacing the filename with your actual file).
3. **Review gates** — The Inferred TDD layer will produce a feedback artifact. Approve or refine until `Approval: Granted`.
4. **Implementation** proceeds automatically once the gate clears.
5. **Audit report** is generated at the end for full traceability.

## Directory Structure

```text
art-of-the-intent-architecture/
├── .agent/
│   └── skills/                    # Agent skill files (one per layer + orchestrator)
│       ├── 00-orchestrator.md     # Full pipeline coordination
│       ├── 01-inferred-tdd.md     # Layer 2: Actor-Critic TDD
│       ├── 02-implementation.md   # Layer 3: Red-Green-Refactor
│       ├── 03-validation.md       # Layer 4: Diagnostic test orchestration
│       ├── 04-audit.md            # Layer 5: Evidence chain generation
│       ├── git-conventions/       # Commit message and branch naming rules
│       └── markdownlint-conventions/  # Markdown linting rules for this repo
├── claude.md                      # Architecture definition (governs agent behavior)
├── README.md                      # This file
├── 01-intent/                     # Layer 1: Intent specifications
│   └── _template.md               # Template for new intent documents
├── 02-inferred-tdd/               # Layer 2: Test suites & feedback artifacts
│   ├── tests/                     # Generated Python test files
│   └── feedback/                  # inferred-tdd-feedback-<topic>.md files
├── 03-implementation/             # Layer 3: Source code
│   └── src/                       # Implementation files
├── 04-validation/                 # Layer 4: Validation results & telemetry
│   └── reports/                   # Test run reports and diagnostics
├── 05-audit/                      # Layer 5: Audit trail
│   └── audit-<datetime>.md        # Final audit artifacts
└── examples/                      # Reference examples
    └── calculator/                # Worked example: simple calculator
```

## Layer Details

### Layer 1 — Intent

Place your specification in `01-intent/`. Use the provided template. The spec must include:

- **Business Goal**: What problem are we solving?
- **Done State**: What does "finished" look like? (must be testable)
- **Domain Vocabulary**: Key terms and their precise definitions.

### Layer 2 — Inferred TDD (Actor-Critic)

The agent reads your intent and produces:

- A Python test suite in `02-inferred-tdd/tests/`
- A feedback artifact in `02-inferred-tdd/feedback/`

**Recursive Gate**: The pipeline will not proceed until the feedback artifact ends with `Approval: Granted`.

### Layer 3 — Implementation

Iterative development loop targeting Δ = 0 between code and intent.

### Layer 4 — Validation

Full test orchestration with diagnostics. Failure telemetry feeds back to Layer 3.

### Layer 5 — Audit

Final artifact mapping results → intent for a transparent evidence chain.
