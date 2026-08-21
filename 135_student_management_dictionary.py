students = {
    "Rahul": 85,
    "Amit": 72,
    "Sneha": 92
}

students["Priya"] = 88

students["Rahul"] = 90

del students["Amit"]

name = input("Enter student name to search: ")
if name in students:
    print("Marks:", students[name])
else:
    print("Student not found")

print("All students:")
for name, marks in students.items():
    print(name, marks)

print("Highest marks:", max(students.values()))
print("Average marks:", sum(students.values()) / len(students))
