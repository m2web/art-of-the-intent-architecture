# Skill: Layer 6 -- Integration (Extract to Standalone Repo)

## Purpose

Extract validated, introspected code from the framework into a standalone Git repository, ready for independent development and deployment.

## Precondition

All three conditions must be met before integration can proceed:

1. An introspection report exists in `05-introspection/` for the target project.
2. The feedback artifact in `02-inferred-tdd/feedback/` ends with `Approval: Granted`.
3. **The test suite passes when re-executed.** This is the real gate -- markdown files are documentation, not proof. The `pytest` exit code is the only verification that cannot be faked.

## Gate Verification

```text
Step 1: Check that 05-introspection/introspection-<datetime>.md EXISTS         (structural)
Step 2: Check that feedback artifact ENDS with                 (text check)
        "Approval: Granted"
Step 3: RUN pytest 02-inferred-tdd/tests/test_<topic>.py -v    (the real gate)
          |
          +-- All pass?  -> Proceed with integration
          +-- Any fail?  -> STOP. Do not integrate.
```

**Trust model:**

| What | Trust level | Role |
| ---- | ----------- | ---- |
| Introspection markdown | Low -- anyone can write "PASS" | Human-readable documentation |
| Feedback markdown | Low -- same issue | Records the Critic's reasoning |
| **pytest exit code** | **High -- deterministic** | **The actual gate** |

## Process

### Step 1 -- Re-Verify (The Real Gate)

1. Run the full test suite:

   ```bash
   python -m pytest 02-inferred-tdd/tests/test_<topic>.py -v
   ```

2. If **any test fails**, halt immediately. Report which tests failed and instruct the user to fix them before retrying integration.
3. If **all tests pass**, record the test count and proceed.

### Step 2 -- Determine Project Identity

Read the intent file from `01-intent/<topic>.md` and extract:

- **Project name**: derived from the intent filename (e.g., `church-event-scraper`)
- **Tech stack**: detected from implementation files (Python, React, etc.)
- **Description**: from the Business Goal section of the intent

### Step 3 -- Scaffold the Standalone Repo

Create the project in a **sibling directory** relative to the framework repo:

```text
../
  art-of-the-intent-architecture/     <-- framework repo (current)
  church-event-scraper/                <-- integrated repo (new)
```

Copy from the namespaced implementation directory (`03-implementation/src/<project>/`) into the new repo root. Then generate these additional files:

- **README.md** -- generated from the intent document (Business Goal, Done State, Domain Vocabulary become sections)
- **.gitignore** -- tailored to the detected tech stack
- **.env.example** -- copied from the implementation if one exists
- **requirements.txt** -- generated from Python imports (if applicable)

### Step 4 -- Copy Pipeline Artifacts and Tests

The integrated repo must be self-contained. Copy pipeline provenance and the test suite into the new repo:

**Artifacts** (into `artifacts/`):

- Layer 1: `01-intent/<topic>.md` -- renamed to `intent-<topic>.md`
- Layer 2: `02-inferred-tdd/feedback/inferred-tdd-feedback-<topic>.md`
- Layer 4: `04-inspection/reports/inspection-<topic>-<date>.md`
- Layer 5: `05-introspection/introspection-<datetime>.md`
- Layer 6: `06-integration/integration-<topic>.md`

**Tests** (into `tests/`):

- `02-inferred-tdd/tests/test_<topic>.py`
- A new `conftest.py` with `sys.path` pointing to the local `backend/` directory (not the framework path)

### Step 5 -- Initialize Git and Push

**Local initialization:**

```bash
cd ../<project-name>
git init
git add .
git commit -m "feat: initial integration from Art of Intent pipeline"
```

**GitHub remote (via gh CLI):**

```bash
gh repo create <project-name> --private --source=. --push
```

Ask the user whether the repo should be **public** or **private** before creating.

### Step 6 -- Clean Up the Framework Repo

After successful integration, remove **all** project-specific files from the framework. The integrated repo already has copies of everything.

Delete the following:

1. `01-intent/<project>.md` (Layer 1)
2. `02-inferred-tdd/tests/test_<project>.py` and `conftest.py` (Layer 2 tests)
3. `02-inferred-tdd/feedback/inferred-tdd-feedback-<project>.md` (Layer 2 feedback)
4. `03-implementation/src/<project>/` (Layer 3 -- entire namespace directory)
5. `04-inspection/reports/inspection-<project>-*.md` (Layer 4)
6. `05-introspection/introspection-<project>-*.md` for this project (Layer 5)
7. `06-integration/integration-<project>.md` (Layer 6)

The framework repo should contain only the template (`01-intent/_template.md`), `.gitkeep` files, skill definitions, and documentation. It must be safe to push to a public repo.

### Step 7 -- Create Integration Record

Create `06-integration/integration-<topic>.md` as the final breadcrumb, **then delete it as part of Step 6 cleanup**. The integration record lives permanently in the integrated repo's `artifacts/` directory, not in the framework.

## Artifact Output

Create `06-integration/integration-<topic>.md` with:

```markdown
# Integration Record -- <Topic>

> **Layer**: 6 (Integration)
> **Date**: <ISO 8601>
> **Intent Source**: `01-intent/<filename>.md`
> **Introspection Source**: `05-introspection/introspection-<datetime>.md`

## Gate Verification

- Introspection report exists: Yes
- Feedback gate: Approval: Granted
- Test suite re-run: <N> passed, 0 failed
- **Gate: PASSED**

## Destination

- **Local path**: `../<project-name>/`
- **GitHub URL**: `https://github.com/<user>/<project-name>` (if pushed)
- **Visibility**: <public/private>

## Extracted Files

<Table: source path in framework -> destination path in new repo>

## Generated Files

<Table: file -> purpose (README.md, .gitignore, requirements.txt, etc.)>

## Cleanup

- Implementation files removed from framework: Yes
- Pipeline artifacts removed from framework: Yes
- All artifacts preserved in integrated repo: Yes (`artifacts/` and `tests/`)
```

## Completion Criteria

- Gate verification passed (pytest exit code 0).
- Standalone repo created and initialized with Git.
- Pipeline artifacts copied to `artifacts/` in the new repo.
- Test suite copied to `tests/` with a standalone `conftest.py`.
- Tests pass from the new repo (verified independently).
- GitHub remote created (if user chose GitHub mode).
- **All** project-specific files removed from the framework repo.
- Framework repo is clean and safe for public push.
- Integration record exists in the integrated repo's `artifacts/`.
