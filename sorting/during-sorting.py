
import functools

# Define a custom comparison function
def cmp(a, b):
    # Print each comparison for debugging or understanding the order
    print("compare", a, b)
    # Return negative if a < b, 0 if equal, positive if a > b
    return a - b

numbers = [4, 1, 3, 2]

# Use functools.cmp_to_key to convert the comparison function to a key function
# This allows Python's sort() to use it, since sort() expects a key function, not cmp directly
numbers.sort(key=functools.cmp_to_key(cmp))

# Print the sorted list
print(numbers)  # Output: [1, 2, 3, 4]
