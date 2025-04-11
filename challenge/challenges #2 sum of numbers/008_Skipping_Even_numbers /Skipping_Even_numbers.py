#-----------------------------------------------------------------------------
# Name:        Skipping Even Numbers (Skipping_Even_Numbers.py)
# Purpose:    This script prints numbers from 1 to 10 but skips even numbers using the continue statement.
#
# Author:      Ozra
# Created:     18-Mar-2025
# Updated:     18-Mar-2025
#-----------------------------------------------------------------------------

# Challenge 3: Skipping Even Numbers (For Loop + continue)

# Loop from 1 to 10
for num in range(1, 11):
# Check if the number is even
    if num % 2 == 0:
# Skip even numbers
        continue
# Print odd number
    print(num)