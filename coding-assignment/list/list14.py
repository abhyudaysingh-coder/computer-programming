# Problem 14: Sort a List
# Write a Python program that sorts a list in ascending order.
def sort_list(lst):
    lst.sort()
    return lst

lst = [4, 2, 1, 3]
print(sort_list(lst))  # Output: [1, 2, 3, 4]