# Write a Python program that takes a list of integers as input (in a single line), removes the duplicates, and prints the sorted list in ascending order.

n = int(input("Enter the number of items to be in the list:"))
print("Enter the items in the list: ")

items = [int(input()) for i in range(n)]


# input - 10 5 2 10 5 7 2 3
# output - [2, 3, 5, 7, 10]

no_dupli_list = list(set(items))
no_dupli_list.sort()
print(no_dupli_list)