class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0  # Initialize diameter as a class variable
        
        def height(node):
            if not node:  # Base case: empty tree has height 0
                return 0
            
            # Recursively calculate the height of left and right subtrees
            left_height = height(node.left)
            right_height = height(node.right)
            
            # Update the diameter: the longest path passing through the current node
            self.diameter = max(self.diameter, left_height + right_height)
            
            # Return the height of the current node
            return max(left_height, right_height) + 1
        
        height(root)  # Calculate height to update diameter
        return self.diameter
