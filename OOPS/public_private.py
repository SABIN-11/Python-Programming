# attributes can be made public, protected and private

class A:
    name = "Sabin"  # Public Attribute, can be accessed by anything (sub-class and objects)
    _age = 17   # Protected Attribute
    __grade = 12    # Private Attribute

    def greet(self):
        print(f"Hello {B.name}")
        print(f"Hello {B._age}")
        print(f"Hello {B.__grade}") # NO ERROR, bcz __grade can be accessed within same class

class B(A):
    
    def greet(self):
        print(f"Hello {B.name}")
        print(f"Hello {B._age}")
        print(f"Hello {B.__grade}") # ERROR, bcz __grade is a private attribute and it can't be accessed by sub-class

obj_A = A()
obj_B = B()

print(obj_A.name)
print(obj_B.name)
print(obj_A._age)
print(obj_B._age)

# obj_B.greet()
obj_A.greet()

# print(obj_A.__grade)  # ERROR, bcz __grade can't be accessed by objects
# print(obj_B.__grade)

print(obj_A._A__grade)  # __grade can be accessed like this
