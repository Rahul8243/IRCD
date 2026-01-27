N = input('enter :')
K = int(input('enter number:'))

num = N * K

while len(num) > 1:
    product = 1
    for digit in num:
        product *= int(digit)
    num = str(product)

print(num)
