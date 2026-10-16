import csv

filename = "students.csv"
with open(filename, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["RollNo", "Name", "Marks"])
    writer.writerows([[101, "Amit", 85], [102, "Priya", 92], [103, "Rahul", 78]])

with open(filename, "r", newline="") as f:
    records = list(csv.DictReader(f))

for student in records:
    print(student)

marks = [(row["Name"], int(row["Marks"])) for row in records]
print("Highest marks:", max(marks, key=lambda item: item[1]))
print("Average marks:", sum(mark for _, mark in marks) / len(marks))
print("Scored above 80:", [name for name, mark in marks if mark > 80])
