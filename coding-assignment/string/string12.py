# Problem 12: Find the First Occurrence of a Character
# Write a Python program that finds the first occurrence of a character in a string.


def first_occurrence(s, char):
    return s.find(char)

string = "hello"
print(first_occurrence(string, "l"))  # Output: 2