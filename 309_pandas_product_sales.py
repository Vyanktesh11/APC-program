import pandas as pd
data = {"Product_ID": [1, 2, 3, 4], "Product_Name": ["Laptop", "Mouse", "Keyboard", "Monitor"], "Category": ["Electronics", "Accessories", "Accessories", "Electronics"], "Price": [55000, 500, 1200, 10000], "Quantity": [2, 10, 5, 3]}
df = pd.DataFrame(data)
df["Total_Amount"] = df["Price"] * df["Quantity"]
print(df)
print("Product with highest total sales:")
print(df.loc[df["Total_Amount"].idxmax()])
