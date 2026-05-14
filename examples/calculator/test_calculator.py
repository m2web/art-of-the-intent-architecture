"""
Inferred TDD Test Suite — Calculator
Generated from: examples/calculator/01-intent.md
Layer: 2 (Actor-Critic)
"""
import pytest


# ---------------------------------------------------------------------------
# AC-1: add(2, 3) returns 5
# ---------------------------------------------------------------------------
def test_add_integers():
    from calculator import add
    assert add(2, 3) == 5


# ---------------------------------------------------------------------------
# AC-2: subtract(10, 4) returns 6
# ---------------------------------------------------------------------------
def test_subtract_integers():
    from calculator import subtract
    assert subtract(10, 4) == 6


# ---------------------------------------------------------------------------
# AC-3: multiply(3, 7) returns 21
# ---------------------------------------------------------------------------
def test_multiply_integers():
    from calculator import multiply
    assert multiply(3, 7) == 21


# ---------------------------------------------------------------------------
# AC-4: divide(10, 2) returns 5.0
# ---------------------------------------------------------------------------
def test_divide_integers():
    from calculator import divide
    assert divide(10, 2) == 5.0


# ---------------------------------------------------------------------------
# AC-5: divide(10, 0) raises ValueError
# ---------------------------------------------------------------------------
def test_divide_by_zero_raises_error():
    from calculator import divide
    with pytest.raises(ValueError, match="division by zero"):
        divide(10, 0)


# ---------------------------------------------------------------------------
# AC-6: add(1.5, 2.5) returns 4.0 (float preservation)
# ---------------------------------------------------------------------------
def test_add_floats_preserves_type():
    from calculator import add
    result = add(1.5, 2.5)
    assert result == 4.0
    assert isinstance(result, float)


# ---------------------------------------------------------------------------
# Critic-added: Negative number edge cases
# ---------------------------------------------------------------------------
def test_add_negative_numbers():
    from calculator import add
    assert add(-3, -7) == -10


def test_multiply_negative_numbers():
    from calculator import multiply
    assert multiply(-3, 7) == -21
    assert multiply(-3, -7) == 21


# ---------------------------------------------------------------------------
# Critic-added: Float preservation across all operations
# ---------------------------------------------------------------------------
def test_subtract_floats():
    from calculator import subtract
    result = subtract(5.5, 2.5)
    assert result == 3.0
    assert isinstance(result, float)


def test_multiply_floats():
    from calculator import multiply
    result = multiply(2.5, 4.0)
    assert result == 10.0
    assert isinstance(result, float)


def test_divide_floats():
    from calculator import divide
    result = divide(7.5, 2.5)
    assert result == 3.0
    assert isinstance(result, float)
