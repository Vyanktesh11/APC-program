class Camera:
    def take_photo(self):
        print("Photograph taken.")

class Phone:
    def make_call(self, number):
        print("Calling", number)

class Smartphone(Camera, Phone):
    def browse_internet(self):
        print("Browsing the internet.")

phone = Smartphone()
phone.take_photo()
phone.make_call("9876543210")
phone.browse_internet()
