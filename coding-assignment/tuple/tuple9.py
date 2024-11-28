# Problem 9: Count Occurrences of an Element in a Tuple
# Write a Python program to count how many times an element appears in a tuple.
def count_occurrences(tup, element):
    return tup.count(element)

tup = (1, 2, 2, 3, 4, 2, 5)
print(count_occurrences(tup, 2))  # Output: 3
