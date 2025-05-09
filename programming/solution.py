# The function min_coins you provided uses dynamic programming to find the minimum number of coins needed to make up a value x using the given coins. Here's a detailed breakdown:

# How the code works:
# Initialization:

# A dictionary result is used where result[s] will store the minimum number of coins needed to make the amount s.

# result[0] = 0 because 0 coins are needed to form the value 0.

# Dynamic Programming Loop:

# For each amount s from 1 to x, it assumes that the minimum coins required is s (i.e., using 1-value coins for all amounts).

# Then, it iterates through all possible coins and updates result[s] with the minimum coins required by considering result[s - c] + 1, where c is the coin being considered. This is because you can subtract a coin value c from s and add 1 coin.

# Example Walkthrough:
# For x = 13 and coins [1, 2, 5]:

# Initially, result = {0: 0, 1: 1, 2: 2, 3: 3, ...}.

# Then, the function loops over all values from 1 to 13, calculating the minimum number of coins for each amount.

# Output:
print(min_coins(13, [1, 2, 5]))  # 4
# Explanation:

# For x = 13, using the coin denominations [1, 2, 5], the minimum number of coins is 4. The optimal combination is [5, 5, 2, 1] (5 + 5 + 2 + 1 = 13).
print(min_coins(13, [1, 4, 5]))  # 3
# Explanation:

# For x = 13, using the coin denominations [1, 4, 5], the minimum number of coins is 3. The optimal combination is [5, 5, 3] (5 + 5 + 3 = 13).
print(min_coins(42, [1, 5, 6, 17]))  # 5
# Explanation:

# For x = 42, using the coin denominations [1, 5, 6, 17], the minimum number of coins is 5. The optimal combination is [17, 17, 6, 1, 1] (17 + 17 + 6 + 1 + 1 = 42).

# Code:
def min_coins(x, coins):
    result = {}
 
    result[0] = 0
    for s in range(1, x + 1):
        result[s] = s  # maximum coins possible is using 1 value coins
        for c in coins:
            if s - c >= 0:
                result[s] = min(result[s], result[s - c] + 1)
 
    return result[x]

print(min_coins(13, [1, 2, 5]))  # 4
print(min_coins(13, [1, 4, 5]))  # 3
print(min_coins(42, [1, 5, 6, 17]))  # 5

# Complexity:
# Time Complexity: O(x * m) where x is the target amount, and m is the number of coins. The algorithm iterates through each amount from 1 to x and for each amount, it checks all the coins.

# Space Complexity: O(x) for storing the result dictionary.
