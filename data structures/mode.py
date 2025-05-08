
# Example usage of the Mode class
m = Mode()
m.add(1)           # Add 1 to the data
m.add(1)           # Add 1 again (now appears twice)
m.add(2)           # Add 2 (appears once)
print(m.mode())    # Output the mode (should be 1 since it appears most)

m.add(2)           # Add 2 again (now appears twice)
m.add(2)           # Add 2 again (now appears three times)
print(m.mode())    # Output the mode (should now be 2)


# Mode class to track the most frequent element added
class Mode:
    def __init__(self):
        # Dictionary to store how many times each number has been added
        self.count = {}
        # status keeps the current mode as a tuple: (frequency, value)
        self.status = (0, 0)
        
    def add(self, x):
        # If x hasn't been seen before, initialize its count to 0
        if x not in self.count:
            self.count[x] = 0
        # Increment the count for x
        self.count[x] += 1
        # Update the mode if x has a higher frequency or is larger with the same frequency
        self.status = max(self.status, (self.count[x], x))
        
    def mode(self):
        # Return the current mode (value with highest frequency)
        return self.status[1]

