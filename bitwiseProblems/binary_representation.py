# Write a function to_8bit_binary(n) that returns the 8-bit 2's complement binary representation of both positive and negative integers.

num = int(input("Enter a number: "))

def to_8bit_binary(n):
    return format(n & 0xff, '08b')  # Format returns the string conversion of any value to required number system 
    # '08b' means 8 characters long binary format string
    # 0xff - 255
    # n & 0xff keeps only 8 bits of the number from right-side

print(f"2's complement Binary representation of {num} = {to_8bit_binary(num)}")