class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def percentage(self):
        return sum(self.marks) / len(self.marks)

    def display(self):
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Percentage:", self.percentage(), "%")

students = [
    Student(1, "Amit", [80, 85, 90, 75, 88]),
    Student(2, "Priya", [92, 87, 95, 90, 89])
]

for student in students:
    student.display()
    print()
