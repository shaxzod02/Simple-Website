# Counts the number of even numbers in a list
# version 1: basic loop
# version 2: using a generator expression with sum()
def count_even1(numbers, version=1):
    if version == 1:
        result = 0
        for x in numbers:
            if x % 2 == 0:  # Check if x is even
                result += 1
        return result
    elif version == 2:
        # This line returns the sum of True values (which are 1s)
        # where each element is checked for evenness
        return sum(x % 2 == 0 for x in numbers)

# Returns the maximum difference between any two elements in the list
# version 1: compares all pairs (slowest)
# version 2: sorts the list and subtracts first from last
# version 3: uses max() and min() functions (most efficient)
def max_diff(numbers, version=1):
    if version == 1:
        result = 0
        for x in numbers:
            for y in numbers:
                result = max(result, abs(x - y))  # Absolute difference between any two elements
        return result
    elif version == 2:
        sorted_1 = sorted(numbers)  # Sort the list
        return sorted_1[-1] - sorted_1[0]  # Difference between max and min after sorting
    elif version == 3:
        # I personally like this one – simple and fast
        return max(numbers) - min(numbers)

# Returns the middle element of the list
# Note: For even-length lists, this returns the element at len // 2
def middle(numbers):
    return numbers[len(numbers) // 2]

# Calculates and returns the sum of all numbers in the list
def calc_sum(numbers):
    result = 0
    for x in numbers:
        result += x  # Add each number to result
    return result

# Checks if any two numbers in the list add up to x
# Returns True if such a pair exists, otherwise False
def has_sum(numbers, x):
    for a in numbers:
        for b in numbers:
            if a + b == x:
                return True
    return False
