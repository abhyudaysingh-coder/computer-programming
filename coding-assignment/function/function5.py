# Problem 5: Write a function to check if a string is a palindrome.
# The function should take a string as an argument and return True if the string is a palindrome, otherwise False.
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam"))  # Output: True
print(is_palindrome("hello"))  # Output: False
