class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, doors):
        super().__init__(brand)
        self.doors = doors

class Bike(Vehicle):
    def __init__(self, brand, engine_cc):
        super().__init__(brand)
        self.engine_cc = engine_cc

class SportsCar(Car):
    def __init__(self, brand, doors, top_speed):
        super().__init__(brand, doors)
        self.top_speed = top_speed

class ElectricBike(Bike):
    def __init__(self, brand, engine_cc, battery_range):
        super().__init__(brand, engine_cc)
        self.battery_range = battery_range

sports_car = SportsCar("Porsche", 2, 300)
electric_bike = ElectricBike("Ather", 0, "120 km")
print("Sports Car:", sports_car.brand, sports_car.doors, sports_car.top_speed)
print("Electric Bike:", electric_bike.brand, electric_bike.battery_range)
