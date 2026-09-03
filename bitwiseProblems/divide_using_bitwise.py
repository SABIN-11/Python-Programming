# Divide two integers a divided by b using only bitwise operators, subtraction, and conditionals (i.e., no /, %, or *).
# a = 43, b = 5
def find_highest_shift(a, b):

    i = 0

    while (b << i) <= a: # increase i until the value of b << i becomes more than a
        i += 1

    return i - 1

def divide_using_bit_operators(a, b):

    quotient = 0

    while a >= b:
        shift = find_highest_shift(a, b)
        quotient |= (1 << shift)
        a -= (b << shift)

    return quotient

print(f"{divide_using_bit_operators(49, 7)}")



 