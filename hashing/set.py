
#Creating and using sets
numbers = set()

numbers.add(1)
numbers.add(2)
numbers.add(3)

print(numbers)  # {1, 2, 3} - Set contains unique values only

#set() creates an empty set. You can add elements using .add(). Duplicates are automatically ignored.

# Creating set from a list
numbers = set([1, 2, 3])
print(numbers)  # {1, 2, 3}
#You can also initialize a set directly from a list.

#Membership checking in a set
print(3 in numbers)  # True
print(4 in numbers)  # False
#in checks whether a value exists in the set. It's very fast – O(1) on average.

#Removing elements from a set
print(numbers)     # {1, 2, 3}
numbers.remove(2)
print(numbers)     # {1, 3}
#.remove() deletes the specified element. If it doesn't exist, it raises an error.

#❌ Indexing sets (invalid operation)
numbers = [1, 2, 3]
print(numbers[1])  # 2 - Lists support indexing

numbers = set([1, 2, 3])
print(numbers[1])  # ❌ TypeError: 'set' object is not subscriptable
#Sets are unordered → you can't use indexes like set[1].

#✅ Duplicates in list vs set
numbers = []
numbers.append(5)
numbers.append(5)
numbers.append(5)
print(numbers)  # [5, 5, 5] - List allows duplicates
#Lists allow duplicates and preserve the order of insertion.
numbers = set()
numbers.add(5)
numbers.add(5)
numbers.add(5)
print(numbers)  # {5} - Set stores only one unique copy
#Sets store only unique values – duplicates are ignored.

#| Feature           | List (`[]`)        | Set (`set()`)       |
#| ----------------- | ------------------ | ------------------- |
#| Ordered           | ✅ Yes              | ❌ No (unordered)    |
#| Allows Duplicates | ✅ Yes              | ❌ No (unique only)  |
#| Indexable         | ✅ Yes (e.g. `[0]`) | ❌ No                |
#| Fast lookup       | ❌ Linear (`O(n)`)  | ✅ Constant (`O(1)`) |

