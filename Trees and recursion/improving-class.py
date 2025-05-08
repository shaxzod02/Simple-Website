
class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children
        
    def __repr__(self):
        return str(self.value)     
    
node1 = Node(1)
node2 = Node(2)

node1.children.append(node2)

print(node1.children) # [2]
print(node2.children) # [2]

class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []
        
    def __repr__(self):
        return str(self.value)        

node1 = Node(1)
node2 = Node(2)

node1.children.append(node2)

print(node1.children) # [2]
print(node2.children) # []

tree = Node(1, [Node(2, [Node(3), Node(4)]), Node(5)])
print(tree) # 1

class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []
        
    def __repr__(self):
        if self.children == []:
            return f"Node({self.value})"
        else:
            return f"Node({self.value}, {self.children})"

tree = Node(1, [Node(2, [Node(3), Node(4)]), Node(5)])
print(tree) # Node(1, [Node(2, [Node(3), Node(4)]), Node(5)])



# Issue with the code:
# In the first version of the Node class, the default children=[] is a mutable list, which can cause unexpected behavior because both node1 and node2 would share the same list of children. When you modify node1.children, it also affects node2.children.

# Fixing the issue:
# Fixed version of the Node class with a better approach to handling mutable default arguments
class Node:
    def __init__(self, value, children=None):
        # Use None as default and initialize an empty list if no children are provided
        self.value = value
        self.children = children if children else []  # If no children, initialize as an empty list
        
    def __repr__(self):
        return str(self.value)

# Create nodes again with the updated constructor
node1 = Node(1)
node2 = Node(2)

# Adding node2 as a child of node1
node1.children.append(node2)

# Now node1's children will contain node2, but node2's children remain an empty list
print(node1.children)  # [2]
print(node2.children)  # []  # Node2 now has no children of its own

# Explanation:
# Default arguments: The issue with mutable default arguments (like children=[]) is that they are shared across instances. The solution is to set the default value as None and initialize the list inside the constructor if it is not provided.

# Tree Structure Example:
# Example of building a tree-like structure
tree = Node(1, [Node(2, [Node(3), Node(4)]), Node(5)])
print(tree)  # Node(1, [Node(2, [Node(3), Node(4)]), Node(5)])

#Improving the __repr__ Method:
# Updated `__repr__` to show child nodes if they exist
class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []
        
    def __repr__(self):
        if self.children == []:  # If no children, print just the value
            return f"Node({self.value})"
        else:  # Otherwise, print the value along with children
            return f"Node({self.value}, {self.children})"

# Creating tree again with new __repr__
tree = Node(1, [Node(2, [Node(3), Node(4)]), Node(5)])
print(tree)  # Expected: Node(1, [Node(2, [Node(3), Node(4)]), Node(5)])
# What happens in this final part:
# __repr__ method: This method is used to represent the object in a string format. If the node has no children (i.e., it is a leaf), it will print just the node’s value. Otherwise, it will print the value along with the children, forming a tree-like structure in the string.

# Output:
# For the final example:
Node(1, [Node(2, [Node(3), Node(4)]), Node(5)])
