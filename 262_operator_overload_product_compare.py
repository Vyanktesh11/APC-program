class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

    def __gt__(self, other):
        return self.price > other.price

p1 = Product("Keyboard", 800)
p2 = Product("Mouse", 400)
print("Same price:", p1 == p2)
print("Keyboard costs more:", p1 > p2)
