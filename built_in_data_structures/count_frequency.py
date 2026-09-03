# Takes a list of n integers
# Prints how many times each element appears in the list
# from collections import Counter

n = int(input('Enter the number of items you want in the list: '))

# [1, 1, 2, 3, 4, 4, 4, 4, 4, 5]

print("Enter the elements in the list: ")
items = list(map(int, input().split()))

# 1ST WAY
# print(Counter(items))

# 2ND WAY
# CREATE AN EMPTY DICTIONARY
freq_dict = {}

for num in items:
    if num in freq_dict:    # CHECKING IF num key is already present in the dictionary
        freq_dict[num] += 1
    else:
        freq_dict[num] = 1

print(freq_dict)





