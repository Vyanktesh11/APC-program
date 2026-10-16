import pandas as pd
prices = pd.Series({"Laptop": 55000, "Mouse": 500, "Keyboard": 1500, "Monitor": 12000})
print("Products and Prices:\\n", prices)
print("Prices after 10% increase:\\n", prices * 1.10)
print("Most Expensive Product:", prices.idxmax())
print("Products costing more than 1000:")
print(prices[prices > 1000])
