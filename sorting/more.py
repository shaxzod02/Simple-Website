# Sorts the list in descending order (largest to smallest)
numbers = [2, 4, 3, 5, 6, 1, 8, 7]
numbers.sort(reverse=True)
print(numbers)  # [8, 7, 6, 5, 4, 3, 2, 1]

# Sorts a list of pairs (tuples) by the first element, then by the second if firsts are equal
pairs = [(3, 5), (1, 6), (1, 2), (2, 4)]
pairs.sort()
print(pairs)  # [(1, 2), (1, 6), (2, 4), (3, 5)]

# Sorts the list based on absolute values of elements
numbers = [4, -1, 6, 2, -7, 8, 3, -5]
numbers.sort(key=abs)
print(numbers)  # [-1, 2, 3, 4, -5, 6, -7, 8]

# A class representing a 2D location with custom comparison and string representation
class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Equality check: two Locations are equal if both x and y are equal
    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    # Less-than comparison: used for sorting Locations
    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)

    # String representation of the object
    def __repr__(self):
        return str((self.x, self.y))

# Creating a list of Location objects
locations = []
locations.append(Location(1, 4))
locations.append(Location(4, 5))
locations.append(Location(2, 2))
locations.append(Location(1, 2))

# Sorts the list of locations using the __lt__ method
locations.sort()

print(locations)  # [(1, 2), (1, 4), (2, 2), (4, 5)]
