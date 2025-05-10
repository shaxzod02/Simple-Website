class TopologicalSort:
    def __init__(self, nodes):
        # Initialize graph and node list
        self.nodes = nodes
        self.graph = {node: [] for node in self.nodes}

    def add_edge(self, a, b):
        # Add a directed edge from 'a' to 'b'
        self.graph[a].append(b)

    def visit(self, node):
        # If the node is currently being visited, a cycle is found
        if self.state[node] == 1:
            self.cycle = True
            return

        # If the node is already visited, skip it
        if self.state[node] == 2:
            return

        # Mark node as visiting
        self.state[node] = 1

        # Visit all neighbors
        for next_node in self.graph[node]:
            self.visit(next_node)

        # Mark node as fully visited
        self.state[node] = 2

        # Add to ordering list
        self.order.append(node)

    def create(self):
        # Initialize visit state: 0 = unvisited, 1 = visiting, 2 = visited
        self.state = {node: 0 for node in self.nodes}
        self.order = []
        self.cycle = False

        # Visit each node if not already visited
        for node in self.nodes:
            if self.state[node] == 0:
                self.visit(node)

        # If a cycle was found, return None
        if self.cycle:
            return None
        else:
            # Reverse the order to get topological sort
            self.order.reverse()
            return self.order

#✅ Example Usage:
t = TopologicalSort([1, 2, 3, 4, 5, 6])

# Add directed edges to the graph
t.add_edge(1, 2)
t.add_edge(2, 3)
t.add_edge(3, 6)
t.add_edge(4, 1)
t.add_edge(4, 5)
t.add_edge(5, 2)
t.add_edge(5, 3)

# Compute and print topological sort order
print(t.create())  # Expected output: [4, 5, 1, 2, 3, 6]
