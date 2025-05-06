
# Example of trying to add a mutable list to a set, which raises an error.
lists = set()
lists.add([1, 2, 3])  # TypeError: unhashable type: 'list'

print(hash([1, 2, 3]))  # TypeError: unhashable type: 'list'

# We can add immutable objects like tuples to a set.
lists = set()
lists.add((1, 2, 3))  # This works because tuples are immutable and hashable.

# Using a dictionary to store values.
lists = {}
lists["apina"] = [1, 2, 3]

# Defining a custom class with a hash function and equality method
class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Implementing the __hash__ method to make the object hashable.
    def __hash__(self):
        return hash((self.x, self.y))  # Hash based on the tuple (x, y)

    # Implementing __eq__ to compare two Location objects.
    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)  # Locations are equal if their coordinates match.


# Creating a set of Location objects.
locations = set()
locations.add(Location(1, 2))
locations.add(Location(3, -5))
locations.add(Location(1, 4))

