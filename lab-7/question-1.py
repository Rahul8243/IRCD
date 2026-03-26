# Q1: Range Sum Query  
# You are given an integer array arr of size n. You will be given q queries where each query 
# contains two integers L and R. Return the sum of elements from index L to R inclusive.

arr = [2,4,1,6,3]

n = len(arr)

prefix = [0]*n

prefix[0] = arr[0]

for i in range(1,n):
    prefix[i] = prefix[i-1] + arr[i]


def range_sum(L,R):

    if L == 0:
        return prefix[R]

    return prefix[R] - prefix[L-1]


print(range_sum(1,2))