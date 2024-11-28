# Problem 9: Replace All Occurrences of a Substring
# Write a Python program that replaces all occurrences of a substring with another substring.

def replace_substring(s, old, new):
    return s.replace(old, new)

string = "hello world"
print(replace_substring(string, "world", "everyone"))  # Output: 'hello everyone'