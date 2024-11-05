from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        
        if s % 2 != 0:
            return False
        
        k = int(s/2)
        n = len(nums)

        dp = [[False for _ in range(k+1)] for _ in range(n)]

        for i in range(0,n-1):
            dp[i][0]= True
        
        if nums[0] <= k:
            dp[0][nums[0]] = True

        for index in range(1,n):
            for target in range(1,k+1):  
                notTake = dp[index-1][target]
                take = False

                if notTake == False : 
                    if nums[index] <= target:
                        take = dp[index-1][target-nums[index]]
                dp[index][target]= take or notTake

        return dp[n-1][k]


    