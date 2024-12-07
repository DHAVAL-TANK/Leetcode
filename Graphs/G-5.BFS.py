from typing import List
from sample_graphs import graph
from collections import deque

def bfs( graph:List[List[int]], start:int):
    visited = [False] * len(graph)
    queue  = deque([start])

    visited[start]= True
    traversal_order = []

    while queue:
        vertex = queue.popleft()
        traversal_order.append(vertex)

        print(f"Visited {vertex}")

        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True


    return traversal_order


bfs(graph,0)