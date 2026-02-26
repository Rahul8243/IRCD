def partition_labels(s):
    last_index = {}

    for i in range(len(s)):
        last_index[s[i]] = i

    result = []
    start = 0
    end = 0

    for i in range(len(s)):
        end = max(end, last_index[s[i]])

        if i == end:
            result.append(end - start + 1)
            start = i + 1

    return result


s = input("Enter string: ")
print("Partition lengths:", partition_labels(s))