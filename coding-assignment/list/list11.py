# Problem 11: Remove an Element from a List by Index
# Write a Python program that removes an element from a list by index.
def remove_by_index(lst, index):
    lst.pop(index)
    return lst