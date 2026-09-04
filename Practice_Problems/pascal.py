
import math

rows = int(input("Enter the number of rows you want: "))

for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end="")

    for k in range(i + 1):
        print(F"{math.comb(i, k)} ", end="")

    print()

