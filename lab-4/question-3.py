# Task:

# Print "Perfect Number" if the number is perfect

# Print "Not Perfect Number" otherwise

n = int(input('enter number:'))

total = 0

for i in range(1, n // 2 + 1):
    if n % i == 0:
        total += i

if total == n:
    print("Perfect Number")
else:
    print("Not Perfect Number")
