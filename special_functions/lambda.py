

# li = [1,2,3,4,15]

# squares = list(map(lambda x: x**2, li))

# print(squares)

# squares = lambda x: x**2
# print(squares(5))

li = [(lambda x: x**2)(i) for i in range(1, 6)]
print(li)