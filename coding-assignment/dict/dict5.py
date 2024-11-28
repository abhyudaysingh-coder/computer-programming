# Problem 5: Check if a Key Exists in a Dictionary
# Write a Python program to check if a specific key exists in a dictionary.
def key_exists(d, key):
    return key in d

d = {"name": "Charlie", "age": 28, "city": "Tokyo"}
print(key_exists(d, "age"))  # Output: True
print(key_exists(d, "country"))  # Output: False
