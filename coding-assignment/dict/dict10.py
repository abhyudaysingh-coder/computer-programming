# Problem 10: Get the Number of Items in a Dictionary
# Write a Python program to get the number of key-value pairs in a dictionary.
def num_items(d):
    return len(d)

d = {"name": "Anna", "age": 32, "city": "Los Angeles"}
print(num_items(d))  # Output: 3
