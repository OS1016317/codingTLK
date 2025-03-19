#-----------------------------------------------------------------------------
# Name:        Guess The number (Guess_the_Number.py)
# Purpose:     This script generates a random number between 1 and 10 and asks the user to guess until correct.
#
# Author:      Ozra
# Created:     18-Mar-2025
# Updated:     18-Mar-2025
#-----------------------------------------------------------------------------

# Challenge 2: Guess the number (While Loop)
import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

while True:
# Ask the user to guess the number
    guess = int(input("Guess the number:"))

    if guess == secret_number:
        print("Correct!")
        break # Exit the loop when the guess is correct
    else:
        print("Wrong, try again!")


