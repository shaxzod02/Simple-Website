import collections

# Create an empty double-ended queue (deque)
items = collections.deque()

# Add 1 to the right end of the deque
items.append(1)

# Add 2 to the right end of the deque
items.append(2)

# Add 3 to the left end of the deque
items.appendleft(3)

# Add 4 to the right end of the deque
items.append(4)

# Add 5 to the left end of the deque
items.appendleft(5)

# Print the entire deque
# The result will be: deque([5, 3, 1, 2, 4])
print(items)

# Access and print the first element (leftmost)
print(items[0])  # Output: 5

# Access and print the second element
print(items[1])  # Output: 3

# Access and print the last element (rightmost)
print(items[-1])  # Output: 4
