# Intent: Simple Calculator

> **Status**: Approved
> **Author**: Example
> **Date**: 2026-05-14
> **Target Language**: Python
> **Testing Framework**: pytest

## Business Goal

Build a calculator module that performs basic arithmetic operations with proper error handling. This serves as a reference implementation of the Art of Intent pipeline.

## Technical Stack & Dependencies

- Pure Python standard library only.
- No external dependencies or packages are permitted.

## Core Interface Specification

The calculator module should expose the following standalone function signatures:

- `add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]`
- `subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]`
- `multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]`
- `divide(a: Union[int, float], b: Union[int, float]) -> Union[int, float]`

## Done State

- [x] Calculator can add two numbers and return the correct sum
- [x] Calculator can subtract two numbers and return the correct difference
- [x] Calculator can multiply two numbers and return the correct product
- [x] Calculator can divide two numbers and return the correct quotient
- [x] Division by zero raises a descriptive ValueError, not a crash

## Domain Vocabulary

| Term | Definition | Precise Data Type / Example |
| --- | --- | --- |
| Operand | A numeric value passed to an operation | `int` or `float` |
| Operation | One of the four basic arithmetic functions | `add`, `subtract`, `multiply`, `divide` |
| Result | The numeric output of an operation | `int` or `float` |
| DivisionByZeroError | A ValueError raised when the divisor is zero | `ValueError("cannot divide by zero")` |

## Constraints & Security

- All operations must accept both `int` and `float` operands.
- Results must preserve `float` precision when any operand is a `float`.
- Compatible with Python 3.8+ on standard operating systems (Windows, macOS, Linux).

## Out of Scope

- [x] Graphical User Interface (GUI) or web interface
- [x] CLI parser or interactive shell modes
- [x] Advanced math operations (powers, roots, trigonometry)

## Acceptance Criteria

1. **AC-1**: `add(2, 3)` returns `5`
2. **AC-2**: `subtract(10, 4)` returns `6`
3. **AC-3**: `multiply(3, 7)` returns `21`
4. **AC-4**: `divide(10, 2)` returns `5.0`
5. **AC-5**: `divide(10, 0)` raises `ValueError` with message containing "cannot divide by zero"
6. **AC-6**: `add(1.5, 2.5)` returns `4.0` (float precision preservation)

## Verification Guide

To verify this reference implementation:

- Run the unit tests using:

  ```bash
  pytest test_calculator.py
  ```

- Run interactive Python to test manual execution:

  ```python
  from calculator import add
  print(add(2, 3))  # Expected: 5
  ```

## Notes

This serves as Layer 1 documentation in the reference pipeline folder.
