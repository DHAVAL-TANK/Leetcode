def frog_jump(heights):
    n = len(heights)
    # dp[i] represents the minimum cost to reach stone i
    dp = [0] * n

    # Base case: Starting from the first stone, cost is 0
    dp[0] = 0

    for i in range(1, n):
        # Jump from stone i-1 to stone i
        cost_from_prev = dp[i - 1] + abs(heights[i] - heights[i - 1])
        
        if i > 1:
            # Jump from stone i-2 to stone i
            cost_from_prev2 = dp[i - 2] + abs(heights[i] - heights[i - 2])
        else:
            # If there's no i-2 (i.e., at the second stone), no need to check this
            cost_from_prev2 = float('inf')
        
        # Take the minimum of the two possible jumps
        dp[i] = min(cost_from_prev, cost_from_prev2)

    # The minimum cost to reach the last stone is in dp[n-1]
    return dp[n - 1]

# Example usage:
heights = [10, 30, 40, 20]
print(frog_jump(heights))  # Output: 30
