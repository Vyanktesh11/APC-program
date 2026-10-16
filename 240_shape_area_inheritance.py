import math

class Shape:
    def display_name(self):
        print("Shape:", self.__class__.__name__)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

shapes = [Circle(7), Rectangle(5, 4), Triangle(6, 3)]
for shape in shapes:
    shape.display_name()
    print("Area:", round(shape.area(), 2))
