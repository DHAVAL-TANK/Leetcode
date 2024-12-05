# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict,deque
from typing import List, Optional

from Tree.Nodes import TreeNode

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        position = defaultdict(list)
        q = deque([(root, 0,0)])
        while q:
            node, r, c = q.popleft()
            position[c].append((r, node.val))
            if node.left:
                q.append((node.left, r+1, c-1))
            if node.right:
                q.append((node.right, r+1, c+1))

        return [[val for _, val in sorted(nodes)] for key, nodes in sorted(position.items())]

        
        