import random
import time

# Most efficient version: max - min
def max_diff(numbers):
    return max(numbers) - min(numbers)

# Generate test list
n = 1000
print("n:", n)
random.seed(1337)
numbers = [random.randint(1, 10**6) for _ in range(n)]

# Measure execution time
start_time = time.time()
result = max_diff(numbers)
end_time = time.time()

# Show result and timing
print("result:", result)
print("time:", round(end_time - start_time, 2), "s")
