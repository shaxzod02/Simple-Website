# Returns the number of even numbers in the given list
def count_even(numbers):
    result = 0
    for x in numbers:
        if x % 2 == 0:  # Check if the number is even
            result += 1
    return result


# Returns the middle element of the list
# For even-length lists, returns the element at n // 2 index
def middle(numbers):
    n = len(numbers)
    return numbers[n // 2]


# Calculates and returns the sum of all elements in the list
def calc_sum(numbers):
    result = 0
    for x in numbers:
        result += x  # Add each element to the total
    return result


# Checks if any two elements in the list add up to the given value x
def has_sum(numbers, x):
    for a in numbers:
        for b in numbers:
            if a + b == x:  # If any pair sums to x, return True
                return True
    return False  # If no such pair found, return False


# Counts how many times the minimum value appears in the list
def count_min(numbers):
    # Stage 1: Find the minimum value in the list
    min_value = numbers[0]
    for x in numbers:
        if x < min_value:
            min_value = x

    # Stage 2: Count how many times the minimum value appears
    result = 0
    for x in numbers:
        if x == min_value:
            result += 1

    return result
