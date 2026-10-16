class Distance:
    def __init__(self, feet, inches):
        total_inches = feet * 12 + inches
        self.feet = total_inches // 12
        self.inches = total_inches % 12

    def __add__(self, other):
        total_inches = self.feet * 12 + self.inches + other.feet * 12 + other.inches
        return Distance(0, total_inches)

    def __str__(self):
        return f"{self.feet} feet {self.inches} inches"

d1 = Distance(5, 8)
d2 = Distance(3, 9)
print("Sum:", d1 + d2)
