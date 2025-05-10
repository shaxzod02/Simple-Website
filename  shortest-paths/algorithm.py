#✅ Explanation of Your Graph:

# 1 --(1)--> 2 --(1)--> 3
#        ↑        |
#        |        |
#        └<--(-2)--┘
#              |
#              v
#             4

# Node 3 → 2 has a negative weight (-2).

# This creates a cycle (2 → 3 → 2) with a total cost of 1 + (-2) = -1.

# The Bellman-Ford algorithm will "tighten" (reduce) distances as long as it keeps finding better paths.

# ✅ Expected Output:

{1: 0, 2: -2, 3: 0, 4: -1}
# dist[1] = 0 (start)

# dist[2] = -2 (due to the negative cycle effect)

# dist[3] = 0 (from 2 → 3)

# dist[4] = -1 (from 2 → 4)

✅ To Detect Negative Cycles
for node_a, node_b, weight in self.edges:
    if distances[node_a] + weight < distances[node_b]:
        raise ValueError("Graph contains a negative weight cycle")

