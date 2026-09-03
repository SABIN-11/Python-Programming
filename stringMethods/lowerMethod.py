# Case-Insensitive Comparison
# Manual conversion of UPPERCASE to lowercase

str1 = input('ENTER FIRST STRING: ')
str2 = input('ENTER SECOND STRING: ')


# def toLowercase(string):
#     new_string = ''
#     for i in range(len(string)):
#         unicode = ord(string[i])
#         if unicode >= 65 and unicode <= 90:
#             new_string += chr(unicode + 32)
#         else:
#             new_string += string[i]
#     else:
#         return new_string
    
# if toLowercase(str1) == toLowercase(str2):
#     print(f"{str1} & {str2} are same string if ignoring the case.")
# else:
#     print(f"{str1} & {str2} are not same string.")

# OR SIMPLY USE .lower() function

if str1.lower() == str2.lower():
   print(f"{str1} & {str2} are same string if ignoring the case.") 
else:
    print(f"{str1} & {str2} are not same string.")
    