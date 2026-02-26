def max_average(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)

    return max_sum / k


arr = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter K: "))

print("Maximum average:", max_average(arr, k))