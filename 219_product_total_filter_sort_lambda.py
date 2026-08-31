products = [
    ("Laptop", 50000, 1),
    ("Mouse", 500, 2),
    ("Keyboard", 1500, 1),
    ("Monitor", 12000, 2)
]

def total_value(product):
    return product[1] * product[2]

values = list(map(lambda product: (product[0], total_value(product)), products))
above_1000 = list(filter(lambda product: total_value(product) > 1000, products))
sorted_products = sorted(products, key=lambda product: total_value(product))

print("Total value of each product:", values)
print("Products costing more than 1000:", above_1000)
print("Products sorted by total value:", sorted_products)
