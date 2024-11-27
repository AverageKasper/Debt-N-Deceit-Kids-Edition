# Basic imports
import random as r

#Task Scripts
#from airport_selection import airport_selector

#SQL scripts



# Remember to change your own credentials in the connector

from player_class import create_player_object

from random_events import random_event

        


# Variables


def start_game():
    from sql import check_name
    easy_dif = [2500, 10000, 7]
    medium_dif = [1000, 7500, 5]
    hard_diff = [100, 5000, 3]
    # Introduction
    print("Welcome to the Flight Game!")
    name_taken = True
    while name_taken == True:
        player_name = input("Enter your name: ")
        name_taken = check_name(player_name)
        if name_taken == True:
            print("Name already taken, try again.")
        
    
    dif_choice = input("""Choose your difficulty: Easy, Medium or Hard: """).upper()

    # Difficulty choice
    while dif_choice != "EASY" and dif_choice != "MEDIUM" and dif_choice != "HARD":
        dif_choice = input("Invalid choice, try again: ").upper()
    if dif_choice == "EASY":
        money, carbon, shark = easy_dif
    elif dif_choice == "MEDIUM":
        money, carbon, shark = medium_dif
    elif dif_choice == "HARD":
        money, carbon, shark = hard_diff

    # Player object, has a name, money, carbon, shark, inventory, airport_name, airport_country, airport_type as attributes
    
    create_player_object(player_name, money, carbon, shark, 0, "Helsinki-Vantaa", "Finland", "large_airport")
    game_loop()
    #end()


# Main game loop
def game_loop():
    game_loops = 1
    event_max_chance = 5
    while True:
        
        # Random event chance 1/5, can be changed if need be
        if game_loops == 1:
            pass
        else:
            random_event_chance = r.randint(1, event_max_chance)
            if random_event_chance == event_max_chance:
                random_event()
        
        
        # Fly to next airport
        from airport_selection import airport_selector
        airport_selector()
        
        print(f"Back at main script. Game loop: {game_loops}")
        
        
        
        
        game_loops += 1


