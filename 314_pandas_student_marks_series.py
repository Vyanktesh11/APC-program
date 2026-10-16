import pandas as pd
marks = pd.Series({"Amit": 85, "Priya": 92, "Rahul": 74, "Sneha": 88, "Kiran": 67})
print(marks)
print("Priya's Marks:", marks["Priya"])
print("Maximum Marks:", marks.max())
print("Minimum Marks:", marks.min())
print("Average Marks:", marks.mean())
print("Students scoring above 75:")
print(marks[marks > 75])
