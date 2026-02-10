n = int(input("enter number of elements: "))
arr = list(map(int, input("enter array elements: ").split()))

result = 0
for x in arr:
    result ^= x

print("Unique element is:", result)