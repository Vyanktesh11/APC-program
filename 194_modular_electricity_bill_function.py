def slab_charge(units):
    if units <= 100:
        return units * 5
    elif units <= 200:
        return 100 * 5 + (units - 100) * 7
    else:
        return 100 * 5 + 100 * 7 + (units - 200) * 10

def fixed_charge():
    return 50

def calculate_tax(amount):
    return amount * 0.05

def calculate_discount(amount):
    if amount > 2000:
        return amount * 0.10
    return 0

def electricity_bill(units):
    charge = slab_charge(units)
    fixed = fixed_charge()
    tax = calculate_tax(charge)
    discount = calculate_discount(charge)

    return charge + fixed + tax - discount

units = float(input("Enter units consumed: "))
print("Final electricity bill:", electricity_bill(units))
