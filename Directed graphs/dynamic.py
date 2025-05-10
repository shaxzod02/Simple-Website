# ✅ Class Overview:
# __init__: Initializes the graph with a set of nodes and an empty adjacency list (edges).

# add_edge(a, b): Adds a directed edge from node a to node b.

# count_from(node): Recursively counts the number of paths from a specific node, caching results to avoid redundant calculations (memoization).

# count_paths(x, y): Counts the number of distinct paths from node x to node y.

# ✅ Commented Code:
class CountPaths:
    def __init__(self, nodes):
        # Initialize the graph with nodes and empty adjacency list for each node
        self.nodes = nodes
        self.graph = {node: [] for node in self.nodes}

    def add_edge(self, a, b):
        # Add a directed edge from node 'a' to node 'b'
        self.graph[a].append(b)

    def count_from(self, node):
        # Return the cached result if the number of paths from 'node' is already computed
        if node in self.result:
            return self.result[node]

        # Initialize path count as 0 for the current node
        path_count = 0
        
        # Recursively count the paths for all adjacent nodes (next_node)
        for next_node in self.graph[node]:
            path_count += self.count_from(next_node)

        # Store the result (memoization) to avoid redundant calculations
        self.result[node] = path_count
        return path_count

    def count_paths(self, x, y):
        # Start by assuming there is exactly one way to reach 'y' (base case)
        self.result = {y: 1}
        # Compute and return the number of distinct paths from 'x' to 'y'
        return self.count_from(x)

#✅ Example Usage:
c = CountPaths([1, 2, 3, 4, 5, 6])

# Add directed edges between the nodes
c.add_edge(1, 2)
c.add_edge(2, 3)
c.add_edge(3, 6)
c.add_edge(4, 1)
c.add_edge(4, 5)
c.add_edge(5, 2)
c.add_edge(5, 3)

# Count the number of distinct paths from node 4 to node 3
print(c.count_paths(4, 3))  # Expected output: 3

# Explanation of Example:
# We define a directed graph with the following edges:
# 1 → 2
# 2 → 3
# 3 → 6
# 4 → 1
# 4 → 5
# 5 → 2
# 5 → 3
# Path Analysis:
# From node 4, there are 3 distinct paths to node 3:

# 4 → 1 → 2 → 3

# 4 → 5 → 2 → 3

# 4 → 5 → 3

#Thus, the result is 3.

