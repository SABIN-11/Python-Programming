#  find() Method but manually
#  find given substring inside string

# Step 1: Take 2 input strings. 1 - the main string, 2 -  the substring to find
main_string = input('Enter the main string: ')
sub_string = input('Enter the substring to find in the main string: ')

# def findSubString(string, subStr):

#     lengthOfSubStr =  len(subStr)   # Get the length of the substring

#     # Step 2: Find the first occurance of the first alphabet of the substring, then slice from that index to its length
#     #         Then check if it matches with the substring or not, if it does return the starting index or return -1
#     for i in range (len(string) - len(sub_string) + 1):
#         if string[i] == subStr[0]:
#             temp = string[i:i + lengthOfSubStr]
#             if temp == subStr:
#                 return i
#     else:
#         return -1
    
# result = findSubString(main_string, sub_string)
# if result != -1:
#     print(f"{{{sub_string}}} is found within main string starting from index {result}")
# else:
#     print(f"{{{sub_string}}} is not found within main string so result is {result}")

# OR SIMPLY USE find() function, returns the index from which substring starts from
# print(f"{main_string.find(sub_string)}")


