students = [
    ("Rahul", 80),
    ("Amit", 70),
    ("Priya", 90),
    ("Sneha", 76)
]

def average_marks(records):
    return sum(mark for name, mark in records) / len(records)

above_75 = list(filter(lambda student: student[1] > 75, students))
sorted_students = sorted(students, key=lambda student: student[1])

print("Average marks:", average_marks(students))
print("Students scoring above 75:", above_75)
print("Students sorted according to marks:", sorted_students)
