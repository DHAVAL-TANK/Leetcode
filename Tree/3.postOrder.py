from typing import List, Optional
from Tree.Nodes import TreeNode


class Solution:
    def postOrderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        return self.postOrderTraversal(root.left) + self.postOrderTraversal(root.right) 
    