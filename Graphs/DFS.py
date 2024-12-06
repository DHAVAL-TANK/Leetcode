from sample_graphs import graph

def dfs_recursive(graph, start, visited=None, traversal_order=None):
    if visited is None:
        visited = set()
    if traversal_order is None:
        traversal_order = []
    
    visited.add(start)
    traversal_order.append(start)
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, traversal_order)
    
    return traversal_order

def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    traversal_order = []

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            traversal_order.append(vertex)
            # Reverse to maintain the same order as recursive
            stack.extend(reversed(graph[vertex]))
    return traversal_order

# Execute both DFS methods
recursive_traversal = dfs_recursive(graph, 0)
iterative_traversal = dfs_iterative(graph, 0)

print("Recursive DFS Traversal Order:", recursive_traversal)
print("Iterative DFS Traversal Order:", iterative_traversal)
