class StudentResult:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return self.total() / (len(self.marks) * 100) * 100

    def grade(self):
        percent = self.percentage()
        if percent >= 90:
            return "A"
        elif percent >= 75:
            return "B"
        elif percent >= 60:
            return "C"
        elif percent >= 40:
            return "D"
        return "F"

    def __del__(self):
        print("Result object destroyed.")

result = StudentResult("Amit", [85, 90, 78, 88, 92])
print("Student Name:", result.name)
print("Marks:", result.marks)
print("Total:", result.total())
print("Percentage:", result.percentage())
print("Grade:", result.grade())
del result
