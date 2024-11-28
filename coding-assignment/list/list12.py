# Problem 12: Check if an Element Exists in a List
# Write a Python program that checks if a specific element exists in a list.
def element_exists(lst, element):
    return element in lst

lst = [1, 2, 3, 4]
print(element_exists(lst, 3))  # Output: True
print(element_exists(lst, 5))  # Output: False
