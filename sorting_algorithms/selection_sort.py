# At each step, find the minimum (or maximum) element in the unsorted part and swap it with the element at the current index.

# Let’s sort: [5, 3, 1, 4]

# Pass 1:
# Unsorted: [5, 3, 1, 4]
# Find min → 1
# Swap 1 with 5 → [1, 3, 5, 4]
# Pass 2:
# Unsorted: [3, 5, 4]
# Find min → 3
# Swap with itself → [1, 3, 5, 4]
# Pass 3:
# Unsorted: [5, 4]
# Find min → 4
# Swap 4 with 5 → [1, 3, 4, 5]

# INPUT THE ELEMENTS IN THE LIST
n = int(input("Enter the number of elements in the list:"))
print("Enter the items in the list:")
items = [int(input()) for i in range(n)]

for i in range(n):
    smallest_index = i
    for j in range(i + 1, n):
        if items[smallest_index] > items[j]:
            smallest_index = j
    items[i], items[smallest_index] = items[smallest_index], items[i]
        
print(items)