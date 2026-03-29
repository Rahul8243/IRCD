from collections import Counter

# Function to return frequency (used for sorting)
def get_frequency(item):
    return item[1]

def topKFrequent(nums, k):
    # Step 1: Count frequency
    freq = Counter(nums)
    print("Frequencies:", freq)
    
    # Step 2: Sort using function instead of lambda
    sorted_items = sorted(freq.items(), key=get_frequency, reverse=True)
    print("Sorted:", sorted_items)
    
    # Step 3: Extract top k elements
    result = []
    for i in range(k):
        result.append(sorted_items[i][0])
    
    return result


# Test Case 1
nums1 = [1,1,1,2,2,3]
k1 = 2
print("Top K Frequent:", topKFrequent(nums1, k1))


# Test Case 2
nums2 = [4,4,4,6,6,7]
k2 = 2
print("Top K Frequent:", topKFrequent(nums2, k2))