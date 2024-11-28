# Problem 17: Create a List with Range of Numbers
# Write a Python program that creates a list of numbers within a given range.
def create_range_list(start, end):
    return list(range(start, end))

print(create_range_list(1, 5))  # Output: [1, 2, 3, 4]