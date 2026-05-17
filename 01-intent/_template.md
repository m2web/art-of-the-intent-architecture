# Intent: [Title]

> **Status**: Draft | Under Review | Approved
> **Author**: [Name]
> **Date**: [YYYY-MM-DD]
> **Target Language**: [e.g., Python | TypeScript | Go | Rust]
> **Testing Framework**: [e.g., pytest | Jest | Vitest | go test | cargo test]

## Business Goal

<!-- 
Define the core problem being solved, the "why" behind this project, and the value it delivers. 
Be concise but thorough.
-->

## Technical Stack & Dependencies (Optional)

<!-- 
Specify any mandatory libraries, packages, or databases required.
If left blank, the agent will propose a suitable stack and dependencies in Layer 2.
- Mandatory dependencies:
- Restricted/forbidden dependencies:
-->

## Core Interface Specification (Optional)

<!--
Describe how the code will be interacted with. 
If left blank, the agent will propose appropriate interfaces in the test suite during Layer 2.
Define the interfaces precisely if you have specific requirements:
- CLI command signatures, arguments, and options
- API endpoint routes, methods, and payload structures
- Main entrypoint function or class signatures with types
-->

## Done State

<!-- 
Define the terminal conditions. What must be true for this to be "done"?
Be highly specific — these statements will directly map to top-level test assertions.
-->

- [ ] Condition 1
- [ ] Condition 2
- [ ] Condition 3

## Domain Vocabulary

<!-- 
Define domain-specific terminology, database fields, or JSON keys precisely. 
The agent Critic, Actor, and downstream tests will utilize these exact definitions.
-->

| Term | Definition | Precise Data Type / Example |
| ---- | ---------- | --------------------------- |
|      |            |                             |

## Constraints & Security

<!-- 
Any performance, environmental, regulatory, or security constraints.
- Performance limits (e.g., "execution must complete in < 5s")
- Sensitive data handling / secret management
- Platform constraints (e.g., Windows OS compatibility)
-->

## Out of Scope

<!-- 
Define what this project WILL NOT do. Setting clear boundaries prevents LLM scope creep 
and ensures the Actor and Critic focus solely on the core problem.
-->

- [ ] Out of scope item 1
- [ ] Out of scope item 2

## Acceptance Criteria

<!-- 
Numbered, testable criteria mapping directly to the Done State. 
Every criterion must be covered by at least one distinct test.
-->

1. **AC-1**: ...
2. **AC-2**: ...
3. **AC-3**: ...

## Verification Guide

<!-- 
Step-by-step instructions on how a human or external script can verify the implementation.
- Expected shell commands:
- Expected output or logs:
-->

## Notes

<!-- Any additional context, wireframe descriptions, or reference links. -->
