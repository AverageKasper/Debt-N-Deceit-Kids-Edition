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
from sql import fly

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
airport_cost = {"small": 100, "medium": 200, "large": 500}
game_loops = 1

# Introduction
print(anim_print("Welcome to the Flight Game!"))
player_name = input(anim_print("Enter your name: "))
dif_choice = input(anim_print("""Choose your difficulty: Easy, Medium or Hard: """)).upper()

# Difficulty choice
while dif_choice != "EASY" and dif_choice != "MEDIUM" and dif_choice != "HARD":
    dif_choice = input(anim_print("Invalid choice, try again: ")).upper()
if dif_choice == "EASY":
    money, carbon, shark = easy_dif
elif dif_choice == "MEDIUM":
    money, carbon, shark = medium_dif
elif dif_choice == "HARD":
    money, carbon, shark = hard_diff

# Player object, has a name, money, carbon, shark, inventory, airport_name, airport_country, airport_type as attributes
player = Player(player_name, money, carbon, shark, "Helsinki-Vantaa", "Finland", "large_airport")


# Main game loop
while True:
    
    # Random event chance 1/5, can be changed if need be
    if game_loops == 1:
        pass
    else:
        random_event_chance = r.randint(1, 5)
        if random_event_chance == 5:
            random_event()
    
    print(f"You are at {player.airport_name}, you can fly to the following airports: ")
    
    # Fly to next airport
    next_small_airport = fly("small_airport")
    next_medium_airport = fly("medium_airport")
    next_large_airport = fly("large_airport")
    
    next_airport = input(f"""1. {next_small_airport[0]}, {next_small_airport[1]}
2. {next_medium_airport[0]}, {next_medium_airport[1]}
3. {next_large_airport[0]}, {next_large_airport[1]}
""")
    next_airport = int_check(next_airport, 3)
    print(next_airport)
    if player.carbon < airport_cost["small"]:
        print("You have run out of Carbon Points. Game Over")
        break
    if next_airport == 1 and player.carbon >= airport_cost["small"]:
        player.update_location(next_small_airport[0], next_small_airport[1], next_small_airport[2])
        player.update_carbon(-airport_cost["small"])
       
    elif next_airport == 2 and player.carbon >= airport_cost["medium"]:
        player.update_location(next_medium_airport[0], next_medium_airport[1], next_medium_airport[2])
        player.update_carbon(-airport_cost["medium"])
        
    elif next_airport == 3 and player.carbon >= airport_cost["large"]:
        player.update_location(next_large_airport[0], next_large_airport[1], next_large_airport[2])
        player.update_carbon(-airport_cost["large"])
        
    else:
        print(f"Error: Unexpected value for next_airport: {next_airport}")
        print(type(next_airport))
        print(player.balance)
        break
    player.display_status()
    
    
    
    
    
    game_loops += 1
