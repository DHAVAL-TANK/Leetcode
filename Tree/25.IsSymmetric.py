# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from Tree.Nodes import TreeNode


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def helper(left, right):
            # Base cases
            if not left and not right:
                return True  # Both are None, so symmetric
            if not left or not right:
                return False  # One is None, the other is not

            # Check values and recurse
            if left.val != right.val:
                return False

            return helper(left.left, right.right) and helper(left.right, right.left)

        # If root is None, it's symmetric
        return root is None or helper(root.left, root.right)
        