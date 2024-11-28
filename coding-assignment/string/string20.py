# Problem 20: Check if a String Starts with a Given Prefix
# Write a Python program that checks if a string starts with a given prefix.


def starts_with(s, prefix):
    return s.startswith(prefix)

string = "hello world"
print(starts_with(string, "hello")) 