# Q1. 
# Problem Statement
# An Armstrong number is a number that is equal to the sum of its digits raised to the power of the total number of digits.
# Given two integers representing a range [lowerⓜ,upper], print all Armstrong numbers within this range (inclusive). 
# If no Armstrong number exists in the given range, print -1.

lower = int(input().strip())
upper = int(input().strip())

armstrong_numbers = []

for num in range(lower, upper + 1):
    digits = str(num)
    power = len(digits)
    total = sum(int(d)**power for d in digits)
    
    if total == num:
        armstrong_numbers.append(num)

if armstrong_numbers:
    print(" ".join(map(str, armstrong_numbers)))
else:
    print(-1)
