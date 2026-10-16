class Student:
    def __init__(self, roll_no, name, course):
        self.roll_no = roll_no
        self.name = name
        self.course = course

class Result(Student):
    def __init__(self, roll_no, name, course, marks):
        super().__init__(roll_no, name, course)
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return self.total() / (len(self.marks) * 100) * 100

    def grade(self):
        p = self.percentage()
        if p >= 90: return "A"
        if p >= 75: return "B"
        if p >= 60: return "C"
        if p >= 40: return "D"
        return "F"

result = Result(21, "Amit", "CSE", [80, 85, 90])
print("Roll No:", result.roll_no)
print("Name:", result.name)
print("Course:", result.course)
print("Total:", result.total())
print("Percentage:", result.percentage())
print("Grade:", result.grade())
