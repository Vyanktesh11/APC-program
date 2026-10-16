class Academic:
    def __init__(self, marks):
        self.marks = marks

class Sports:
    def __init__(self, sports_points):
        self.sports_points = sports_points

class Student(Academic, Sports):
    def __init__(self, name, marks, sports_points):
        Academic.__init__(self, marks)
        Sports.__init__(self, sports_points)
        self.name = name

    def overall_performance(self):
        return sum(self.marks) / len(self.marks) + self.sports_points

student = Student("Amit", [80, 85, 90], 8)
print("Name:", student.name)
print("Academic Marks:", student.marks)
print("Sports Points:", student.sports_points)
print("Overall Performance Score:", student.overall_performance())
