#-----------------------------------------------------------------------------
# Name:       Even or Odd Number Checker (Even_or_odd_number_checker.py)
# Purpose:     Python program that asks the user for a number and then tells them if the number is even or odd.
#
# Author:      Ozra
# Created:     4-Mar-2025
# Updated:     4-Mar-2025
#-------------------------------------------------------------------------



# Ask the user to enter a number.
# Store the number in a variable.
user_input = int(input("Enter a number: "))

# - If the number is even (i.e., divisible by 2), print: `"The number is even."`
if user_input % 2 == 0:
    print("Even")

# - If the number is odd, print: `"The number is odd."`
if user_input % 2 != 0:
    print("Odd")
