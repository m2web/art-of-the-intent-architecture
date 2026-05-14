"""
Calculator Module
Implemented via Layer 3 (Implementation Layer)
Intent Source: examples/calculator/01-intent.md
Delta Target: Δ = 0
"""


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b


def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


def divide(a, b):
    """Return the quotient of two numbers.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("division by zero")
    return a / b
