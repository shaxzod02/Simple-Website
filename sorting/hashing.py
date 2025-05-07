
# Version 1: Using a set to count distinct elements
def count_distinct(numbers):
    seen = set()  # Create an empty set to store unique elements

    for x in numbers:
        seen.add(x)  # Add each element to the set (duplicates are automatically ignored)

    return len(seen)  # The number of unique elements is the size of the set


# Version 2: Using sorting to count distinct elements manually
def count_distinct(numbers):
    numbers = sorted(numbers)  # Sort the list so duplicates are next to each other
   
    result = 1  # At least one element exists, so start with 1
    for i in range(1, len(numbers)):
        if numbers[i] != numbers[i - 1]:  # If current is different from the previous
            result += 1  # It's a new distinct value, increase the count

    return result  # Return the total count of distinct elements
