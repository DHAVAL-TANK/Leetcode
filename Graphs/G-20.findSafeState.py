from collections import deque
from typing import List
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        v = len(graph)
        #reverse the graph and update indegree
        reverseGraph = [ [] for _ in range(v)]
        inDegree = [0]*v
        safeNode=[]

        for node in range(v):
            for n in graph[node]:
                reverseGraph[n].append(node)
                inDegree[node]+= 1

        #find terminal node and put it queue

        #queue = deque([node for node in inDegree if node == 0])
        queue = deque([i for i in range(v) if inDegree[i] == 0])

        #until the queue is not empty
        while queue:
            currentNode = queue.popleft()
            safeNode.append(currentNode)

            for neighbour in reverseGraph[currentNode]:
                inDegree[neighbour] -= 1

                if inDegree[neighbour] == 0:
                    queue.append(neighbour)

            #pop the leftmost node and process all neighbour of new node

            #
        return sorted(safeNode)