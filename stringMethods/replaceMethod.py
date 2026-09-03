# Manual Replacing old word with new one

#Step 1: Ask for string, old word to be replaced and new word to be added in place of old word

string = input('Enter the string: ')
old_word = input('Enter the word which you want to replace: ')
new_word = input('Enter the new word which you want to add inplace of the old one: ')

# Input String: "Python is easy. Python is powerful."
# Replace: "Python"
# With: "Java"

# Output: "Java is easy. Java is powerful."

# def replaceOldWithNewWord(string, old, new):

#     # Step 2: Remove leading and trailing spaces if present
#     new_string = string.strip()
#     temp_word = ''
#     result_string = ''

#     # Step 3: If white space is encountered, it means a word has been traced
#     #         Thus, we check is the traced word is the one to replace or not
#     #         If it is then in the result string, just concatenate new word and if not just concatenate whatever it was
#     for i in range (len(new_string)):
        
#         if new_string[i] != ' ':
#             temp_word += new_string[i]

#         if new_string[i] == ' ' or i == len(new_string) - 1:
#             if temp_word.lower() == old.lower():
#                 result_string += new + ' '
#             else:
#                 result_string += temp_word + ' '
#             temp_word = ''
#     else:
#         return result_string.strip()

# print(f"Before: {string}")
# print(f"After : {replaceOldWithNewWord(string, old_word, new_word)}")

# OR SIMPLY USE REPLACE FUNCTION
print(f"Before: {string}")
print(f"After : {string.replace(old_word, new_word)}")

