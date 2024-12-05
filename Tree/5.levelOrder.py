# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
import queue
from typing import List, Optional

from Tree.Nodes import TreeNode
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:  # Handle empty tree
            return []
        
        q = deque([root])  # Initialize deque with root
        result = []
        
        while q:
            level = []  # Stores nodes at the current level
            for _ in range(len(q)):  # Iterate over the current level
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)  # Add left child to the queue
                if node.right:
                    q.append(node.right)  # Add right child to the queue
            result.append(level)  # Append the current level to result
        
        return result
        

            

            
                
            


        