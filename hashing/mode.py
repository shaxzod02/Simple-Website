#✅ Version 1: Track mode with a dictionary and update when necessary
def find_mode(numbers):
    count = {}         # Create a dictionary to store the frequency of each number
    mode = numbers[0] # Assume the first element is the mode initially

    for x in numbers:
        if x not in count:
            count[x] = 0  # If x is not in the dictionary, initialize its count as 0
        count[x] += 1      # Increment the count for x

        # If current count of x is greater than the count of the current mode, update mode
        if count[x] > count[mode]:
            mode = x

    return mode  # Return the most frequent element

#✅ Version 2: Track mode using a tuple to compare frequencies
def find_mode(numbers):
    count = {}        # Create a dictionary to store the frequency of each number
    mode = (0, 0)     # Initialize mode as a tuple with (frequency, number)

    for x in numbers:
        if x not in count:
            count[x] = 0  # Initialize frequency to 0 if not already in dictionary
        count[x] += 1      # Increment the frequency count for number x

        # Update mode with the number that has the highest frequency
        mode = max(mode, (count[x], x))

    return mode[1]  # Return the number with the highest frequency (mode)

#| Version | Approach                              | Key Points                                                          |
#| ------- | ------------------------------------- | ------------------------------------------------------------------- |
#| 1       | **Dictionary** with direct comparison | Updates `mode` directly if the current value has a higher frequency |
#| 2       | **Tuple comparison**                  | Uses a tuple `(frequency, number)` for a clean comparison of mode   |
