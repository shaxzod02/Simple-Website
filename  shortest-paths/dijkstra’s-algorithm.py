import heapq  # Importing the heapq module to use a priority queue (min-heap)

# Define the Dijkstra class for shortest path computation
class Dijkstra:
    def __init__(self, nodes):
        self.nodes = nodes
        # Initialize an adjacency list for the graph
        self.graph = {node: [] for node in nodes}
        
    # Method to add a directed edge from node_a to node_b with a given weight
    def add_edge(self, node_a, node_b, weight):
        self.graph[node_a].append((node_b, weight))
        
    # Method to compute the shortest distances from the start_node to all other nodes
    def find_distances(self, start_node):
        # Initialize all distances as infinity
        distances = {node: float("inf") for node in self.nodes}
        distances[start_node] = 0  # Distance to the start node is 0
        
        # Priority queue to always expand the node with the current smallest distance
        queue = []
        heapq.heappush(queue, (0, start_node))  # (distance, node)
        
        visited = set()  # To track processed nodes
        
        while queue:
            # Extract the node with the smallest distance
            node_a = heapq.heappop(queue)[1]
            
            # Skip if this node has already been visited
            if node_a in visited:
                continue
            visited.add(node_a)
            
            # Iterate over neighbors of node_a
            for node_b, weight in self.graph[node_a]:
                new_distance = distances[node_a] + weight
                # If a shorter path to node_b is found, update it
                if new_distance < distances[node_b]:
                    distances[node_b] = new_distance
                    # Add updated distance to the queue
                    heapq.heappush(queue, (new_distance, node_b))
                    
        return distances  # Final shortest distances from start_node

#First Test Case:
d = Dijkstra([1, 2, 3, 4, 5])
d.add_edge(1, 2, 8)
d.add_edge(1, 3, 1)
d.add_edge(2, 5, 5)
d.add_edge(3, 2, 4)
d.add_edge(3, 4, 2)
d.add_edge(4, 2, 1)
d.add_edge(4, 5, 3)

distances = d.find_distances(1)
print(distances)  # Expected output: {1: 0, 2: 4, 3: 1, 4: 3, 5: 6}

#Second Test Case (⚠️ Problematic):
d = Dijkstra([1, 2, 3, 4])
d.add_edge(1, 2, 3)
d.add_edge(2, 3, -4)  # ⚠️ Negative weight
d.add_edge(1, 3, 1)
d.add_edge(3, 4, 1)

distances = d.find_distances(1)
print(distances)  # Output: {1: 0, 2: 3, 3: 1, 4: 2}
