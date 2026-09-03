# Finding all permutations of n distinct objects taken all at a time
# Using the concept of Recursion and Backtracking

# Base Case: When the input_list is emtpy, print the current_permutation
# For loop runs from 0 to length of the remaining input_list

def permutation_print(input_list, curr_permut = []):
    # Base Case
    if not input_list:    # IF INPUT_LIST IS EMPTY
        print(curr_permut)
        return
    else:
        for i in range(len(input_list)):    # LOOP THROUGH THE PROCESS OF TAKING-REMOVING ITEM FROM INPUT_LIST
            new_permut = curr_permut + [input_list[i]]  # APPEND THE CURRENT ITEM FROM INPUT_LIST TO THE PERMUTATION LIST
            new_input_list = input_list[:i] + input_list[i + 1:]    # SLICE FROM 0 TO JUST BEFORE i AND THEN FROM i + 1 TO END TO NOT INCLUDE element at i index as it is used in new_permut
            permutation_print(new_input_list, new_permut)




permutation_print([1, 2, 3])