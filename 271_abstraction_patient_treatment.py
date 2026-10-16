from abc import ABC, abstractmethod

class Patient(ABC):
    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def treatment(self):
        pass

class InPatient(Patient):
    def calculate_bill(self):
        return 5000
    def treatment(self):
        return "Hospital admission and care"

class OutPatient(Patient):
    def calculate_bill(self):
        return 800
    def treatment(self):
        return "Consultation and medicines"

class EmergencyPatient(Patient):
    def calculate_bill(self):
        return 10000
    def treatment(self):
        return "Immediate emergency care"

for patient in [InPatient(), OutPatient(), EmergencyPatient()]:
    print(patient.treatment(), "- Bill:", patient.calculate_bill())
