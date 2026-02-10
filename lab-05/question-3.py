a = 5
b = 9
arr = list(range(1, 11))

part1 = []
part2 = []
part3 = []

for x in arr:
    if x < a:
        part1.append(x)
    elif a < x < b:
        part2.append(x)
    elif x > b:
        part3.append(x)

print(part1, part2, part3)