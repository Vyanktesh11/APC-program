from patient_management.patients import patient_details
from doctor_management.doctors import doctor_details
from billing.invoice import calculate_bill
from medical_records.records import create_record

patient = patient_details("Amit", 22)
doctor = doctor_details("Dr. Patil", "General Medicine")
record = create_record(patient["name"], "Routine check-up")
print("Patient:", patient)
print("Doctor:", doctor)
print("Record:", record)
print("Bill:", calculate_bill(500, 250))
