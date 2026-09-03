# Problem: Given an array where every element appears twice except for two numbers that appear once. Find those two numbers.

test_array = [1, 2, 2, 3, 1, 4, 4, 3, 0, 5]
# 1, 1, 2, 2, 3, 4

def find_two_non_repeating_element(arr):

    arr.sort()   # Sort the list
    result = []

    i = 0
    while i < len(arr):
        
        if i == len(arr) - 1:
            result.append(arr[i])
            break
        
        if arr[i] ^ arr[i + 1] == 0:
            i += 2
        else:
            result.append(arr[i])
            i += 1
    return result

print(f"{find_two_non_repeating_element(test_array)}")