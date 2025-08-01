import threading
import time
import random
import pytest
from unittest.mock import patch, MagicMock

# ===============================================
# EXERCISE 3: Parametrized Testing
# ===============================================
# Test a password validation function with multiple test cases

def is_strong_password(password):
    """Check if password meets strength requirements"""
    if len(password) < 8:
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.islower() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    return True

# TODO: Create parametrized tests with different password examples:
# Valid: "MyPass123", "StrongP@ss1"
# Invalid: "weak", "NOLOWER123", "noupper123", "NoDigits"


# def test_password_valid_mypass123():
#     assert is_strong_password("MyPass123") == True
#
# def test_password_valid_strongpass():
#     assert is_strong_password("StrongP@ss1") == True
#
#
#
# def test_password_invalid_short():
#     assert is_strong_password("weak") == False
#
# def test_password_invalid_no_lowercase():
#     assert is_strong_password("NOLOWER123") == False
#
# def test_password_invalid_no_uppercase():
#     assert is_strong_password("noupper123") == False
#
# def test_password_invalid_no_digits():
#     assert is_strong_password("NoDigits") == False
#
# def test_password_invalid_too_short_even_if_valid_chars():
#     assert is_strong_password("Ab1cD") == False


@pytest.mark.parametrize("password, expected", [
        ("MyPass123",True),
        ("StrongP@ss1",True),
        ("weak",False),
        ("NOLOWER123",False),
        ("noupper123",False),
        ("NoDigits",False),
])

def test_password_valid(password, expected):
    assert is_strong_password(password) == expected



