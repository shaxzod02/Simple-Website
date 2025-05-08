
# A basic implementation of a stack data structure
class Stack:
    def __init__(self):
        self.stack = []  # Initialize an empty list to represent the stack

    def push(self, x):
        self.stack.append(x)  # Add an element to the top of the stack

    def top(self):
        return self.stack[-1]  # Return the top element of the stack without removing it

    def pop(self):
        self.stack.pop()  # Remove the top element from the stack


#Example usage:

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.top()) # 3 — returns the top element (3)
print(s.top()) # 3 — returns the top element again (still 3)
s.pop()        # removes the top element (3)
print(s.top()) # 2 — now the top is 2

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.stack) # [1, 2, 3] — shows internal list representing the stack

# Optional Improvement
# Right now, the stack list is publicly accessible (e.g., s.stack). If you'd like to encapsulate it (hide it from direct access), you could rename it with a leading underscore:
self._stack = []
