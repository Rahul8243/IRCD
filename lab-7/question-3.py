# Q3: Count Subarrays with Given Sum Given an array and an integer k, 
# find the number of subarrays whose sum equals k.

def subarraySum(nums, k):
    prefix = {0:1}
    current_sum = 0
    count = 0

    for num in nums:
        current_sum += num

        if current_sum - k in prefix:
            count += prefix[current_sum - k]

        prefix[current_sum] = prefix.get(current_sum,0) + 1

    return count


print(subarraySum([1,2,3],3))