#-----------------------------------------------------------------------------
# Program Name:Access and Modify List Items (Access_and_Modify_List_Items.py)
# Purpose:     Modify an existing item in the list and access an item
#
# Author:      Ozra
# Created:     24-Mar-2025
# Updated:     24-Mar-2025
#-----------------------------------------------------------------------------

# initial grocery list
grocery_list = ['apple', 'banana', 'carrots', 'milk', 'bread']

#Change 'banana' to 'grapes'
grocery_list[1] = 'grapes'

# Print the updated list
print(grocery_list)

# Access the third items in the list and print it
third_items = grocery_list[2]
print(third_items)