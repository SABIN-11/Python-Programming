# Remove all duplicates from a list while maintaining the original order.

n = int(input('Enter the number of items you want in the list: '))

print("Enter the elements in the list: ")
items = [int(input()) for i in range(n)]

# 1ST WAY
# freq = {}   # EMPTY DICTIONARY

# for num in items:
#     if num not in freq:
#         freq[num] = True

# # [3, 5, 2, 3, 8, 5, 6, 2]

result = []

# for num in items:
#     if freq[num] == True:
#         result.append(num)
#         freq[num] = False

# 2ND WAY
temp = []
for num in items:
    if num not in temp:
        temp.append(num)
        result.append(num)


print(result)

