import pandas as pd
data = {"Employee_ID": [1, 2, 3, 4, 5], "Employee_Name": ["Amit", "Priya", "Rahul", "Sneha", "Kiran"], "Department": ["CSE", "HR", "CSE", "Sales", "IT"], "Salary": [60000, 45000, 72000, 52000, 48000], "Experience": [5, 3, 8, 4, 6]}
df = pd.DataFrame(data)
print(df[df["Salary"] > 50000])
print("Average Salary:", df["Salary"].mean())
print("Highest Salary:", df["Salary"].max())
print("Employee with highest experience:")
print(df.loc[df["Experience"].idxmax()])
