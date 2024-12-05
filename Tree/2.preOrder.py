from typing import List, Optional
from Tree.Nodes import TreeNode


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        return [root.val]+ self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
    