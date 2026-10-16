class ShoppingCart:
    def __init__(self, customer_name, cart_id):
        self.customer_name = customer_name
        self.cart_id = cart_id
        self.products = []

    def add_product(self, name, price):
        self.products.append({"name": name, "price": price})

    def remove_product(self, name):
        for product in self.products:
            if product["name"] == name:
                self.products.remove(product)
                return True
        return False

    def total_bill(self):
        return sum(product["price"] for product in self.products)

    def __del__(self):
        print("Shopping cart object destroyed.")

cart = ShoppingCart("Amit", 101)
cart.add_product("Book", 300)
cart.add_product("Pen", 20)
print("Customer:", cart.customer_name)
print("Cart ID:", cart.cart_id)
print("Total Bill: Rs.", cart.total_bill())
cart.remove_product("Pen")
print("Bill after removal: Rs.", cart.total_bill())
del cart
