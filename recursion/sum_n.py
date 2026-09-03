# Sum of First N Natural Numbers

# Write a recursive function sum_n(n) that returns the sum of first n natural numbers.
# Input: n = 5
# Expected Output: 15
# (Because 1 + 2 + 3 + 4 + 5 = 15)

# Base Case: if n is 1, return 1

def sum_n(n):
    if n == 1:
        return 1
    else:
        return sum_n(n - 1) + n

print(sum_n(5))