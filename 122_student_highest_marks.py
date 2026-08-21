marks = {
    "Rahul": 85,
    "Amit": 92,
    "Sneha": 78,
    "Priya": 95
}

student = max(marks, key=marks.get)

print("Highest marks:", marks[student])
print("Student:", student)
