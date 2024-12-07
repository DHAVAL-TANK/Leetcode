from typing import List
from sample_graphs import graph_matrix


def numberOfProvince(isConnected: List[List[int]]) -> int :
    def dfs(vertex, visited):
        for neighbor in range(len(isConnected[vertex])):
            if isConnected[neighbor][vertex] ==  1 and neighbor not in visited:
                visited.add(vertex)
                dfs(neighbor,visited)
    
    visited = set()
    numberOfP = 0

    for node in range(len(isConnected)):
        if node not in visited:
            numberOfP += 1
            visited.add(node)
            dfs(node,visited)
    return numberOfP

print("num of province - ", numberOfProvince(graph_matrix))
        
    