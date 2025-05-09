# This class performs a Breadth-First Search on an undirected graph
class BFS:
    def __init__(self, nodes):
        # Initialize the graph with the given nodes
        self.nodes = nodes
        # Create an adjacency list with empty neighbor lists
        self.graph = {node: [] for node in nodes}

    def add_edge(self, a, b):
        # Add an undirected edge between nodes a and b
        self.graph[a].append(b)
        self.graph[b].append(a)

    def search(self, start_node):
        # Set to keep track of visited nodes
        visited = set()
        # Initialize the queue with the starting node
        queue = [start_node]
        visited.add(start_node)

        # Iterate through the queue
        for node in queue:
            # Visit all unvisited neighbors
            for next_node in self.graph[node]:
                if next_node not in visited:
                    queue.append(next_node)
                    visited.add(next_node)

        # Return the set of all visited nodes (i.e., reachable from start_node)
        return visited

# Create BFS object with 5 nodes
b = BFS([1, 2, 3, 4, 5])

# Add undirected edges
b.add_edge(1, 2)
b.add_edge(1, 3)
b.add_edge(1, 4)
b.add_edge(2, 4)
b.add_edge(2, 5)
b.add_edge(3, 4)
b.add_edge(4, 5)

# Perform BFS starting from node 1 and print the visited nodes
print(b.search(1))  # Output: {1, 2, 3, 4, 5}

# Explanation:
# queue is used to explore the graph level by level.

# visited ensures that each node is processed only once.

# The algorithm visits all nodes that are connected to start_node.