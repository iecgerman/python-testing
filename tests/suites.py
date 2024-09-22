import unittest

from test_bank_account import BankAccountTest

def bank_account_suite():
    suite = unittest.TestSuite()
    suite.addTest(BankAccountTest("test_deposit"))
    suite.addTest(BankAccountTest("test_withdraw"))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(bank_account_suite())

# clase 9 min 10:53

# Para windows:

# cmd /c "set PYTHONPATH=. && python tests/test_suites.py"