#✅ Version 1: Using .index() to find positions of numbers
def count_rounds(numbers):
    n = len(numbers)  # Get the length of the numbers list
    
    rounds = 1  # Start with 1 round as the initial assumption
    for i in range(1, n):  # Iterate through the list from index 1
        # Find the positions of i and i + 1 in the list using `.index()`
        if numbers.index(i + 1) < numbers.index(i):  # Check if the next number appears before the current one
            rounds += 1  # If so, increment the round counter
            
    return rounds  # Return the total number of rounds

#✅ Version 2: Using a dictionary to store positions of numbers
def count_rounds(numbers):
    n = len(numbers)  # Get the length of the numbers list
    
    pos = {}  # Create a dictionary to store the position of each number
    for i, x in enumerate(numbers):
        pos[x] = i  # Map each number to its position in the list
        
    rounds = 1  # Start with 1 round as the initial assumption
    for i in range(1, n):  # Iterate through the list from index 1
        # Compare the positions of i and i + 1 using the dictionary `pos`
        if pos[i + 1] < pos[i]:  # If the next number appears before the current one
            rounds += 1  # Increment the round counter

    return rounds  # Return the total number of rounds

#| Version | Approach                             | Key Points                                                   |
#| ------- | ------------------------------------ | ------------------------------------------------------------ |
#| 1       | Uses `.index()` to find positions    | Simpler but less efficient (O(n) for each `.index()` call)   |
#| 2       | Uses a dictionary to store positions | More efficient, O(1) lookups for positions in the dictionary |
