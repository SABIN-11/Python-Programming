# Check if a Number is Power of Two

num = int(input("Enter a number: "))

def is_power_of_two(n):

    # Brian Kernighan’s Algorithm to count how many set bits are there
    # if n < 0:
    #     return -1
    
    # count = 0

    # while n:
    #     n = n & (n - 1) # It removes 1 set bit from righthand side at every iteration
    #     count += 1
    # return result

    # BETTER AND CLEANER WAY TO DO IT
    return n > 0 and (n & (n - 1)) == 0 # n & n - 1 gives 0 for power of 2

result = is_power_of_two(num)

if num < 0:
    print("Number is negative.")
elif is_power_of_two(num):
    print(f"{num} is a power of 2.")
else:
    print(f"{num} is not a power of 2.")

# if result == -1:
#     print(f"Number is negative.")
# elif result == 1:
#     print(f"{num} is power of 2.")
# else:
#     print(f"{num} is not power of 2.")
