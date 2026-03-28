# Q5: Maximum Submatrix Sum  
# Given a matrix of integers (positive and negative), find the maximum sum of any 
# rectangular submatrix.

def maxSubmatrixSum(matrix):

    rows = len(matrix)
    cols = len(matrix[0])

    max_sum = float('-inf')

    for left in range(cols):

        temp = [0] * rows

        for right in range(left, cols):

            for i in range(rows):
                temp[i] += matrix[i][right]

            # Kadane Algorithm
            current_sum = temp[0]
            best = temp[0]

            for i in range(1, rows):
                current_sum = max(temp[i], current_sum + temp[i])
                best = max(best, current_sum)

            max_sum = max(max_sum, best)

    return max_sum


matrix = [
[1,-2,-1,4],
[-8,3,4,2],
[3,8,10,-8],
[-4,-1,1,7]
]

print(maxSubmatrixSum(matrix))