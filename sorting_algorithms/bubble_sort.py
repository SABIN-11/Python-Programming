# Repeatedly compare adjacent elements and swap them if they’re in the wrong order. This way, the largest element "bubbles" to the end on each pass.

# [5, 3, 1, 4]

# Pass 1:
# Compare 5 > 3 → swap → [3, 5, 1, 4]
# Compare 5 > 1 → swap → [3, 1, 5, 4]
# Compare 5 > 4 → swap → [3, 1, 4, 5]
# Pass 2:
# Compare 3 > 1 → swap → [1, 3, 4, 5]
# Compare 3 < 4 → no swap
# Compare 4 < 5 → no swap

# INPUT THE ELEMENTS IN THE LIST
n = int(input("Enter the number of elements in the list:"))
print("Enter the items in the list:")
items = [int(input()) for i in range(n)]

for i in range(n):
    for j in range(n - 1 - i): # This is to avoid index out of bound error and we subtract i bcz at every iteration of i, the largest element moves to the rightmost side
        if items[j] > items[j + 1]:
            items[j], items[j + 1] = items[j + 1], items[j]

print(items)









