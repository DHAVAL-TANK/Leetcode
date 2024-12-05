# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from Tree.Nodes import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        LeftLim = -float('inf')
        rightLim = float('inf')

        def helper(root, leftLim,rightLim):
            if root is None:
                return True
            
            if  not (leftLim < root.val < rightLim):
                return False

            return helper(root.left,leftLim,root.val) and helper(root.right,root.val,rightLim)
        
        return helper(root,LeftLim,rightLim)
        