# You are given two sorted arrays, each of size N

# Merge them into one sorted array

# Find the sum of the two middle elements of the merged array

n = int(input('entter the number:'))

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

merged = []
i = j = 0

# Merge both arrays
while i < n and j < n:
    if arr1[i] <= arr2[j]:
        merged.append(arr1[i])
        i += 1
    else:
        merged.append(arr2[j])
        j += 1

while i < n:
    merged.append(arr1[i])
    i += 1

while j < n:
    merged.append(arr2[j])
    j += 1

# Sum of middle elements
mid_sum = merged[n-1] + merged[n]
print(mid_sum)
