from abc import ABC, abstractmethod

class FoodOrder(ABC):
    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def delivery_charge(self):
        pass

class RestaurantOrder(FoodOrder):
    def __init__(self, amount):
        self.amount = amount
    def calculate_bill(self):
        return self.amount
    def delivery_charge(self):
        return 0

class HomeDeliveryOrder(FoodOrder):
    def __init__(self, amount):
        self.amount = amount
    def calculate_bill(self):
        return self.amount + self.delivery_charge()
    def delivery_charge(self):
        return 50

for order in [RestaurantOrder(300), HomeDeliveryOrder(300)]:
    print("Bill:", order.calculate_bill(), "Delivery:", order.delivery_charge())
