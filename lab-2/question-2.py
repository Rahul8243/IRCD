# Euclidean Algorithm to find GCD
a = int(input('enter first number:'))
b = int(input('enter second number:'))

while b != 0:
    a, b = b, a % b

print("GCD using Euclidean Algorithm:", a)
