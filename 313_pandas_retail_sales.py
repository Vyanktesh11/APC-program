import pandas as pd
data = {"Product_ID": [1, 2, 3, 4], "Product_Name": ["Laptop", "Phone", "Mouse", "Monitor"], "Category": ["Electronics", "Electronics", "Accessories", "Electronics"], "Price": [50000, 20000, 600, 9000], "Quantity": [2, 3, 20, 4]}
df = pd.DataFrame(data)
df["Total_Sales"] = df["Price"] * df["Quantity"]
print(df)
print("Products with sales above 10000:")
print(df[df["Total_Sales"] > 10000])
print("Product with maximum sales:")
print(df.loc[df["Total_Sales"].idxmax()])
print("Average Sales:", df["Total_Sales"].mean())
