import pytest, os
from src.bank_account import BankAccount

@pytest.mark.parametrize("ammount, expected", [
    (100, 1100),
    (3000, 4000),
    (4500, 5500),
])
def test_deposit_multiple_ammounts(ammount, expected):

    account = BankAccount(balance=1000, log_file="transactions.txt")
    new_balance = account.deposit(ammount)
    assert new_balance == expected

# pytest tests/test_pytest.py -v

# tests/test_pytest.py::test_deposit_multiple_ammounts[100-1100] PASSED                             [ 33%]
# tests/test_pytest.py::test_deposit_multiple_ammounts[3000-4000] PASSED                            [ 66%]
# tests/test_pytest.py::test_deposit_multiple_ammounts[4500-5500] PASSED                            [100%]



# def test_sum():
#     a = 4
#     b = 8
#     assert a + b == 8

# Supermaiven:
def test_deposit_negative():
    account = BankAccount(balance=1000, log_file="transactions.txt")
    with pytest.raises(ValueError):
        account.deposit(-100)

# chatGPT:
@pytest.mark.parametrize(
    "initial_balance, deposit_amount, expected_balance, expect_exception", 
    [
        (1000, 100, 1100, None),        # Positive deposit, valid case
        (1000, -100, 1000, ValueError), # Negative deposit, should raise ValueError
        (500, 200, 700, None),          # Another positive deposit case
        (500, 0, 500, None),            # Deposit zero, no balance change
    ]
)
def test_deposit(initial_balance, deposit_amount, expected_balance, expect_exception):
    # Setup: Initialize account with initial balance and log file
    account = BankAccount(balance=initial_balance, log_file="transactions.txt")
    
    if expect_exception:
        # Act & Assert: Expect the exception to be raised for negative deposits
        with pytest.raises(expect_exception):
            account.deposit(deposit_amount)
    else:
        # Act: Perform deposit and check the balance for positive/zero deposits
        new_balance = account.deposit(deposit_amount)
        assert new_balance == expected_balance

    # Cleanup: Remove the log file after the test
    if os.path.exists("transactions.txt"):
        os.remove("transactions.txt")