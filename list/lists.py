numbers = [4, 3, 7, 3, 2]
print(numbers[2])  # 7 → Access the element at index 2 (third element)

numbers[2] = 5     # Change the element at index 2 to 5
print(numbers[2])  # 5 → Now index 2 contains 5

numbers = [4, 3, 7, 3, 2]
print(len(numbers))  # 5 → Length of the list

numbers = [4, 3, 7, 3, 2]

print(3 in numbers)  # True → 3 exists in the list
print(8 in numbers)  # False → 8 does not exist in the list

print(numbers.index(3))   # 1 → Index of the first occurrence of 3
print(numbers.count(3))   # 2 → Number of times 3 appears in the list

# Custom function to count how many times target appears in items
def count(items, target):
    result = 0
    for item in items:
        if item == target:  # Compare each item to the target
            result += 1
    return result

numbers = [1, 2, 3, 4]

numbers.append(5)            # Adds 5 to the end of the list
print(numbers)               # [1, 2, 3, 4, 5]

numbers.insert(1, 6)         # Inserts 6 at index 1 (between 1 and 2)
print(numbers)               # [1, 6, 2, 3, 4, 5]

numbers = [1, 2, 3, 4, 5, 6]

numbers.pop()                # Removes and returns the last element (6)
print(numbers)               # [1, 2, 3, 4, 5]

numbers.pop(1)               # Removes and returns the element at index 1 (2)
print(numbers)               # [1, 3, 4, 5]

numbers = [1, 2, 3, 1, 2, 3]

numbers.remove(3)            # Removes the first occurrence of 3
print(numbers)               # [1, 2, 1, 2, 3]


#| Method         | Description                              | Example            |
#| -------------- | ---------------------------------------- | ------------------ |
#| `append(x)`    | Adds `x` to the end                      | `lst.append(5)`    |
#| `insert(i, x)` | Inserts `x` at index `i`                 | `lst.insert(2, 7)` |
#| `pop()`        | Removes and returns last element         | `lst.pop()`        |
#| `pop(i)`       | Removes and returns element at index `i` | `lst.pop(1)`       |
#| `remove(x)`    | Removes **first** occurrence of `x`      | `lst.remove(3)`    |

