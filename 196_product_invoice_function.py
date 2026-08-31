products = {}

def add_product(name, price, quantity):
    products[name] = [price, quantity]

def remove_product(name):
    if name in products:
        del products[name]

def subtotal():
    total = 0
    for price, quantity in products.values():
        total += price * quantity
    return total

def coupon_discount(amount, coupon):
    if coupon.upper() == "SAVE10":
        return amount * 0.10
    return 0

def calculate_gst(amount):
    return amount * 0.18

def invoice(coupon):
    sub = subtotal()
    discount = coupon_discount(sub, coupon)
    taxable = sub - discount
    gst = calculate_gst(taxable)
    return sub, discount, gst, taxable + gst

add_product("Laptop", 50000, 1)
add_product("Mouse", 500, 2)

coupon = input("Enter coupon code: ")
sub, discount, gst, final_total = invoice(coupon)

print("Subtotal:", sub)
print("Coupon discount:", discount)
print("GST:", gst)
print("Final invoice amount:", final_total)
