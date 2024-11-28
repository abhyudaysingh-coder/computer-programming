# Problem 3: Count Vowels in a String
# Write a Python program that counts the number of vowels in a given string.
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

string = "hello"
print(count_vowels(string))  # Output: 2