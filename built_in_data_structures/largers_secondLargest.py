# Takes n numbers into a list from the user
# Prints the largest and second largest number in the list

n = int(input('Enter number of elements in a list: '))

print(f"Enter {n} elements in the list: ")
items = [int(input()) for i in range(n)]

item_dupli = list(set(items))

print(f"Largest: {max(item_dupli)}")
item_dupli.remove(max(item_dupli))
print(f"Second Largest: {max(item_dupli)}")
