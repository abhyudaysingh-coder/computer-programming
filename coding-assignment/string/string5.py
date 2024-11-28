# Problem 5: Count Occurrences of a Substring
# Write a Python program that counts the number of occurrences of a substring in a string.
def count_substring(s, sub):
    return s.count(sub)

string = "hello world, hello"
substring = "hello"
print(count_substring(string, substring))  # Output: 2