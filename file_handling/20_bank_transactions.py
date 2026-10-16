import csv

transactions = [["Type", "Amount"], ["Deposit", 1000], ["Withdrawal", 250],
                ["Deposit", 500], ["Withdrawal", 100]]

with open("transactions.csv", "w", newline="") as f:
    csv.writer(f).writerows(transactions)

with open("transactions.csv", "r", newline="") as f:
    rows = list(csv.DictReader(f))

deposits = [int(row["Amount"]) for row in rows if row["Type"] == "Deposit"]
withdrawals = [int(row["Amount"]) for row in rows if row["Type"] == "Withdrawal"]
amounts = [int(row["Amount"]) for row in rows]

print("Total deposits:", sum(deposits))
print("Total withdrawals:", sum(withdrawals))
print("Final balance:", sum(deposits) - sum(withdrawals))
print("Largest transaction:", max(amounts))
