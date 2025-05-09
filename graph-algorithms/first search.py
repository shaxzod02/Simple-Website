# Define a class for performing Depth-First Search (DFS) on a graph
class DFS:
    def __init__(self, nodes):
        # Initialize the list of nodes
        self.nodes = nodes
        # Create an adjacency list for each node
        self.graph = {node: [] for node in nodes}
        
    def add_edge(self, a, b):
        # Add an undirected edge (both directions)
        self.graph[a].append(b)
        self.graph[b].append(a)
        
    def visit(self, node):
        # If the node is already visited, do nothing (base case)
        if node in self.visited:
            return
        # Mark the node as visited
        self.visited.add(node)

        # Recursively visit all unvisited neighbors
        for next_node in self.graph[node]:
            self.visit(next_node)
        
    def search(self, start_node):
        # Initialize the visited set
        self.visited = set()
        # Start DFS from the given start node
        self.visit(start_node)
        # Return the set of all visited nodes
        return self.visited
    
# Create a DFS object with 5 nodes
d = DFS([1, 2, 3, 4, 5])

# Add undirected edges to the graph
d.add_edge(1, 2)
d.add_edge(1, 3)
d.add_edge(1, 4)
d.add_edge(2, 4)
d.add_edge(2, 5)
d.add_edge(3, 4)
d.add_edge(4, 5)

# Perform DFS starting from node 1
print(d.search(1))  # Output: {1, 2, 3, 4, 5}

# What this does:
# Starts DFS at node 1.

# Explores all reachable nodes.

# Returns all visited nodes as a set.