from typing import List
from Tree.Nodes import nAryNode


class Solution:
    def postorder(self, root: 'nAryNode') -> List[int]:
        if root is None:
            return []

        result = []
        for child in root.children:
            result += self.postorder(child)
        
        result += [root.val]

        return result

class Solution:
    def preorder(self, root: 'nAryNode') -> List[int]:
        if root is None:
            return []

        result = [root.val]
        for child in root.children:
            result += self.preorder(child)
        
     

        return result