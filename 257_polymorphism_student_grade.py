class Student:
    def calculate_grade(self, marks):
        return "Not defined"

class EngineeringStudent(Student):
    def calculate_grade(self, marks):
        return "A" if marks >= 80 else "B" if marks >= 60 else "C"

class MedicalStudent(Student):
    def calculate_grade(self, marks):
        return "Pass" if marks >= 50 else "Fail"

class ManagementStudent(Student):
    def calculate_grade(self, marks):
        return "Excellent" if marks >= 85 else "Good" if marks >= 60 else "Needs Improvement"

for student in [EngineeringStudent(), MedicalStudent(), ManagementStudent()]:
    print(type(student).__name__, student.calculate_grade(75))
