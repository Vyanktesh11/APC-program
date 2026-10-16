import pandas as pd
data = {"Date": ["2026-01-01", "2026-01-02", "2026-01-03", "2026-01-04", "2026-01-05"], "City": ["Pune", "Mumbai", "Pune", "Nashik", "Mumbai"], "Temperature": [32, 36, 38, 30, 35], "Humidity": [45, 70, 50, 40, 65], "Rainfall": [0, 2, 0, 1, 3]}
pd.DataFrame(data).to_csv("weather.csv", index=False)
df = pd.read_csv("weather.csv")
print("Maximum temperature:", df["Temperature"].max())
print("Minimum temperature:", df["Temperature"].min())
print("Average temperature:", df["Temperature"].mean())
print("Temperature above 35 C:\\n", df[df["Temperature"] > 35])
print("City-wise average temperature:\\n", df.groupby("City")["Temperature"].mean())
