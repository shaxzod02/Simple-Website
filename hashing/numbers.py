#✅ Version 1: Using a list to track seen elements
def count_distinct(numbers):
    seen = []  # Create an empty list to store unique elements
    for x in numbers:
        if x not in seen:  # Check if the element is not already in the list
            seen.append(x)  # Add it if it's new
    return len(seen)  # Return the count of unique elements
#This method works but is less efficient – x not in seen is O(n).

#✅ Version 2: Using a set for faster lookup
def count_distinct(numbers):
    seen = set()  # Use a set to store unique elements (faster lookup)
    for x in numbers:
        if x not in seen:  # Check if element is new
            seen.add(x)     # Add new unique element
    return len(seen)       # Return the size of the set
#This is more efficient – checking membership in a set is O(1) on average.

#✅ Version 3: Simplified – always add to set
def count_distinct(numbers):
    seen = set()        # Initialize an empty set
    for x in numbers:
        seen.add(x)     # Add the element (duplicates are ignored automatically)
    return len(seen)    # Return how many unique values were added

#✅ Version 4: One-liner using set() directly
def count_distinct(numbers):
    return len(set(numbers))  # Convert list to set and count unique elements

#| Version | Approach       | Efficiency | Comment                              |
#| ------- | -------------- | ---------- | ------------------------------------ |
#| 1       | List-based     | Slow       | `O(n^2)` in worst case               |
#| 2       | Set with check | Fast       | Efficient, safe approach             |
#| 3       | Set, no check  | Faster     | Even cleaner, thanks to set behavior |
#| 4       | One-liner      | Fastest    | Pythonic and concise                 |

