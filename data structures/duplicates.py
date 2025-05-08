
# Method to push a value x k times into the SuperStack.
def push_many(self, k, x):
    for i in range(k):
        self.push(x)

# Example usage of SuperStack.
s = SuperStack()
s.push_many(3, 8)  # Push value 8 three times.
s.push(4)          # Push value 4 once.
s.push_many(2, 5)  # Push value 5 two times.


# SuperStack class that stores elements in a compressed form (value with count).
class SuperStack:
    def __init__(self):
        # Initialize an empty stack where each element is stored as a (count, value) tuple.
        self.stack = []
        
    def push(self, x):
        # Push a single value x into the stack as (1, x).
        self.stack.append((1, x))
        
    def push_many(self, k, x):
        # Push a value x k times in a compressed form.
        self.stack.append((k, x))
        
    def top(self):
        # Return the value of the top element (ignoring the count).
        return self.stack[-1][1]
        
    def pop(self):
        # Remove the top element from the stack.
        last = self.stack[-1]
        if last[0] == 1:
            # If there's only one occurrence, remove the element completely.
            self.stack.pop()
        else:
            # If there are multiple occurrences, decrease the count by one.
            self.stack[-1] = (last[0] - 1, last[1])


