def binary_search_iterative(arr, key):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1

    return -1

arr = [1, 2, 3, 4, 5, 6  ] 
print(binary_search_iterative(arr, 4))  
print(binary_search_iterative(arr, 7))