# Problem 13: Find the Index of an Element in a List
# Write a Python program that finds the index of a specific element in a list.
def find_index(lst, element):
    return lst.index(element)

lst = [1, 2, 3, 4]
print(find_index(lst, 3))  # Output: 2