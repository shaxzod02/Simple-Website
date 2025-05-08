
def count_queens(n):
    return count(n, 0, [])

def count(n, row, queens):
    if row == n:
        return 1
    result = 0
    for col in range(n):
        attacks = [attack(queen, (row, col)) for queen in queens]
        if not any(attacks):
            result += count(n, row + 1, queens + [(row, col)])
    return result

def attack(queen1, queen2):
    if queen1[0] == queen2[0] or queen1[1] == queen2[1]:
        return True
    if abs(queen1[0] - queen2[0]) == abs(queen1[1] - queen2[1]):
        return True
    return False

print(count_queens(4)) # 2
print(count_queens(8)) # 92

# Breakdown of the Code:
# count_queens(n):

# This function is the main entry point. It starts the process of counting valid queen placements on an n x n board by calling the recursive count function, starting from row 0 and an empty list of queens.

# count(n, row, queens):

# This function recursively places queens row by row.

# Base Case: When row == n, it means all queens have been placed successfully on the board, and the function returns 1, indicating one valid arrangement.

# Recursive Case: For each column in the current row, it checks if placing a queen there would cause any attacks with previously placed queens (from earlier rows). If not, it adds this placement to the list of queens and proceeds to the next row.

# attack(queen1, queen2):

# This function checks if two queens can attack each other:

# Same row: If both queens are in the same row (queen1[0] == queen2[0]).

# Same column: If both queens are in the same column (queen1[1] == queen2[1]).

# Same diagonal: If the absolute difference in their row and column positions is the same (abs(queen1[0] - queen2[0]) == abs(queen1[1] - queen2[1])).

# How the Code Works:
# Recursive Backtracking:

# The code uses a backtracking technique to try placing queens in each row, checking for attacks with previous queens. If a valid position is found, it recursively moves to the next row.

# If a valid arrangement of queens is reached, it adds 1 to the result count.

# Attack Check:

# For each potential position, the function checks if the new queen is attacking any of the previously placed queens (in queens list).

# The list queens holds tuples, where each tuple represents the coordinates of a queen on the board.

# Example Outputs:
# For n = 4 (4x4 chessboard):

# The function finds 2 valid solutions (there are two ways to place 4 queens on a 4x4 board such that no two queens can attack each other).

# The two solutions are:

# Solution 1:
# . Q . .
# . . . Q
# Q . . .
# . . Q .
#Solution 2:
# . . Q .
# Q . . .
# . . . Q
# . Q . .

# Performance Consideration:
# The time complexity of the algorithm is O(n!) because, in the worst case, the function tries to place queens row by row, with each row having n potential placements. This results in n * (n-1) * (n-2) * ... * 1 (which is factorial time).

# However, the backtracking ensures that many invalid placements are pruned early, making it much more efficient than brute force.

# Suggested Improvements:
# Optimization: The attacks list comprehension can be avoided by directly checking each queen's position for attacks without creating a list.

# Space Complexity: The space complexity is primarily O(n), as the recursion stack and the queens list both grow linearly with the number of queens.
