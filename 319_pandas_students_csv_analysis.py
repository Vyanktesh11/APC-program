import pandas as pd
data = {"Student_ID": [101, 102, 103, 104, 105, 106], "Name": ["Amit", "Priya", "Rahul", "Sneha", "Kiran", "Meera"], "Department": ["CSE", "IT", "CSE", "ENTC", "CSE", "IT"], "Python": [85, 78, 92, 67, 88, 75], "DBMS": [80, 82, 90, 70, 86, 79], "Maths": [75, 88, 85, 72, 91, 80]}
pd.DataFrame(data).to_csv("students.csv", index=False)
df = pd.read_csv("students.csv")
subjects = ["Python", "DBMS", "Maths"]
df["Total"] = df[subjects].sum(axis=1)
df["Average"] = df[subjects].mean(axis=1)
print("First 5 records:\\n", df.head())
print("Last 5 records:\\n", df.tail())
print(df[["Name", "Total", "Average"]])
print("Students with average above 75:\\n", df[df["Average"] > 75])
print("Student with highest average:\\n", df.loc[df["Average"].idxmax()])
print("Subject averages:\\n", df[subjects].mean())
