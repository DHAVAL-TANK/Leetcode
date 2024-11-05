from typing import List
import math

def minSubsetSumDifference(arr: List[str], n: int) -> int:
    k = sum (arr)

    dp = [[False for _ in range(k+1)] for _ in range(n)]

    for i in range(n):
        dp[i][0] = True
    
    if arr[0] <= k:
        dp[0][arr[0]] = True
    
    for index in range(1,n):
        for target in range(k+1):
            notTake = dp[index-1][target]
            take=False

            if arr[index] <= target:
                take = dp[index-1][target - arr[index]]

            dp[index][target] = take or notTake
            
        print(dp[index])
        print()
    s1= k if dp[n-1][k]==True else 0
    half= math.floor(k/2)
    
    for i in range(half,0,-1):
        if dp[n-1][i] == True:
            return abs(2*i - k)
        
    return s1


print(minSubsetSumDifference([0,0,0,15],4))