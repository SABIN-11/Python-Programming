# isalnum() Method returns True if all characters are alphanumeric
# isalnum() but manually

input_text = input('Enter a string: ')

def isalnumMethod(input_text):

    for i in range(len(input_text)):
        ordinal = ord(input_text[i])
        if (ordinal >= 65 and ordinal <= 90) or (ordinal >= 97 and ordinal <= 122) or (ordinal >= 48 and ordinal <= 57):
            continue
        else:
            return False
        
    return True

result = isalnumMethod(input_text)

print(f"{result}")