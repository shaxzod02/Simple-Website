
#  Stack

A **stack** is a linear data structure that follows the Last In First Out (LIFO) principle. The most recent element added to the stack is the first one to be removed. Stacks are commonly used in scenarios such as function calls, undo operations, and parsing expressions.

## How Not to Implement a Class

Here is an example of a poorly designed class for a stack:

```python
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)  # This is okay, but we could optimize
    
    def pop(self):
        return self.stack.pop()  # This is also fine
    
    def peek(self):
        return self.stack[-1] if self.stack else None
    
    def is_empty(self):
        return len(self.stack) == 0
```

## Additional Class Features
Here are some additional features you might want to add to a stack class:

Size tracking: Keep track of the stack size to avoid recalculating the length.

Clear stack: Add a method to clear the entire stack.

Search method: Check if an item exists in the stack.

```python
class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0
    
    def push(self, item):
        self.stack.append(item)
        self.size += 1
    
    def pop(self):
        if not self.is_empty():
            self.size -= 1
            return self.stack.pop()
    
    def peek(self):
        return self.stack[-1] if self.stack else None
    
    def is_empty(self):
        return self.size == 0
    
    def clear(self):
        self.stack.clear()
        self.size = 0
    
    def search(self, item):
        return item in self.stack
```

## Efficient Duplicates
When working with stacks, handling duplicate elements efficiently is crucial. Using additional data structures like sets can help quickly check and remove duplicates.
```python
class UniqueStack:
    def __init__(self):
        self.stack = []
        self.seen = set()
    
    def push(self, item):
        if item not in self.seen:
            self.stack.append(item)
            self.seen.add(item)
    
    def pop(self):
        if self.stack:
            item = self.stack.pop()
            self.seen.remove(item)
            return item
    
    def peek(self):
        return self.stack[-1] if self.stack else None
    
    def is_empty(self):
        return len(self.stack) == 0
```

## Mode
In statistical analysis, the mode is the value that appears most frequently in a dataset. A stack could be modified to track the mode, making it easier to calculate during operations.
```python
class ModeStack:
    def __init__(self):
        self.stack = []
        self.frequency = {}
        self.max_freq = 0
    
    def push(self, item):
        self.stack.append(item)
        self.frequency[item] = self.frequency.get(item, 0) + 1
        self.max_freq = max(self.max_freq, self.frequency[item])
    
    def pop(self):
        item = self.stack.pop()
        self.frequency[item] -= 1
        if self.frequency[item] == 0:
            del self.frequency[item]
        # Update max frequency (naive approach for simplicity)
        if self.frequency:
            self.max_freq = max(self.frequency.values())
        return item
    
    def get_mode(self):
        for key, value in self.frequency.items():
            if value == self.max_freq:
                return key
        return None
```

