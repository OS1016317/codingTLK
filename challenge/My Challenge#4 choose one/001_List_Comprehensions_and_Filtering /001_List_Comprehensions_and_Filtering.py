#-----------------------------------------------------------------------------
# Name:          List Comprehensions and Filtering (List_Comprehensions_and_Filtering.py)
# Purpose:       Use list comprehensions to filter and manipulate data
#
# Author:      Ozra
# Created:     25-Mar-2025
# Updated:     25-Mar-2025
#-----------------------------------------------------------------------------


# Initial list od numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Create a list of even numbers using list comprehension
even_numbers = [num for num in numbers if num % 2 == 0]

# Create a list of squares of the even numbers
squared_numbers = [num ** 2 for num in even_numbers]

# Print both lists
print(f"even_numbers = {even_numbers}")
print(f"squared_numbers = {squared_numbers}")
