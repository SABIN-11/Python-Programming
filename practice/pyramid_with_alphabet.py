
n = int(input('Enter the number of rows: '))

for i in range(1, n + 1):
    alphabet = 65
    for j in range(1, n - i + 1):
        print(" ", end = "")
    for k in range(1, 2*i):
        print(chr(alphabet), end = "")
        alphabet += 1

    print()