
# Search Problems

Search problems are a core part of algorithm design. They involve finding one or more solutions from a large space of possibilities, often under specific constraints. This chapter explores key techniques such as iteration, ordering, greedy strategies, and validation methods for solving these problems efficiently.

---

## Iterating Solutions

Brute-force (exhaustive) search involves iterating over all possible candidates and checking each for validity. This is straightforward but can be slow for large input spaces.

### Example: Finding all subsets of a list:
```python
from itertools import combinations

data = [1, 2, 3]
for r in range(len(data)+1):
    for subset in combinations(data, r):
        print(subset)
```

## Orderings
Many problems become easier when candidates are considered in a specific order, such as:

Lexicographical order

Increasing/decreasing numerical order

Priority based on a heuristic (as used in greedy algorithms)

Ordering can significantly reduce the search space or help reach a solution faster.

## Balanced Parenthesis
A classic search problem is generating or validating balanced parenthesis expressions. A string of parentheses is balanced if each opening has a corresponding closing bracket and they are properly nested.

### Example of checking balanced parenthesis:
```python
def is_balanced(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return not stack
```

## Speeding up the Search
Several techniques can improve search performance:

Pruning: Skip unnecessary branches in the search tree.

Memoization: Cache intermediate results to avoid redundant work.

Early stopping: End the search once a solution is found.

## Greedy Algorithms
Greedy algorithms make locally optimal choices at each step with the hope of reaching a globally optimal solution. They're efficient but not always correct.

### Example: Coin change with greedy method:
```python
def greedy_change(coins, target):
    result = []
    for coin in sorted(coins, reverse=True):
        while target >= coin:
            target -= coin
            result.append(coin)
    return result if target == 0 else None
```
Note: This works when the coin system is canonical, but fails in some cases (e.g. coins 
= [1, 3, 4], target = 6).

## Why the Algorithm is Correct?
To ensure an algorithm's correctness:

Prove that it always finds a valid solution.

Show that no better solution exists (optimality).

Use loop invariants or induction to validate behavior at every step.

## Algorithm Checking
Algorithm checking involves writing tests and validations to ensure output correctness. Techniques include:

Comparing to brute-force or naive solutions.

Cross-validation with random inputs.

Asserting known invariants in the algorithm.

### Example:
```python
assert greedy_change([1, 3, 4], 6) == [3, 3]  # May fail, showing the greedy choice is not optimal
```




