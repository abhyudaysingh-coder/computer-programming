# Problem 3: Write a function to find the greatest common divisor (GCD) of two numbers.
# The function should take two numbers as arguments and return their GCD.
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd(56, 98))  # Output: 14