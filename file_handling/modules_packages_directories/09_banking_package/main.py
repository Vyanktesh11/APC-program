from banking.account import create_account
from banking.transaction import deposit, withdraw
from banking.loan import simple_interest

account = create_account("Amit", 1000)
deposit(account, 500)
withdraw(account, 200)
print("Account:", account)
print("Loan simple interest:", simple_interest(10000, 8, 2))
