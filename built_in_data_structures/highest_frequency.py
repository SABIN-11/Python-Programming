# Find the element with the highest frequency in the list.

n = int(input('Enter the number of elements you want in the list: '))

print("Enter the numbers in the list:")
items = list(map(int, input().split()))

def highest_freq(li):
    freq = {} # EMPTY DICTIONARY

    for num in li:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    key_highest_freq = max(freq, key = freq.get)
    return (key_highest_freq, freq[key_highest_freq])   # RETURN A TUPLE


result = highest_freq(items)
print(f"Element with highest frequency: {result[0]}")
print(f"Frequency: {result[1]}")


