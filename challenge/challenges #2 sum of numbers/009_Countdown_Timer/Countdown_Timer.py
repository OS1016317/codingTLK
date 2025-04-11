#-----------------------------------------------------------------------------
# Name:        Countdown Timer (Countdown_Timer.py)
# Purpose:      This script counts down from 10 to 1, allowing the user to stop it by typing "stop".
#
# Author:      Ozra
# Created:     18-Mar-2025
# Updated:     18-Mar-2025
#-----------------------------------------------------------------------------

# Challenge 4: Countdown Timer (While loop + Break)

# Start countdown at 10
count = 10
while count>=0:
# print current number
    print(count)
# prompt user input
    user_input =input('Enter "stop" to cancel or press Enter:')
# Check if user types 'stop'
    if user_input.lower() =="stop":
        print("Countdown Stopped")
    # Break the loop if 'stop' is entered
        break
    else:
    # Decrease the count by 1
        count -=1