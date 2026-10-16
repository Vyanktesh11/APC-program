import pandas as pd
data = {"Employee_ID": [1, 2, 3, 4, 5], "Name": ["Amit", "Priya", "Rahul", "Sneha", "Kiran"], "Department": ["CSE", "HR", "CSE", "IT", "HR"], "Experience": [5, 3, 8, 4, 6], "Salary": [60000, 45000, 72000, 52000, 48000]}
pd.DataFrame(data).to_csv("employees.csv", index=False)
df = pd.read_csv("employees.csv")
print("CSE employees:\\n", df[df["Department"] == "CSE"])
print("Average salary:", df["Salary"].mean())
print("Highest salary:", df["Salary"].max())
print("Lowest salary:", df["Salary"].min())
print("Salary above 50000:\\n", df[df["Salary"] > 50000])
print("Department-wise average salary:\\n", df.groupby("Department")["Salary"].mean())
