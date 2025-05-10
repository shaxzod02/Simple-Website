# Class to manage road network using Union-Find (Disjoint Set Union)
class NewRoads:
    def __init__(self, n):
        # Initialize UnionFind for cities labeled from 1 to n
        self.uf = UnionFind(range(1, n + 1))

    def add_road(self, a, b):
        # Connect city a and city b (merge their components)
        self.uf.union(a, b)

    def has_route(self, a, b):
        # Check if there is a path (route) between city a and city b
        return self.uf.find(a) == self.uf.find(b)

# Explanation:
# add_road(a, b): adds a road between cities a and b.

# has_route(a, b): returns True if a path exists between a and b, otherwise False.