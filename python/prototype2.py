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
from sql import create_player

# Utilities 
from utilities import anim_print
from utilities import clear_window
from utilities import int_check
from utilities import loading
# Remember to change your own credentials in the connector
from utilities import conn


class Player:
    def __init__(self, name, balance, cp, shark, airport_name, airport_country, airport_type):
        self.name = name
        self.balance = balance
        self.cp = cp
        self.shark = shark
        self.airport_name = airport_name
        self.airport_country = airport_country
        self.airport_type = airport_type
        create_player(self.name, self.balance, self.cp, self.shark)

    def update_location(self, airport_name, airport_country, airport_type):
        self.airport_name = airport_name
        self.airport_country = airport_country
        self.airport_type = airport_type

    def update_balance(self, amount):
        self.balance += amount

    def update_cp(self, amount):
        self.cp += amount

    def display_status(self):
        anim_print(f"""
You are at {self.airport_name}, {self.airport_country}.
You have {self.cp}CP and {self.balance}€ in the bank.
""")
        


# Variables
easy_dif = [2500, 10000, 7]
medium_dif = [1000, 7500, 5]
hard_diff = [100, 5000, 3]

player_name = input(anim_print("Enter your name: "))
dif_choice = input(anim_print("""Choose your difficulty: Easy, Medium or Hard: """)).upper()
while dif_choice != "EASY" and dif_choice != "MEDIUM" and dif_choice != "HARD":
    dif_choice = input(anim_print("Invalid choice, try again: ")).upper()
if dif_choice == "EASY":
    money, cp, shark = easy_dif
elif dif_choice == "MEDIUM":
    money, cp, shark = medium_dif
elif dif_choice == "HARD":
    money, cp, shark = hard_diff

player = Player(player_name, money, cp, shark, "Helsinki-Vantaa", "Finland", "large_airport")

