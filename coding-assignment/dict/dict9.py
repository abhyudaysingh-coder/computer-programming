# Problem 9: Merge Two Dictionaries
# Write a Python program to merge two dictionaries into one.
def merge_dicts(d1, d2):
    d1.update(d2)
    return d1

d1 = {"name": "Tom", "age": 50}
d2 = {"city": "Rome", "country": "Italy"}
print(merge_dicts(d1, d2))  # Output: {'name': 'Tom', 'age': 50, 'city': 'Rome', 'country': 'Italy'}
