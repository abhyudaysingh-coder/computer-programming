# Problem 13: Extract a Substring from a String
# Write a Python program that extracts a substring from a string.


def extract_substring(s, start, end):
    return s[start:end]

string = "hello world"
print(extract_substring(string, 0, 5))  # Output: 'hello'