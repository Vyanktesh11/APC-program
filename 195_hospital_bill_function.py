def consultation_charges(amount):
    return amount

def laboratory_charges(amount):
    return amount

def medicine_charges(amount):
    return amount

def room_charges(amount):
    return amount

def discount(category, total):
    if category.lower() == "senior":
        return total * 0.10
    elif category.lower() == "child":
        return total * 0.05
    return 0

consultation = float(input("Enter consultation charges: "))
laboratory = float(input("Enter laboratory charges: "))
medicine = float(input("Enter medicine charges: "))
room = float(input("Enter room charges: "))
category = input("Enter patient category: ")

total = (consultation_charges(consultation) +
         laboratory_charges(laboratory) +
         medicine_charges(medicine) +
         room_charges(room))

final_bill = total - discount(category, total)

print("Final bill:", final_bill)
