# Skill: Layer 6 -- Graduation (Eject to Standalone Repo)

## Purpose

Extract validated, audited code from the framework into a standalone Git repository, ready for independent development and deployment.

## Precondition

All three conditions must be met before graduation can proceed:

1. An audit report exists in `05-audit/` for the target project.
2. The feedback artifact in `02-inferred-tdd/feedback/` ends with `Approval: Granted`.
3. **The test suite passes when re-executed.** This is the real gate -- markdown files are documentation, not proof. The `pytest` exit code is the only verification that cannot be faked.

## Gate Verification

```text
Step 1: Check that 05-audit/audit-<datetime>.md EXISTS         (structural)
Step 2: Check that feedback artifact ENDS with                 (text check)
        "Approval: Granted"
Step 3: RUN pytest 02-inferred-tdd/tests/test_<topic>.py -v    (the real gate)
          |
          +-- All pass?  -> Proceed with graduation
          +-- Any fail?  -> STOP. Do not graduate.
```

**Trust model:**

| What | Trust level | Role |
| ---- | ----------- | ---- |
| Audit markdown | Low -- anyone can write "PASS" | Human-readable documentation |
| Feedback markdown | Low -- same issue | Records the Critic's reasoning |
| **pytest exit code** | **High -- deterministic** | **The actual gate** |

## Process

### Step 1 -- Re-Verify (The Real Gate)

1. Run the full test suite:

   ```bash
   python -m pytest 02-inferred-tdd/tests/test_<topic>.py -v
   ```

2. If **any test fails**, halt immediately. Report which tests failed and instruct the user to fix them before retrying graduation.
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
  church-event-scraper/                <-- graduated repo (new)
```

Copy from the namespaced implementation directory (`03-implementation/src/<project>/`) into the new repo root. Then generate these additional files:

- **README.md** -- generated from the intent document (Business Goal, Done State, Domain Vocabulary become sections)
- **.gitignore** -- tailored to the detected tech stack
- **.env.example** -- copied from the implementation if one exists
- **requirements.txt** -- generated from Python imports (if applicable)

### Step 4 -- Copy Pipeline Artifacts and Tests

The graduated repo must be self-contained. Copy pipeline provenance and the test suite into the new repo:

**Artifacts** (into `artifacts/`):

- Layer 1: `01-intent/<topic>.md` -- renamed to `intent-<topic>.md`
- Layer 2: `02-inferred-tdd/feedback/inferred-tdd-feedback-<topic>.md`
- Layer 4: `04-validation/reports/validation-<topic>-<date>.md`
- Layer 5: `05-audit/audit-<datetime>.md`
- Layer 6: `06-graduation/graduation-<topic>.md`

**Tests** (into `tests/`):

- `02-inferred-tdd/tests/test_<topic>.py`
- A new `conftest.py` with `sys.path` pointing to the local `backend/` directory (not the framework path)

### Step 5 -- Initialize Git and Push

**Local initialization:**

```bash
cd ../<project-name>
git init
git add .
git commit -m "feat: initial graduation from Art of Intent pipeline"
```

**GitHub remote (via gh CLI):**

```bash
gh repo create <project-name> --private --source=. --push
```

Ask the user whether the repo should be **public** or **private** before creating.

### Step 6 -- Clean Up the Framework Repo

After successful graduation, remove **all** project-specific files from the framework. The graduated repo already has copies of everything.

Delete the following:

1. `01-intent/<topic>.md` (Layer 1)
2. `02-inferred-tdd/tests/test_<topic>.py` and `conftest.py` (Layer 2 tests)
3. `02-inferred-tdd/feedback/inferred-tdd-feedback-<topic>.md` (Layer 2 feedback)
4. `03-implementation/src/<project>/` (Layer 3 -- entire namespace directory)
5. `04-validation/reports/validation-<topic>-*.md` (Layer 4)
6. `05-audit/audit-*.md` for this project (Layer 5)
7. `06-graduation/graduation-<topic>.md` (Layer 6)

The framework repo should contain only the template (`01-intent/_template.md`), `.gitkeep` files, skill definitions, and documentation. It must be safe to push to a public repo.

### Step 7 -- Create Graduation Record

Create `06-graduation/graduation-<topic>.md` as the final breadcrumb, **then delete it as part of Step 6 cleanup**. The graduation record lives permanently in the graduated repo's `artifacts/` directory, not in the framework.

## Artifact Output

Create `06-graduation/graduation-<topic>.md` with:

```markdown
# Graduation Record -- <Topic>

> **Layer**: 6 (Graduation)
> **Date**: <ISO 8601>
> **Intent Source**: `01-intent/<filename>.md`
> **Audit Source**: `05-audit/audit-<datetime>.md`

## Gate Verification

- Audit report exists: Yes
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
- All artifacts preserved in graduated repo: Yes (`artifacts/` and `tests/`)
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
- Graduation record exists in the graduated repo's `artifacts/`.
