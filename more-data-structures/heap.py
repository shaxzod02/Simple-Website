import heapq

# Initialize an empty list to be used as a heap
items = []

# Push elements into the heap
heapq.heappush(items, 4)
heapq.heappush(items, 2)
heapq.heappush(items, 3)
heapq.heappush(items, 1)
heapq.heappush(items, 5)

# Print the smallest element (heap is a min-heap by default)
print(items[0])  # Output: 1

# Remove the smallest element from the heap
heapq.heappop(items)

# Print the new smallest element
print(items[0])  # Output: 2


# Demonstration of duplicate values in a heap
import heapq

# Initialize another empty heap
items = []

# Push duplicate values into the heap
heapq.heappush(items, 1)
heapq.heappush(items, 1)
heapq.heappush(items, 1)

# Print the heap list (still a valid min-heap)
print(items)  # Output: [1, 1, 1]
