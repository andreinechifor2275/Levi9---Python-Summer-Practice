import threading
import time
import random
import pytest
from unittest.mock import patch, MagicMock


# ===============================================
# EXERCISE 1: Basic Unit Testing
# ===============================================

class Calculator:
    def add(self, a, b):
        return a + b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def multiply(self, a, b):
        return a * b

# TODO: Write pytest tests for Calculator class
# Test cases should include:
# - Normal addition, multiplication and division
# - Division by zero error
# - Test for negative numbers

@pytest.fixture
def calc():
    return Calculator()

def test_addition(calc):
    assert calc.add(3, 5) == 8
    assert calc.add(-2, 4) == 2

def test_multiplication(calc):
    assert calc.multiply(4, 3) == 12
    assert calc.multiply(-2, 5) == -10

def test_division(calc):
    assert calc.divide(10, 2) == 5
    assert calc.divide(-9, 3) == -3

def test_divide_by_zero(calc):
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.divide(20, 0)