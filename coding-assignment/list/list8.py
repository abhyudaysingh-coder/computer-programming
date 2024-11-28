# Problem 8: Append an Element to a List
# Write a Python program that appends an element to the end of a list.
def append_element(lst, element):
    lst.append(element)
    return lst

lst = [1, 2, 3]
print(append_element(lst, 4))  # Output: [1, 2, 3, 4]