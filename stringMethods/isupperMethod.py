# isupper() Method returns True if all characters are uppercase otherwise returns False
# isupper() Method but manually

input_text = input('Enter a string: ')

def isupperMethod(input_text):
    
    for i in range (len(input_text)):
        ordinal = ord(input_text[i])
        if ordinal >= 97 and ordinal <= 122:
            return False
    
    countNonAlpha = 0

    for i in range(len(input_text)):
        ordinal = ord(input_text[i])
        if ordinal < 65 or (ordinal > 90 and ordinal < 97) or ordinal > 122:
            countNonAlpha += 1

    if countNonAlpha == len(input_text):
        return False
    
    return True

result = isupperMethod(input_text)

print(f"{result}")