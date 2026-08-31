students = {
    "Rahul": "CSE",
    "Amit": "ENTC",
    "Priya": "CSE",
    "Sneha": "IT",
    "Rohan": "ENTC"
}

result = {}

for name, dept in students.items():
    if dept not in result:
        result[dept] = []
    result[dept].append(name)

print(result)
