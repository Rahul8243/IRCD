def count_triplets(arr, target):
    arr.sort()
    n = len(arr)
    count = 0

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            curr_sum = arr[i] + arr[left] + arr[right]

            if curr_sum < target:
                count += (right - left)
                left += 1
            else:
                right -= 1

    return count


arr = list(map(int, input("Enter array elements: ").split()))
target = int(input("Enter target: "))

print("Valid triplets count:", count_triplets(arr, target))