def count_lists(numbers):
    n = len(numbers)
    a = b = -1           # a: start index of current run, b: start of previous run
    result = 0           # This will hold the total count of valid sublists

    for i in range(1, n):
        # Check if current element is different from the previous one
        if numbers[i] != numbers[i - 1]:
            # If current element is different from the one at position a,
            # it means we're starting a new run after a different run
            if numbers[i] != numbers[a]:
                b = a    # Move b to a: track start of the previous different run
            a = i - 1    # Start of new run is previous index (i - 1)
        
        # For each position i, add the distance between a and b to the result
        result += a - b

    return result

numbers = [1, 2, 1, 2]

