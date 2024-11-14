# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from Tree.Nodes import TreeNode


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(node):
            if not node:  # Base case: an empty tree is balanced
                return 0
            
            left_height = helper(node.left)  # Recursively check left subtree
            if left_height == -1:  # If left subtree is unbalanced
                return -1
            
            right_height = helper(node.right)  # Recursively check right subtree
            if right_height == -1:  # If right subtree is unbalanced
                return -1
            
            # If the current node is unbalanced
            if abs(left_height - right_height) > 1:
                return -1
            
            # Return the height of the current subtree
            return max(left_height, right_height) + 1
        
        # The tree is balanced if helper doesn't return -1
        return helper(root) != -1

        

        
        
        