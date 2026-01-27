# Basic Method to find GCD
a = int(input('enter number first:'))
b = int(input('enter number second:'))

min_num = min(a, b)

gcd = 1
for i in range(1, min_num + 1):
    if a % i == 0 and b % i == 0:
        gcd = i

print("GCD using Basic Method:", gcd)
