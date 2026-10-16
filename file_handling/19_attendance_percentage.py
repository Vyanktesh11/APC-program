import csv

records = [
    ["Name", "Present", "Total"],
    ["Amit", 70, 90],
    ["Priya", 80, 90],
    ["Rahul", 60, 90]
]

with open("attendance.csv", "w", newline="") as f:
    csv.writer(f).writerows(records)

with open("attendance.csv", "r", newline="") as f:
    students = list(csv.DictReader(f))

for student in students:
    percentage = int(student["Present"]) / int(student["Total"]) * 100
    print(student["Name"], f"{percentage:.2f}%")
    if percentage < 75:
        print("Below 75%:", student["Name"])
