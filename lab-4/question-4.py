# Input:

# First line → integer A

# Second line → integer B

# Task:

# Find prime numbers between A and B (inclusive)

# From those primes, count how many have an even digit sum


A = int(input('enter num first: '))
B = int(input('enter num second: '))

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

count = 0

for num in range(A, B + 1):
    if is_prime(num):
        digit_sum = sum(int(d) for d in str(num))
        if digit_sum % 2 == 0:
            count += 1

print(count)
