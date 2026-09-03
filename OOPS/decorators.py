# decorators are callable functions that take one function as input, changes its behaviour and wrap it in a function and returns that function
# Examples - @staticmethod, @classmethod, @property etc

# class Book:

#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

#     # @classmethod    # can be used as alternative constructor for creating objects
#     # def from_string(cls, info):
#     #     title, author = info.split('-')
#     #     return cls(title, author)

#     @classmethod
#     def from_string(cls, info: str):
#         title, author = info.split('-')
#         instance = cls(title, author)
#         instance.genre = "Action"   # genre attribute is just for the instane created from this function
#         return instance


#     def __str__(self):
#         return f"{self.title}, {self.author}"

# book1 = Book("Naruto", "Masashi Kishimoto")
# book2 = Book.from_string("One Piece-Eiichiro Oda")

# print(book1)
# print(book2)
# print(book2.genre)
# print(book1.genre)

# USER-DEFINED DECORATORS

# def greet(*args, **kwargs): 
#     print(args) # args stores any no of postitional arguments as tuple (1, 2, 3)
#     print(kwargs)   # kwargs stores any no of keyword arguments as dictioanary {'x' : 10}

# greet(1, 2, 3, x = 10)

import time

# task: find the time of execution of our function

def timer(func):
    def wrapper(*args, **kwargs):
        # Before calling original function
        start_time = time.time()    # seconds passed since EPOCH(Jan 1, 1970)
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} function ran for {end_time - start_time} seconds.")
        return result
    return wrapper

@timer  
def add(x, y):
    return x + y
        
# @timer  
# def add(x, y):
    #return x + y

# This whole thing is equivalent to add = timer(add), timer gets executed once and it returns wrapper function
# then it becomes add = wrapper, so when we do add(x, y), actually wrapper function gets called
# basically wrapper and add both holds the reference for the same function

result = add(5, 6)  # this is equivalent to result = wrapper(5, 6) and (5, 6) is store in *args as tuple
print(result)