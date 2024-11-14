# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from Tree.Nodes import TreeNode


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = root.val
        def dfs(r):
            if not r:
                return 0
            
            lh = max(0, dfs(r.left))
            rh = max(0, dfs(r.right))

            self.maxSum = max(self.maxSum, r.val+lh+rh)

            return max(lh,rh)+ r.val

        if root.left or root.right:
            dfs(root)
        
        return self.maxSum
        