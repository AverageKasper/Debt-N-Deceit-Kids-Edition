# Basic imports
import random as r
import time

#Task Scripts
from triviasql import trivia_game
from gambling import casino
from random_events import random_event
from pickpocket import pickpocket
from rules import rule_print
from dumpster import dumpster_dive
from smoking import smoking_action

#SQL scripts
from sql import create_player, update_money

# Utilities 
from utilities import anim_print
from utilities import clear_window
from utilities import int_check
from utilities import loading
# Remember to change your own credentials in the connector
from utilities import conn
from player_class import Player


        


# Variables
easy_dif = [2500, 10000, 7]
medium_dif = [1000, 7500, 5]
hard_diff = [100, 5000, 3]

player_name = input(anim_print("Enter your name: "))
dif_choice = input(anim_print("""Choose your difficulty: Easy, Medium or Hard: """)).upper()
while dif_choice != "EASY" and dif_choice != "MEDIUM" and dif_choice != "HARD":
    dif_choice = input(anim_print("Invalid choice, try again: ")).upper()
if dif_choice == "EASY":
    money, carbon, shark = easy_dif
elif dif_choice == "MEDIUM":
    money, carbon, shark = medium_dif
elif dif_choice == "HARD":
    money, carbon, shark = hard_diff

player = Player(player_name, money, carbon, shark, "Helsinki-Vantaa", "Finland", "large_airport")
print(player.balance)

# Flying to a new location
