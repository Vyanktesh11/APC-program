class ATM:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def check_balance(self):
        print("Current Balance: Rs.", self.balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit successful.")
        else:
            print("Enter a valid amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Enter a valid amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print("Withdrawal successful.")

    def display_details(self):
        print("Account Holder:", self.account_holder)
        print("Balance: Rs.", self.balance)

atm = ATM("Amit", 5000)

while True:
    print("\\n1. Check Balance\\n2. Deposit\\n3. Withdraw\\n4. Account Details\\n5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        atm.check_balance()
    elif choice == "2":
        atm.deposit(float(input("Enter deposit amount: ")))
    elif choice == "3":
        atm.withdraw(float(input("Enter withdrawal amount: ")))
    elif choice == "4":
        atm.display_details()
    elif choice == "5":
        break
    else:
        print("Invalid choice.")
