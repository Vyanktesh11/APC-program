import pandas as pd
data = {"Patient_ID": [1, 2, 3, 4, 5], "Name": ["Amit", "Priya", "Rahul", "Sneha", "Kiran"], "Age": [65, 42, 72, 55, 30], "Gender": ["M", "F", "M", "F", "M"], "Disease": ["Diabetes", "Fever", "Heart Disease", "Asthma", "Fever"], "Medical_Expense": [60000, 1500, 85000, 12000, 2000]}
pd.DataFrame(data).to_csv("patients.csv", index=False)
df = pd.read_csv("patients.csv")
print("Patients above 60:\\n", df[df["Age"] > 60])
print("Average medical expense:", df["Medical_Expense"].mean())
print("Highest expense patient:\\n", df.loc[df["Medical_Expense"].idxmax()])
print("Count by disease:\\n", df["Disease"].value_counts())
print("Expenses above 50000:\\n", df[df["Medical_Expense"] > 50000])
