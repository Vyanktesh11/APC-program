class Payment:
    def make_payment(self, amount):
        print("Processing payment:", amount)

class UPIPayment(Payment):
    def make_payment(self, amount):
        print("Paid Rs.", amount, "using UPI.")

class CardPayment(Payment):
    def make_payment(self, amount):
        print("Paid Rs.", amount, "using card.")

class WalletPayment(Payment):
    def make_payment(self, amount):
        print("Paid Rs.", amount, "using wallet.")

def process_payment(payment, amount):
    payment.make_payment(amount)

for method in [UPIPayment(), CardPayment(), WalletPayment()]:
    process_payment(method, 1000)
