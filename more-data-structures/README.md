
# 📦 More Data Structures

This section introduces additional data structures that are widely used in efficient algorithms and systems programming. Understanding these structures will help you solve problems that require fast access, insertion, or deletion of elements.

---

## 🌀 Deque (Double-Ended Queue)

A **deque** is a data structure that allows you to add and remove elements from both the front and back.

### Features:
- `append(x)` – add to the end
- `appendleft(x)` – add to the beginning
- `pop()` – remove from the end
- `popleft()` – remove from the beginning

### Example:

```python
from collections import deque

dq = deque()
dq.append(10)
dq.appendleft(5)
dq.pop()       # 10
dq.popleft()   # 5
```

## 📚 Stack and Queue
Stack (LIFO – Last In, First Out)
Access the most recently added item first.

Operations: push, pop, peek

Queue (FIFO – First In, First Out)
Access the oldest added item first.

Operations: enqueue, dequeue

Example:
```python
stack = []
stack.append(1)
stack.append(2)
stack.pop()  # 2

from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
queue.popleft()  # 1
```

## 🔺 Heap (Binary Heap)
A heap is a special tree-based data structure that satisfies the heap property – either a min-heap or a max-heap.

Python example (min-heap):
```python
import heapq

heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
heapq.heappop(heap)  # 1
```

## 🧊 Sliding Window
Sliding window is a technique for efficiently computing values over subarrays of a fixed size.

Example: Find max average of a subarray of size k
```python
def max_avg(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i-k]
        max_sum = max(max_sum, window_sum)
    return max_sum / k
```
## 🌐 Data Structures in Other Languages
| Structure | Python              | C++              | Java              | JavaScript        |
| --------- | ------------------- | ---------------- | ----------------- | ----------------- |
| Stack     | `list`              | `std::stack`     | `Stack` class     | Array-based       |
| Queue     | `deque`             | `std::queue`     | `Queue` interface | Array or `Deque`  |
| Deque     | `collections.deque` | `std::deque`     | `ArrayDeque`      | Custom array impl |
| Heap      | `heapq`             | `priority_queue` | `PriorityQueue`   | No built-in       |

```python
Let me know if you’d like this saved as a downloadable file or if you want the next topic prepared.
```
