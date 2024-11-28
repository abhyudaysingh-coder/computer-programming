# Problem 3: Add a Key-Value Pair to a Dictionary
# Write a Python program to add a new key-value pair to an existing dictionary.
def add_key_value(d, key, value):
    d[key] = value
    return d

d = {"name": "Bob", "age": 40}
print(add_key_value(d, "city", "Paris"))  # Output: {'name': 'Bob', 'age': 40, 'city': 'Paris'}