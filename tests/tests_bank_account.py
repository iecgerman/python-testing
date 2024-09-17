import unittest

from src.bank_account import BankAccount

class BankAccountTest(unittest.TestCase):

    def setUp(self) -> None:
        self.account = BankAccount(balance=1000)

    def test_deposit(self):
        # account = BankAccount(balance=1000)
        new_balance = self.account.deposit(500)
        assert new_balance == 1500

# .\venv\Scripts\activate    

# python -m unittest discover -v -s tests

# Resultado:

# (venv) PS C:\Users\info\python-testing> python -m unittest discover -v -s tests
# test_deposit (tests_bank_account.BankAccountTest.test_deposit) ... ok
# test_divide (tests_calculator.CalculatorTest.test_divide) ... ok
# test_multiply (tests_calculator.CalculatorTest.test_multiply) ... ok
# test_subtract (tests_calculator.CalculatorTest.test_subtract) ... ok
# test_sum (tests_calculator.CalculatorTest.test_sum) ... ok

# ----------------------------------------------------------------------
# Ran 5 tests in 0.001s

# OK
# (venv) PS C:\Users\info\python-testing> 

    def test_withdraw(self):
        # account = BankAccount(balance=1000)
        new_balance = self.account.withdraw(200)
        assert new_balance == 800

# Resultado

# (venv) PS C:\Users\info\python-testing> python -m unittest discover -v -s tests
# test_deposit (tests_bank_account.BankAccountTest.test_deposit) ... ok
# test_withdraw (tests_bank_account.BankAccountTest.test_withdraw) ... ok

    def test_get_balance(self):
        # account = BankAccount(balance=1000)
        assert self.account.get_balance() == 1000

# Resultado:

# test_get_balance (tests_bank_account.BankAccountTest.test_get_balance) ... ok

    def test_transfer(self):
        new_balance = self.account.transfer(1700)
        assert new_balance == 300

# Resultado:
# test_transfer (tests_bank_account.BankAccountTest.test_transfer) ... ok

