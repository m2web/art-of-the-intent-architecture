# Intent: Simple Calculator

> **Status**: Approved
> **Author**: Example
> **Date**: 2026-05-14

## Business Goal

Build a calculator module that performs basic arithmetic operations with proper error handling. This serves as a reference implementation of the Art of Intent pipeline.

## Done State

- [x] Calculator can add two numbers and return the correct sum
- [x] Calculator can subtract two numbers and return the correct difference
- [x] Calculator can multiply two numbers and return the correct product
- [x] Calculator can divide two numbers and return the correct quotient
- [x] Division by zero raises a descriptive error, not a crash

## Domain Vocabulary

| Term | Definition |
| ------ | ------------ |
| Operand | A numeric value (int or float) passed to an operation |
| Operation | One of: add, subtract, multiply, divide |
| Result | The numeric output of an operation |
| DivisionByZeroError | A ValueError raised when the divisor is zero |

## Constraints

- Pure Python, no external dependencies.
- All operations must accept both `int` and `float` operands.
- Results must preserve `float` precision when any operand is a `float`.

## Acceptance Criteria

1. **AC-1**: `add(2, 3)` returns `5`
2. **AC-2**: `subtract(10, 4)` returns `6`
3. **AC-3**: `multiply(3, 7)` returns `21`
4. **AC-4**: `divide(10, 2)` returns `5.0`
5. **AC-5**: `divide(10, 0)` raises `ValueError` with message containing "division by zero"
6. **AC-6**: `add(1.5, 2.5)` returns `4.0` (float preservation)
