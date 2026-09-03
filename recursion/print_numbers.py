# Print Numbers from 1 to N
# Base Case, n can't be 0

def print_numbers(n):
    if n > 0:
        print_numbers(n - 1)    # Before printing from 1 to n, print upto 1 to n - 1
        print(n, end="\t")

# Print Numbers from N to 1
# Base Case, n can't be 0
def print_reverse(n):
    if n > 0:
        print(n, end="\t")
        print_reverse(n - 1)

n = 5
print_numbers(n)
print()
print_reverse(n)
