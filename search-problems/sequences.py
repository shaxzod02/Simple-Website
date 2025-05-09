
import itertools

for repetition in itertools.product([1, 2, 3], repeat=2):
    print(repetition)

(1, 1)
(1, 2)
(1, 3)
(2, 1)
(2, 2)
(2, 3)
(3, 1)
(3, 2)
(3, 3)

import itertools

for permutation in itertools.permutations([1, 2, 3]):
    print(permutation)

(1, 2, 3)
(1, 3, 2)
(2, 1, 3)
(2, 3, 1)
(3, 1, 2)
(3, 2, 1)

import itertools

for combination in itertools.combinations([1, 2, 3, 4], 2):
    print(combination)

(1, 2)
(1, 3)
(1, 4)
(2, 3)
(2, 4)
(3, 4)

# ✅ Overview of the Three Functions:
# 1. itertools.product(..., repeat=n)
# Cartesian product with repetition.

# Example: [1, 2, 3] with repeat=2 → all possible ordered pairs.

# Total results: 
# 3
# 2
# =
# 9
# 3 
# 2
#  =9

# 2. itertools.permutations(iterable)
# Generates all possible ordered arrangements without repetition.

# [1, 2, 3] → 
# 3
# !
# =
# 6
# 3!=6 permutations.

# 3. itertools.combinations(iterable, r)
# Generates all unordered selections of r elements without repetition.

# [1, 2, 3, 4], r = 2 → 
# (
# 4
# 2
# )
# =
# 6
# ( 
# 2
# 4
# ​
#  )=6 combinations.