# Define a dictionary representing a graph with adjacency lists
graph = {
    1: [2, 3, 4],
    2: [1, 4, 5],
    3: [1, 4],
    4: [1, 2, 3, 5],
    5: [2, 4]
}

# Define a class to represent an undirected graph
class Graph:
    def __init__(self, nodes):
        # Initialize a list of nodes and an empty adjacency list for each node
        self.nodes = nodes
        self.graph = {node: [] for node in nodes}
        
    def add_edge(self, a, b):
        # Add an edge from node a to node b
        self.graph[a].append(b)
        # Since the graph is undirected, also add an edge from b to a
        self.graph[b].append(a)

# Create a graph with 5 nodes
g = Graph([1, 2, 3, 4, 5])

# Add edges between the nodes (undirected connections)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 4)
g.add_edge(2, 5)
g.add_edge(3, 4)
g.add_edge(4, 5)
