# Problem 6: Repeat a Tuple
# Write a Python program to repeat a tuple a given number of times.
def repeat_tuple(tup, n):
    return tup * n

tup = (1, 2, 3)
print(repeat_tuple(tup, 3))  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)