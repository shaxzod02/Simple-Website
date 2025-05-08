# This function traverses the tree and prints the depth of each node.
def traverse(node, depth):
    print("node", node, "depth", depth)  # Print current node and its depth
    for child in node.children:
        traverse(child, depth + 1)  # Recursively call for each child with increased depth

# Tree structure (same as before)
tree = Node(1, [Node(4, [Node(3), Node(7)]),
                Node(5),
                Node(2, [Node(6)])])

# Start traversal from root node (depth 0)
traverse(tree, 0)

# Expected output will show the depth of each node in the tree:
# node 1 depth 0
# node 4 depth 1
# node 3 depth 2
# node 7 depth 2
# node 5 depth 1
# node 2 depth 1
# node 6 depth 2


# Function to collect the depths of all nodes in the tree and return them sorted
def get_depths(node):
    depths = []  # List to store the depths
    get_depths_helper(node, 0, depths)  # Start the helper function at depth 0
    return sorted(depths)  # Return sorted depths

# Helper function to perform the recursive collection of depths
def get_depths_helper(node, depth, depths):
    depths.append(depth)  # Add current depth to the list
    for child in node.children:
        get_depths_helper(child, depth + 1, depths)  # Recursive call for each child

# Sample tree (same as before)
tree = Node(1, [Node(4, [Node(3), Node(7)]),
                Node(5),
                Node(2, [Node(6)])])

# Collect and print all depths, sorted in ascending order
print(get_depths(tree))  # Expected output: [0, 1, 1, 1, 2, 2, 2]


# Optimized version of `get_depths` and `get_depths_helper` with list building in the helper function
def get_depths(node):
    return sorted(get_depths_helper(node, 0))  # Return sorted depths directly from helper function

# Helper function with optimized structure (returns all depths at once)
def get_depths_helper(node, depth):
    depths = [depth]  # Start with the current node's depth
    for child in node.children:
        depths += get_depths_helper(child, depth + 1)  # Append depths from each child recursively
    return depths  # Return list of depths

# Key Concepts:
# traverse(node, depth): This function traverses the tree and prints each node’s depth as it goes. It uses recursion, increasing the depth for each child node.

# get_depths(node) and get_depths_helper(node, depth): These functions collect all the depths of the nodes in the tree, and the helper function handles the recursive depth collection.

# Sorting the depths: The get_depths function sorts the depths before returning them, ensuring the list is in ascending order.

# Optimized recursion: In the second get_depths function, we directly return the sorted depths from the helper function, eliminating an extra step where we would need to pass the depths list around.

# Expected Output:

# For the traverse function:
# node 1 depth 0
# node 4 depth 1
# node 3 depth 2
# node 7 depth 2
# node 5 depth 1
# node 2 depth 1
# node 6 depth 2


#For the get_depths function:
[0, 1, 1, 1, 2, 2, 2]
