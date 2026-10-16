import pandas as pd
data = {"Patient_ID": [1, 2, 3, 4, 5], "Patient_Name": ["Amit", "Priya", "Rahul", "Sneha", "Kiran"], "Age": [65, 42, 72, 55, 30], "Disease": ["Diabetes", "Fever", "Heart Disease", "Asthma", "Fever"], "Medical_Charges": [60000, 1500, 85000, 12000, 2000]}
df = pd.DataFrame(data)
print("Patients above 60:")
print(df[df["Age"] > 60])
print("Average Medical Charge:", df["Medical_Charges"].mean())
print("Maximum Medical Charge:", df["Medical_Charges"].max())
print("Charges above 50000:")
print(df[df["Medical_Charges"] > 50000])
