import pandas as pd
data = {"Student_ID": [1, 2, 3, 4], "Name": ["Amit", "Priya", "Rahul", "Sneha"], "Department": ["CSE", "CSE", "IT", "CSE"], "Total_Classes": [100, 100, 90, 80], "Classes_Attended": [80, 70, 60, 75]}
df = pd.DataFrame(data)
df["Attendance_Percentage"] = df["Classes_Attended"] / df["Total_Classes"] * 100
print(df)
print("Students below 75% attendance:")
print(df[df["Attendance_Percentage"] < 75])
