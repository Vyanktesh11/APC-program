class ElectricityBill:
    def __init__(self, consumer_no, consumer_name, units):
        self.consumer_no = consumer_no
        self.consumer_name = consumer_name
        self.units = units

    def calculate_bill(self):
        units = self.units
        if units <= 100:
            amount = units * 3
        elif units <= 200:
            amount = 100 * 3 + (units - 100) * 5
        elif units <= 300:
            amount = 100 * 3 + 100 * 5 + (units - 200) * 7
        else:
            amount = 100 * 3 + 100 * 5 + 100 * 7 + (units - 300) * 10
        return amount

bill = ElectricityBill(1001, "Amit", 250)
print("Consumer Number:", bill.consumer_no)
print("Consumer Name:", bill.consumer_name)
print("Units Consumed:", bill.units)
print("Electricity Bill: Rs.", bill.calculate_bill())
