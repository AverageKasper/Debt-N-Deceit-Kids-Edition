from python.smoking import smoking_action
from sql import fly
from utilities import int_check

# Task imports
from dumpster import dumpster_dive
from pickpocket import pickpocket
from player_class import player
from gambling import casino
from smoking import smoking_action

airport_cost = {"small": 100, "medium": 200, "large": 500}

# Function for selecting the next airport
def airport_selector():
    print(f"You are at {player.airport_name}, you can fly to the following airports: ")
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
        return
    if next_airport == 1 and player.carbon >= airport_cost["small"]:
        player.update_location(next_small_airport[0], next_small_airport[1], next_small_airport[2])
        player.update_carbon(-airport_cost["small"])
        small_airport_task()
    
    elif next_airport == 2 and player.carbon >= airport_cost["medium"]:
        player.update_location(next_medium_airport[0], next_medium_airport[1], next_medium_airport[2])
        player.update_carbon(-airport_cost["medium"])
        medium_airport_task()
        
    elif next_airport == 3 and player.carbon >= airport_cost["large"]:
        player.update_location(next_large_airport[0], next_large_airport[1], next_large_airport[2])
        player.update_carbon(-airport_cost["large"])
        large_airport_task()
        
    else:
        print(f"Error: Unexpected value for next_airport: {next_airport}")
        print(type(next_airport))
        return
    player.display_status()


# Small airport tasks are selected here
def small_airport_task():
    task_done_count = 0

    while task_done_count < 3:
        print(f"You can do {3 - task_done_count} more tasks, the shark is {player.shark} steps behind you.")
        print("You are at a small airport, you can do the following tasks: ")
        print("1. Dumpster diving")
        print("2. Pickpocket")
        print("3. Go to the next airport")
    
        task_choice = input("Choose a task: ")
        if task_choice == "1":
            dumpster_dive()
        elif task_choice == "2":
            pickpocket()
        elif task_choice == "3":
            return
        else:
            print("Invalid choice")
            continue
        task_done_count += 1
        player.update_shark(-1)
            

# Medium airport tasks are selected here
def medium_airport_task():
    task_done_count = 0

    while task_done_count < 3:
        print(f"You can do {3 - task_done_count} more tasks, the shark is {player.shark} steps behind you.")
        print("You are at a medium airport, you can do the following tasks: ")
        print("1. Trivia")
        print("2. Go to the next airport")

        task_choice = input("Choose a task: ")
        if task_choice == "1":
            pass
        elif task_choice == "2":
            return
        else:
            print("Invalid choice")
            continue
        task_done_count += 1
        player.update_shark(-1)

# Large airport tasks are selected here
def large_airport_task():
    task_done_count = 0

    while task_done_count < 3:
        print(f"You can do {3 - task_done_count} more tasks, the shark is {player.shark} steps behind you.")
        print("You are at a small airport, you can do the following tasks: ")
        print("1. Gamble")
        print("2. Smoking break")
        print("3. Go to the next airport")

        task_choice = input("Choose a task: ")
        if task_choice == "1":
            casino(player.balance)
        elif task_choice == "2":
            smoking_action(player.balance)
        elif task_choice == "3":
            return
        else:
            print("Invalid choice")
            continue
        task_done_count += 1
        player.update_shark(-1)



# ideas
# - airport tasks
# go to a bar
# actual stealing
# look for a job
# join a gang
# zombie apocalypse

