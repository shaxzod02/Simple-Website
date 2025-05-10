
# Shortest Path Algorithms Overview
# Dijkstra’s Algorithm
# Dijkstra’s algorithm is typically a good choice for finding the shortest paths in graphs without negative edge weights. It is efficient, especially when implemented with a priority queue (e.g., a heap), and works well in practical scenarios where edge weights represent things like distances or costs—values that are naturally non-negative.

# Bellman-Ford Algorithm
# The Bellman-Ford algorithm is more versatile because it can handle negative edge weights, as long as there are no negative-weight cycles in the graph. While it is slower than Dijkstra’s algorithm, its broader applicability makes it valuable in cases where negative weights are possible.

# Floyd-Warshall Algorithm
# The Floyd-Warshall algorithm is designed to find the shortest distances between all pairs of nodes. It is especially useful for dense graphs or when all-pairs distances are needed in advance (e.g., for routing or analysis). However, it has a higher time complexity (O(n³)) and is best suited for smaller graphs or graphs where frequent shortest path queries are required.