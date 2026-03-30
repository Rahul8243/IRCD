def fractional_knapsack(weights, values, capacity):
    items = []
    
    # Step 1: Store (ratio, weight, value)
    for i in range(len(weights)):
        ratio = values[i] / weights[i]
        items.append((ratio, weights[i], values[i]))
    
    # Step 2: Sort by ratio descending
    items.sort(reverse=True)
    
    total_value = 0
    
    # Step 3: Fill knapsack
    for ratio, weight, value in items:
        if capacity >= weight:
            total_value += value
            capacity -= weight
        else:
            total_value += ratio * capacity
            break
    
    return total_value


# Input
weights = [10,20,30]
values = [60,100,120]
capacity = 50

print("Maximum value:", fractional_knapsack(weights, values, capacity))