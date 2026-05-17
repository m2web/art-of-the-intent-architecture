# The "Art of Intent" Architecture

All development must strictly adhere to this 6-layer pipeline:

## 1. The Intent Layer

* **Input**: Human-provided, machine-readable Markdown specification.
* **Requirement**: Define business goals, the terminal "Done State," and domain-specific vocabulary.

## 2. The Inferred TDD Layer (Actor-Critic)

* **Action**: Agent translates intent into a test suite (Python-based by default, or using the target language's native framework) while a Critic agent identifies logical gaps.
* **Artifact**: Create an `inferred-tdd-feedback-<topic>.md` file.
* **Recursive Gate**:
  * **IF** the Intent Layer Markdown is modified **AND** the feedback artifact **DOES NOT** contain `Approval: Granted` as the **last string** in the markdown:
    * **RE-RUN Layer 2**: Update tests and regenerate the feedback artifact.

  * **ELSE IF** the feedback artifact contains `Approval: Granted` as the **last string**:
    * **PROCEED** to Layer 3.

  * **OTHERWISE**: Enter a **WAIT STATE**.

## 3. The Implementation Layer

* **Action**: High-speed iterative loop (Code → Test → Fail → Refactor).
* **Goal**: Eliminate the "Delta" (Δ) between the generated code and verified intent until the gap is exactly zero.

## 4. The Inspection Layer (Diagnostic)

* **Action**: Full agent orchestration of the test suite (Integration, Regression, E2E).
* **Goal**: Utilize system logs and telemetry to provide "operational instinct," ensuring global system integrity.

## 5. The Introspection Layer (Introspector)

* **Artifact**: Generate a separate `introspection-<date-time>.md` file mapping final results back to the original intent for a transparent evidence chain.

## 6. The Integration Layer (Eject)

* **Gate**: Re-run the full test suite. The test runner's exit code (e.g., `pytest` by default, or the target language's runner) is the only trusted verification -- markdown artifacts are documentation, not proof.
* **Action**: Extract validated code into a standalone Git repo (sibling directory), scaffold production files (README, .gitignore, requirements.txt), and optionally push to GitHub via `gh` CLI.
* **Cleanup**: Remove implementation files from the framework repo. Pipeline artifacts (intent, tests, feedback, reports, introspection) remain permanently.
* **Artifact**: Generate a `integration-<topic>.md` record linking the new repo back to the introspection trail.

## Language-Agnostic Support

The architecture is fully language-agnostic. While Python/pytest is the default baseline for framework testing, the pipeline supports generating, validating, and integrating code in any programming language that the LLM is capable of producing:

- **Layer 2 (Inferred TDD)** generates a test suite for the target language's native test framework (e.g., Jest, Cargo test, Go test) in the project namespace.
- **Layer 3 & 4 (Implementation & Inspection)** executes the target language's test runner command to iteratively drive the test failure count down to zero.
- **Layer 6 (Integration)** uses the target language's test suite exit code (0 for success) as the deterministic gate before ejecting.

---

> **Operational Note**: All layers are permitted to interact with **adjacent layers** to complete tasks more effectively (e.g., Layer 4 providing failure telemetry back to Layer 3 to expedite the refactoring loop).
