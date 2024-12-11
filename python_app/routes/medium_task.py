# Trivia and a potential new event type are the tasks for the medium airport.
import requests
from flask import Blueprint, jsonify


medium_blueprint = Blueprint('medium', __name__)

# categories 
# 9: General Knowledge
# 15: Video Games
# 18: Science: Computers
# 21: Sports

@medium_blueprint.route('/trivia/questions/<category>')
def trivia_questions(category):
    pyyntö = f"https://opentdb.com/api.php?amount=4&category={category}&type=multiple"
    vastaus = requests.get(pyyntö).json()
    if vastaus["response_code"] != 0:
        return jsonify({"error": 404})
    trimmed_result = {
                      "question_1": {"question": vastaus["results"][0]["question"],
                                     "correct_answer": vastaus["results"][0]["correct_answer"],
                                     "incorrect_answers": vastaus["results"][0]["incorrect_answers"]},
                      "question_2": {"question": vastaus["results"][1]["question"],
                                     "correct_answer": vastaus["results"][1]["correct_answer"],
                                     "incorrect_answers": vastaus["results"][1]["incorrect_answers"]},
                      "question_3": {"question": vastaus["results"][2]["question"],
                                     "correct_answer": vastaus["results"][2]["correct_answer"],
                                     "incorrect_answers": vastaus["results"][2]["incorrect_answers"]},
                      "question_4": {"question": vastaus["results"][3]["question"],
                                     "correct_answer": vastaus["results"][3]["correct_answer"],
                                     "incorrect_answers": vastaus["results"][3]["incorrect_answers"]}}
    
    return trimmed_result

@medium_blueprint.route('/trivia/reward/<correct>', methods=["POST"])
def trivia_reward(correct):
    from python_app.player_class import player
    if correct == "1":
        player.update_balance(100)
    elif correct == "2":
        player.update_balance(300)
    elif correct == "3":
        player.update_balance(700)
    elif correct == "4":
        player.update_balance(1200)
        player.update_carbon(500)   
    else:
        return jsonify({"error": "Invalid answer"})
    return jsonify({"message": "Reward given"})