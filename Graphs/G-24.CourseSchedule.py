from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDegree = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        
        # Build the graph and update in-degree
        for v, u in prerequisites:
            graph[u].append(v)
            inDegree[v] += 1
        
        # Initialize queue with nodes having in-degree 0
        queue = deque([node for node in range(numCourses) if inDegree[node] == 0])
        
        topo_sort = []

        # Perform topological sort
        while queue:
            currentNode = queue.popleft()
            topo_sort.append(currentNode)

            for nbr in graph[currentNode]:
                inDegree[nbr] -= 1
                if inDegree[nbr] == 0:
                    queue.append(nbr)
        
        # Check if topological sort contains all courses
        return topo_sort if len(topo_sort) == numCourses else []