
# 🌲 Components and Spanning Trees

Understanding the structure of graphs is essential for solving many real-world problems such as network design, clustering, and connectivity. In this section, we explore how to identify connected components, build trees, and find optimal spanning structures using efficient algorithms.

---

## 🔗 Union-Find Data Structure (Disjoint Set Union - DSU)

The Union-Find data structure efficiently keeps track of disjoint sets and supports two main operations:

- `find(x)`: determines the representative (root) of the set containing `x`
- `union(a, b)`: merges the sets containing `a` and `b`

### Python Example:

```python
class UnionFind:
    def __init__(self, nodes):
        self.parent = {x: x for x in nodes}
        self.size = {x: 1 for x in nodes}

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            if self.size[ra] < self.size[rb]:
                ra, rb = rb, ra
            self.parent[rb] = ra
            self.size[ra] += self.size[rb]
```

## 🛣️ New Roads Problem
In connectivity problems, we often want to determine whether two cities are connected or how many new roads are needed to make the graph fully connected. The Union-Find structure is used to track and merge components as new edges are added.
```python
class NewRoads:
    def __init__(self, n):
        self.uf = UnionFind(range(1, n + 1))

    def add_road(self, a, b):
        self.uf.union(a, b)

    def has_route(self, a, b):
        return self.uf.find(a) == self.uf.find(b)
```

## 🌳 Trees in Graphs
A tree is a connected, acyclic graph. A tree with n nodes always has n-1 edges. If a graph has more than n-1 edges, it may contain cycles.

Removing an edge disconnects the tree.

Adding an edge creates a cycle.

## 📉 Kruskal’s Algorithm – Minimum Spanning Tree (MST)
Kruskal’s algorithm builds a minimum spanning tree by:

Sorting all edges by weight.

Adding edges one by one, skipping any that would form a cycle.

Using Union-Find to detect and prevent cycles.

Python Example:
```python
class Kruskal:
    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = []

    def add_edge(self, a, b, w):
        self.edges.append((w, a, b))

    def construct(self):
        self.edges.sort()
        uf = UnionFind(self.nodes)
        total_weight = 0
        for w, a, b in self.edges:
            if uf.find(a) != uf.find(b):
                uf.union(a, b)
                total_weight += w
        return total_weight
```

## ↕️ Minimizing vs. Maximizing
The same Kruskal algorithm can be used for maximum spanning trees by simply:

Sorting edges in descending order instead of ascending.

This allows solving problems like maximizing total capacity or bandwidth in a network.

