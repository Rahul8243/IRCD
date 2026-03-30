def activity_selection(start, finish):
    n = len(start)

    activities = []
    for i in range(n):
        activities.append((finish[i], start[i], i))  

    activities.sort()

    selected = [activities[0][2]]
    last_finish = activities[0][0]

    for i in range(1, n):
        if activities[i][1] >= last_finish:
            selected.append(activities[i][2])
            last_finish = activities[i][0]

    return selected


start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]

result = activity_selection(start, finish)

print("Selected activity indices:", result)
print("Maximum number of activities:", len(result))