# Q4.  
# Problem Statement
# Given two integers L and R, count the number of prime numbers in the range [Lⓜ,R], inclusive.

L = int(input().strip())
R = int(input().strip())

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

count = 0
for num in range(L, R + 1):
    if is_prime(num):
        count += 1

print(count)
