from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:  # If the tree is empty, return an empty list
            return []
        
        result = []
        q = deque([root])  # Initialize a deque with the root node
        left_to_right = True  # Flag to toggle traversal order
        
        while q:
            level = []
            for _ in range(len(q)):  # Process all nodes in the current level
                if left_to_right:  # If left-to-right, pop from the left
                    node = q.popleft()
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)  # Add children to the deque
                    if node.right:
                        q.append(node.right)
                else:  # If right-to-left, pop from the right
                    node = q.pop()
                    level.append(node.val)
                    if node.right:
                        q.appendleft(node.right)  # Add children to the left of the deque
                    if node.left:
                        q.appendleft(node.left)
            
            result.append(level)  # Append the current level to the result
            left_to_right = not left_to_right  # Toggle the order for the next level
        
        return result
