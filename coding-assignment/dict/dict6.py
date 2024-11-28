# Problem 6: Get All Keys from a Dictionary
# Write a Python program to get all the keys of a dictionary.
def get_keys(d):
    return list(d.keys())

d = {"name": "David", "age": 35, "city": "Madrid"}
print(get_keys(d))  # Output: ['name', 'age', 'city']