roll = int(input("Enter Roll Number: "))
name = input("Enter Name: ")
department = input("Enter Department: ")
marks = float(input("Enter Marks: "))

student = (roll, name, department, marks)

print("Student Details:")
print("Roll Number:", student[0])
print("Name:", student[1])
print("Department:", student[2])
print("Marks:", student[3])
