# Function to find GCD using Euclid's Algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Input
A = int(input("Enter first number: "))
B = int(input("Enter second number: "))

# Check co-prime
if gcd(A, B) == 1:
    print("Co-Prime")
else:
    print("Not Co-Prime")