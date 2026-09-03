# FINDING THE nth Fibonacci number

# Base Case: if n is 0, then 0th fibonacci number is 0
# Base Case: if n is 1, then 1th fibonacci number is 1

def nth_fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return nth_fibo(n - 1) + nth_fibo(n - 2)

def fibo_series(n):
    for i in range(n):
        print(nth_fibo(i), end="\t")
    
print(nth_fibo(5))
fibo_series(5)