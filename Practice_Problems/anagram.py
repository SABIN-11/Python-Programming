
def anagram(s1: str, s2: str) -> bool:
    d1, d2 = {}, {}

    for i in s1:
        if i in d1:
            d1[i] += 1
        else:
            d1[i] = 1
    
    for i in s2:
        if i in d2:
            d2[i] += 1
        else:
            d2[i] = 1

    return True if d1 == d2 else False

s1 = input('Enter first string: ')
s2 = input('Enter second string: ')

result = anagram(s1, s2)

if result:
    print(f"{s1} and {s2} are anagrams.")
else:
    print(f"{s1} and {s2} are not anagrams.")