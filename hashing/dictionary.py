#✅ Dictionary – basic usage
weights = {}

weights["apina"] = 100       # Add key "apina" with value 100
weights["banaani"] = 1       # Add key "banaani" with value 1
weights["cembalo"] = 500     # Add key "cembalo" with value 500
weights = {"apina": 100, "banaani": 1, "cembalo": 500}
# Equivalent to the previous block – initializing with values directly

#✅ Accessing and modifying dictionary values
print(weights["apina"])  # 100 - Access the value for key "apina"

weights["apina"] = 150   # Update value for "apina"
print(weights["apina"])  # 150 - Now the value is updated

#✅ Checking if key exists in a dictionary
print("apina" in weights)   # True - Key exists
print("ananas" in weights)  # False - Key doesn't exist

#✅ Deleting a key-value pair
print(weights)               # {'apina': 100, 'banaani': 1, 'cembalo': 500}
del weights["banaani"]       # Remove the key "banaani"
print(weights)               # {'apina': 100, 'cembalo': 500}

#✅ Using a dictionary as a set (with boolean values)
seen = {}
for x in items:
    seen[x] = True

#✅ Using actual set instead
seen = set()
for x in items:
    seen.add(x)

#✅ Counting frequency of items using dictionary
count = {}
for x in items:
    if x not in count:
        count[x] = 0     # Initialize count for new item
    count[x] += 1        # Increment count

#✅ Tracking last position/index of each item
pos = {}
for i, x in enumerate(items):
    pos[x] = i           # Store the latest position of each item

#| Purpose                 | Structure Used  | Example                           |
#| ----------------------- | --------------- | --------------------------------- |
#| Key-value storage       | `dict`          | `weights["key"] = val`            |
#| Unique item tracking    | `set` or `dict` | `seen.add(x)` or `seen[x] = True` |
#| Counting frequencies    | `dict`          | `count[x] += 1`                   |
#| Storing index positions | `dict`          | `pos[x] = i`                      |

