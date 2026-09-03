# Count Set Bits in an Integer
# Set Bits - 1

num = int(input("Enter a number: "))

# def count_set_bits(n):

#     if n < 0:
#         return -1
    
#     count = 0

#     while n:
#         count += (n & 1)
#         n >>= 1

#     return count

# OR using Brian Kernighan’s Algorithm
# O(k) where k is the number of set bits

def count_set_bits(n):

    if n < 0:
        return -1
    
    count = 0

    while n:
        n = n & (n - 1) # It removes 1 set bit from righthand side at every iteration
        count += 1

    return count

# for i in range (1, 1001):
#     print("{} = {}".format(i, count_set_bits(i)))

result = count_set_bits(num)

print(f"Number is negative") if result == -1 else print("Number of set bits are {} in {}".format(result, num))

# if result == -1:
#     print(f"Number is negative.")
# else:
#     print("Number of set bits are {} in {}.".format(result, num))


