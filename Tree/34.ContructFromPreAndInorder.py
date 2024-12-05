class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder, inorder):
    if not preorder or not inorder:
        return None

    # Root is the first element of preorder
    root_val = preorder[0]
    root = TreeNode(root_val)

    # Find the index of the root in inorder
    root_index = inorder.index(root_val)

    # Elements to the left of root_index are the left subtree
    left_inorder = inorder[:root_index]
    # Elements to the right of root_index are the right subtree
    right_inorder = inorder[root_index + 1:]

    # Slice preorder to match the left and right subtree
    left_preorder = preorder[1:1 + len(left_inorder)]
    right_preorder = preorder[1 + len(left_inorder):]

    # Recursively build left and right subtrees
    root.left = buildTree(left_preorder, left_inorder)
    root.right = buildTree(right_preorder, right_inorder)

    return root

# Helper function to print the tree (optional)
def printTree(node):
    if not node:
        return None
    print(node.val, end=" ")
    printTree(node.left)
    printTree(node.right)

# Example usage
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
root = buildTree(preorder, inorder)

# Print the constructed tree in preorder (for verification)
printTree(root)
