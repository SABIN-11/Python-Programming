
def is_palindrome(st: str) -> bool:
    st = st.lower()
    return st == st[::-1]

st = input("Enter a string: ")
result = is_palindrome(st)
if result:
    print(f"{st} is a palindrome.")
else:
    print(f"{st} is not a palindrome.")