# Disjoint Set Union (Union-Find) data structure with union by size
class UnionFind:
    def __init__(self, nodes):
        # Initialize each node with no parent (None) and size 1
        self.link = {node: None for node in nodes}
        self.size = {node: 1 for node in nodes}

    def find(self, x):
        # Find the root of the set containing x by following parent pointers
        while self.link[x]:
            x = self.link[x]
        return x

    def union(self, a, b):
        # Find roots of the sets containing a and b
        a = self.find(a)
        b = self.find(b)
        
        # If already in the same set, do nothing
        if a == b: return

        # Union by size: attach smaller tree to larger tree
        if self.size[a] > self.size[b]:
            a, b = b, a
        self.link[a] = b
        self.size[b] += self.size[a]

# Example usage:
u = UnionFind([1, 2, 3, 4, 5, 6, 7, 8])

# Merge sets containing the given pairs
u.union(1, 4)
u.union(2, 5)
u.union(5, 6)
u.union(3, 7)
u.union(7, 8)

# Print the root representative of each element
print(u.find(1)) # 4
print(u.find(2)) # 5
print(u.find(3)) # 7
print(u.find(4)) # 4
print(u.find(5)) # 5
print(u.find(6)) # 5
print(u.find(7)) # 7
print(u.find(8)) # 7
