# Definition for a binary tree node.

from typing import Optional
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        t =[]
        def iot(r):
            if r is not None:
                iot(r.left)
                t.append(r.val)
                iot(r.right)

        iot(root)

        print(t)
        return t
    
    #with stack
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack =[]
        result =[]
        current = root



        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            result.append(current.val)
            current=current.right
        return result


        