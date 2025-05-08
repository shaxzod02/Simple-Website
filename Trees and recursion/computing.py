
# Function to count the number of nodes in a subtree rooted at `node`
def count_nodes(node):
    result = 1  # Count the current node
    for child in node.children:
        result += count_nodes(child)  # Recursively count each child
    return result


# Create a tree:
#         1
#     /   |   \
#    4    5    2
#   / \        \
#  3   7        6
tree = Node(1, [Node(4, [Node(3), Node(7)]),
                Node(5),
                Node(2, [Node(6)])])

print(count_nodes(tree))  # Output: 7


# Modified version with detailed logging for subtree sizes
def count_nodes(node):
    result = 1
    for child in node.children:
        result += count_nodes(child)
    print("subtree of node", node, "has", result, "nodes")
    return result

# Sample output will trace how many nodes each subtree contains:
# subtree of node 3 has 1 nodes
# subtree of node 7 has 1 nodes
# subtree of node 4 has 3 nodes
# subtree of node 5 has 1 nodes
# subtree of node 6 has 1 nodes
# subtree of node 2 has 2 nodes
# subtree of node 1 has 7 nodes


# Function to compute the height of the tree
# Height = number of edges on the longest downward path from this node to a leaf
def count_height(node):
    result = 0
    for child in node.children:
        result = max(result, count_height(child) + 1)
    return result

#✅ Explanation:
# count_nodes(node) counts all nodes in the subtree rooted at node, including the node itself.

# count_height(node) computes the height of the tree. A single node has height 0. If it has children, height increases based on the depth of the deepest child.

# The logging version of count_nodes() gives insight into the recursive flow and helps visualize subtree sizes.