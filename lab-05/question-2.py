def xor_upto(n):
    if n % 4 == 0:
        return n
    elif n % 4 == 1:
        return 1
    elif n % 4 == 2:
        return n + 1
    else:
        return 0

L, R = map(int, input().split())

result = xor_upto(R) ^ xor_upto(L - 1)
print(result)