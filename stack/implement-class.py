#✅ Fixed Stack Implementation

class Stack:
    def __init__(self):
        # Initialize an empty list for each instance
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


#✅ Usage Example (Corrected)

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.top())  # Output: 3 (top of the stack for `s`)

a = Stack()
b = Stack()
a.push(1)
b.push(2)

print(a.top())  # Output: 1 (top of the stack for `a`)
print(b.top())  # Output: 2 (top of the stack for `b`)
