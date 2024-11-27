import mysql.connector
import time
import os
import sys

# Mysql Connector thingy
conn = mysql.connector.connect(
                host='localhost',
                database='flight_game',
                user='group_international',
                password='EEKPAMSMAW',
                autocommit=True,
                collation="utf8mb4_general_ci"
                )

# Animated print function
def anim_print(text, delay=0.0):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    return ""

# Loading screen animation if ever needed
def loading():
    plane = '🛬'
    trail = '-'
    width = 20  # Adjust the width 
    spaces = 0
    while spaces <= width:
        sys.stdout.write('\r' + ' ' * spaces + plane + trail * (width - spaces))
        sys.stdout.flush()
        time.sleep(0.2)
        spaces += 1
    
# Clearing console function
def clear_window():
    os.system('cls' if os.name=='nt' else 'clear')

# Checks if value can be changed to int, used when a number is needed for an answer
def int_check(player_input, max_value):
    while True:
        try:
            # Try to convert the player_input to an integer
            player_input = int(player_input)

            # Check if the input is within the valid range: 1 <= player_input <= max_value
            if 1 <= player_input <= max_value:
                break  # Valid input, break the loop
            else:
                # If input is outside the range, raise a ValueError
                raise ValueError
        except ValueError:
            # If there is an error (invalid input), prompt the user again
            player_input = input(f"Please enter a valid number between 1 and {max_value}: ")

    return player_input

