import pandas as pd
ages = pd.Series({"P101": 45, "P102": 67, "P103": 72, "P104": 35, "P105": 61})
print("Average Age:", ages.mean())
print("Oldest Patient:", ages.idxmax(), ages.max())
print("Youngest Patient:", ages.idxmin(), ages.min())
print("Patients above 60:")
print(ages[ages > 60])
