# Problem 18: Write a function to find the longest word in a sentence.
# The function should take a sentence as an argument and return the longest word.
def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

print(longest_word("I love programming in Python"))  # Output: programming
