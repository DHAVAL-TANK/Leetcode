def knapsack(weights, values, capacity):
    n = len(weights)
    # Create a 2D DP array where dp[i][w] represents the maximum value we can get
    # with the first i items and weight capacity w
    dp= [0]*capacity

    for i in range(n) :
        for j in range(capacity,weights[i]-1, -1):
            dp[j] = max(dp[j],dp[capacity-weights[i]] + values[i])

    return dp[capacity]
# Test cases
weights1 = [1, 2, 3]
values1 = [10, 20, 30]
capacity1 = 5
print("Test Case 1 Output:", knapsack(weights1, values1, capacity1))  # Expected Output: 50

weights2 = [1, 3, 4, 5]
values2 = [1, 4, 5, 7]
capacity2 = 7
print("Test Case 2 Output:", knapsack(weights2, values2, capacity2))  # Expected Output: 9
