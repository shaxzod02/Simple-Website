#✅ Fully Commented Code:
class FloydWarshall:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = {}

        # Initialize the distance between all pairs of nodes
        for a in self.nodes:
            for b in self.nodes:
                # Distance to self is 0, otherwise infinity
                distance = 0 if a == b else float("inf")
                self.graph[(a, b)] = distance

    def add_edge(self, a, b, w):
        # Update the distance for edge (a, b) if the new weight is smaller
        self.graph[(a, b)] = min(self.graph[(a, b)], w)

    def find_distances(self):
        # Make a copy of the current graph distances to update during algorithm
        distances = self.graph.copy()

        # Try every node as an intermediate node in paths
        for k in self.nodes:
            for a in self.nodes:
                for b in self.nodes:
                    # Update the shortest distance from a to b via k
                    distance = min(distances[(a, b)],
                                   distances[(a, k)] + distances[(k, b)])
                    distances[(a, b)] = distance

        return distances

#✅ Test Code:
f = FloydWarshall([1, 2, 3, 4, 5])

# Add edges between nodes with weights
f.add_edge(1, 2, 8)
f.add_edge(1, 3, 1)
f.add_edge(2, 5, 5)
f.add_edge(3, 2, 4)
f.add_edge(3, 4, 2)
f.add_edge(4, 2, 1)
f.add_edge(4, 5, 3)

# Run the Floyd-Warshall algorithm
distances = f.find_distances()

# Print some specific shortest distances
print(distances[(1, 4)])  # 3: path 1 → 3 → 4
print(distances[(2, 1)])  # inf: no path from 2 to 1
print(distances[(3, 5)])  # 5: path 3 → 4 → 5

# 🔍 Why the Output is Correct:
# (1, 4): 1 → 3 → 4 = 1 + 2 = 3

# (2, 1): No path → inf

# (3, 5): 3 → 4 → 5 = 2 + 3 = 5