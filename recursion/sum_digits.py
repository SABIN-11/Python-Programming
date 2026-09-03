# Sum of Digits

# Base Case: n == 0

def sum_digits(n):
    if n == 0:
        return 0
    else:
        rem = n % 10    # GET THE LAST DIGIT
        return sum_digits(n // 10) + rem 


print(sum_digits(123456))