# Problem 14: Convert First Character of Each Word to Uppercase
# Write a Python program that converts the first character of each word in a string to uppercase.

def capitalize_words(s):
    return s.title()

string = "hello world"
print(capitalize_words(string))  # Output: 'Hello World'