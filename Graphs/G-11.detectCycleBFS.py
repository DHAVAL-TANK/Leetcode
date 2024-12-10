from typing import List
from collections import deque
from sample_graphs import graph

class Solution:
    # Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        visited = set()
        queue = deque()
        
        # Iterate through all vertices to handle disconnected graphs
        for vertex in range(V):
            if vertex not in visited:
                # Start BFS from the current vertex
                queue.append((vertex, -1))  # (current_vertex, parent_vertex)
                visited.add(vertex)
                
                while queue:
                    current, parent = queue.popleft()
                    
                    for neighbor in adj[current]:
                        if neighbor != parent:
                            if neighbor in visited:
                                return True  # Cycle detected
                            visited.add(neighbor)
                            queue.append((neighbor, current))
        
        return False  # No cycle detected

# Driver Code
if __name__ == '__main__':
    
    obj = Solution()
    ans = obj.isCycle(0, graph)
    print("1" if ans else "0")
    print("~")
