n = int(input('Enter the number of rows: '))

for i in range(n, 0, -1):
    for j in range(1, n - i + 1):
        print(" ", end = "")
    for k in range(1, 2*i):
        print("*", end = "")

    print()

# *********
#  *******
#   *****
#    ***
#     *