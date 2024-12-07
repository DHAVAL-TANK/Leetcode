from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1  # Handle empty grid

        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        max_time = 0

        # Initialize the queue with all rotten oranges and count fresh ones
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))  # (row, col, time)
                elif grid[r][c] == 1:
                    fresh += 1

        # Directions: up, down, left, right
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        while queue:
            r, c, time = queue.popleft()
            max_time = max(max_time, time)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # Check boundaries and if the orange is fresh
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2  # Mark as rotten
                    fresh -= 1
                    queue.append((nr, nc, time + 1))
        # If there are still fresh oranges, return -1
        return max_time if fresh == 0 else -1