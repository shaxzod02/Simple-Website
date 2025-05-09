def count_sequences(n, d=0):
    # Base case: If the depth 'd' is out of bounds (negative or more than n), return 0.
    # This means the parentheses are unbalanced.
    if d < 0 or d > n:
        return 0
    
    # Base case: If there are no more parentheses to process (n == 0), 
    # and the depth is 0, it means we have a valid sequence, so return 1.
    if n == 0:
        return 1 if d == 0 else 0
    
    # Recursive case:
    # - If we add an opening parenthesis, we increase the depth ('d + 1').
    # - If we add a closing parenthesis, we decrease the depth ('d - 1').
    return count_sequences(n - 1, d + 1) + count_sequences(n - 1, d - 1)

# Explanation:
# count_sequences(n, d=0): This is a recursive function that counts the valid sequences of parentheses for a given number of parentheses n. The d parameter tracks the depth or balance of parentheses.

# Key Points:
# Base Cases:

# If the depth d goes below 0 (more closing than opening parentheses) or if d exceeds n (too many opening parentheses), it returns 0 because the sequence is invalid.

# If n == 0 and d == 0, it returns 1 because we have successfully balanced the parentheses, and we reached a valid configuration.

# Recursive Step:

# The function calls itself twice:

# One call simulates adding an opening parenthesis ( (incrementing the depth d + 1).

# The other simulates adding a closing parenthesis ) (decrementing the depth d - 1).

# The sum of the two recursive calls represents the total valid sequences for the current state.

# Example Usage:
# If you call count_sequences(4), this will compute the number of valid parentheses sequences of length 4.

# For example:

# count_sequences(2, 0) would return 1, corresponding to the valid sequence ().