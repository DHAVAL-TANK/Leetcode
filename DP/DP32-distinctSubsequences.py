class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n=len(s)
        m=len(t)

        dp = [1 if j == 0 else 0 for j in range(m + 1)] 

        for i in range(1,n+1):
            for j in range(m,0,-1):
                if s[i-1] == t[j-1]:
                    dp[j] = dp[j-1] + dp[j]

        return dp[m] 

# 2d DP
# class Solution:
#     def numDistinct(self, s: str, t: str) -> int:
#         n=len(s)
#         m=len(t)

#         dp = [[ 1  if i == 0 else 0 for i in  range(m+1)  ] for j in range(n+1) ]

#         for i in range(1,n+1):
#             for j in range(1,m+1):
#                 if s[i-1] == t[j-1]:
#                     dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
#                 else:
#                     dp[i][j] = dp[i-1][j]

#         return dp[n][m] 

#recursive :
    # class Solution:
    # def numDistinct(self, s: str, t: str) -> int:

    #     def helper(i,j):
    #         if j < 0 :
    #             return 1
    #         if i < 0:
    #             return 0
            
    #         if s[i] == t[j]:
    #             return helper(i-1,j-1) + helper(i-1,j)
           
    #         return helper(i-1,j)


    #     n = len(s)
    #     m = len(t)

    #     return helper(n-1,m-1)
        