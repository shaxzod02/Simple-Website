
#✅ Stack Implementation (with comments)
class Stack:
    def __init__(self):
        # Initialize an empty list to act as the stack
        self.stack = []

    def push(self, x):
        # Push element x to the top of the stack
        self.stack.append(x)

    def top(self):
        # Return the element on the top of the stack without removing it
        return self.stack[-1]

    def pop(self):
        # Remove the top element from the stack
        self.stack.pop()

#✅ Usage Example
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.top())  # Output: 3
print(s.top())  # Output: 3 (top does not remove)
s.pop()         # Removes 3
print(s.top())  # Output: 2

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.stack)  # Output: [1, 2, 3] (internal list)
