class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)

class Car(Vehicle):
    def __init__(self, brand, model, fuel_type, price):
        super().__init__(brand, model)
        self.fuel_type = fuel_type
        self.price = price

    def discounted_price(self, discount_percent):
        return self.price - self.price * discount_percent / 100

    def display(self):
        super().display()
        print("Fuel Type:", self.fuel_type)
        print("Price:", self.price)
        print("Price after discount:", self.discounted_price(10))

car = Car("Tata", "Nexon", "Petrol", 900000)
car.display()
