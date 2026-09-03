# Reversing a Number Recursively
# Base Case: num can't be 0

def rev_num(num, rev = 0):
    if num == 0:
        return rev
    else:
        rem = num % 10
        rev = rev * 10 + rem
        return rev_num(num // 10, rev)
    
print(rev_num(120))