# Explanation of the Code:
# Initialization:

# The dictionary result is used to store the length of the longest increasing subsequence that ends at each index.

# max_len is used to keep track of the maximum length of any increasing subsequence found so far.

# Outer Loop (i):

# The outer loop iterates over each element in the array items. For each i, the goal is to find the longest increasing subsequence that ends at the index i.

# Inner Loop (j):

# The inner loop compares the current element (items[i]) with all previous elements (items[j]). If items[j] is less than items[i], this means that items[i] can extend the subsequence that ends at items[j]. Thus, the length of the subsequence ending at i is updated.

# result[i] is the maximum of its current value and result[j] + 1 (i.e., extending the subsequence ending at j).

# Updating max_len:

# After processing each element i, we update max_len with the maximum value of result[i].

# Final Result:

# After processing all elements, max_len will contain the length of the longest increasing subsequence.

# Example:
# For the input list [4, 1, 5, 6, 3, 4, 1, 8]:

# The longest increasing subsequence is [1, 3, 4, 8], so the result will be 4.

# Code:
def find_longest(items):
    result = {}

    max_len = 0
    for i in range(len(items)):
        result[i] = 1
        for j in range(i):
            if items[j] < items[i]:
                result[i] = max(result[i], result[j] + 1)
        max_len = max(max_len, result[i])

    return max_len

print(find_longest([4, 1, 5, 6, 3, 4, 1, 8]))  # Output: 4

#Output:
4
# Explanation of Output:
# The longest increasing subsequence is [1, 3, 4, 8], which has a length of 4. Therefore, the function returns 4.

# Time Complexity:
# The time complexity of this solution is O(n^2) because there are two nested loops: one loop over the array (i) and another loop over all previous elements (j), which results in a quadratic time complexity.

# Space Complexity:
# The space complexity is O(n) because we are storing the length of the longest subsequence ending at each index in the result dictionary.