# Write a function flatten(lst) that takes a nested list and returns a single flat list.
# Test with: [1, [2, 3], [4, [5, 6]], 7] → [1, 2, 3, 4, 5, 6, 7]
# Note: the nesting can be more than one level deep.

def flatten(lst: list) -> list:
    result = [] 
    for item in lst:
        if isinstance(item, list):
            result += flatten(item)
        else:
            result.append(item)

    return result

lst = [1, [2, 3], [4, [5, 6]], 7]

print(F"Flatten version of {lst} is {flatten(lst)}")