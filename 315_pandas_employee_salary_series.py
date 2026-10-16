import pandas as pd
salaries = pd.Series({"Amit": 60000, "Priya": 48000, "Rahul": 75000, "Sneha": 52000, "Kiran": 42000})
print(salaries)
print("Highest Salary:", salaries.max())
print("Lowest Salary:", salaries.min())
print("Average Salary:", salaries.mean())
print("Employees earning above 50000:")
print(salaries[salaries > 50000])
