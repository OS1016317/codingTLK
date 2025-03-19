#-----------------------------------------------------------------------------
# Name:        Sum of Numbers (sum_of_Numbers.py)
# Purpose:     This program calculates the sum of all numbers from `1` to `n` using a `for` loop.
#
# Author:      Ozra
# Created:     18-Mar-2025
# Updated:     18-Mar-2025
#-----------------------------------------------------------------------------


# Sun of numbers (For Loop)

# Ask the user for a number 'n'
n = int(input("Enter a number"))

# Initialize the sum to 0
sum = 0

# use a for loop to iterate through numbers from 1 to n
for i in range(1,n+1):
    sum = sum + i

# output the result
print(f"sum = {sum}")

