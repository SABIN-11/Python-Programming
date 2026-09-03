# count() returns the number of times a substring appears in the main string.
# count() method but manually

# Step 1: Take 2 input strings. 1 - the main string, 2 -  the substring to find
main_string = input('Enter the main string: ')
sub_string = input('Enter the substring to find in the main string: ')

# "Python is powerful and Python is easy."
# "aaaa" "aa"

# def countSubString(main, sub):
    
#     count = 0
#     lengthOfSubString = len(sub)
#     for i in range (len(main) - len(sub) + 1):
#         if main[i] == sub[0]:
#             new_str = main[i: i + lengthOfSubString]
#             if new_str == sub:
#                 count += 1
#     else:
#         return count
    
# print(f"The word {{{sub_string}}} appears {countSubString(main_string, sub_string)} times in the main string")

# OR SIMPLY USE count() method
print(f"The word {{{sub_string}}} appears {main_string.count(sub_string)} times in the main string")


