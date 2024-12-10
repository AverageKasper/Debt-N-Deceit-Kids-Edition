# Basic imports
import random as r
from flask import Blueprint, jsonify, request

from python_app.player_class import create_player_object
from python_app.routes.sql import initial_setup


start_blueprint = Blueprint('start', __name__)

@start_blueprint.route('/start_game/<player_name>/<difficulty>')
def start_game(player_name, difficulty):
    initial_setup()
    easy_dif = [2500, 10000, 7]
    medium_dif = [1000, 7500, 5]
    hard_diff = [100, 5000, 3]
    
    if difficulty == "EASY":
        money, carbon, shark = easy_dif
    elif difficulty == "MEDIUM":
        money, carbon, shark = medium_dif
    elif difficulty == "HARD":
        money, carbon, shark = hard_diff

    # Player object, has a name, money, carbon, shark, inventory, airport_name, airport_country, airport_type as attributes
    create_player_object(player_name, money, carbon, shark, 0, "Helsinki-Vantaa", "Finland", "large_airport")
    return jsonify({"monke": "monke"})
    














# the game loop is probably not needed anymore since the game is now a web app and the loop is most likely handled
# by javascript on the client side

# Main game loop
# def game_loop():
#     game_loops = 1
#     event_max_chance = 5
#     while True:
        
#         # Random event chance 1/5, can be changed if need be
#         if game_loops == 1:
#             pass
#         else:
#             random_event_chance = r.randint(1, event_max_chance)
#             if random_event_chance == event_max_chance:
#                 random_event()
        
        
#         # Fly to next airport
#         from airport_selection import airport_selector
#         airport_selector()
        
        
#         print(f"Back at main script. Game loop: {game_loops}")
        
        
        
        
#         game_loops += 1


