# Problem 10: Slice a Tuple
# Write a Python program to slice a tuple and return a part of it (from index 1 to 3).
def slice_tuple(tup):
    return tup[1:4]

tup = (10, 20, 30, 40, 50)
print(slice_tuple(tup))  # Output: (20, 30, 40)
