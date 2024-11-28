# Problem 2: Check if a String is Palindrome
# Write a Python program that checks if a given string is a palindrome.
def is_palindrome(s):
    return s == s[::-1]

string = "madam"
print(is_palindrome(string))  # Output: True