# Add 1 to a Number Without Using +

num = int(input("Enter a number: "))
def add_one_without_plus(n):
    return -~n

print("{0} + 1 = {1}".format(num, add_one_without_plus(num)))