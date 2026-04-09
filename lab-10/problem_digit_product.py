def digit_product(x):
    prod = 1
    for d in str(x):
        prod *= int(d)
    return prod

def super_digit_product(N, K):
    # Step 1: product of digits of N
    P = digit_product(N)
    
    # Step 2: power
    num = P ** K
    
    # Step 3: reduce to single digit
    while num >= 10:
        num = digit_product(num)
    
    return num

print(digit_product(9))