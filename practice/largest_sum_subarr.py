# Input: arr[] = [2, 3, -8, 7, -1, 2, 3]
# Output: 11
# Explanation: The subarray [7, -1, 2, 3] has the largest sum 11.

# Input: arr[] = [-2, -4]
# Output: -2
# Explanation: The subarray [-2] has the largest sum -2.

# Input: arr[] = [5, 4, 1, 7, 8]
# Output: 25
# Explanation: The subarray [5, 4, 1, 7, 8] has the largest sum 25.

arr = list(map(int, input("Enter numbers: ").split()))

largest_sum = 0
size = len(arr)
largest_sum = arr[0]

for i in range(size):
    sum = 0 
    for j in range(i, size):
        sum = sum + arr[j]
        if sum > largest_sum:
            largest_sum = sum

print(f"Largest sum of sub array in {arr} is {largest_sum}")

