import pytest
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