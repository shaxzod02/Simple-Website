# Explanation of the Kosaraju's Algorithm
# Kosaraju's algorithm is used to find the strongly connected components (SCCs) in a directed graph. A strongly connected component is a maximal subgraph in which every node is reachable from every other node in the same subgraph. This algorithm efficiently computes the SCCs in O(V + E) time, where V is the number of vertices and E is the number of edges.

# Algorithm Steps:
# Phase 1: Perform a Depth-First Search (DFS) on the original graph and push nodes onto a stack in the order of their finishing times.

# Phase 2: Reverse all the edges of the graph (reverse graph), and perform DFS again, but this time in the order of nodes in the stack (from Phase 1). Each DFS tree rooted at an unvisited node in the stack corresponds to a strongly connected component.

# Code Breakdown:
# Initialization (__init__):

# The graph is initialized as an adjacency list self.graph, and self.reverse stores the reversed graph.

# Adding Edges (add_edge):

# Adds edges to both the original graph and its reversed version.

# DFS Visit (visit):

# This is a recursive function that visits nodes.

# It is used in two phases:

# Phase 1: DFS on the original graph to determine the order of finishing times.

# Phase 2: DFS on the reversed graph to find strongly connected components.

# Counting Strongly Connected Components (count_components):

# This function performs both phases of Kosaraju's algorithm and counts the number of SCCs.

# Phase 1 DFS is used to compute the finishing order of nodes.

# Phase 2 DFS is used to explore the SCCs, incrementing the count whenever a new component is found.

# Code:
class Kosaraju:
    def __init__(self, nodes):
        # Initialize the graph and its reversed version
        self.nodes = nodes
        self.graph = {node: [] for node in self.nodes}
        self.reverse = {node: [] for node in self.nodes}
        
    def add_edge(self, a, b):
        # Add edge (a -> b) to the graph and reverse graph
        self.graph[a].append(b)
        self.reverse[b].append(a)
        
    def visit(self, node, phase):
        # If the node has already been visited, return
        if node in self.visited:
            return
        self.visited.add(node)

        # Choose the graph based on the phase (1 for original graph, 2 for reverse graph)
        if phase == 1:
            graph = self.graph
        elif phase == 2:
            graph = self.reverse
        
        # Explore all adjacent nodes
        for next_node in graph[node]:
            self.visit(next_node, phase)

        # After finishing the DFS, record the node in the order (Phase 1)
        if phase == 1:
            self.order.append(node)
        
    def count_components(self):
        # Step 1: Perform DFS on the original graph to get the order of finishing times
        self.visited = set()
        self.order = []
        
        for node in self.nodes:
            if node not in self.visited:
                self.visit(node, 1)
                
        # Reverse the order of nodes
        self.order.reverse()
        
        # Step 2: Perform DFS on the reversed graph to identify SCCs
        self.visited.clear()
        count = 0
        for node in self.order:
            if node not in self.visited:
                count += 1
                self.visit(node, 2)
                
        # Return the number of strongly connected components
        return count

#Usage Example:
# Create a graph with nodes 1 to 7
k = Kosaraju([1, 2, 3, 4, 5, 6, 7])

# Add directed edges between nodes
k.add_edge(1, 2)
k.add_edge(1, 4)
k.add_edge(2, 1)
k.add_edge(2, 5)
k.add_edge(3, 2)
k.add_edge(3, 7)
k.add_edge(5, 4)
k.add_edge(6, 3)
k.add_edge(6, 5)
k.add_edge(7, 6)

# Compute the number of strongly connected components
print(k.count_components())  # Expected output: 4

# Explanation of the Example:
# In the given graph, we have the following directed edges:

# 1 → 2
# 1 → 4
# 2 → 1
# 2 → 5
# 3 → 2
# 3 → 7
# 5 → 4
# 6 → 3
# 6 → 5
# 7 → 6
# The graph can be visualized as follows:
#     1 ↔ 2 → 5 ↔ 4
#     ↓ ↑     ↓ ↑
#     3 → 7 ← 6

# By applying Kosaraju's algorithm, we detect 4 strongly connected components:

# SCC 1: {1, 2, 5, 4} (nodes that are mutually reachable)

# SCC 2: {3}

# SCC 3: {6}

# SCC 4: {7}

# Thus, the output is 4.
