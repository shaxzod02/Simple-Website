#Updated SuperStack Implementation

class SuperStack:
    def __init__(self):
        self.stack = []  # Initializes an empty stack
    
    def push(self, x):
        # Pushes a single element onto the stack as a tuple (1, x)
        self.stack.append((1, x))
    
    def push_many(self, k, x):
        # Pushes 'k' occurrences of 'x' onto the stack as a tuple (k, x)
        self.stack.append((k, x))
    
    def top(self):
        # Returns the value at the top of the stack
        return self.stack[-1][1]
    
    def pop(self):
        # Pops an element from the stack
        last = self.stack[-1]
        if last[0] == 1:
            # If the last element in the stack is a single element, simply pop it
            self.stack.pop()
        else:
            # Otherwise, decrease the count 'k' and update the stack
            self.stack[-1] = (last[0] - 1, last[1])

# Example usage:
s = SuperStack()
s.push_many(3, 8)  # Adds three '8's to the stack
print(s.top())     # Should print 8
s.push(4)          # Adds one '4' to the stack
print(s.top())     # Should print 4
s.push_many(2, 5)  # Adds two '5's to the stack
print(s.top())     # Should print 5
s.pop()            # Pops one '5'
print(s.top())     # Should print 5 again (still one '5' in the stack)
s.pop()            # Pops the last '5'
print(s.top())     # Should print 4 (top of the stack now)
s.pop()            # Pops '4'
print(s.top())     # Should print 8 (top of the stack now)
s.pop()            # Pops one '8'
print(s.top())     # Should print 8 again (still two '8's left in the stack)
s.pop()            # Pops another '8'
print(s.top())     # Should print 8 again (still one '8' left in the stack)
s.pop()            # Pops the last '8'

# Explanation of the Code:
# push method:

# Pushes a single element x as a tuple (1, x). The first element in the tuple is always 1, meaning it is a single occurrence of x.

# push_many method:

# Pushes k occurrences of x as a tuple (k, x). The first element in the tuple indicates how many times x is being pushed. This allows for efficient "batch" pushing of multiple identical values.

# top method:

# Returns the most recently pushed value. This is done by accessing the second element of the top tuple in the stack (self.stack[-1][1]).

# pop method:

# If the top element is a single occurrence ((1, x)), it pops it directly.

# If the top element is multiple occurrences ((k, x)), it decrements k by 1 and updates the stack. It only removes the tuple when k becomes 1, which means there is only one instance of x left.

#Example Output:
8
4
5
5
4
8
8
8
