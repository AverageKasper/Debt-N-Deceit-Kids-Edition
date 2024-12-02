#api formatting
from flask import Blueprint, jsonify, request
from python_app.player_class import player
task_blueprint = Blueprint('task', __name__)
# this whole sript is, in the end, kind of useless, 
# since the tasks dont change and could be displayed in the javascript part.

# Small airport tasks are selected here
@task_blueprint.route('/small')
def small_airport_task():
    options = {"1": "Dumpster diving", "2": "Pickpocket", "3": "Go to the next airport"}
    return jsonify(options)

# Medium airport tasks are selected here
@task_blueprint.route('/medium')
def medium_airport_task():
    options = {"1": "Trivia", "2": "Go to the next airport"}
    return jsonify(options)

# Large airport tasks are selected here
@task_blueprint.route('/large')
def large_airport_task():
    options = {"1": "Gamble", "2": "Lollipop", "3": "Go to the next airport"}
    return jsonify(options)


# ideas
# - airport tasks
# go to a bar
# actual stealing
# look for a job
# join a gang
# zombie apocalypse
#monke69
