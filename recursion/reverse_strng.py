# Write a recursive function that takes a string s and returns the reversed version of it.

def rev_string(s):
    if len(s) == 0:
        return ""
    return s[-1] + rev_string(s[:-1])

string = "hello world"
print(rev_string(string)) 



