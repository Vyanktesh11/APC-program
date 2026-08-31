employees = [
    ("Rahul", "IT", 45000),
    ("Amit", "HR", 60000),
    ("Priya", "IT", 75000),
    ("Sneha", "Finance", 50000)
]

above_50000 = list(filter(lambda employee: employee[2] > 50000, employees))

increased_salary = list(map(
    lambda employee: (employee[0], employee[1], employee[2] * 1.10),
    employees
))

sorted_employees = sorted(employees, key=lambda employee: employee[2])

print("Employees earning more than 50000:", above_50000)
print("Salaries increased by 10%:", increased_salary)
print("Employees sorted by salary:", sorted_employees)
