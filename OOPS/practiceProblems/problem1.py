# 1. Create a class 2D vector and use it to create another class representing 3D vector

# 2. Create a class pets from a class Animal and further create a class Dog from Pets. Add a method back to class Dog.

# 3. Create a class Employee and add salary and increment properties to it. Write a method salaryAfterIncrement method with a
# @property decorator with a setter which changes the value of increment based on the salaryAfterIncrement

# 4. Write a class complex to represent complex numbers, along with overloaded operators + and * which adds and multiplies them

# 5. Write a class vector representing a vector of n dimension. Overload the + and * operator which calculates the sum and the 
# dot product of them.

# 6. Write __str__() method to print the vector as follows. 
# 7i + 8j + 10k, Assume vector of dimension 3 for this problem

# 7. Override the __len__() method on Vector of problem 5 to display dimension of the vector

# Problem 5
class Vector:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __mul__(self, other):
        return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)
    
    @property
    def magnitude(self):
        return ((self.x)**2 + (self.y)**2 + (self.z)**2)**(1/2)
    
    def __str__(self):
        return f"{self.x}î + {self.y}ĵ + {self.z}k̂"
    
    def __len__(self):
        return sum(1 for component in (self.x, self.y, self.z) if component != 0)
    
    def active_dimension(self):
        dimension = len(self)
        if dimension == 1:
            print(f"{self} has 1 direction in 3D space.")
        elif dimension == 2:
            print(f"{self} has 2 directions in 3D space.")
        else:
            print(f"{self} has 3 directions in 3D space.")
    

    
v1 = Vector(2, 3, 4)
v2 = Vector(2, 4, 3)
v3 = Vector(5, 0, 0)

print(v1 + v2)
print(v1 * v2)

print(v1.magnitude)
v1.active_dimension()
v3.active_dimension()

        

# Problem 4
# class Complex:
#     def __init__(self, real, imag):
#         self.real = real
#         self.imag = imag

#     @property
#     def complex_no(self):
#         return f"{self.real} + {self.imag}i"
    
#     def __add__(self, other):
#         return Complex(self.real + other.real, self.imag + other.imag)
#         # return f"{self} + {other} = {self.real + other.real} + {self.imag + other.imag}i"
    
#     def __mul__(self, other):
#         return Complex(self.real * other.real - self.imag * other.imag, self.real * other.imag + self.imag * other.real)
#         # return f"{self} * {other} = {self.real * other.real - self.imag * other.imag} + {self.real * other.imag + self.imag * other.real}i"
    
#     def __str__(self):
#         return f"({self.real} + {self.imag}i)"


# first_complex_no = Complex(1, 2)
# print(first_complex_no.complex_no)
# second_complex_no = Complex(1, 2)
# print()
# print(first_complex_no + second_complex_no) # 9 + 11i
# print(first_complex_no.__add__(second_complex_no))  # 9 + 11i     
# print(Complex.__add__(first_complex_no, second_complex_no)) # 9 + 11i
# print()
# print(first_complex_no * second_complex_no)

        

# Problem 3
# class Employee:

#     def __init__(self, salary, increment):
#         self.salary = salary
#         self.increment = increment

#     @property
#     def salaryAfterIncrement(self):
#         return self.salary * self.increment
    
#     @salaryAfterIncrement.setter
#     def salaryAfterIncrement(self, new_salAfterIncrement):
#         if new_salAfterIncrement <= 0:
#             print("Salary can't be less than or equal to 0.")
#         else:
#             self.increment = new_salAfterIncrement / self.salary 

#     def display_salary(self):
#         print(f"Salary After Increment of {((self.increment - 1) * 100):.2f}%: {self.salaryAfterIncrement}")


# emp1 = Employee(10000, 1.05)
# emp1.display_salary()
# emp1.salaryAfterIncrement = 11000
# print(emp1.increment)
# emp1.display_salary()


# Problem 1
# class twoDVector:
#     def __init__(self, x_component, y_component):
#         self.x_component = x_component
#         self.y_component = y_component

# class threeDVector(twoDVector):
#     def __init__(self, x_component, y_component, z_component):
#         super().__init__(x_component, y_component)
#         self.z_component = z_component

#     def displayVector(self) -> None:
#         print(f"Vector is {self.x_component}i + {self.y_component}j + {self.z_component}k")

# v1 = threeDVector(3, 4, 5)
# v1.displayVector()

# # Problem 2
# class Animal:
#     def __init__(self, name: str, color: str, kept_at_home: bool):
#         self.name = name
#         self.color = color
#         self.kept_at_home = kept_at_home
        
#     def is_growable(self):
#         if self.kept_at_home:
#             print(f"Yes, {self.name} is growable at home.")
#         else:
#             print(f"{self.name} can't be grown at home.")

# class Pet(Animal):
#     pass

# class Dog(Pet):

#     def __init__(self, petName, color, kept_at_home):
#         super().__init__("Dog", color, kept_at_home)
#         self.petName = petName

#     def is_growable(self):
#         print("Yes, Dog is growable at home.")

#     def dog_name(self):
#         print(f"{self.petName} is the name of our Dog.")

# d = Dog("Daizy", "white", True)
# d.is_growable()
# d.dog_name()
    



        

# def init(self, name, age):
#     self.name = name
#     self.age = age

# Student = type("Student", (), {
#     "__init__" : init,
#     "introduction" : lambda self : print(f"Name: {self.name} & Age: {self.age}")
# })

# s1 = Student("Sabin", 17)
# s1.introduction()




