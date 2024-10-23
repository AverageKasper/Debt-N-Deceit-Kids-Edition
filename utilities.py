import mysql.connector
import time
import os
import sys

# Mysql Connector thingy
conn = mysql.connector.connect(
                host='localhost',
                database='flight_game',
                user='kasper',
                password='Monkey',
                autocommit=True,
                collation="utf8mb4_general_ci"
                )

# Animated print function
def anim_print(text, delay=0.02):
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
def int_check(player_input):
    while player_input is not int:
        try:
            player_input = int(player_input)
        except:
           player_input =  input("Invalid option, try again: ")
        else:
           player_input = int(player_input)
           break 
    return player_input

