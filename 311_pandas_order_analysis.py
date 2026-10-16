import pandas as pd
data = {"Order_ID": [101, 102, 103, 104], "Customer": ["Amit", "Priya", "Rahul", "Sneha"], "Product": ["Laptop", "Phone", "Mouse", "Monitor"], "Quantity": [1, 2, 5, 1], "Price": [60000, 20000, 500, 10000], "Discount": [3000, 1500, 100, 500]}
df = pd.DataFrame(data)
df["Final_Amount"] = df["Quantity"] * df["Price"] - df["Discount"]
print("All Orders:\\n", df)
print("Orders above 5000:\\n", df[df["Final_Amount"] > 5000])
print("Highest-value order:\\n", df.loc[df["Final_Amount"].idxmax()])
print("Average Order Value:", df["Final_Amount"].mean())
