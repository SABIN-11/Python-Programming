# Create a base Shape class and two child classes that add specific calculations.

import math

class Shape:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def describe(self):
        print(F"This is a {self.color} colored {self.name}")

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__("Circle", color)
        self.radius = radius

    def area(self):
        ar = math.pi * self.radius**2
        print(F"Area of the circle is {ar} sq. unit.")

    def perimeter(self):
        peri_mtr = 2 * math.pi * self.radius
        print(F"Perimeter of the circle is {peri_mtr} unit.")

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__("Rectangle", color)
        self.width = width
        self.height = height
    
    def area(self):
        print(F"Area of this rectangle is {self.width * self.height} sq. unit.")

    def perimeter(self):
        print(F"Perimeter of this rectangle is {2 * (self.width + self.height)} unit.")
        

cir_1 = Circle("red", 5)
cir_1.area()
cir_1.perimeter()
cir_1.describe()

print()

rect_1 = Rectangle("red", 5, 7)
rect_1.area()
rect_1.perimeter()
rect_1.describe()
        