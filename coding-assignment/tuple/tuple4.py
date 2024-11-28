# Problem 4: Check if an Element Exists in a Tuple
# Write a Python program to check if a specific element exists in a tuple.
def element_exists(tup, element):
    return element in tup

tup = (1, 2, 3, 4, 5)
print(element_exists(tup, 3))  # Output: True
print(element_exists(tup, 6))  # Output: False