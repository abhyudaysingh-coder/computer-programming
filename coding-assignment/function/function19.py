# Problem 19: Write a function to check if a string contains only digits.
# The function should take a string as an argument and return True if it contains only digits, otherwise False.
def is_digit(s):
    return s.isdigit()

print(is_digit("12345"))  # Output: True
print(is_digit("abc123"))  # Output: False