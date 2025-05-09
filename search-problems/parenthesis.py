import itertools

# Function to count all valid sequences of parentheses of length 'n'
def count_sequences(n):
    count = 0  # Initialize a variable to count the valid sequences
    # itertools.product generates all combinations of "(" and ")" repeated 'n' times
    for sequence in itertools.product("()", repeat=n):
        # Check if the current sequence is valid
        if valid_sequence(sequence):
            count += 1  # Increment the count if the sequence is valid
    return count  # Return the total number of valid sequences

# Function to check if a sequence of parentheses is valid
def valid_sequence(sequence):
    depth = 0  # Initialize the depth to 0, representing balance of parentheses
    # Iterate through each character (parenthesis) in the sequence
    for bracket in sequence:
        if bracket == "(":
            depth += 1  # Increase depth when encountering an open parenthesis
        if bracket == ")":
            depth -= 1  # Decrease depth when encountering a closing parenthesis
        if depth < 0:
            # If depth goes below zero, it means there are more closing than opening parentheses,
            # so the sequence is invalid
            return False
    # After iterating through all the parentheses, check if depth is zero
    # A valid sequence must have equal opening and closing parentheses
    return depth == 0
