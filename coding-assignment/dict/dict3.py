# Problem 2: Access Dictionary Elements by Key
# Write a Python program to access the value of a specific key in a dictionary.
def access_by_key(d, key):
    return d.get(key)

d = {"name": "Alice", "age": 30, "city": "London"}
print(access_by_key(d, "age"))  # Output: 30
print(access_by_key(d, "city"))  # Output: London
