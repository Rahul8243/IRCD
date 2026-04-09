def gcd_euclidean(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(gcd_euclidean(12,18))