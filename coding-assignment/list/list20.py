# Problem 20: Find the Common Elements Between Two Lists
# Write a Python program that finds the common elements between two lists.
def common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

lst1 = [1, 2, 3, 4]
lst2 = [3, 4, 5, 6]
print(common_elements(lst1, lst2))