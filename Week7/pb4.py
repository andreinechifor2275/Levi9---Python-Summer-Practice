import threading
import time
import random
import pytest
from unittest.mock import patch, MagicMock
# ===============================================
# EXERCISE 4: Threading Race Condition
# ===============================================
# Create a bank account class and demonstrate race conditions

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        current = self.balance
        time.sleep(0.001)  # Simulate processing time
        self.balance = current + amount

    def withdraw(self, amount):
        if self.balance >= amount:
            current = self.balance
            time.sleep(0.001)  # Simulate processing time
            self.balance = current - amount
            return True
        return False

# TODO:
# 1. Create multiple threads that deposit/withdraw simultaneously
# 2. Show the race condition (final balance will be incorrect)
# 3. Fix it using threading.Lock

# ===============================================
# BankAccount - without proteccion (with race condition)
# ===============================================

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        current = self.balance
        time.sleep(0.001)
        self.balance = current + amount

    def withdraw(self, amount):
        if self.balance >= amount:
            current = self.balance
            time.sleep(0.001)
            self.balance = current - amount
            return True
        return False

def test_race_condition():
    account = BankAccount(100)

    def deposit_and_withdraw():
        for _ in range(100):
            account.deposit(5)
            account.withdraw(5)

    threads = []
    for _ in range(10):
        t = threading.Thread(target=deposit_and_withdraw)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Final balance (with race condition):", account.balance)
    assert account.balance != 100


# ===============================================
# SafeBankAccount - with proteccion (thread-safe)
# ===============================================

class SafeBankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self, amount):
        with self.lock:
            current = self.balance
            time.sleep(0.001)
            self.balance = current + amount

    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                current = self.balance
                time.sleep(0.001)
                self.balance = current - amount
                return True
            return False

def test_no_race_condition():
    account = SafeBankAccount(100)

    def deposit_and_withdraw():
        for _ in range(100):
            account.deposit(5)
            account.withdraw(5)

    threads = []
    for _ in range(10):
        t = threading.Thread(target=deposit_and_withdraw)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Final balance (with lock):", account.balance)
    assert account.balance == 100