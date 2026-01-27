S = input('enter string:')

S = S.lower()

if S == S[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
