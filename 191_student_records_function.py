def calculate_result(marks):
    total = sum(marks)
    percentage = total / 5

    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    return total, percentage, grade

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter name: ")
    roll = input("Enter roll number: ")
    marks = []

    for j in range(5):
        marks.append(float(input("Enter marks: ")))

    total, percentage, grade = calculate_result(marks)
    students.append({
        "name": name,
        "roll": roll,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade
    })

class_average = sum(student["percentage"] for student in students) / n
highest = max(students, key=lambda student: student["percentage"])
lowest = min(students, key=lambda student: student["percentage"])

for student in students:
    print(student["name"], student["roll"], student["total"],
          student["percentage"], student["grade"])

print("Class average:", class_average)
print("Highest scorer:", highest["name"])
print("Lowest scorer:", lowest["name"])
