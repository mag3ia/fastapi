import pytest
from app.calc import *

# Fixtures
@pytest.fixture
def zero_bank_account():
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(50)


# Parametrization
@pytest.mark.parametrize("num1, num2, expected",
    [
        (3, 2, 5),
        (2, 7, 9),
        (1, 1, 2)
    ])
def test_add(num1, num2, expected):
    assert add(num1, num2) == expected

# Dummy classes tests

def test_bank_default_amount(zero_bank_account):
    assert zero_bank_account.balance == 0

def test_bank_withdraw(bank_account):
    bank_account.withdraw(20)
    assert bank_account.balance == 30

def test_bank_deposit(bank_account):
    bank_account.deposit(50)
    assert bank_account.balance == 100

def test_bank_interest(bank_account):
    bank_account.collect_interest()
    # as float will fail, rounded it
    assert round(bank_account.balance, 6) == 55

 