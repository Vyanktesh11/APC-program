class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

class Manager(Employee):
    def salary(self):
        return self.basic_salary + self.basic_salary * 0.30

class Developer(Employee):
    def salary(self):
        return self.basic_salary + self.basic_salary * 0.20

class Tester(Employee):
    def salary(self):
        return self.basic_salary + self.basic_salary * 0.10

employees = [
    Manager(1, "Amit", 50000),
    Developer(2, "Priya", 40000),
    Tester(3, "Rahul", 35000)
]
for employee in employees:
    print(employee.name, "Salary:", employee.salary())
