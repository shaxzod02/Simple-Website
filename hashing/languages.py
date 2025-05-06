# Using a set (equivalent to HashSet in Java, unordered_set in C++)
numbers = set()

# Adding elements to the set
numbers.add(1)
numbers.add(2)
numbers.add(3)

print(numbers)  # {1, 2, 3} - sets store unique elements and don't maintain order

# Using a dictionary (equivalent to HashMap in Java, unordered_map in C++)
weights = {}

# Adding key-value pairs to the dictionary
weights["apina"] = 100
weights["banaani"] = 1
weights["cembalo"] = 500

print(weights)  # {'apina': 100, 'banaani': 1, 'cembalo': 500}

# Accessing values in the dictionary
print(weights["apina"])  # 100

# Checking if a key exists in the dictionary
print("apina" in weights)  # True
print("ananas" in weights)  # False

# Removing a key-value pair
del weights["banaani"]
print(weights)  # {'apina': 100, 'cembalo': 500}

# Using a dictionary for counting occurrences (like a frequency map)
items = ["apple", "banana", "apple", "orange", "banana", "banana"]
count = {}

for item in items:
    if item not in count:
        count[item] = 0
    count[item] += 1

print(count)  # {'apple': 2, 'banana': 3, 'orange': 1}

# Using a set of custom objects with a custom hash function
class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

# Adding custom objects to a set
locations = set()
locations.add(Location(1, 2))
locations.add(Location(3, -5))
locations.add(Location(1, 4))

print(locations)  # Set of unique Location objects, based on their x and y coordinates
