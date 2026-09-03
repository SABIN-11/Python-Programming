# Find the Only Odd Occurring Element in an Array

test_array = [1, 2, 3, 2, 3, 1, 4]


# def find_odd_occurring_element(arr):

#     arr.sort()   # Sort the list
#     i = 0
#     while i < len(arr):
        
#         if i == len(arr) - 1:
#             return arr[i]
        
#         if arr[i] ^ arr[i + 1] == 0:
#             i += 2
#         else:
#             return arr[i]

# BETTER APPROACH

def find_odd_occurring_element(arr):
    result = 0
    for num in arr:
        result ^= num
    return result

print(find_odd_occurring_element(test_array))

