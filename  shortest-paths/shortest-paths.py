#✅ Commented Code:
def shortest_path(self, start_node, end_node):
    # Step 1: Initialize distances to all nodes as infinity
    distances = {node: float("inf") for node in self.nodes}
    distances[start_node] = 0  # Distance to the start node is 0

    # Dictionary to store the previous node on the shortest path
    previous = {start_node: None}

    # Step 2: Relax all edges |V| - 1 times (V = number of nodes)
    for _ in range(len(self.nodes) - 1):
        for edge in self.edges:
            node_a, node_b, weight = edge
            new_distance = distances[node_a] + weight
            # If a shorter path to node_b is found, update it
            if new_distance < distances[node_b]:
                distances[node_b] = new_distance
                previous[node_b] = node_a  # Track the path

    # Step 3: If the destination is unreachable, return None
    if distances[end_node] == float("inf"):
        return None

    # Step 4: Reconstruct the shortest path from end_node to start_node
    path = []
    node = end_node
    while node:
        path.append(node)
        node = previous[node]  # Move backwards along the path

    path.reverse()  # Reverse to get path from start to end
    return path

#✅ Test Code:
b = BellmanFord([1, 2, 3, 4, 5])

b.add_edge(1, 2, 8)
b.add_edge(1, 3, 1)
b.add_edge(2, 5, 5)
b.add_edge(3, 2, 4)
b.add_edge(3, 4, 2)
b.add_edge(4, 2, 1)
b.add_edge(4, 5, 3)

path = b.shortest_path(1, 5)
print(path)  # Output: [1, 3, 4, 5]

# 📌 Why This Output Is Correct:
# 1 → 3 (cost 1)

# 3 → 4 (cost 2)

# 4 → 5 (cost 3)

# Total cost = 6 (which is the shortest)