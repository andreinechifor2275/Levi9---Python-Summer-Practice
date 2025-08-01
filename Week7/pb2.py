import threading
import time
import random
import pytest
from unittest.mock import patch, MagicMock

# ===============================================
# EXERCISE 2: Mock Testing
# ===============================================
# Test a function that sends emails. Mock the print function to verify email sending behavior.

def send_notification(email, message):
    print(f"Sending email to {email}: {message}")
    # Simulate email sending
    if "@" not in email:
        raise ValueError("Invalid email address")
    return f"Email sent to {email}"

# TODO: Write a test using @patch to mock the email sending
# Verify that:
# - Function is called with correct arguments
# - Invalid emails raise ValueError
# - Function returns expected message


import pytest

def test_send_notification_success():
    email = "test@example.com"
    message = "Hello!"

    with patch("builtins.print") as mock_print:
        result = send_notification(email, message)
        mock_print.assert_called_once_with(f"Sending email to {email}: {message}")
        assert result == f"Email sent to {email}"

def test_send_notification_invalid_email():
    email = "invalid-email"
    message = "Hello!"

    with patch("builtins.print") as mock_print:
        with pytest.raises(ValueError, match="Invalid email address"):
            send_notification(email, message)
        mock_print.assert_called_once_with(f"Sending email to {email}: {message}")
