# Q2. 
# Problem Statement
# A Perfect Number is a positive integer that is equal to the sum of
#  its proper positive divisors, excluding itself. Given an integer X, determine whether it is a Perfect Number.

X = int(input().strip())

divisor_sum = 0

for i in range(1, X // 2 + 1):
    if X % i == 0:
        divisor_sum += i

if divisor_sum == X:
    print("Perfect Number")
else:
    print("Not Perfect Number")
