# second largest in a list\
# [5,1]

def second_largest(lst: list):

    if len(lst) < 2:
        return None
    
    largest = lst[0]
    sec_largest = float('-inf') # negative infinity

    for i in lst:
        if i > largest:
            sec_largest = largest
            largest = i
        if i > sec_largest and i < largest:
            sec_largest = i

    return sec_largest

lst = list(map(int, input("Enter a list: ").split()))
s_largest = second_largest(lst)

print(f"Second largest in the list {lst} is {s_largest}")

