from collections import deque
from typing import List
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        queue = deque()
        count=0

        visited = [[ 0 for _ in range(col) ] for _ in range(row)]

        def dfs(r,c):
            if r >= 0 and r < row and c >= 0 and c < col and grid[r][c] == 1 and not visited[r][c]:
                visited[r][c] = 1 
                dfs(r-1,c)
                dfs(r+1,c)
                dfs(r,c-1)
                dfs(r,c+1)  
            return 
            


        for r in range(row):
            for c in range(col):
                if r==0 or r == row-1 or c ==0 or c==col-1:
                    if grid[r][c]== 1:
                        queue.append((r,c))
        
        while queue:
            (r,c) = queue.popleft()
            if visited[r][c] != 1:
                dfs(r,c)
        
        for r in range(row):
            for c in range(col):
                    if grid[r][c]== 1 and visited[r][c] != 1:
                        count+=1
        print(visited)
        return count
