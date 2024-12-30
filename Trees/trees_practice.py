class Node:
    """Represents a single node in a binary tree."""
    def __init__(self, val=0):
        self.left = None 
        self.right = None 
        self.val = val 

class BinaryTree:
    """Represents a binary tree with traversal and search methods."""
    def __init__(self, root=None):
        self.root = root

    def inorder_recursive(self, node):
        if node:
            self.inorder_recursive(node.left)
            print(node.val, end=' ')
            self.inorder_recursive(node.right)

    def preorder_recursive(self, node):
        if node:
            print(node.val, end = ' ')
            self.preorder_recursive(node.left)
            self.preorder_recursive(node.right)

    def postorder_recursive(self, node):
        if node:
            self.postorder_recursive(node.left)
            self.postorder_recursive(node.right)
            print(node.val, end=" ")

tree = BinaryTree(Node(15))
tree.root.left = Node(10)
tree.root.right = Node(20)
tree.root.left.left = Node(8)
tree.root.left.right = Node(12)

print("Inorder Recursive:")
tree.inorder_recursive(tree.root)
print("\nPreorder Recursive:")
tree.preorder_recursive(tree.root)
print("\nPostorder recursive: ")
tree.postorder_recursive(tree.root)
