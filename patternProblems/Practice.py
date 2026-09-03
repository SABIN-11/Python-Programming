
n = 4

# Right-Angled Triangle
for i in range (1, n + 1):
    for j in range (1, i + 1):
        print("*", end = "")
    print()

print()

# Inverted Right-Angled Triangle
for i in range (1, n + 1):
    for j in range (1, n - i + 2):
        print("*", end = "")
    print()

print()

# Right-Angled Triangle with Same Numbers
for i in range (1, n + 1):
    for j in range (1, i + 1):
        print(i, end = "")
    print()

print()

# Right-Aligned Triangle (using spaces)
for i in range (1, n + 1):
    for j in range (1, n - i + 1):
        print(" ", end="")
    for k in range (1, i + 1):
        print("*", end="")
    print()

print()

# Pyramid (Center-Aligned)
for i in range (1, n + 1):
    for j in range (1, n - i + 1):
        print(" ", end = "")
    for k in range (1, 2 * i):
        print("*", end = "")
    print()

print()

# Hollow Right-Angled Triangle:
for i in range (1, n + 1):
    for j in range (1, i + 1):
        if j == 1 or j == i or i == n:
            print("*", end = "")
        else:
            print(" ", end="")
    print()

print()

# Hollow Pyramid
for i in range (1, n + 1):
    for k in range (1, n - i + 1):
        print(" ", end="")
    for j in range (1, 2 * i):
        if j == 1 or j == 2 * i - 1 or i == n:
            print("*", end="")
        else:
            print(" ", end="")
    print() 

print()

# Diamond Pattern

# First Part of Diamond
for i in range (1, n + 1):
    for j in range (1, n - i + 1):  # white spaces
        print(" ", end = "")
    for k in range (1, 2 * i):
        print("*", end="")
    print()

# Second Part of Diamond
for i in range (1, n): # Second part has 1 less row than first part of the diamond
    for j in range (1, i + 1):
        print(" ", end="")
    for k in range (1, 2 * (n - i)):
        print("*", end="")
    print()

print()

# Floyd's Triangle
var = 1

for i in range (1, n + 1):
    for j in range (1, i + 1):
        print(var, end=" ")
        var += 1
    print()
