
# 10. Dynamic Programming

Dynamic Programming (DP) is a powerful algorithmic technique for solving optimization and counting problems by breaking them into overlapping subproblems and solving each subproblem only once.

---

## 10.1 Finding the Optimal Solution

DP helps to find the best (maximum/minimum) value for a problem by solving subproblems and combining their solutions.

Example: Maximum sum of non-adjacent numbers in a list.
```python
def max_sum(nums):
    if not nums: return 0
    prev, curr = 0, 0
    for x in nums:
        prev, curr = curr, max(curr, prev + x)
    return curr
```

## Constructing an Optimal Solution
After computing the value of an optimal solution, we can reconstruct the actual choices made.

Example: Reconstructing chosen items in the 0/1 knapsack problem by tracing back from the DP table.

## Counting Solutions
DP can also be used to count how many solutions exist.

Example: Count number of ways to climb n steps using 1 or 2 steps at a time.
```python
def count_ways(n):
    dp = [0] * (n + 2)
    dp[0] = 1
    for i in range(n):
        dp[i+1] += dp[i]
        dp[i+2] += dp[i]
    return dp[n]
```

## Subsequences
DP is often used in string and sequence problems, like finding the longest common subsequence (LCS).

Example:
```python
def lcs(a, b):
    dp = [[0]*(len(b)+1) for _ in range(len(a)+1)]
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
    return dp[-1][-1]
```

## Balanced Parenthesis
Balanced parenthesis problems can also be solved with DP, for example, counting the number of valid expressions using Catalan numbers.
```python
def catalan(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(i):
            dp[i] += dp[j] * dp[i - j - 1]
    return dp[n]
```

## Nested Recursion
Nested recursive problems, like computing values where subproblems depend on each other in a tree-like structure, can often be optimized using memoization or DP.

Example: Ackermann-style recursive problems with caching.