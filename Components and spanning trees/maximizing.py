
# Maximizing Spanning Tree Weight
# In the case of finding a Maximum Spanning Tree, we can use the same approach as for finding a Minimum Spanning Tree (MST) but with the key difference being the treatment of the edge weights.

# Minimum Spanning Tree (MST): Kruskal’s or Prim’s algorithm are typically used to minimize the sum of edge weights in a spanning tree.

# Maximum Spanning Tree: If we negate the edge weights (multiply by -1), then by finding the MST of the transformed graph, we effectively find the maximum spanning tree of the original graph.

# How to Find the Maximum Spanning Tree with Kruskal’s Algorithm
# To apply this to Kruskal's algorithm, we can simply:

# Negate the weights of all the edges.

# Use Kruskal’s algorithm to find the Minimum Spanning Tree on the negated graph.

# Since the weights were negated, the result will be the Maximum Spanning Tree for the original graph.

# Step-by-Step Process Using Kruskal’s Algorithm:
# Negate Edge Weights: Multiply each edge weight by -1.

# Sort Edges by Weight: Sort the edges in non-decreasing order of the negated weight (which is the same as sorting them in non-increasing order of the original weight).

# Union-Find: Use the union-find structure (or disjoint-set) to ensure that we don't form cycles while selecting edges.

# Select Edges: Keep adding edges in the sorted order as long as they don’t form a cycle. Stop when you’ve added n - 1 edges (where n is the number of nodes).

# Code Example (Modified Kruskal’s Algorithm for Maximum Spanning Tree)
# Here’s how we could modify your Kruskal algorithm to compute the maximum spanning tree:
class KruskalMax:
    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = []

    def add_edge(self, node_a, node_b, weight):
        self.edges.append((node_a, node_b, weight))

    def construct(self):
        # Negate the edge weights to maximize the total weight
        self.edges.sort(key=lambda x: -x[2])  # Sort in decreasing order of weight

        uf = UnionFind(self.nodes)
        edges_count = 0
        tree_weight = 0

        for edge in self.edges:
            node_a, node_b, weight = edge
            if uf.find(node_a) != uf.find(node_b):
                uf.union(node_a, node_b)
                edges_count += 1
                tree_weight += weight

        # If we don't have exactly n-1 edges, the graph is disconnected, and we can't form a spanning tree
        if edges_count != len(self.nodes) - 1:
            return None
        return tree_weight

# Example usage
k_max = KruskalMax([1, 2, 3, 4, 5])

k_max.add_edge(1, 2, 2)
k_max.add_edge(1, 3, 4)
k_max.add_edge(2, 3, 1)
k_max.add_edge(2, 4, 2)
k_max.add_edge(3, 5, 7)
k_max.add_edge(4, 5, 5)

print(k_max.construct())  # Output will be the weight of the Maximum Spanning Tree

# Explanation of Changes:
# Sort by Negative Weights: Instead of sorting edges by increasing weight (as done in the MST case), we sort by the negative of the weight (-x[2]). This ensures that we are effectively prioritizing the edges with the highest original weights.

# Union-Find Structure: The rest of the algorithm remains the same, using the union-find structure to ensure no cycles are formed while adding edges to the spanning tree.

# Example Graph for the Maximum Spanning Tree:
# Given the edges:

# (1, 2, 2)

# (1, 3, 4)

# (2, 3, 1)

# (2, 4, 2)

# (3, 5, 7)

# (4, 5, 5)

# The sorted edges (in reverse order of original weights) would be:

# (3, 5, 7)

# (1, 3, 4)

# (4, 5, 5)

# (1, 2, 2)

# (2, 4, 2)

# (2, 3, 1)

# After processing them with Kruskal’s algorithm, the maximum spanning tree might consist of the edges with weights 7, 5, 4, 2, giving a total weight of 18.

