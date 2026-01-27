N = int(input('enter number:'))

count = 0

for i in range(1, N + 1):
    if N % i == 0:
        count += 1

print("Total number of divisors:", count)
