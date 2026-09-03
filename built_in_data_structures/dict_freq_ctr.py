# Write a Python function that takes a list of strings and returns a dictionary where:
# The keys are the unique strings from the list.
# The values are the number of times each string appears.

def dictionary_freq_counter(li_string):

    freq_ctr = {}

    for s in li_string:
        if s in freq_ctr:
            freq_ctr[s] += 1
        else:
            freq_ctr[s] = 1
    else:
        return freq_ctr


print("Enter the strings in the list: ")
string = input().split()

print(dictionary_freq_counter(string))




