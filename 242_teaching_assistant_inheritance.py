class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no

class Faculty(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

class TeachingAssistant(Student, Faculty):
    def __init__(self, name, roll_no, subject):
        Person.__init__(self, name)
        self.roll_no = roll_no
        self.subject = subject

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Subject:", self.subject)

ta = TeachingAssistant("Amit", 21, "Python")
ta.display()
