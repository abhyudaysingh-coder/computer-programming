# Problem 8: Remove Whitespaces from a String
# Write a Python program to remove leading and trailing whitespaces from a string.


def remove_whitespaces(s):
    return s.strip()

string = "  hello  "
print(remove_whitespaces(string))  # Output: 'hello'