import pandas as pd
data = {"Student_ID": [101, 102, 103, 104, 105], "Student_Name": ["Amit", "Priya", "Rahul", "Sneha", "Kiran"], "Python": [85, 78, 92, 67, 88], "DBMS": [80, 82, 90, 70, 86], "Mathematics": [75, 88, 85, 72, 91]}
df = pd.DataFrame(data)
subjects = ["Python", "DBMS", "Mathematics"]
df["Total"] = df[subjects].sum(axis=1)
df["Average"] = df[subjects].mean(axis=1)
print(df)
print("Students with average above 75:")
print(df[df["Average"] > 75])
