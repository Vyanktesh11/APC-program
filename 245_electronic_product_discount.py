class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

class ElectronicProduct(Product):
    def __init__(self, product_id, name, price, brand, warranty):
        super().__init__(product_id, name, price)
        self.brand = brand
        self.warranty = warranty

    def final_price(self, discount_percent):
        return self.price - self.price * discount_percent / 100

product = ElectronicProduct(1, "Laptop", 60000, "Lenovo", "2 years")
print("Product ID:", product.product_id)
print("Name:", product.name)
print("Brand:", product.brand)
print("Warranty:", product.warranty)
print("Final Price:", product.final_price(10))
