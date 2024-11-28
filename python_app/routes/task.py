#api formatting
from flask import Blueprint, jsonify, request

task_blueprint = Blueprint('task', __name__)

























# Small airport tasks are selected here
@task_blueprint.route('/small')
def small_airport_task():
    options = {"1": "Dumpster diving", "2": "Pickpocket", "3": "Go to the next airport"}
    return jsonify(options)

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
            casino()
        elif task_choice == "2":
            lollipop_action()
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
#monke69
