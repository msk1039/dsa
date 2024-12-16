class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        # Base case: if the subtree root is None, insert the new node here
        if root is None:
            return Node(key)

        # Duplicate key handling
        if key == root.key:
            print(f"{key}, Duplicate key can't insert. Ignored...")
            return root

        # Recursive case: Traverse left or right subtree
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        return root

    def find_min(self, root):
        if root is None:
            return None  # Defensive programming in case find_min is called with None
        current = root
        while current.left:
            current = current.left
        return current

    def delete(self, root, key):
        if root is None:
            return root

        # Traverse the tree to find the node to delete
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # If the node to be deleted is found
            # Case 1: Node with only one child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # Case 2: Node with two children
            # Find the inorder successor (smallest in the right subtree)
            if root.right is not None:
                temp = self.find_min(root.right)
                # Copy the inorder successor's content to this node
                root.key = temp.key
                # Delete the inorder successor
                root.right = self.delete(root.right, temp.key)

        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.key, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key, end=" ")


if __name__ == "__main__":
    bst = BinarySearchTree()

    nodes = [50, 30, 20, 40, 70, 60, 80, 70]  # List contains duplicate keys for testing
    for key in nodes:
        bst.root = bst.insert(bst.root, key)

    print("Inorder Traversal: ")
    bst.inorder(bst.root)
    print("\n")

    print("Preorder Traversal: ")
    bst.preorder(bst.root)
    print("\n")

    print("PostOrder Traversal: ")
    bst.postorder(bst.root)
    print("\n")

    # Testing deletion of nodes
    bst.root = bst.delete(bst.root, 50)  # Deleting the root node (two children)
    bst.root = bst.delete(bst.root, 40)  # Deleting node with one child
    bst.inorder(bst.root)
    print("\n")
