import collections

# Stack implementation (Last-In, First-Out)
class Stack:
    def __init__(self):
        # Initialize an empty deque to use as the stack
        self.stack = collections.deque()

    def push(self, x):
        # Add an element to the top of the stack
        self.stack.append(x)

    def top(self):
        # Return the top element without removing it
        return self.stack[-1]

    def pop(self):
        # Remove the top element from the stack
        self.stack.pop()

# Queue implementation (First-In, First-Out)
class Queue:
    def __init__(self):
        # Initialize an empty deque to use as the queue
        self.queue = collections.deque()

    def push(self, x):
        # Add an element to the end of the queue
        self.queue.append(x)

    def top(self):
        # Return the front element without removing it
        return self.queue[0]

    def pop(self):
        # Remove the front element from the queue
        self.queue.popleft()
