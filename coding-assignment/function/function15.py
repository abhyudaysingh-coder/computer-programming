# Problem 15: Write a function to check if a number is a perfect square.
# The function should take a number as an argument and return True if it's a perfect square, otherwise False.
import math

def is_perfect_square(n):
    return int(math.sqrt(n)) ** 2 == n

print(is_perfect_square(16))  # Output: True
print(is_perfect_square(14))  # Output: False
