# Example using the list's sort() method which sorts the list in-place (modifies the original list)
numbers = [4, 2, 1, 2]
numbers.sort()  # Sorts the list in ascending order, modifies 'numbers' directly
print(numbers)  # Output: [1, 2, 2, 4]

# Example using the built-in sorted() function which returns a new sorted list (does not modify the original)
numbers = [4, 2, 1, 2]
print(sorted(numbers))  # Output: [1, 2, 2, 4]; 'numbers' remains unchanged
