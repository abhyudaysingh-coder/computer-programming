# Problem 16: Join a List of Strings into a Single String
# Write a Python program that joins a list of strings into a single string.

def join_strings(lst):
    return " ".join(lst)

words = ["hello", "world"]
print(join_strings(words))  # Output: 'hello world'