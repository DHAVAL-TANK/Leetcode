from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:  # Edge case: no prices
            return 0

        # Initialize 3D dp array with dimensions [n+1][2][3]
        dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n + 1)]

        # Fill the dp table iteratively
        for i in range(n - 1, -1, -1):  # Traverse days in reverse
            for buy in range(2):  # Buy can be 0 (sell) or 1 (buy)
                for cap in range(1, 3):  # Transactions allowed: 1 or 2
                    if buy == 1:  # Buying state
                        dp[i][buy][cap] = max(-prices[i] + dp[i + 1][0][cap],  # Buy and move to sell state
                                              dp[i + 1][1][cap])  # Skip the current day
                    else:  # Selling state
                        dp[i][buy][cap] = max(prices[i] + dp[i + 1][1][cap - 1],  # Sell and decrease capacity
                                              dp[i + 1][0][cap])  # Skip the current day

        # Final result is in dp[0][1][2] (start with buying allowed and 2 transactions)
        return dp[0][1][2]
