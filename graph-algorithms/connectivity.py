# This class finds connected components in an undirected graph
class Components:
    def __init__(self, nodes):
        # Initialize list of nodes
        self.nodes = nodes
        # Create an empty adjacency list for each node
        self.graph = {node: [] for node in nodes}
        
    def add_edge(self, a, b):
        # Add undirected edge between nodes a and b
        self.graph[a].append(b)
        self.graph[b].append(a)
        
    def visit(self, node):
        # If this node is already part of a component, skip it
        if node in self.components:
            return
        # Assign the current component number to this node
        self.components[node] = self.counter

        # Recursively visit all its neighbors
        for next_node in self.graph[node]:
            self.visit(next_node)
        
    def find_components(self):
        # Component counter starts at 0
        self.counter = 0
        # Dictionary to store the component number of each node
        self.components = {}

        # Loop over all nodes in the graph
        for node in self.nodes:
            # If node hasn't been visited yet, it's part of a new component
            if node not in self.components:
                self.counter += 1
                self.visit(node)
                
        # Return a dictionary mapping each node to its component number
        return self.components

# Create a Components object with 5 nodes
c = Components([1, 2, 3, 4, 5])

# Add edges to form two connected components: {1,2} and {3,4,5}
c.add_edge(1, 2)
c.add_edge(3, 4)
c.add_edge(3, 5)
c.add_edge(4, 5)

# Find and print the connected components
print(c.find_components())  # Output: {1: 1, 2: 1, 3: 2, 4: 2, 5: 2}
