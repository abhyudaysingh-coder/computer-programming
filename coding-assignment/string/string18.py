# Problem 18: Find the Last Occurrence of a Character
# Write a Python program that finds the last occurrence of a character in a string.


def last_occurrence(s, char):
    return s.rfind(char)

string = "hello world"
print(last_occurrence(string, "o"))  # Output: 7