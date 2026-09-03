# Reverse all elements in a list without using reversed() or [::-1]

n = int(input('Enter the number of items you want in the list: '))

print("Enter the elements in the list: ")
items = [int(input()) for i in range(n)]

# [1, 2, 3, 4, 5]
def reverse_list(li):

    start = 0
    end = len(li) - 1

    while start < end:
        li[start], li[end] = li[end], li[start]
        start += 1
        end -= 1

    return li

print(f"Original List: {items}")
print(f"Reversed List: {reverse_list(items)}")