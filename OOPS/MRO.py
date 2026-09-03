class A:
    def greet(self):
        print(f"A from {self.__class__.__name__}")
        super().greet()

class F:
    def greet(self):
        print(f"F from {self.__class__.__name__}")

class B(A, F):
    def greet(self):
        print(f"B from {self.__class__.__name__}")
        super().greet()

class E:
    def greet(self):
        print(f"E from {self.__class__.__name__}")

class C(E, F):
    
    def greet(self):
        print(f"C from {self.__class__.__name__}")
        super().greet()

class D(B, C):
    pass

d = D()
print(D.__mro__)    
d.greet()   








