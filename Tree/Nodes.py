from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class nAryNode:
    def __init__(self, val: Optional[int] = None, children: Optional[List['TreeNode']] = None):
        self.val = val
        self.children = children
