class Graph:
    def __init__(self, nodes):
        # Initialize the graph with a list of nodes
        # Create an empty adjacency list for each node
        self.nodes = nodes
        self.graph = {node: [] for node in self.nodes}

    def add_edge(self, a, b):
        # Add a directed edge from node 'a' to node 'b'
        self.graph[a].append(b)


# Create a graph with 5 nodes: 1, 2, 3, 4, 5
g = Graph([1, 2, 3, 4, 5])

# Add directed edges between nodes
g.add_edge(1, 2)
g.add_edge(2, 4)
g.add_edge(2, 5)
g.add_edge(3, 1)
g.add_edge(4, 1)
g.add_edge(4, 5)
#🧠 Graph Structure (After Adding Edges):
1: [2]
2: [4, 5]
3: [1]
4: [1, 5]
5: []
