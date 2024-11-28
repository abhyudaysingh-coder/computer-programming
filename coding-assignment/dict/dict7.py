# Problem 7: Get All Values from a Dictionary
# Write a Python program to get all the values of a dictionary.
def get_values(d):
    return list(d.values())

d = {"name": "Zoe", "age": 27, "city": "Moscow"}
print(get_values(d))  # Output: ['Zoe', 27, 'Moscow']
