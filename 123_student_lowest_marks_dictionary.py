marks = {
    "Rahul": 85,
    "Amit": 92,
    "Sneha": 78,
    "Priya": 95
}

student = min(marks, key=marks.get)

print("Lowest marks:", marks[student])
print("Student:", student)
