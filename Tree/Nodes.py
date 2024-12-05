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

class BuildTree:
    def build(values):
        if not values:
            return None

        nodes = [TreeNode(val) if val is not None else None for val in values]
        kids = nodes[::-1]
        root = kids.pop()

        for node in nodes:
            if node:
                if kids:
                    node.left = kids.pop()
                if kids:
                    node.right = kids.pop()

        return root

