#-----------------------------------------------------------------------------
# Name:        Temperature Advice (Temperature_advice.py)
# Purpose:    Python program that asks the user for the current temperature and suggests whether they should wear a jacket, short-sleeves, or stay indoors.
#
# Author:      Ozra
# Created:     4-Mar-2025
# Updated:     4-Mar-2025
#-------------------------------------------------------------------------


# Ask the user to enter the current temperature (in Celsius).
# Store the temperature in a variable.
user_input = int(input("enter the current temperature: "))

#  - If the temperature is below 10°C, print: `"It's cold outside. Wear a jacket!"`
if user_input < 10:
    print("It's cold outside!")

#   - If the temperature is between 10°C and 25°C, print: `"It's a nice day. Wear short-sleeves!"`
if 10 <= user_input <= 25:
    print("It's a nice day.wear short-sleeves!")

# - If the temperature is above 25°C, print: `"It's hot outside. Stay cool!"`
if user_input > 25:
    print("It's hot outside. Stay cool!")