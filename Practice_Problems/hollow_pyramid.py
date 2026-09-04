#     *
#    * *
#   *   *
#  *     *
# *********

n = int(input("Enter the number of row: "))

for i in range(1, n + 1):
    for j in range(1, n - i + 1):
        print(" ", end = "")
    
    for k in range(1, 2*i):
        if k == 1 or k == 2 * i - 1 or i == n:
            print("*", end = "")
        else:
            print(" ", end = "")
    
    print()
