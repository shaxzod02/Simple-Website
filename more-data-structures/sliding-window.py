import heapq

def find_minima(items, k):
    n = len(items)
    heap = []       # Min-heap to store (value, index) pairs
    result = []     # List to store the minimums of each window
    
    for i in range(n):
        # Add current item and its index to the heap
        heapq.heappush(heap, (items[i], i))
        
        # Remove elements from the heap that are outside the current window
        while heap[0][1] <= i - k:
            heapq.heappop(heap)
        
        # Once we have at least k elements, start adding minimums to result
        if i >= k - 1:
            result.append(heap[0][0])  # The smallest value in the window
            
    return result

# What This Function Does:
# It computes the minimum value in every sliding window of size k in the list items.

# Uses a min-heap to efficiently keep track of the smallest element in the current window.

# Elements that fall out of the sliding window (i - k) are removed from the heap.

# Example:
print(find_minima([2, 1, 4, 5, 3, 4, 1, 2], 3))
# Output: [1, 1, 3, 3, 3, 1]
