# MANUALLY REMOVING LEADING AND TRAILING WHITE SPACES

string = input('ENTER A STRING: ')
string2 = ''

# start = 0
# end = len(string) - 1

# # Step 1: Remove leading spaces
# while start < len(string) and string[start] == ' ':
#     start += 1

# # Step 2: Remove trailing spaces
# while end >= 0 and string[end] == ' ':
#     end -= 1

# # Step 3: Slice the string
# if start <= end:
#     string2 = string[start:end+1]
# else:
#     string2 = ''    # Only spaces in the string

# print(f"Result: {string2}")

# Using strip() function to remove leading and trailing white spaces

string2 = string.strip()
print(f"Result: {string2}")

