# Returns the maximum absolute difference between any two elements in the list
def max_diff(numbers):
    result = 0
    for x in numbers:
        for y in numbers:
            result = max(result, abs(x - y))  # Compare all pairs
    return result

# Returns the difference between the largest and smallest element using sorting
def max_diff(numbers):
    numbers = sorted(numbers)  # Sort the list
    return numbers[-1] - numbers[0]  # Last - first element after sorting

# Returns the difference between the maximum and minimum elements (fastest way)
def max_diff(numbers):
    return max(numbers) - min(numbers)

