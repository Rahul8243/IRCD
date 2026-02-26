def threeSumClosest(nums, target):
    nums.sort()
    n = len(nums)

    closest_sum = float('inf')
    closest_triplet = ()

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            # Update closest
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum
                closest_triplet = (nums[i], nums[left], nums[right])

            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return closest_triplet, current_sum  # Exact match

    return closest_triplet, closest_sum


# 🔹 Input Section
arr = list(map(int, input("Enter array elements: ").split()))
target = int(input("Enter target value: "))

triplet, total = threeSumClosest(arr, target)

print("\nClosest Triplet:", triplet)
print("Sum of Triplet:", total)