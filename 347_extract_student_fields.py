import re

text = input("Enter text containing student name, roll number, and marks: ")
names = re.findall(r"(?i)name\\s*[:=-]\\s*([A-Za-z ]+)", text)
roll_numbers = re.findall(r"(?i)roll\\s*(?:no\\.?|number)?\\s*[:=-]\\s*([A-Za-z0-9/-]+)", text)
marks = re.findall(r"(?i)marks?\\s*[:=-]\\s*(\\d+(?:\\.\\d+)?)", text)
print("Names:", [name.strip() for name in names])
print("Roll numbers:", roll_numbers)
print("Marks:", marks)
