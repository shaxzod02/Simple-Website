
#  Hashing
Overview
Hashing is a powerful technique used to store and retrieve data efficiently. It underpins data structures like sets and dictionaries, allowing constant-time average-case access. This section introduces how hashing works and how it applies to solving common algorithmic problems.

##  Set
A set is a data structure that stores unique elements. Hashing allows:

Fast insertion

Quick membership checking

Efficient removal

Common use cases include removing duplicates or tracking seen elements.

## How Many Numbers?
This subtopic deals with determining how many distinct numbers are in a list.

### Using a set:
```Python
 unique_numbers = set(numbers)
 print(len(unique_numbers))
 ```

##  Dictionary
A dictionary (or map) stores key-value pairs. It allows you to:

Store counts

Map items to categories

Track occurrences or metadata

Hashing is used internally to provide fast access to values based on keys.

## Mode
The mode of a list is the number that appears most frequently.

### Efficiently solved using a dictionary:
```Python
from collections import defaultdict
count = defaultdict(int)
for x in numbers:
    count[x] += 1
mode = max(count, key=count.get)
```

## Rounds
This subtopic may involve grouping or scheduling items using hash tables.

For example:

Grouping players into rounds

Hashing names or IDs to ensure even distribution

## Play List
Tasks such as detecting repeated songs or tracking play history can be done using sets or dictionaries.

Examples:

Checking for duplicates

Counting how many times a song was played

Finding the most played track

## List Sums
The goal is to check whether any two elements in a list sum to a specific value.

### Hash-based solution:

```Python
  seen = set()
for num in numbers:
    if target - num in seen:
        print("Pair found")
    seen.add(num)
```

##  How Does Hashing Work?
Hashing involves applying a hash function to a key, which maps it to an index in a fixed-size table.

Key concepts:

Hash collisions (when two keys hash to the same index)

Load factor

Rehashing

Chaining vs open addressing

Good hash functions minimize collisions and distribute data uniformly.

##  Hashing in Other Programming Languages
Hash tables are used across many languages:

Python: set, dict

Java: HashSet, HashMap

C++: unordered_set, unordered_map

JavaScript: Objects and Map

Each language may differ in implementation details like hash functions, resizing strategies, or memory layout.


