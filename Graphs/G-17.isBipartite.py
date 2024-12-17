from collections import deque
from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        v = len(graph)
        colors = [-1] * v  # -1 means unvisited, 0 and 1 are the two colors
        
        def bfs(start: int) -> bool:
            queue = deque([start])
            colors[start] = 0  # Start coloring with color 0
            
            while queue:
                node = queue.popleft()
                current_color = colors[node]
                
                for neighbor in graph[node]:
                    if colors[neighbor] == -1:  # If not visited
                        colors[neighbor] = 1 - current_color  # Assign opposite color
                        queue.append(neighbor)
                    elif colors[neighbor] == current_color:
                        return False  # Found two adjacent nodes with the same color
            
            return True
        
        for i in range(v):  # Handle disconnected graph components
            if colors[i] == -1:
                if not bfs(i):
                    return False
        
        return True
