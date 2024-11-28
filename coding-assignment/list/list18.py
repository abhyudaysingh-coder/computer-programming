# Problem 18: Remove All Duplicates from a List
# Write a Python program that removes all duplicates from a list.
def remove_duplicates(lst):
    return list(set(lst))

lst = [1, 2, 3, 1, 4, 2]
print(remove_duplicates(lst))  # Output: [1, 2, 3, 4]