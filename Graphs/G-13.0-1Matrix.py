from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        if not mat:
            return []

        row, col = len(mat), len(mat[0])
        q = deque()

        # Initialize sol matrix with infinity and enqueue all 0's
        sol = [[float('inf') for _ in range(col)] for _ in range(row)]

        for r in range(row):
            for c in range(col):
                if mat[r][c] == 0:
                    sol[r][c] = 0
                    q.append((r, c))

        # Directions: up, down, left, right
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # Check boundaries
                if 0 <= nr < row and 0 <= nc < col:
                    # If a shorter path is found
                    if sol[nr][nc] > sol[r][c] + 1:
                        sol[nr][nc] = sol[r][c] + 1
                        q.append((nr, nc))

        return sol
                    



