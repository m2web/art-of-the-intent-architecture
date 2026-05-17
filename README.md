# Art of the Intent Architecture

A 6-layer agentic development pipeline that enforces rigorous intent-to-implementation traceability.

## How It Works

```text
+---------------------------------------------------------------------+
|  🎯 Layer 1: INTENT          Human spec (Markdown)                  |
|  🧪 Layer 2: INFERRED TDD    Actor -> Critic -> Generate tests      |
|                              -> (gate) -> Critic reviews for gaps   |
|  🛠️ Layer 3: IMPLEMENTATION  Code -> Test -> Fail -> Refactor       |
|  🔍 Layer 4: INSPECTION      Integration / Regression / E2E         |
|  🪞 Layer 5: INTROSPECTION   Evidence chain -> introspection report |
|  🚀 Layer 6: INTEGRATION     Re-verify -> Extract -> New Repo       |
+---------------------------------------------------------------------+
```

### Language-Agnostic Design

While Python/pytest is the default baseline, the "Art of Intent" architecture is entirely language-agnostic. The pipeline can generate, test, and integrate code in any language supported by the LLM (e.g., JavaScript/TypeScript, Go, Rust, C#, Java).

To utilize another language:

- **Layer 2 (Inferred TDD)** generates a test suite for the corresponding testing framework (e.g., Jest, Go test, Cargo test) in the project namespace.
- **Layer 3 & 4 (Implementation & Inspection)** executes the language's native test runner command to drive the implementation delta to zero.
- **Layer 6 (Integration)** uses the target language's deterministic test exit code (0 for success) as the final checkout gate.

## Quick Start

1. **Write your intent** -- Copy `01-intent/_template.md` and rename it for your project (e.g., `01-intent/my-code-project.md`). Fill out all template sections as fully and precisely as possible to best guide the synthetic agents through coding, testing, implementation, and stand-alone repository integration.
2. **Run the pipeline** -- Ask Antigravity: *"Run the Art of Intent pipeline on `01-intent/my-code-project.md`"*.
3. **Review gates** -- The Inferred TDD layer produces a feedback artifact. Approve or refine until `Approval: Granted`.
4. **Implementation** proceeds automatically once the gate clears.
5. **Introspection report** is generated for full traceability.
6. **Integration** extracts the validated code into its own repo.

## Directory Structure

```text
art-of-the-intent-architecture/
+-- .agent/
|   +-- skills/                                 # Agent skill files
|       +-- 00-orchestrator.md                  # Full pipeline coordination
|       +-- 01-inferred-tdd.md                  # Layer 2: Actor-Critic TDD
|       +-- 02-implementation.md                # Layer 3: Red-Green-Refactor
|       +-- 03-inspection.md                    # Layer 4: Diagnostic test orchestration
|       +-- 04-introspection.md                 # Layer 5: Evidence chain generation
|       +-- 05-integration.md                   # Layer 6: Integrate to standalone repo
|       +-- git-conventions/                    # Commit message and branch naming rules
|       +-- markdownlint-conventions/           # Markdown linting rules for this repo
+-- claude.md                                   # Architecture definition (governs agent behavior)
+-- README.md                                   # This file 👀
+-- 01-intent/                                  # Layer 1: Intent specifications
|   +-- _template.md                            # Template for new intent documents
+-- 02-inferred-tdd/                            # Layer 2: Test suites & feedback artifacts
|   +-- tests/                                  # Generated test files
|   +-- feedback/                               # inferred-tdd-feedback-<topic>.md files
+-- 03-implementation/                          # Layer 3: Source code (namespaced by project)
|   +-- src/<project>/                          # Each project in its own subdirectory
+-- 04-inspection/                              # Layer 4: Validation results & telemetry
|   +-- reports/                                # Test run reports and diagnostics
+-- 05-introspection/                           # Layer 5: Audit trail
|   +-- <datetime>-introspection-<topic>.md     # Final audit artifacts
+-- 06-integration/                             # Layer 6: Graduation records
|   +-- <datetime>-integration-<topic>.md       # Breadcrumb linking to the new, integrated repository
+-- examples/                                   # Reference examples
    +-- calculator/                             # Worked example: simple calculator
```

## Layer Details

### Layer 1 — Intent

The foundation of the entire pipeline. The human operator provides a rich, machine-readable specification in `01-intent/` based on the provided template.

To best guide our synthetic friends (the LLM agents) into producing highly accurate tests, implementations, and stand-alone repository graduations, the intent template must be filled out **as fully and precisely as possible**. A detailed intent document minimizes the ambiguity loop and ensures that downstream steps execute flawlessly.

The specification must include:

- **Business Goal**: What problem are we solving and why does it matter?
- **Done State**: The terminal conditions. What must be true for the feature to be complete?
- **Domain Vocabulary**: Precise, unambiguous definitions of terms and structures that the agents and code will use.
- **Acceptance Criteria**: Numbered, testable statements that map directly to the Done State.

### Layer 2 — Inferred TDD (Actor-Critic)

The agent reads your intent and produces:

- A test suite in `02-inferred-tdd/tests/` (in Python/pytest by default, or the target language's native test framework)
- A feedback artifact in `02-inferred-tdd/feedback/`

**Recursive Gate**: The pipeline will not proceed until the feedback artifact ends with `Approval: Granted`.

### Layer 3 -- Implementation

Iterative development loop targeting D = 0 between code and intent. Projects are namespaced under `03-implementation/src/<project>/`.

### Layer 4 -- Inspection

Full test orchestration with diagnostics. Failure telemetry feeds back to Layer 3.

### Layer 5 -- Introspection

Final artifact mapping results back to intent for a transparent evidence chain.

### Layer 6 -- Integration

Extracts validated code into a standalone Git repo. The gate is **not** the introspection markdown -- it is a fresh execution of the target language's test suite. If tests pass (exit code 0), the code is integrated into a sibling directory and optionally pushed to GitHub via `gh` CLI. Implementation files are removed from the framework; pipeline artifacts remain for traceability.
