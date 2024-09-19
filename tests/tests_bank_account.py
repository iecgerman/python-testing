import unittest, os

from src.bank_account import BankAccount

class BankAccountTest(unittest.TestCase):

    def setUp(self) -> None:
        self.account = BankAccount(balance=1000, log_file="transaction_log.txt")

    def tearDown(self) -> None:
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)

    def _count_lines(self, filename):
        with open(filename, "r") as f:
            return len(f.readlines())

    def test_deposit(self):
        # account = BankAccount(balance=1000)
        new_balance = self.account.deposit(500)
        # assert new_balance == 1500 se quita en la clase 7
        self.assertEqual(new_balance, 1500, "El balance no es igual") # clase 7

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
        # assert new_balance == 800
        self.assertEqual(new_balance, 800, "El Balance no es igual") # clase 7

# Resultado

# (venv) PS C:\Users\info\python-testing> python -m unittest discover -v -s tests
# test_deposit (tests_bank_account.BankAccountTest.test_deposit) ... ok
# test_withdraw (tests_bank_account.BankAccountTest.test_withdraw) ... ok

    def test_get_balance(self):
        # account = BankAccount(balance=1000)
        # assert self.account.get_balance() == 1000
        self.assertEqual(self.account.get_balance(), 1000) # clase 7


# Resultado:

# test_get_balance (tests_bank_account.BankAccountTest.test_get_balance) ... ok

    def test_transaction_log(self):
        self.account.deposit(500)
        # assert os.path.exists("transaction_log.txt")
        self.assertTrue(os.path.exists("transaction_log.txt"))

# test_transaction_log (tests_bank_account.BankAccountTest.test_transaction_log) ... ok

    def test_count_transactions(self):
        assert self._count_lines(self.account.log_file) == 1
        self.account.deposit(500)
        assert self._count_lines(self.account.log_file) == 2

# test_count_transactions (tests_bank_account.BankAccountTest.test_count_transactions) ... ok

