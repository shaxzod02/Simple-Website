#Version 1: Full slicing sums – O(n²)
def count_splits(numbers):
    n = len(numbers)
    result = 0
    for i in range(n - 1):
        left_sum = sum(numbers[0:i+1])      # Sum of elements from start to i
        right_sum = sum(numbers[i+1:])      # Sum of elements from i+1 to end
        if left_sum == right_sum:           # Check if both sides are equal
            result += 1                     # Count this valid split
    return result

#Version 2: Incremental left sum – still O(n²)
def count_splits(numbers):
    n = len(numbers)
    result = 0
    left_sum = 0
    for i in range(n - 1):
        left_sum += numbers[i]              # Keep running sum from the left
        right_sum = sum(numbers[i+1:])      # Still recalculating right side fully
        if left_sum == right_sum:           # Compare left and right sums
            result += 1
    return result

#Version 3: Fully optimized – O(n)

def count_splits(numbers):
    n = len(numbers)
    result = 0
    left_sum = 0
    total_sum = sum(numbers)               # Compute total sum once
    for i in range(n - 1):
        left_sum += numbers[i]             # Incrementally build left sum
        right_sum = total_sum - left_sum   # Derive right sum
        if left_sum == right_sum:          # Check for valid split
            result += 1
    return result

#| Version | Description              | Time Complexity |
#| ------- | ------------------------ | --------------- |
#| 1       | Recalculates both sums   | O(n²)           |
#| 2       | Optimized left sum       | O(n²)           |
#| 3 ✅     | Uses total sum for speed | O(n)            |


