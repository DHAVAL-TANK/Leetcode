class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # Initialize a DP array where dp[i] represents the minimum coins needed for amount i
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins needed to make amount 0

        # Loop over each coin
        for coin in coins:
            # Update the DP array for each possible target from coin to amount
            for target in range(coin, amount + 1):
                dp[target] = min(dp[target], 1 + dp[target - coin])

        # If dp[amount] is still float('inf'), it means amount cannot be formed with given coins
        return dp[amount] if dp[amount] != float('inf') else -1

    # def coinChange(self, coins, amount):
    #     """
    #     :type coins: List[int]
    #     :type amount: int
    #     :rtype: int
    #     """
    #     dp = [[ 0 if i==0 else -1 for i in range(amount+1) ] for _ in range(2) ]
        

    #     n = len(coins)

    #     #each dp[i][j] cell tells -> to get amount, i coins will be required. 

    #     for i in range(amount+1):
    #         if i % coins[0] == 0:
    #             dp[0][i] = i / coins[0]
    #         else:
    #             dp[0][i] = float('inf')

    #     for i in range(1,n):
    #         for t in range(amount+1):
    #             notTake = dp[i-1][t]
    #             take=float('inf')
    #             if coins[i] <= t:
    #                 take = 1 + dp[i-1][t-coins[i]]
    #             dp[i][t]= min(take,notTake)
    #         print(dp[i])
    #         print()
    #     return int(dp[n-1][amount])
    
sol = Solution()
coins= [1,2,5]
amount = 11
print(sol.coinChange(coins,amount))

        



    #     if amount == 0:
    #         return 0
    #     else:
    #         dp = [[ -1 for _ in range(amount+1)] for _ in coins ]
    #         x= self.f(len(coins)-1,coins,amount,dp)
    #         return x if x!= float('inf') else -1

    # def f(self,index,coins,target,dp):

    #     # basecase
    #     if index==0:
    #         if target % coins[index] == 0 :
    #             return target / coins[0]
    #         else:
    #             return float('inf')
        
    #     if dp[index][target] != -1:
    #         return dp[index][target]

    #     notTake = 0 + self.f(index-1,coins,target,dp)
    #     take = float('inf')

    #     if coins[index] <= target:
    #         take = 1 +  self.f(index,coins,target-coins[index],dp)
        
    #     dp[index][target]=min(take,notTake)
        
    #     return dp[index][target]


        