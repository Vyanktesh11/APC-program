class FoodOrder:
    def __init__(self, order_id, customer_name, food_item, quantity, price):
        self.order_id = order_id
        self.customer_name = customer_name
        self.food_item = food_item
        self.quantity = quantity
        self.price = price

    def total_bill(self, tax_percent=5):
        subtotal = self.quantity * self.price
        return subtotal + subtotal * tax_percent / 100

    def __del__(self):
        print("Order completed.")

order = FoodOrder(501, "Priya", "Pizza", 2, 250)
print("Order ID:", order.order_id)
print("Customer:", order.customer_name)
print("Food Item:", order.food_item)
print("Quantity:", order.quantity)
print("Total including 5% tax: Rs.", order.total_bill())
del order
