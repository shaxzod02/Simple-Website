
# ➤ Directed Graphs

Directed graphs (digraphs) are graphs where edges have direction, going from one node to another. These structures are fundamental in modeling dependencies, one-way relationships, and sequences.

---

## 🎯 Representing Directed Graphs

Directed graphs can be represented using:

- **Adjacency List**: Dictionary where each node maps to a list of its neighbors.
- **Adjacency Matrix**: 2D array where `matrix[i][j]` is `1` if there's an edge from node `i` to node `j`.

### Example (Adjacency List):

```python
graph = {
    1: [2, 3],
    2: [4],
    3: [],
    4: [1]
}
```

## 📐 Topological Ordering
A topological ordering of a directed acyclic graph (DAG) is a linear ordering of its nodes such that for every directed edge u → v, node u comes before v.

Applications:
Task scheduling

Build systems

Dependency resolution

Example (DFS-based):
```python
def topological_sort(graph):
    visited = set()
    order = []

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor)
        order.append(node)

    for node in graph:
        dfs(node)

    return order[::-1]
```

## 💡 Dynamic Programming on DAGs
Dynamic programming can be efficiently applied on DAGs using topological ordering to ensure that all dependencies are solved before each node is processed.

Example: Longest path in DAG
```python
def longest_path(graph, start):
    order = topological_sort(graph)
    dist = {node: float('-inf') for node in graph}
    dist[start] = 0

    for node in order:
        for neighbor in graph[node]:
            dist[neighbor] = max(dist[neighbor], dist[node] + 1)

    return dist
```

## 🔁 Strong Connectivity
A strongly connected component (SCC) is a subgraph where every node is reachable from every other node in the component.

Kosaraju’s Algorithm:
Perform DFS and record post-order.

Reverse all edges.

Do DFS in the reverse order of post-order.

Python Sketch:
```python
def kosaraju_scc(graph):
    def dfs(u, visited, stack):
        visited.add(u)
        for v in graph[u]:
            if v not in visited:
                dfs(v, visited, stack)
        stack.append(u)

    def reverse_graph(graph):
        rev = {u: [] for u in graph}
        for u in graph:
            for v in graph[u]:
                rev[v].append(u)
        return rev

    stack, visited = [], set()
    for u in graph:
        if u not in visited:
            dfs(u, visited, stack)

    rev_graph = reverse_graph(graph)
    visited.clear()
    sccs = []

    while stack:
        u = stack.pop()
        if u not in visited:
            component = []
            dfs(u, visited, component)
            sccs.append(component)

    return sccs
```

## 📌 Summary
Directed graphs are used to represent one-way relationships.

Topological sort is essential for processing DAGs.

Dynamic programming benefits from topological order.

Strong connectivity helps identify tightly connected clusters in graphs.
```python

Would you like this in `.md` file format or want the next section prepared as well?
```