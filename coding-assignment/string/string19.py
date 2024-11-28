# Problem 19: Remove All Non-Alphabetic Characters from a String
# Write a Python program that removes all non-alphabetic characters from a string.


def remove_non_alpha(s):
    return ''.join([char for char in s if char.isalpha()])

string = "hello123!"
print(remove_non_alpha(string))  # Output: 'hello'