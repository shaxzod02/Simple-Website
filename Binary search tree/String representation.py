#✅ Final Version with Comments:
# This method returns the string representation of the TreeSet
def __repr__(self):
    items = []
    self.traverse(self.root, items)  # Fill the list with sorted elements
    return str(items)  # Convert the list to a string

# Recursive in-order traversal helper function
def traverse(self, node, items):
    if not node:
        return  # Base case: reached a leaf
    self.traverse(node.left, items)   # Visit left subtree
    items.append(node.value)          # Visit current node
    self.traverse(node.right, items)  # Visit right subtree
