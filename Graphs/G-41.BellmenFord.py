from typing import List, Tuple

def bellman_ford(vertices: int, edges: List[Tuple[int, int, int]], source: int):
    # Initialize distances
    distances = [float('inf')] * vertices
    distances[source] = 0

    # Relax all edges V-1 times
    for _ in range(vertices - 1):
        for u, v, weight in edges:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight

    # Check for negative weight cycles
    for u, v, weight in edges:
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            return "Graph contains a negative weight cycle"

    return distances

# Example usage
edges = [
    (0, 1, 4),  # Edge from node 0 to 1 with weight 4
    (0, 2, 5),  # Edge from node 0 to 2 with weight 5
    (1, 3, 3),  # Edge from node 1 to 3 with weight 3
    (2, 3, -6), # Edge from node 2 to 3 with weight -6
    (3, 4, 2)   # Edge from node 3 to 4 with weight 2
]

vertices = 5
source = 0
print(bellman_ford(vertices, edges, source))
