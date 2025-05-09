#🔢 Class to Compute Distances (BFS-based):
# This class finds shortest distances from a start node using BFS
class Distances:
    def __init__(self, nodes):
        # Initialize the graph with given nodes and empty adjacency lists
        self.nodes = nodes
        self.graph = {node: [] for node in nodes}

    def add_edge(self, a, b):
        # Add undirected edge between nodes a and b
        self.graph[a].append(b)
        self.graph[b].append(a)

    def find_distances(self, start_node):
        # Dictionary to store shortest distance from start_node to each node
        distances = {}
        # Initialize the queue for BFS with the start node
        queue = [start_node]
        # Distance to the start node is 0
        distances[start_node] = 0

        # BFS traversal
        for node in queue:
            distance = distances[node]
            for next_node in self.graph[node]:
                if next_node not in distances:
                    queue.append(next_node)
                    distances[next_node] = distance + 1
                    
        return distances

# Example usage:
d = Distances([1, 2, 3, 4, 5])
d.add_edge(1, 2)
d.add_edge(1, 3)
d.add_edge(1, 4)
d.add_edge(2, 4)
d.add_edge(2, 5)
d.add_edge(3, 4)
d.add_edge(4, 5)

print(d.find_distances(1))  # {1: 0, 2: 1, 3: 1, 4: 1, 5: 2}

#🧭 Class to Find the Shortest Path Between Two Nodes:
# This class finds the shortest path between two nodes using BFS
class ShortestPaths:
    def __init__(self, nodes):
        # Initialize the graph
        self.nodes = nodes
        self.graph = {node: [] for node in nodes}

    def add_edge(self, a, b):
        # Add undirected edge
        self.graph[a].append(b)
        self.graph[b].append(a)

    def find_path(self, start_node, end_node):
        # Distance dictionary: stores shortest distance from start_node
        distances = {}
        # Previous dictionary: used to reconstruct the path
        previous = {}

        queue = [start_node]
        distances[start_node] = 0
        previous[start_node] = None

        # BFS traversal
        for node in queue:
            distance = distances[node]
            for next_node in self.graph[node]:
                if next_node not in distances:
                    queue.append(next_node)
                    distances[next_node] = distance + 1
                    previous[next_node] = node

        # If end_node was not reached
        if end_node not in distances:
            return None

        # Reconstruct the path from end_node to start_node
        node = end_node
        path = []
        while node:
            path.append(node)
            node = previous[node]

        # Reverse the path to get it from start_node to end_node
        path.reverse()
        return path

# Example usage:
s = ShortestPaths([1, 2, 3, 4, 5])
s.add_edge(1, 2)
s.add_edge(1, 3)
s.add_edge(1, 4)
s.add_edge(2, 4)
s.add_edge(2, 5)
s.add_edge(3, 4)
s.add_edge(4, 5)

print(s.find_path(2, 4))  # [2, 4]
print(s.find_path(1, 5))  # [1, 2, 5]
print(s.find_path(5, 1))  # [5, 2, 1]

# ✅ Summary:
# Distances → Computes distance from start_node to all others.

# ShortestPaths → Reconstructs actual path between two nodes using BFS and backtracking with a previous pointer.