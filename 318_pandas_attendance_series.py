import pandas as pd
attendance = pd.Series({"Amit": 80, "Priya": 95, "Rahul": 68, "Sneha": 92, "Kiran": 73})
print("Average Attendance:", attendance.mean())
print("Attendance below 75%:")
print(attendance[attendance < 75])
print("Attendance above 90%:")
print(attendance[attendance > 90])
print("Highest Attendance:", attendance.idxmax(), attendance.max())
