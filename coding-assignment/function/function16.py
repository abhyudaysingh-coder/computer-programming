# Problem 16: Write a function to generate a Fibonacci sequence up to a given number.
# The function should take a number as an argument and return the Fibonacci sequence up to that number.
def fibonacci(n):
    sequence = [0, 1]
    while sequence[-1] + sequence[-2] <= n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

print(fibonacci(20))  # Output: [0, 1, 1, 2, 3, 5, 8, 13]