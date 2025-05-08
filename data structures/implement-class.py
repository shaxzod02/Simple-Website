#Problem:
class Stack:
    stack = []  # ⚠️ Class variable — shared by all instances

#So when you do:
a = Stack()
b = Stack()
a.push(1)
b.push(2)
print(a.top())  # Prints 2, because both use the same shared list

#✅ Fix: Use an instance variable instead

class Stack:
    def __init__(self):
        self.stack = []  # ✅ Instance variable

    def push(self, x):
        self.stack.append(x)

    def top(self):
        return self.stack[-1]

    def pop(self):
        self.stack.pop()

a = Stack()
b = Stack()
a.push(1)
b.push(2)
print(a.top())  # 1 ✅
print(b.top())  # 2 ✅
