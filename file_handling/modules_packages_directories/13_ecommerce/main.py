from products.catalog import products
from products.pricing import price
from customers.profile import customer
from customers.address import shipping_address
from orders.cart import total
from orders.status import order_status
from payments.method import payment_method
from payments.receipt import receipt

items = products()
buyer = customer("Amit")
address = shipping_address("Pune")
amount = total([price(item) for item in items])
print("Products:", items)
print("Customer:", buyer)
print("Address:", address)
print(order_status())
print("Payment:", payment_method())
print(receipt(amount))
