# Problem 8: Find the Index of an Element in a Tuple
# Write a Python program to find the index of a specific element in a tuple.
def find_index(tup, element):
    return tup.index(element)

tup = (10, 20, 30, 40)
print(find_index(tup, 30))  # Output: 2
