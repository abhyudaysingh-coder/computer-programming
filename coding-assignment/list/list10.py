# Problem 10: Remove an Element from a List by Value
# Write a Python program that removes an element from a list by value.
def remove_element(lst, element):
    lst.remove(element)
    return lst

lst = [1, 2, 3, 4]
print(remove_element(lst, 3))  # Output: [1, 2, 4]