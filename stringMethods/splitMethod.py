# split() method but manually

string = input('Enter a string: ')

# "Python is fun".split()
# Output: ['Python', 'is', 'fun']

def splitString(string):

    collection = [] # Empty list

    new_string = string.strip() # Remove any leading and trailing spaces if present
    temp_str = ''

    for i in range (len(new_string)):
        if new_string[i] != ' ':
            temp_str += new_string[i]
        if new_string[i] == ' ' or i == len(new_string) - 1:
           if temp_str != '':
                collection.append(temp_str) 
                temp_str = ''
    else:
        return collection

print(splitString(string))

# OR SIMPLY USE split() function
# print(string.split())

            

