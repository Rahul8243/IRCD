def findMinArrowShots(points):
    if not points:
        return 0

    # Sort by ending coordinate
    points.sort(key=lambda x: x[1])

    arrows = 1
    end = points[0][1]

    for start, finish in points[1:]:
        if start > end:
            arrows += 1
            end = finish

    return arrows


# Input
points = [[10,16],[2,8],[1,6],[7,12]]

# Output
print("Minimum arrows needed:", findMinArrowShots(points))