# Write a function group_anagrams(words) that takes a list of words and groups anagrams together. Return a list of lists.
# Test with: ["eat", "tea", "tan", "ate", "nat", "bat"]
# Should return: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

def group_anagrams(lst: list) -> list:
    result = {}

    for word in lst:
        key = "".join(sorted(word))
        if key not in result:
            result[key] = []

        result[key].append(word)

    return list(result.values())

lst = list(map(str, input("Enter list of words: ").split()))

print(F"Group of anagrams for {lst} is {group_anagrams(lst)}")
