class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        # Initialize a 1D DP array where dp[i] represents the number of ways to make amount i
        dp = [0] * (amount + 1)
        dp[0] = 1  # There is 1 way to make amount 0: using no coins
        
        # Update dp array for each coin
        for coin in coins:
            for target in range(coin, amount + 1):
                dp[target] += dp[target - coin]
        
        return dp[amount]
