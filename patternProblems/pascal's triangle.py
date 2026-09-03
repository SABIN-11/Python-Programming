# Printing Pascal's Triangle
# Pascal's Triangle's row and column starts from 0
# Value at (i, j) = i! / {(i - j)! * j!}

# Function for calculation of factorial
def factorial(num):
    result = 1

    for i in range (2, num + 1):
        result *= i

    return result

row = 6

for i in range (row + 1):
    
    for k in range (row - i):
        print(" ", end="")

    for j in range (i + 1):
        value = factorial(i) // (factorial(j) * (factorial(i - j)))
        print(value, end= " ")
    print()