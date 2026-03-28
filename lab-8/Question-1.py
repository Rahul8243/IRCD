import heapq

def k_largest(arr, k):
    print("Input Array:", arr)
    print("Value of k:", k)

    min_heap = arr[:k]
    heapq.heapify(min_heap)

    print("Initial Min Heap:", min_heap)

    for num in arr[k:]:
        print("\nChecking:", num)

        if num > min_heap[0]:
            removed = heapq.heappop(min_heap)
            print("Removed:", removed)

            heapq.heappush(min_heap, num)
            print("Inserted:", num)
        else:
            print("Ignored")

        print("Heap now:", min_heap)

    result = sorted(min_heap)
    print("\nFinal Answer:", result)

    return result

k_largest([7,10,4,3,20,15], 3)