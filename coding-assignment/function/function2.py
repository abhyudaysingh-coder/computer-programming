# Problem 2: Write a function to check if a number is prime.
# The function should take a number as an argument and return True if it's prime, otherwise False.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(11))  # Output: True
print(is_prime(4))   # Output: False