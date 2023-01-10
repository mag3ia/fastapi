import pytest
from app.calc import *

# Fixtures
@pytest.fixture
def zero_bank_account():
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(50)

@pytest.mark.parametrize("x, y, z",
    [
        (200, 100, 100),
        (50, 10, 40),
        (1200, 200, 1000),
        # (0, 100, 0)
    ])
def test_bank_transaction(zero_bank_account, x, y, z):
    zero_bank_account.deposit(x)
    zero_bank_account.withdraw(y)
    assert zero_bank_account.balance == z

def test_insufficient_founds(bank_account):
    with pytest.raises(InsufficientFunds):
        bank_account.withdraw(100)