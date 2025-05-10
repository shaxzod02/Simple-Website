class BellmanFord:
    def __init__(self, nodes):
        self.nodes = nodes  # List of nodes in the graph
        self.edges = []     # List to store all edges as (start, end, weight)
        
    def add_edge(self, node_a, node_b, weight):
        # Add a directed edge from node_a to node_b with given weight
        self.edges.append((node_a, node_b, weight))
        
    def find_distances(self, start_node):
        # Initialize all distances to infinity, except the start node
        distances = {}
        for node in self.nodes:
            distances[node] = float("inf")
        distances[start_node] = 0
        
        # Relax all edges (V - 1) times, where V = number of nodes
        num_rounds = len(self.nodes) - 1
        for _ in range(num_rounds):
            for edge in self.edges:
                node_a, node_b, weight = edge
                # Only relax if the start node distance is not infinity
                new_distance = distances[node_a] + weight
                if new_distance < distances[node_b]:
                    distances[node_b] = new_distance
        
        # Return the computed shortest distances from the start_node
        return distances

#✅ Usage Example:
b = BellmanFord([1, 2, 3, 4, 5])

# Adding edges with weights
b.add_edge(1, 2, 8)
b.add_edge(1, 3, 1)
b.add_edge(2, 5, 5)
b.add_edge(3, 2, 4)
b.add_edge(3, 4, 2)
b.add_edge(4, 2, 1)
b.add_edge(4, 5, 3)

# Calculate shortest distances from node 1
distances = b.find_distances(1)
print(distances)  # Expected output: {1: 0, 2: 4, 3: 1, 4: 3, 5: 6}

# ✅ Step-by-step Explanation:
# Start Node = 1

# Initially: {1: 0, 2: ∞, 3: ∞, 4: ∞, 5: ∞}

# After relaxing edges over 4 rounds:

# Path from 1 → 3 = 1

# Path from 1 → 3 → 4 = 3

# Path from 1 → 3 → 4 → 2 = 4

#Path from 1 → 3 → 4 → 5 = 6

# ⚠️ Optional Improvement – Negative Cycle Detection
# To detect negative cycles, you can add an extra pass after the main loop:

# After main loop
for node_a, node_b, weight in self.edges:
    if distances[node_a] + weight < distances[node_b]:
        raise ValueError("Graph contains a negative weight cycle")



