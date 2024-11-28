# Problem 9: Write a function to check if a number is even or odd.
# The function should take a number as an argument and return whether it is even or odd.
def even_or_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(even_or_odd(4))  # Output: Even
print(even_or_odd(7))  # Output: Odd