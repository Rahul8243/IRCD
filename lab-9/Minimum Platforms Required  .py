def min_platforms(arr, dep):
    n = len(arr)
    
    # Step 1: Sort both arrays
    arr.sort()
    dep.sort()
    
    platform_needed = 1
    max_platforms = 1
    
    i = 1  # arrival pointer
    j = 0  # departure pointer
    
    # Step 2: Traverse
    while i < n and j < n:
        if arr[i] <= dep[j]:
            platform_needed += 1
            i += 1
        else:
            platform_needed -= 1
            j += 1
        
        max_platforms = max(max_platforms, platform_needed)
    
    return max_platforms


# Input
arr = [900,940,950,1100,1500,1800]
dep = [910,1200,1120,1130,1900,2000]

print("Minimum platforms required:", min_platforms(arr, dep))