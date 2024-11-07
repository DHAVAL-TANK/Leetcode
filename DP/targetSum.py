class Solution(object):
    def findTargetSumWays(self,nums, target):
        total_sum = sum(nums)
        
        # Check if it's possible to partition into subsets
        if (target + total_sum) % 2 != 0 or target > total_sum or target < -total_sum:
            return 0
        
        subset_sum = (target + total_sum) // 2
        
        # Initialize a 1D DP array to count subsets that sum to subset_sum
        dp = [0] * (subset_sum + 1)
        dp[0] = 1  # There's one way to achieve a sum of 0: using no elements
        
        # Update the DP array for each number in nums
        for num in nums:
            # Traverse from right to left to avoid reusing elements
            for j in range(subset_sum, num - 1, -1):
                dp[j] += dp[j - num]
        
        return dp[subset_sum]

