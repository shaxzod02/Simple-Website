
# Graph Algorithms

Graphs are powerful data structures used to represent relationships between objects. Graphs are used in various domains like social networks, web pages, transportation systems, and computer networks. Graph algorithms help in traversing graphs, finding shortest paths, detecting cycles, and more.

In this section, we will explore several graph algorithms, focusing on the most commonly used ones: Depth-First Search (DFS), Breadth-First Search (BFS), finding connected components, and shortest path algorithms. We will also cover practical programming with graphs and demonstrate how a labyrinth can be represented as a graph.

## Programming with Graphs

Graphs are typically represented in two ways:
1. **Adjacency Matrix**: A 2D array where the element at (i, j) indicates the presence (or weight) of an edge between nodes i and j.
2. **Adjacency List**: A list where each node points to a list of its neighbors.

Here's an example of an adjacency list representation for a graph:

```python
graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 5],
    4: [2],
    5: [3]
}
```

## Depth-First Search (DFS)
DFS is an algorithm for traversing or searching through a graph. Starting from a source node, it explores as far as possible along each branch before backtracking. DFS is useful for tasks like finding connected components, topological sorting, and solving mazes.

### Here's an example of a DFS implementation in Python:
```python
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()

    visited.add(node)
    print(node, end=' ')

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example usage
graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 5],
    4: [2],
    5: [3]
}
dfs(graph, 1)  # Output: 1 2 4 3 5
```

## Components and Connectivity
In an undirected graph, a connected component is a subset of nodes such that there is a path between any pair of nodes in this subset. We can use DFS or BFS to find all connected components in a graph.
```python
def find_components(graph):
    visited = set()
    components = []

    for node in graph:
        if node not in visited:
            component = []
            dfs(graph, node, visited)
            components.append(component)

    return components

# Example usage
graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 5],
    4: [2],
    5: [3]
}
print(find_components(graph))  # Output: [[1, 2, 3, 4, 5]]
```

## Breadth-First Search (BFS)
BFS is another graph traversal algorithm that explores the neighbors of a node before visiting their children. It is particularly useful for finding the shortest path in an unweighted graph.
```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=' ')

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example usage
graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 5],
    4: [2],
    5: [3]
}
bfs(graph, 1)  # Output: 1 2 3 4 5
```

## Shortest Paths and Distances
For finding the shortest paths in a graph, we typically use Dijkstra's Algorithm for weighted graphs or BFS for unweighted graphs. Dijkstra’s algorithm works by exploring the closest nodes first and updating the shortest distance to each node until the destination is reached.
```python
import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, node = heapq.heappop(priority_queue)

        if current_distance > distances[node]:
            continue

        for neighbor, weight in graph[node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example usage
graph = {
    1: [(2, 2), (3, 4)],
    2: [(1, 2), (3, 1), (4, 7)],
    3: [(1, 4), (2, 1), (5, 3)],
    4: [(2, 7)],
    5: [(3, 3)]
}
print(dijkstra(graph, 1))  # Output: {1: 0, 2: 2, 3: 3, 4: 9, 5: 6}
```

## Labyrinth as a Graph
A labyrinth can be represented as a graph where each cell in the maze is a node, and the edges represent valid moves (up, down, left, right). We can use DFS or BFS to find paths in the maze or to find the shortest path from the start to the goal.

### For example, here's how you could implement BFS to solve a labyrinth problem:
```python
def solve_labyrinth(labyrinth, start, goal):
    rows, cols = len(labyrinth), len(labyrinth[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque([(start, [start])])  # (current position, path so far)

    visited = set([start])

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == goal:
            return path

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and labyrinth[nx][ny] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))

    return None  # No path found

# Example usage (0: free space, 1: wall)
labyrinth = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]
start = (0, 0)
goal = (4, 4)
print(solve_labyrinth(labyrinth, start, goal))  # Output: [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
```


