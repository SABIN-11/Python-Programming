# Takes a list of integers from the user using a single input line
# Converts them to a list
# Prints the sum of the list

n = int(input('Enter number of elements in a list: '))

print(f"Enter {n} elements in the list: ")
items = [int(input()) for i in range(n)]

# items = list(map(int, input().split()))

print(sum(items))



