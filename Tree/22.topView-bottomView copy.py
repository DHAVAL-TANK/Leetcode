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
    def topView(self, root: Optional[TreeNode]) -> List[List[int]]:

        col_table =  defaultdict(list)

        if not root:
            return  []

        queue =  deque([(root,0,0)])

        while queue :
            node,row,col = queue.popleft()

            if col not in col_table:
                # Add the first (topmost) node for this column
                col_table[col] = (row, node.val)

            if node.left:
                queue.append((node.left,row+1,col-1))
                
            if node.right:
                queue.append((node.right,row+1,col+1))
            
        print(col_table)

        return [col_table[col][1] for col in sorted(col_table.keys())]

    def bottomView(self, root: Optional[TreeNode]) -> List[List[int]]:

            col_table =  defaultdict(list)

            if not root:
                return  []

            queue =  deque([(root,0,0)])

            while queue :
                node,row,col = queue.popleft()

                col_table[col] = (row, node.val)

                if node.left:
                    queue.append((node.left,row+1,col-1))
                    
                if node.right:
                    queue.append((node.right,row+1,col+1))
                
            print(col_table)

            return [col_table[col][1] for col in sorted(col_table.keys())]
        
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
    print(sol.topView(root))
    print(sol.bottomView(root))

        
        