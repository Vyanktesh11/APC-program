def deposit(account, amount):
    if amount > 0: account["balance"] += amount
    return account["balance"]
def withdraw(account, amount):
    if 0 < amount <= account["balance"]: account["balance"] -= amount
    return account["balance"]
