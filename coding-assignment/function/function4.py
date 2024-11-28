#  Problem 4: Write a function to count the number of vowels in a string.
# The function should take a string as an argument and return the count of vowels (a, e, i, o, u).
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

print(count_vowels("hello world"))  # Output: 3