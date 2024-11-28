# Problem 4: Remove a Key-Value Pair from a Dictionary
# Write a Python program to remove a key-value pair from a dictionary by key.
def remove_key(d, key):
    d.pop(key, None)  # Avoids KeyError if the key doesn't exist
    return d

d = {"name": "Eve", "age": 22, "city": "Berlin"}
print(remove_key(d, "age"))  # Output: {'name': 'Eve', 'city': 'Berlin'}