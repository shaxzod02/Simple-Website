
#  Sorting

Sorting is a fundamental operation in computer science used to arrange data in a particular order, typically ascending or descending. Efficient sorting allows for faster searching, merging, and data organization.

##  Sorting in Python

Python provides a built-in `sorted()` function and the `list.sort()` method, both of which use the efficient Timsort algorithm. These allow sorting of lists and other iterable data types easily.

Example:
```python
numbers = [4, 1, 3, 2]
numbers.sort() 
        # In-place sorting
# or
sorted_numbers = sorted(numbers)
```
  

### Smallest Difference
A common problem that benefits from sorting is finding the smallest difference between elements in an array. By sorting the array first, comparing adjacent pairs becomes efficient.
```python
numbers = [5, 2, 9, 1]
numbers.sort()
min_diff = min(b - a for a, b in zip(numbers, numbers[1:]))
```
## Hashing vs. Sorting
Hashing is typically faster for operations like membership testing (x in set) and counting. However, sorting is better for ordered operations, such as finding minimum differences or working with ranges.

## More about Sorting
There are many classical sorting algorithms:

Bubble Sort (slow, educational)

Selection Sort

Insertion Sort

Merge Sort

Quick Sort

Heap Sort

Each has its own time complexity and use cases.

## Restaurant
This problem typically involves sorting customer orders, tables, or times. Sorting makes it easier to manage overlapping schedules, seat assignments, or queue management.

## How is Sorting Done?
Under the hood, efficient sorting algorithms like Timsort (Python), Merge Sort, or Quick Sort rely on divide-and-conquer techniques to reduce time complexity to O(n log n).

## Sorting in Other Languages
Most modern programming languages have built-in sorting:

Java: Arrays.sort()

C++: std::sort()

JavaScript: array.sort()

Go: sort.Ints()

Each uses optimized internal sorting strategies for performance.
