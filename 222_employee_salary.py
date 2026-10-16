class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def calculate_hra(self):
        return self.basic_salary * 0.20

    def calculate_da(self):
        return self.basic_salary * 0.10

    def gross_salary(self):
        return self.basic_salary + self.calculate_hra() + self.calculate_da()

employee = Employee(101, "Amit", 30000)
print("Employee ID:", employee.emp_id)
print("Name:", employee.name)
print("Basic Salary:", employee.basic_salary)
print("HRA:", employee.calculate_hra())
print("DA:", employee.calculate_da())
print("Gross Salary:", employee.gross_salary())
