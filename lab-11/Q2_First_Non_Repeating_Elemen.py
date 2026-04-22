def first_non_repeating(arr):
    freq = {}

   
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    for num in arr:
        if freq[num] == 1:
            return num

    return "No non-repeating element"

print(first_non_repeating([4, 5, 1, 2, 0, 4]))   # Output: 5
print(first_non_repeating([7, 7, 8, 8, 9, 10, 9]))  # Output: 10