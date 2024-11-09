from sys import stdin
import sys

def cutRod(price, n):

    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        max_value = price[i - 1]
        for j in range(1, i):
            max_value = max(max_value, price[j - 1] + dp[i - j])
        dp[i] = max_value
    
    return dp[n]

print(cutRod([1,3,4,5,6], 5))
