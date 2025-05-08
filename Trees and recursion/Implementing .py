
# Define a Node class to represent each node in the tree
class Node:
    def __init__(self, value, children=[]):
        self.value = value              # The value stored in the node
        self.children = children        # List of children nodes
        
    def __repr__(self):
        return str(self.value)          # How the node is represented when printed


# Example: creating individual nodes and linking them
node2 = Node(2)
node3 = Node(3)
node1 = Node(1, [node2, node3])         # node1 has two children: node2 and node3

node = Node(1)
print(node)  # Output: 1


# Building a larger tree
# Tree structure:
#        1
#     /  |  \
#    4   5   2
#   / \      \
#  3   7      6
tree = Node(1, [Node(4, [Node(3), Node(7)]),
                Node(5),
                Node(2, [Node(6)])])


# Simple depth-first traversal (pre-order)
def traverse(node):
    print(node)                        # Visit the current node
    for child in node.children:       # Recursively visit all children
        traverse(child)


# Enhanced traversal showing "enter" and "leave" events
def traverse(node):
    print("enter", node.value)        # Before visiting children
    for child in node.children:
        traverse(child)
    print("leave", node.value)        # After visiting children

#✅ Explanation:
# The Node class builds a general tree where each node can have multiple children.

# The first version of traverse() simply prints each node in pre-order.

# The second version adds "enter" and "leave" logs to show the recursive structure clearly — it's useful for understanding how traversal dives into and returns from branches.