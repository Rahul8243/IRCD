def partitionArray(arr, pivot):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] < pivot:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1

        elif arr[mid] == pivot:
            mid += 1

        else:  # arr[mid] > pivot
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr


# 🔹 Input Section
arr = list(map(int, input("Enter array elements: ").split()))
pivot = int(input("Enter pivot value: "))

result = partitionArray(arr, pivot)

print("\nPartitioned Array:", result)