# Kruskal's Algorithm in the Code:
# Initialization:

# You start by creating a class Kruskal, which accepts a list of nodes.

# Inside the __init__ method, you initialize an empty list edges where you'll store all the edges of the graph.

# Adding Edges:

# The add_edge method allows you to add edges between two nodes (node_a and node_b) with a specific weight. These edges are stored in the edges list.

# Constructing the Minimum Spanning Tree (MST):

# The construct method is where the magic of Kruskal's algorithm happens:

# Sort Edges by Weight: The edges are sorted in non-decreasing order based on their weight using self.edges.sort(key=lambda x: x[2]).

# Union-Find Structure: A Union-Find (Disjoint Set) data structure is used to track which nodes are connected and ensure that no cycles are formed when adding edges.

# Iterating over Edges: For each edge, the algorithm checks if the nodes of the edge are in the same connected component (i.e., uf.find(node_a) != uf.find(node_b)). If they aren't, it means adding this edge won't form a cycle, so it is added to the MST.

# Counting Edges: The algorithm keeps track of how many edges are added to the MST using the edges_count variable. For a graph with n nodes, a tree will have n - 1 edges.

# Returning the Tree Weight: If edges_count == len(self.nodes) - 1, the MST is successfully constructed, and the total weight of the MST is returned. Otherwise, it returns None, indicating the graph is not connected (and thus cannot form a spanning tree).

# Explanation of the Example:
# Given the graph with nodes 1, 2, 3, 4, 5 and the following edges:

# (1, 2, 2)

# (1, 3, 4)

# (2, 3, 1)

# (2, 4, 2)

# (3, 5, 7)

# (4, 5, 5)

# The sorted edges by weight would be:

# (2, 3, 1)

# (1, 2, 2)

# (2, 4, 2)

# (4, 5, 5)

# (1, 3, 4)

# (3, 5, 7)

# The Kruskal algorithm proceeds as follows:

# Add (2, 3, 1) (no cycle).

# Add (1, 2, 2) (no cycle).

# Add (2, 4, 2) (no cycle).

# Add (4, 5, 5) (no cycle).

# Stop because there are now n - 1 = 4 edges in the MST.

# Thus, the MST weight is 1 + 2 + 2 + 5 = 10.

# Output:
print(k.construct())  # Output: 10

# Next Steps:
# Union-Find: Make sure you have a UnionFind class defined (or it will throw an error).

# Edge Cases: If the graph is disconnected or has fewer than n - 1 edges, the algorithm will return None, which is good for handling disconnected graphs.