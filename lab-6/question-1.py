def closest_pair(arr, target):
    left = 0
    right = len(arr) - 1
    
    closest_sum = float('inf')
    result = (None, None)
    
    while left < right:
        curr_sum = arr[left] + arr[right]
        
        if abs(target - curr_sum) < abs(target - closest_sum):
            closest_sum = curr_sum
            result = (arr[left], arr[right])
        
        if curr_sum < target:
            left += 1
        else:
            right -= 1
            
    return result


arr = list(map(int, input("Enter sorted array elements (space separated): ").split()))
target = int(input("Enter target value: "))

arr.sort()
pair = closest_pair(arr, target)

print("\nClosest Pair:", pair)
print("Sum of Pair:", sum(pair))