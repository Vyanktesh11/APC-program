class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Animal makes a sound.")

class Dog(Animal):
    def sound(self):
        print("Woof!")

class Cat(Animal):
    def sound(self):
        print("Meow!")

class Cow(Animal):
    def sound(self):
        print("Moo!")

for animal in [Dog("Dog"), Cat("Cat"), Cow("Cow")]:
    print(animal.name, end=": ")
    animal.sound()
