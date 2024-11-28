# Problem 3: Count Occurrences of an Element in a List
# Write a Python program that counts the number of occurrences of a specific element in a list.
def count_occurrences(lst, element):
    return lst.count(element)

lst = [1, 2, 3, 1, 1, 4]
print(count_occurrences(lst, 1))  # Output: 3