# Your function count_orders(n) is counting all permutations of the numbers 1 through n such that no two adjacent numbers differ by 1. These are known as permutations with restricted adjacent differences.

# The function valid_order(order) ensures that no adjacent elements have a difference of 1, i.e.:
if abs(order[i] - order[i + 1]) == 1:
    return False

# This filters out permutations like (1, 2, 3) or (3, 2, 1) where neighbors like (2, 3) differ by 1.

# Example Output for n = 4:
# Valid permutations:

# (2, 4, 1, 3)

# (3, 1, 4, 2)

# Tips for Improvement:
# Move items = range(1, n + 1) into the function so it's self-contained.

# You can also return the list of valid orders if you're interested in inspecting or processing them further.

# Optional Refactored Version:
import itertools

def valid_order(order):
    return all(abs(order[i] - order[i+1]) != 1 for i in range(len(order) - 1))

def count_orders(n):
    items = range(1, n + 1)
    valid = [order for order in itertools.permutations(items) if valid_order(order)]
    return len(valid), valid

count, orders = count_orders(4)
print(f"Count: {count}")
for order in orders:
    print(order)
