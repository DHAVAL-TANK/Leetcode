from sample_graphs import dag
from typing import List

from collections import deque

def topological_sort_kanh(graph):
    v = len(graph)
    in_degree = [0] * v

    # Compute in-degree for each node
    for node in range(v):
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    # Initialize queue with nodes having in-degree 0
    queue = deque([node for node in range(v) if in_degree[node] == 0])
    topo_sort = []

    # Perform topological sort
    while queue:
        current = queue.popleft()
        topo_sort.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return topo_sort


def topological_sort(graph : List[List[int]]) :
    stack = []
    v= len(graph)
    visited = set()

    def dfs(v):
        visited.add(v)
        for neighbor in graph[v]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(v)


    for vertex in range(v):
        if vertex not in visited:
            dfs(vertex)
    stack.reverse()
    return stack

    
print(dag,topological_sort(dag),topological_sort_kanh(dag))

