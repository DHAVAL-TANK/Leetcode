from typing import List

class Solution:
    # Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        visited = set()
        
        def dfs(vertex: int, parent: int) -> bool:
            visited.add(vertex)
            
            for neighbor in adj[vertex]:
                if neighbor == parent:
                    continue  # Skip the parent vertex
                if neighbor in visited:
                    return True  # Cycle detected
                if dfs(neighbor, vertex):
                    return True
            return False
        
        # Handle disconnected graph by checking all components
        for vertex in range(V):
            if vertex not in visited:
                if dfs(vertex, -1):
                    return True
        return False

# 📌 **Driver Code**
if __name__ == '__main__':
    adj = {
                0: [1, 4],
                1: [0, 2],
                2: [1, 4, 3],
                3: [2],
                4: [2, 0]
            }

    obj = Solution()
    ans = obj.isCycle(2, adj)
    print("1" if ans else "0")
    print("~")
