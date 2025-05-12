
# 📏 Shortest Paths in Graphs

Finding the shortest path between nodes in a graph is one of the fundamental problems in computer science and algorithm design. Depending on the graph's properties, different algorithms are used for optimal performance.

---

## 🚧 Bellman-Ford Algorithm

The **Bellman-Ford algorithm** computes shortest paths from a source node to all other nodes in a **weighted** graph, even when **negative edge weights** are present.

### Key Features:
- Handles negative weights.
- Detects **negative weight cycles**.

### Time Complexity:
- **O(n × m)** where `n` is the number of nodes and `m` is the number of edges.

### Python Example:

```python
def bellman_ford(graph, n, source):
    dist = [float('inf')] * n
    dist[source] = 0

    for _ in range(n - 1):
        for u, v, w in graph:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    return dist
```

## ⚡ Dijkstra’s Algorithm
The Dijkstra algorithm is used to find the shortest paths from a source node to all other nodes, assuming non-negative edge weights.

Key Features:
Very efficient with non-negative weights.

Uses a priority queue (heap) to optimize performance.

Time Complexity:
O((n + m) log n) using a min-heap.

Python Example:
```python
import heapq

def dijkstra(graph, source):
    dist = {node: float('inf') for node in graph}
    dist[source] = 0
    queue = [(0, source)]

    while queue:
        d, node = heapq.heappop(queue)
        if d > dist[node]:
            continue
        for neighbor, weight in graph[node]:
            new_dist = d + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(queue, (new_dist, neighbor))

    return dist
```

## 🛠️ Constructing Shortest Paths
To construct the actual shortest path, not just the distance, keep track of the predecessor of each node while updating distances.

Example:
```python
# During Dijkstra or Bellman-Ford:
prev = {}

# On edge relaxation
if new_dist < dist[v]:
    dist[v] = new_dist
    prev[v] = u

# Reconstruct path
def get_path(prev, target):
    path = []
    while target in prev:
        path.append(target)
        target = prev[target]
    path.append(target)
    return path[::-1]
```

## 🌐 Floyd-Warshall Algorithm
The Floyd-Warshall algorithm computes the shortest paths between all pairs of nodes.

Key Features:
Works on both positive and negative weights (no negative cycles).

Based on dynamic programming.

Time Complexity:
O(n³) — best for small, dense graphs.

Python Example:
```python
def floyd_warshall(n, graph):
    dist = [[float('inf')] * n for _ in range(n)]
    for u in range(n):
        dist[u][u] = 0
    for u, v, w in graph:
        dist[u][v] = w

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist
```

## 🧠 Choice of Algorithm
| Algorithm      | Handles Negative Weights | Finds All-Pairs | Efficiency              |
| -------------- | ------------------------ | --------------- | ----------------------- |
| Bellman-Ford   | ✅ Yes                    | ❌ No            | Slower for large graphs |
| Dijkstra       | ❌ No (only positive)     | ❌ No            | Fast with heaps         |
| Floyd-Warshall | ✅ Yes                    | ✅ Yes           | Best for small graphs   |

