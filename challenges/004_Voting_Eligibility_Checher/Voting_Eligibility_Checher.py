#-----------------------------------------------------------------------------
# Name:        Voting Eligibility Checker (Voting_Eligibility_Checker.py)
# Purpose:     Python program that checks if a person is eligible to vote based on their age.
#
# Author:      Ozra
# Created:     4-Mar-2025
# Updated:     4-Mar-2025
#-------------------------------------------------------------------------


# Ask the user to enter their age.
# Store the age in a variable.
user_input = int(input("Enter your age: "))

#   - If the age is 18 or older, print: `"You are eligible to vote!"`
if user_input >= 18:
    print("You are eligible to vote!")

# - If the age is under 18, print: `"Sorry, you are not eligible to vote yet."`
if user_input < 18:
    print("You are not eligible to vote!")

