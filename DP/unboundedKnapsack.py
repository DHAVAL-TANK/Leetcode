from typing import List

def unboundedKnapsack(n: int, w: int, profit: List[int], weight: List[int]) -> int:
    
    # This line is redundant since `n` is already passed as a parameter
    # n = len(profit)

    # Correction 1: Initialize dp with n rows (one per item) and w+1 columns (one per capacity)
    dp = [[0 for _ in range(w + 1)] for _ in range(n)]

    # Correction 2: Initialize the first row explicitly to allow multiple use of the first item
    # When we only consider the first item, we should maximize profit by using it as many times as possible
    for target in range(w + 1):
        if weight[0] <= target:
            dp[0][target] = (target // weight[0]) * profit[0]

    # Correction 3: Start index loop from 1 to avoid redoing the first row
    for index in range(1, n):
        for target in range(w + 1):
            # Case 1: Do not take the current item
            notTake = dp[index - 1][target]  # Only take from the previous row

            # Case 2: Take the current item if it fits within the current capacity
            take = 0
            if weight[index] <= target:
                # Correction 4: Use dp[index][target - weight[index]] to allow multiple uses of the same item
                take = profit[index] + dp[index][target - weight[index]]

            # Correction 5: Take the maximum of taking or not taking the item
            dp[index][target] = max(take, notTake)

    # Correction 6: Return dp[n-1][w] which holds the maximum profit for capacity w considering all items
    return dp[n - 1][w]

# Example usage
print(unboundedKnapsack(3, 10, [5, 11, 13], [2, 4, 6]))  # Expected output: 27
print(unboundedKnapsack(3, 15, [7, 2, 4], [5, 10, 20]))   # Expected output: 21
print(unboundedKnapsack(2, 3, [6, 12], [4, 17]))          # Expected output: 0
