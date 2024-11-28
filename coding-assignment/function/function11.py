# Problem 11: Write a function to remove duplicates from a list.
# The function should take a list as an argument and return the list without duplicates.
def remove_duplicates(lst):
    return list(set(lst))

print(remove_duplicates([1, 2, 2, 3, 4, 4]))  # Output: [1, 2, 3, 4]