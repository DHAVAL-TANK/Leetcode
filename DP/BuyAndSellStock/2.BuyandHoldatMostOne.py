from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Recursive approach with dynamic programming
        n = len(prices)

        # Initialize dp array with dimensions (n+1) x 2
        dp = [[0, 0] for _ in range(n + 1)]

        # Iterate from n-1 to 0 to calculate max profit
        for i in range(n - 1, -1, -1):
            # Not holding a stock at day i
            dp[i][0] = max(dp[i + 1][0], dp[i + 1][1] + prices[i])
            # Holding a stock at day i
            dp[i][1] = max(dp[i + 1][1], dp[i + 1][0] - prices[i])

        # Return the maximum profit if we do not hold any stock at day 0
        return dp[0][0]

# Test the solution with some data
sol = Solution()
prices = [7, 1, 5, 3, 6, 4]
print(sol.maxProfit(prices))  # Output: 7
