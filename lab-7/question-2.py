# Q2: Difference Array for Range Updates  
# You are given an array of size n initialized with zeros. You must perform q operations of 
# the form:  
# add value v to all elements from index L to R  
# Use the difference array technique to apply all updates efficiently and return the final 
# array.  

def range_update(n, queries):

    diff = [0] * (n + 1)

    for L, R, v in queries:
        diff[L] += v
        if R + 1 < n:
            diff[R + 1] -= v

    arr = [0] * n
    arr[0] = diff[0]

    for i in range(1, n):
        arr[i] = arr[i-1] + diff[i]

    return arr


queries = [
    (1,3,10),
    (2,4,5)
]

print(range_update(5, queries))