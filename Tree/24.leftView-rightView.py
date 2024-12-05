# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict,deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = deque()
        rightView={}
        queue.append((root,0))

        while queue:
            node, level = queue.popleft()
            
            rightView[level]= node.val

            if node.left:
                queue.append((node.left,level+1))
            if node.right:
                queue.append((node.right,level+1))
        
        return [rightView[level] for level in sorted(rightView.keys())]



    def leftSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = deque()
        rightView={}
        queue.append((root,0))

        while queue:
            node, level = queue.popleft()
            
            if level not in rightView:
                rightView[level]= node.val

            if node.left:
                queue.append((node.left,level+1))
            if node.right:
                queue.append((node.right,level+1))
        
        return [rightView[level] for level in sorted(rightView.keys())]


        
# Example Usage
if __name__ == "__main__":
    def build_tree(values):
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
    
    values = [1, 2, 3, 4, 6, 5, 7]
    root = build_tree(values)
    sol = Solution()
    print(sol.rightSideView(root))
    print(sol.leftSideView(root))

        
        