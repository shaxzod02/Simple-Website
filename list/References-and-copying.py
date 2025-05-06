a = [1, 2, 3, 4]
b = a              # b points to the same list as a
a.append(5)

print(a)  # [1, 2, 3, 4, 5]
print(b)  # [1, 2, 3, 4, 5] → b is also affected since it refers to the same list

a = [1, 2, 3, 4]
b = a.copy()       # b is now a separate copy of a
a.append(5)

print(a)  # [1, 2, 3, 4, 5]
print(b)  # [1, 2, 3, 4] → b is not changed

# This version modifies the original list
def double(numbers):
    result = numbers  # result refers to the same list
    for i in range(len(result)):
        result[i] *= 2
    return result

numbers = [1, 2, 3, 4]
print(double(numbers))  # [2, 4, 6, 8]
print(numbers)          # [2, 4, 6, 8] → original list was changed

# This version returns a new modified list without changing the original
def double(numbers):
    result = numbers.copy()  # make a copy to avoid changing the original
    for i in range(len(result)):
        result[i] *= 2
    return result

numbers = [1, 2, 3, 4]
print(double(numbers))  # [2, 4, 6, 8]
print(numbers)          # [1, 2, 3, 4] → original list is safe

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(numbers[2:6])  # [3, 4, 5, 6] → slice from index 2 to 5 (6 is not included)

result = numbers.copy()  # makes a copy of the list
result = numbers[:]      # another way to copy using slicing

first = [1, 2, 3, 4]
second = [5, 6, 7, 8]
print(first + second)  # [1, 2, 3, 4, 5, 6, 7, 8] → concatenates the lists


#| Operation            | Example                | Description                          |
#| -------------------- | ---------------------- | ------------------------------------ |
#| Assignment           | `b = a`                | Both `a` and `b` point to same list  |
#| Shallow Copy         | `b = a.copy()` / `[:]` | Create a new list with same elements |
#| Modify original list | In-place               | Changes original list                |
#| Avoid modification   | `copy()` before edit   | Protect original list                |
#| Slicing              | `list[2:5]`            | Get elements from index 2 to 4       |
#| Concatenation        | `a + b`                | Combine two lists                    |
