lower = int(input())
upper = int(input())

result = []

for num in range(lower, upper + 1):
    digits = str(num)
    power = len(digits)
    total = 0

    for d in digits:
        total += int(d) ** power

    if total == num:
        result.append(str(num))

if result:
    print(" ".join(result))
else:
    print(-1)
