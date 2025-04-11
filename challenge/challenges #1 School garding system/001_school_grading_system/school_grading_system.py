#-----------------------------------------------------------------------------
# Name:        School grading system (School_grading_system.py)
# Purpose:     Python program that asks for a student's score and then provides a grade based on the score.
#
# Author:      Ozra
# Created:     4-Mar-2025
# Updated:     4-Mar-2025
#-----------------------------------------------------------------------------


user_input = int(input("please enter your grade: "))
# user_input = int(user_input)

# If the score is greater than and equal to 90, print: `"Grade: A"`
if user_input >= 90:
    print("grade A")

# If the score is between 80 and 89, print: `"Grade: B"`
if 80 < user_input < 89:
    print("grade B")
    
# If the score is between 70 and 79, print: `"Grade: C"`
if 70 < user_input < 79:
    print("grade C")

# If the score is between 60 and 69, print: `"Grade: D"`
if 60 < user_input < 69:
    print("grade D")

# If the score is below 60, print: `"Grade: F"`
if user_input < 60:
    print("grade E")
