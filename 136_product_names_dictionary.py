products = {
    "Pen": 15,
    "Book": 8,
    "Bag": 20
}

products["Pencil"] = 12

products["Pen"] = 25

del products["Book"]

name = input("Enter product to search: ")

if name in products:
    print("Quantity:", products[name])
else:
    print("Product not found")

print("Products with quantity below 10:")
for name, quantity in products.items():
    if quantity < 10:
        print(name, quantity)
