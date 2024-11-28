# Problem 1: Write a function to find the factorial of a number.
# The function should take a number as an argument and return its factorial.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120