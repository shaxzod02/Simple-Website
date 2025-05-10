#✅ Final Version with Comments:
# Node class to represent elements in the binary search tree
class Node:
    def __init__(self, value):
        self.value = value     # The value stored in this node
        self.left = None       # Left child (smaller values)
        self.right = None      # Right child (greater values)

# TreeSet class: implements a basic binary search tree without duplicates
class TreeSet:
    def __init__(self):
        self.root = None  # Root of the BST

    # Add a value to the tree
    def add(self, value):
        if not self.root:
            self.root = Node(value)  # First node becomes the root
            return

        node = self.root
        while True:
            if node.value == value:
                return  # Value already exists, do nothing
            if value < node.value:
                if not node.left:
                    node.left = Node(value)  # Insert on the left
                    return
                node = node.left
            else:
                if not node.right:
                    node.right = Node(value)  # Insert on the right
                    return
                node = node.right

    # Check if a value exists in the tree
    def __contains__(self, value):
        node = self.root
        while node:
            if value == node.value:
                return True
            elif value < node.value:
                node = node.left
            else:
                node = node.right
        return False

    # In-order traversal to get sorted values
    def __iter__(self):
        return self._inorder(self.root)

    def _inorder(self, node):
        if node:
            yield from self._inorder(node.left)
            yield node.value
            yield from self._inorder(node.right)

    # String representation of the set
    def __repr__(self):
        return str(list(self))

#✅ Example Usage:
s = TreeSet()

s.add(1)
s.add(2)
s.add(3)

print(2 in s)  # True
print(4 in s)  # False
print(s)       # [1, 2, 3]
