from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0  # Handle empty grid

        islands = 0
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            # Base case: check boundaries and if the cell is water or already visited
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
                return 

            # Mark the current cell as visited by setting it to '0'
            grid[i][j] = '0'

            # Explore all four directions
            dfs(i + 1, j)  # Down
            dfs(i - 1, j)  # Up
            dfs(i, j + 1)  # Right
            dfs(i, j - 1)  # Left

        # Iterate through each cell in the grid
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    islands += 1
                    dfs(i, j)  # Start DFS from the current cell

        return islands

# 📌 **Example Usage**
if __name__ == "__main__":
    solution = Solution()
    grid = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","1"]
    ]
    print("Number of islands:", solution.numIslands(grid))
    # Expected Output: Number of islands: 2
