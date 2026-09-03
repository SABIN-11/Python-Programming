# class variable and instance variable
# class variable is same for all instances and defined outside any method but within the class
# instance variable is unique for each instance and is defined within the method

class Car:
    # wheels: int = 4 # class variable, same for all instances
    def __init__(self, brand: str, color: str):
        self.brand = brand  # instance variable
        self.color = color  # instance variable
    
    def __str__(self) -> str:
        return f"Brand: {self.brand} & Color: {self.color}"


c1 = Car("tesla", "black")
c2 = Car("audi", "yellow")
c3 = Car("lamborghini", "red")

print(c1)
print(c2)
print(c3)

# print(c1.wheels)
c1.wheels = 5
print(c1.wheels)
# print(c2.wheels)
# print(c3.wheels)



    
        