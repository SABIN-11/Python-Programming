# Write a function caesar_cipher(text, shift) that encrypts a string using the Caesar cipher 
# — each letter is shifted forward by shift positions in the alphabet. It should wrap around 
# (so z shifted by 1 becomes a). Non-letter characters stay unchanged. Preserve the original case.
# Test with: caesar_cipher("Hello, World!", 3) → "Khoor, Zruog!"

# C = (P + shift) MOD 26, for encryption, C = cipher text, P = plain text
# P = (C - shift) MOD 26, for decryption


# def caesar_cipher(text: str, shift: int) -> str:
#     result = ""
#     for ch in text:
#         if ch.isupper():
#             result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
#         elif ch.islower():
#             result += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
#         else:
#             result += ch
#     return result

def ceaser_cipher(text: str, shift: int) -> str:

    upper_alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_alp = "abcdefghijklmnopqrstuvwxyz"
    result = ""

    for ch in text:
        if ch.isupper():
            P = upper_alp.index(ch)
            C = (P + shift) % 26
            result += upper_alp[C]
        elif ch.islower():
            p = lower_alp.index(ch)
            c = (p + shift) % 26
            result += lower_alp[c]
        else:
            result += ch


    return result


text = input("Enter a text: ")
print(f"Encrypted text for {text} is {ceaser_cipher(text, 3)}")

