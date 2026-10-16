class Employee:
    def calculate_salary(self):
        return 0

class Manager(Employee):
    def calculate_salary(self):
        return 60000

class Developer(Employee):
    def calculate_salary(self):
        return 50000

class Tester(Employee):
    def calculate_salary(self):
        return 40000

for employee in [Manager(), Developer(), Tester()]:
    print(type(employee).__name__, "Salary:", employee.calculate_salary())
