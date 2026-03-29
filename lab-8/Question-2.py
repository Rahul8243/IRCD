def heapify(arr, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        print(f"Heapify swap: {arr}")
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    print("Original array:", arr)

    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    print("After building max heap:", arr)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        print(f"\nSwap root with index {i}: {arr}")

        heapify(arr, i, 0)
        print(f"Heap after heapify (size={i}): {arr}")

    print("\nFinal sorted array:", arr)
    return arr

arr = [4, 10, 3, 5, 1]
heap_sort(arr)