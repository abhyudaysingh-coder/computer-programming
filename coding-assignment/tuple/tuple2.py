# Problem 2: Access Tuple Elements
# Write a Python program to access elements of a tuple and print the second and fourth elements.
def access_elements(tup):
    return tup[1], tup[3]

tup = (10, 20, 30, 40, 50)
print(access_elements(tup))  # Output: (20, 40)
