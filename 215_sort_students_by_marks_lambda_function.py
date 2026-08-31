students = [
    ("Rahul", 85),
    ("Amit", 72),
    ("Priya", 95),
    ("Sneha", 80)
]

students.sort(key=lambda student: student[1])

print("Students sorted by marks:")
for student in students:
    print(student)
