students = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter Name: ")
    roll = int(input("Enter Roll Number: "))
    marks = float(input("Enter Marks: "))
    students.append([name, roll, marks])

print("Student Details")
for i in students:
    print("Name:", i[0], "Roll:", i[1], "Marks:", i[2])