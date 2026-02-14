def knapsack(values, weights, capacity):
    # Number of items
    n = len(values)
    
    # Initialize the DP table
    dp = [[0] * (capacity + 1) for _ in range(n)]
    
    # Fill the DP table
    for i in range(1, n):  # Skip the 0th index since it represents no item
        for j in range(capacity + 1):  # Iterate over all capacities
            if weights[i] > j:  # If the item's weight exceeds current capacity
                dp[i][j] = dp[i-1][j]
            else:  # Check if including the item increases the value
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i]] + values[i])
    
    return dp

# Example Usage
values = [0, 15, 25, 35, 45]
weights = [0, 2, 3, 5, 7]
capacity = 10

result = knapsack(values, weights, capacity)
for row in result:
    print(row)
