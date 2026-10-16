class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate / 100

class PremiumSavingsAccount(SavingsAccount):
    def __init__(self, account_number, balance, interest_rate, benefits):
        super().__init__(account_number, balance, interest_rate)
        self.benefits = benefits

    def display(self):
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)
        print("Interest:", self.calculate_interest())
        print("Benefits:", self.benefits)

account = PremiumSavingsAccount("SB101", 50000, 5, "Priority service and higher withdrawal limit")
account.display()
