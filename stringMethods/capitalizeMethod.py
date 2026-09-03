# Capitalize method only converts the first character of a string to Uppercase
# Capitalize method but manually

# input - 'hello world'
# output - 'Hello world'

string = input('Enter a string: ')

def capitalizeString(string):
    ordinal = ord(string[0])
    if ordinal >= 65 and ordinal <= 90:
        return string
    else:
        return chr(ordinal - 32) + string[1:]
    
print(f"Before: {string}")
print(f"After : {capitalizeString(string)}")