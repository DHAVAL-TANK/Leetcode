class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        dp = [[0]*cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):

                if i == 0 and j == 0:
                    dp[i][j] = grid[0][0]
                else:
                    down=right=grid[i][j]
                    if j > 0 :
                        right += dp[i][j-1] 
                    else :
                        right += float('inf')
                    if i > 0 :
                        down += dp[i-1][j]
                    else:
                        down += float('inf')

                    dp[i][j] = min(right,down) 

        return dp[rows-1][cols-1]