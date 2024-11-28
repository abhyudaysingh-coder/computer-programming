# Problem 17: Write a function to find the common elements between two lists.
# The function should take two lists as arguments and return the common elements.
def common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

print(common_elements([1, 2, 3], [2, 3, 4]))  # Output: [2, 3]
