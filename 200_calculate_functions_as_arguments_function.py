def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

def calculate(operation, a, b):
    return operation(a, b)

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", calculate(addition, a, b))
print("Subtraction:", calculate(subtraction, a, b))
print("Multiplication:", calculate(multiplication, a, b))

if b != 0:
    print("Division:", calculate(division, a, b))
else:
    print("Division: Cannot divide by zero")
