
# Explanation of Code:
# __init__ method:

# Initializes an empty dictionary self.count to keep track of how many times each number has appeared.

# Initializes self.status as a tuple (0, 0), where the first element of the tuple represents the highest frequency count seen so far, and the second element is the corresponding value.

# add method:

# If the number x is not in the dictionary self.count, it initializes the count for x to 0.

# Then, it increments the count for x.

# After updating the count, the method updates self.status by checking if the current number's frequency is greater than the current maximum frequency. It uses max to ensure self.status always holds the number with the highest frequency and its corresponding count.

# mode method:

# Simply returns the second element of self.status, which holds the mode (the most frequent element).

#Code Example and Output:
m = Mode()
m.add(1)
m.add(1)
m.add(2)
print(m.mode()) # 1
m.add(2)
m.add(2)
print(m.mode()) # 2
