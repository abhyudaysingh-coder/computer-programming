# Problem 9: Insert an Element at a Specific Position in a List
# Write a Python program that inserts an element at a specific position in a list.
def insert_element(lst, index, element):
    lst.insert(index, element)
    return lst

lst = [1, 2, 3, 4]
print(insert_element(lst, 2, 10))  # Output: [1, 2, 10, 3, 4]