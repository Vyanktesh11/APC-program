class Vehicle:
    def __init__(self, vehicle_number, model, rental_rate, available=True):
        self.vehicle_number = vehicle_number
        self.model = model
        self.rental_rate = rental_rate
        self.available = available

    def rent(self):
        if self.available:
            self.available = False
            print("Vehicle rented successfully.")
        else:
            print("Vehicle is not available.")

    def return_vehicle(self):
        self.available = True
        print("Vehicle returned.")

    def rental_charges(self, days):
        return self.rental_rate * days

vehicle = Vehicle("MH09AB1234", "Hatchback", 1200)
vehicle.rent()
print("Rental charges for 3 days: Rs.", vehicle.rental_charges(3))
vehicle.return_vehicle()
