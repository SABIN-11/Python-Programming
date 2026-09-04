# return the number of vowels in a given string


def count_vowels(st:str) -> int:
    st = st.upper()
    ctr = 0
    vowels = "AEIOU"
    for i in range(len(st)):
        if st[i] in vowels:
            ctr += 1

    return ctr

st = input('Enter the string: ')
print(F"Number of vowels in {st} is {count_vowels(st)}")