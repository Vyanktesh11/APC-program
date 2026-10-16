import csv

employees = [
    ["EmployeeID", "Name", "Department", "Salary"],
    [1, "Amit", "IT", 45000],
    [2, "Priya", "HR", 52000],
    [3, "Rahul", "Sales", 40000]
]

with open("employees.csv", "w", newline="") as f:
    csv.writer(f).writerows(employees)

with open("employees.csv", "r", newline="") as f:
    records = list(csv.DictReader(f))

for employee in records:
    print(employee)

salaries = [(row["Name"], int(row["Salary"])) for row in records]
print("Highest-paid:", max(salaries, key=lambda item: item[1]))
print("Average salary:", sum(salary for _, salary in salaries) / len(salaries))

limit = float(input("Salary threshold: "))
print("Above threshold:", [name for name, salary in salaries if salary > limit])
