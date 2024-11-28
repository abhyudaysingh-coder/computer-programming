# Problem 2: Check if a List is Palindrome
# Write a Python program that checks if a given list is a palindrome.
def is_palindrome(lst):
    return lst == lst[::-1]

lst = [1, 2, 3, 2, 1]
print(is_palindrome(lst))  # Output: True