# Problem 15: Sort a List in Descending Order
# Write a Python program that sorts a list in descending order.
def sort_descending(lst):
    lst.sort(reverse=True)
    return lst

lst = [4, 2, 1, 3]
print(sort_descending(lst))  # Output: [4, 3, 2, 1]