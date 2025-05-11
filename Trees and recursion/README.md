
# Trees and Recursion

Trees are hierarchical data structures consisting of nodes connected by edges. Each tree has a root node, and each node may have zero or more child nodes. Trees are widely used in applications like file systems, database indexing, and decision-making processes.

In this section, we explore how trees can be implemented using recursion and how we can compute various information about trees, including depths, and improve the class design.

## Implementing a Tree

To implement a tree, we start by creating a **TreeNode** class. Each node will have a value and a list of children. The root node is the entry point to the entire tree structure.

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

# Example usage
root = TreeNode(1)
child1 = TreeNode(2)
child2 = TreeNode(3)
root.add_child(child1)
root.add_child(child2)
```

## Computing Information from a Tree
We can compute different types of information from a tree, such as the number of nodes, the maximum depth of the tree, or the height of each node.

For example, we can recursively calculate the depth (height) of each node:
```python
def compute_depth(node):
    if not node.children:
        return 0
    return 1 + max(compute_depth(child) for child in node.children)

# Example usage
depth = compute_depth(root)  # This will compute the depth of the tree
```

## Computing Depths
The depth of a node in a tree refers to the length of the path from the root to that node. We can compute the depths of all nodes by recursively traversing the tree.
```python
def compute_depths(node, depth=0):
    print(f"Node {node.value} has depth {depth}")
    for child in node.children:
        compute_depths(child, depth + 1)

# Example usage
compute_depths(root)  # This will print the depth of each node
```

## Improving the Class
We can improve our tree structure by adding additional features such as:

Parent pointer: Keeping track of each node's parent can make traversal easier in some cases.

Node deletion: Allowing nodes to be removed from the tree, ensuring proper rebalancing.

Here’s how we might improve the tree class to include a parent pointer:
```python
class TreeNode:
    def __init__(self, value, parent=None):
        self.value = value
        self.children = []
        self.parent = parent

    def add_child(self, child_node):
        self.children.append(child_node)
        child_node.parent = self

    def remove_child(self, child_node):
        self.children.remove(child_node)
        child_node.parent = None
```

## Example: Employees
Consider a company hierarchy where each employee has a manager. We can represent this as a tree, with each employee as a node and the manager as the parent node.
```python
class EmployeeTreeNode:
    def __init__(self, name):
        self.name = name
        self.subordinates = []
        self.manager = None

    def add_subordinate(self, subordinate):
        self.subordinates.append(subordinate)
        subordinate.manager = self


ceo = EmployeeTreeNode("CEO")
vp = EmployeeTreeNode("VP of Marketing")
employee = EmployeeTreeNode("Marketing Manager")
ceo.add_subordinate(vp)
vp.add_subordinate(employee)
```

## Queens (Classic Example)
A classic example of using trees and recursion is solving the N-Queens problem, where we are tasked with placing N queens on an NxN chessboard such that no two queens attack each other. This can be efficiently solved using recursion to place queens row by row and backtrack when conflicts arise.
```python
def solve_n_queens(board, row=0):
    if row == len(board):
        print_board(board)
        return True

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row] = col  # Place the queen
            if solve_n_queens(board, row + 1):  # Recurse to place the next queen
                return True
            board[row] = -1  # Backtrack
    return False

def print_board(board):
    for row in board:
        print(" ".join("Q" if col == row else "." for col in range(len(board))))

def is_safe(board, row, col):
    for r in range(row):
        if board[r] == col or abs(board[r] - col) == row - r:
            return False
    return True

# Example usage
n = 4
board = [-1] * n
solve_n_queens(board)
```

