
# 💧 Maximum Flow and Applications

Flow networks are a powerful tool used to model and solve problems related to transporting resources through a system. This section explores how to compute the **maximum flow**, its connection to the **minimum cut**, and how these concepts apply in real-world problems such as escape planning and matchmaking.

---

## 🔄 Ford-Fulkerson Algorithm

The **Ford-Fulkerson** algorithm calculates the **maximum flow** from a source node to a sink node in a flow network. It works by repeatedly finding **augmenting paths** — paths where additional flow can be pushed — and updating the flow until no more augmenting paths exist.

### Python Implementation (DFS-based):

```python
class MaximumFlow:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = { (i, j): 0 for i in nodes for j in nodes }

    def add_edge(self, u, v, capacity):
        self.graph[(u, v)] += capacity

    def add_flow(self, u, sink, flow):
        if u in self.seen:
            return 0
        self.seen.add(u)
        if u == sink:
            return flow
        for v in self.nodes:
            if self.flow[(u, v)] > 0:
                min_flow = min(flow, self.flow[(u, v)])
                pushed = self.add_flow(v, sink, min_flow)
                if pushed > 0:
                    self.flow[(u, v)] -= pushed
                    self.flow[(v, u)] += pushed
                    return pushed
        return 0

    def construct(self, source, sink):
        self.flow = self.graph.copy()
        total = 0
        while True:
            self.seen = set()
            pushed = self.add_flow(source, sink, float("inf"))
            if pushed == 0:
                break
            total += pushed
        return total
```

## ✂️ Minimum Cut
A cut is a partition of the graph such that the source and sink are in separate components. The minimum cut is the smallest total capacity of edges that, when removed, disconnect the sink from the source.

📌 The Max-Flow Min-Cut Theorem guarantees that:

The maximum amount of flow equals the minimum capacity of any cut.

## 🚨 Prison Escape Problem
Model each room and corridor as nodes and edges in a flow network. Compute the maximum flow from the prison to the exit, representing the maximum number of prisoners that can escape at the same time.

## 🧭 Choosing Augmenting Paths
The way augmenting paths are selected affects performance:

DFS: simple, but may be slow on large graphs

BFS: leads to the Edmonds-Karp algorithm, which ensures polynomial runtime

## 🔗 Maximum Matching
In bipartite graphs (e.g. job assignments, student-project pairing), we can model the problem as a flow network:

Each node on the left connects to the right through a middle layer

Solve with Ford-Fulkerson to get the maximum matching

