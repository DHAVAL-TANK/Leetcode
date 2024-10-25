class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # if m == 1 or n == 1:
        #     return 1
        # return self.uniquePaths(m-1,n) + self.uniquePaths(m,n-1)
        dp = [[1] * n for _ in range(m)]

    # Fill the table based on the number of ways to get to each cell
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        # The bottom-right corner contains the answer
        return dp[m - 1][n - 1]
        
        