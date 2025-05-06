
#Version 1: Brute-force – O(n²)
def count_ways(bits):
    n = len(bits)
    result = 0
    # Iterate over all possible i positions
    for i in range(n):
        # Iterate over all j > i positions
        for j in range(i + 1, n):
            # Check if we have a '0' at i and '1' at j
            if bits[i] == '0' and bits[j] == '1':
                result += 1  # Count this valid pair
    return result


#Version 2: Optimized – O(n)
def count_ways(bits):
    n = len(bits)
    result = 0
    zeros = 0  # Count of '0's seen so far
    for i in range(len(bits)):
        if bits[i] == '0':
            zeros += 1  # Increase zero count
        if bits[i] == '1':
            result += zeros  # For each '1', add all previous '0's
    return result

