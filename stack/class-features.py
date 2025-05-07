#✅ Updated Stack Class with Improvements

class Stack:
    def __init__(self):
        self.stack = []  # Each instance gets its own stack

    def push(self, x):
        self.stack.append(x)  # Adds element x to the stack

    def __repr__(self):
        # Custom string representation for the stack instance
        return str(self.stack)

    def __len__(self):
        # Returns the number of elements in the stack
        return len(self.stack)

    def pop(self):
        # Removes the top element from the stack and raises an error if empty
        if len(self.stack) == 0:
            raise IndexError("pop from empty stack")
        return self.stack.pop()

    def top(self):
        # Returns the top element without removing it, raises an error if empty
        if len(self.stack) == 0:
            raise IndexError("top from empty stack")
        return self.stack[-1]


#✅ Usage Example

s = Stack()
s.push(1)
s.push(2)
s.push(3)

print(s)  # Output: [1, 2, 3]

print(len(s))  # Output: 3

print(s.top())  # Output: 3 (top element without removing)

s.pop()  # Removes 3
print(s)  # Output: [1, 2]

s.pop()  # Removes 2
s.pop()  # Removes 1
# Now the stack is empty

try:
    s.pop()  # Raises IndexError: pop from empty stack
except IndexError as e:
    print(e)  # Output: pop from empty stack

