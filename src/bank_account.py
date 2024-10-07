from datetime import datetime
from src.exceptions import InsufficientFundsError, WithdrawalTimeRestrictionError

class BankAccount:
    def __init__(self, balance=0, log_file=None):
        self.balance = balance
        self.log_file = log_file
        self._log_transaction('Cuenta creada')

    def _log_transaction(self, message):
        if self.log_file:
            with open(self.log_file, "a") as f:
                f.write(f"{message}\n")

    def deposit(self, ammount):
        if ammount > 0:
            self.balance += ammount
            self._log_transaction(f"Deposited {ammount}. New balance: {self.balance}")
        return self.balance
    
    def withdraw(self, ammount):
        now = datetime.now()
        if now.hour < 8 and now.hour > 17:
            raise WithdrawalTimeRestrictionError("Withdrawal are only allowed from 8am to 5pm")


        if ammount > 0:
            self.balance -= ammount
            self._log_transaction(f"Withdrew {ammount}. New balance: {self.balance}")
        return self.balance
    
    def get_balance(self):
        self._log_transaction(f"Checked balance. Current balance: {self.balance}")
        return self.balance
    