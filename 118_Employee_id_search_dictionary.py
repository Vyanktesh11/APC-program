employees = {
    101: "Rahul",
    102: "Amit",
    103: "Sneha",
    104: "Priya"
}

eid = int(input("Enter employee ID: "))

if eid in employees:
    print("Employee exists:", employees[eid])
else:
    print("Employee does not exist")
