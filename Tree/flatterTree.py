from typing import Optional
from Tree.Nodes import TreeNode


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Base case: if the root is None, there's nothing to flatten
        if root is None:
            return
        
        # Recursively flatten the left and right subtrees
        self.flatten(root.left)
        self.flatten(root.right)
        
        # If the left subtree exists, we need to rewire the connections
        if root.left:
            # Store the original right subtree
            temp_right = root.right
            
            # Move the left subtree to the right
            root.right = root.left
            root.left = None  # Set the left child to None
            
            # Find the rightmost node of the new right subtree
            current = root.right
            while current.right:
                current = current.right
            
            # Attach the original right subtree to the rightmost node
            current.right = temp_right
