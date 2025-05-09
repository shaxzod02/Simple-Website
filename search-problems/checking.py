# Example:
# For x = 8 with coins [1, 4, 5]:

# Greedy Approach: The greedy approach will first try to subtract the largest coin, which is 5. So, for x = 8, it subtracts 5 (leaving 3), then subtracts 3 using the coin 1, resulting in a total of 4 coins (5 + 1 + 1 + 1).

# Brute Force Approach: The brute force method explores all combinations and finds that the optimal solution for x = 8 is using two coins (4 + 4), which results in only 2 coins.

# Why the Greedy Approach Fails:
# The greedy algorithm is designed to pick the largest possible coin at each step, which can be suboptimal in certain cases. In this scenario, for x = 8, it picks 5, then tries to subtract the remaining 3 with 1s, but there is a better combination: two 4 coins.

# Correct Approach: Dynamic Programming
# The brute force approach works by examining all possible combinations of coins to ensure the minimal number of coins is used, but it is inefficient, especially for large values of x.

# A more efficient and always correct approach is dynamic programming, which guarantees finding the minimum number of coins by considering the subproblems of smaller amounts and combining them optimally. Here’s how you can implement this approach:

# Dynamic Programming Solution:
def find_coins_dp(x, coins):
    dp = [float('inf')] * (x + 1)  # Initialize the dp table with infinity
    dp[0] = 0  # Base case: 0 coins needed to make amount 0

    for amount in range(1, x + 1):
        for coin in coins:
            if amount >= coin:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[x] if dp[x] != float('inf') else -1  # Return the result if possible

coins = [1, 4, 5]

x = 1
while True:
    result_brute = find_coins_brute(x)
    result_greedy = find_coins_greedy(x)
    result_dp = find_coins_dp(x, coins)

    if result_brute != result_greedy or result_greedy != result_dp:
        print(f"Different answer for {x} coins")
        print(f"Brute: {result_brute}, Greedy: {result_greedy}, DP: {result_dp}")
        break

    x += 1

# Explanation of the Dynamic Programming Approach:
# dp[i] represents the minimum number of coins needed to make the amount i.

# We initialize dp[0] = 0 because no coins are needed to make 0.

# For each possible amount from 1 to x, we check all coins and update dp[amount] with the minimum number of coins needed to make that amount.

# The final result is found in dp[x].

# Why Dynamic Programming Works:
# It considers all possibilities and ensures the optimal solution by solving smaller subproblems.

# Unlike the greedy approach, it doesn't make a locally optimal choice (like always picking the largest coin), ensuring the globally optimal solution.

# Example Output:
Different answer for 8 coins
Brute: 2, Greedy: 4, DP: 2
