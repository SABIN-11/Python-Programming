# @property decorator is used to define a getter method for attributes

class Rectangle:

    def __init__(self, length: float, breadth: float):
        self._length = length
        self._breadth = breadth
    
    @property   # making getter methods
    def length(self):
        print("Length is being accessed right now ...")
        return self._length
    
    @property
    def breadth(self):
        print("Breadth is being accessed right now ...")
        return self._breadth
    
    @length.setter
    def length(self, n_length):
        if n_length > 0:
            self._length = n_length
        else:
            print("Length can't be less than or equal to 0") 

    @breadth.setter
    def breadth(self, n_breadth):
        if n_breadth > 0:
            self._breadth = n_breadth
        else:
            print("Breadth can't be less than 0") 




obj = Rectangle(12, 10)

print(obj.length)
print(obj.breadth)

obj.length = 0
obj.breadth = 0

print(obj.length)
print(obj.breadth)