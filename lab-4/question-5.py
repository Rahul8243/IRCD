# Given:

# A number N

# A natural number K > 0

# Task:

# Concatenate N, K times

# Add all digits of the resulting number

# Repeat digit addition until only one digit remains


N = input('enter number:').strip()
K = int(input('enter natural number: '))

# Step 1: sum of digits of N
digit_sum = sum(int(d) for d in N)

# Step 2: multiply by K
total = digit_sum * K

# Step 3: reduce to single digit
while total >= 10:
    total = sum(int(d) for d in str(total))

print(total)
