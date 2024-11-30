# Trivia and a potential new event type are the tasks for the medium airport.
import requests
from flask import Blueprint, jsonify

medium_blueprint = Blueprint('medium', __name__)

@medium_blueprint.route('/trivia/questions')
def trivia_questions():
    pyyntö = "https://opentdb.com/api.php?amount=5"
    vastaus = requests.get(pyyntö).json()
    print(vastaus)
    return vastaus

