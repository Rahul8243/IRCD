# Q3. 
# Problem Statement
# Given an integer N, determine whether the number is a palindrome. A palindrome number remains the same when its digits are reversed.

N = int(input().strip())

temp = N
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

if reverse == N:
    print("Palindrome")
else:
    print("Not Palindrome")
