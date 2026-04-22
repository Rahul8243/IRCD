def binary_search_recursive(arr, left, right, key):
    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == key:
        return mid
    elif arr[mid] < key:
        return binary_search_recursive(arr, mid + 1, right, key)
    else:
        return binary_search_recursive(arr, left, mid - 1, key)
    
arr = [1, 2, 3, 4, 5, 6]        
print(binary_search_recursive(arr, 0, len(arr) - 1, 4))
print(binary_search_recursive(arr, 0, len(arr) - 1, 7))