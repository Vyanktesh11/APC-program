class BankAccount:
    def calculate_interest(self, balance):
        return 0

class SavingsAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.04

class CurrentAccount(BankAccount):
    def calculate_interest(self, balance):
        return 0

class FixedDepositAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.07

for account in [SavingsAccount(), CurrentAccount(), FixedDepositAccount()]:
    print(type(account).__name__, "Interest:", account.calculate_interest(10000))
