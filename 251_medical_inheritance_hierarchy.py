class Person:
    def __init__(self, name):
        self.name = name

class Doctor(Person):
    def __init__(self, name, specialty):
        super().__init__(name)
        self.specialty = specialty

class Patient(Person):
    def __init__(self, name, patient_id):
        super().__init__(name)
        self.patient_id = patient_id

class Surgeon(Doctor):
    def perform_surgery(self):
        print(self.name, "performs surgery.")

class MedicalResearcher(Doctor):
    def conduct_research(self):
        print(self.name, "conducts medical research.")

surgeon = Surgeon("Dr. Patil", "Surgery")
researcher = MedicalResearcher("Dr. Shah", "Research")
patient = Patient("Amit", 101)
surgeon.perform_surgery()
researcher.conduct_research()
print("Patient:", patient.name, patient.patient_id)
