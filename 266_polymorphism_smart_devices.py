class SmartDevice:
    def turn_on(self):
        print("Device turned on.")
    def turn_off(self):
        print("Device turned off.")

class Light(SmartDevice):
    def turn_on(self):
        print("Light switched on.")
    def turn_off(self):
        print("Light switched off.")

class Fan(SmartDevice):
    def turn_on(self):
        print("Fan started.")
    def turn_off(self):
        print("Fan stopped.")

class AC(SmartDevice):
    def turn_on(self):
        print("AC started cooling.")
    def turn_off(self):
        print("AC turned off.")

class TV(SmartDevice):
    def turn_on(self):
        print("TV turned on.")
    def turn_off(self):
        print("TV turned off.")

for device in [Light(), Fan(), AC(), TV()]:
    device.turn_on()
    device.turn_off()
