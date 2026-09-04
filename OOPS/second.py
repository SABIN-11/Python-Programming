# creating a rectangle class

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2*(self.width + self.height)
    
    def is_square(self) -> bool:
        return self.width == self.height
    
rec_1 = Rectangle(5, 10)
rec_2 = Rectangle(15, 15)

print(F"Area of reatangle 1 is {rec_1.area()}")             
print(F"Area of reatangle 2 is {rec_2.area()}")      

print(F"Perimeter of reatangle 1 is {rec_1.perimeter()}")             
print(F"Perimeter of reatangle 2 is {rec_2.perimeter()}")  

print(F"Rectangle 1 is a square is a {rec_1.is_square()} statement.")
print(F"Rectangle 2 is a square is a {rec_2.is_square()} statement.")
        