from collections import deque

def first_negative(arr, k):
    q = deque()
    result = []

    for i in range(len(arr)):

        if arr[i] < 0:
            q.append(i)

        if i >= k - 1:

            while q and q[0] < i - k + 1:
                q.popleft()

            if q:
                result.append(arr[q[0]])
            else:
                result.append(0)

    return result


arr = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter K: "))

print("First negatives:", first_negative(arr, k))