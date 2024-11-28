# Problem 19: List Comprehension to Create a New List
# Write a Python program that uses list comprehension to create a new list containing squares of even numbers from an existing list.
def squares_of_even_numbers(lst):
    return [x**2 for x in lst if x % 2 == 0]

lst = [1, 2, 3, 4, 5, 6]
print(squares_of_even_numbers(lst))  # Output: [4, 16, 36]