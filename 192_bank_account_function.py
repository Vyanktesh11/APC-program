balance = 0
transactions = []

def deposit(amount):
    global balance
    balance += amount
    transactions.append("Deposited: " + str(amount))

def withdrawal(amount):
    global balance

    if amount <= balance:
        balance -= amount
        transactions.append("Withdrawn: " + str(amount))
        print("Withdrawal successful")
    else:
        print("Insufficient balance")

def balance_enquiry():
    print("Balance:", balance)

def transaction_history():
    print("Transaction History:")
    for transaction in transactions:
        print(transaction)

deposit(5000)
withdrawal(1500)
balance_enquiry()
transaction_history()
