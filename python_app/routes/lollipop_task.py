import random
import time
from flask import Blueprint, jsonify, request
#from python_app.utilities import anim_print, clear_window  # these are not needed but Just in case u know
from python_app.player_class import player

# Create a Flask Blueprint thingy
lollipop_blueprint = Blueprint('lollipop', __name__)

# Turn-based combat function
@lollipop_blueprint.route('/start_fight', methods=['GET'])
def start_fighting():
    from python_app.player_class import player
    try:
        salvia_mode = request.args.get('salvia_mode', 'false').lower() == 'true'
        player_lost = False

        fighter = {
            "name": "Player",
            "health": 100,
            "attacks": {
                "Lollipop eye poke": (10, 20),
                "Lollipop throw": (15, 25),
                "Nut cracker": (20, 35)
            }
        }

        enemy = {
            "name": "Enemy",
            "health": 100,
            "attacks": {
                "Pop Bite": (8, 18),
                "Claw": (12, 25),
                "Crotch grab": (18, 30)
            }
        }

        if salvia_mode:
            fighter["attacks"] = {
                "Moomin punch": (15, 30),
                "ChupaChups kick": (20, 40),
                "Sugar rage": (25, 50)
            }
            enemy["name"] = "Lollipop hater"
            enemy["health"] = 80

        # Main fight logic
        while fighter["health"] > 0 and enemy["health"] > 0:
            turn = random.choice(["player", "enemy"])
            
            if turn == "player":
                player_attack = random.choice(list(fighter["attacks"].keys()))
                damage = random.randint(*fighter["attacks"][player_attack])
                enemy["health"] = max(0, enemy["health"] - damage)
            else:
                enemy_attack = random.choice(list(enemy["attacks"].keys()))
                damage = random.randint(*enemy["attacks"][enemy_attack])
                fighter["health"] = max(0, fighter["health"] - damage)

            if enemy["health"] <= 0:
                return jsonify({"status": "success", "message": "Enemy defeated!"})
            if fighter["health"] <= 0:
                player.death("Lost due to losing a fight over sucking a lollipop")
                return jsonify({"status": "fail", "message": "You lost the fight!"})
        
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


# Ringpop Route
@lollipop_blueprint.route('/ring_pop', methods=['GET'])
def ring_pop():
    from python_app.player_class import player
    random_bucks = random.randint(1, 1500)
    player.update_balance(random_bucks)
    return jsonify({"status": "success", "message": f"You got {random_bucks}€", "balance": player.get_balance()})


# Moomin Route
@lollipop_blueprint.route('/moomin', methods=['GET'])
def suck_moomin():
    from python_app.player_class import player
    player_lost = start_fighting()
    if player_lost:
        player.death("Lost due to losing a fight over sucking a lollipop")
        return jsonify({"status": "fail", "message": "You lost the fight!"})
    return jsonify({"status": "success", "message": "You won the fight!"})


# Jolly Rancher Route
@lollipop_blueprint.route('/jolly', methods=['GET'])
def suck_jolly():
    from python_app.player_class import player
    random_money = random.randint(100, 300)
    player.update_balance(random_money)
    return jsonify({"status": "success", "message": f"You got {random_money}€", "balance": player.get_balance()})


# John Player Route
@lollipop_blueprint.route('/john_player', methods=['GET'])
def suck_john():
    from python_app.player_class import player
    random_outcome = random.choice(['good', 'bad'])
    if random_outcome == 'bad':
        player.death("Lost while sucking in a back alley")
        return jsonify({"status": "fail", "message": "You died in the back alley."})
    return jsonify({"status": "success", "message": "You survived the encounter!"})


# Salvia Route
@lollipop_blueprint.route('/salvia', methods=['GET'])
def suck_salvia():
    from python_app.player_class import player
    player_lost = start_fighting(salvia_mode=True)
    if player_lost:
        player.death("Lost while being sugar high")
        return jsonify({"status": "fail", "message": "You lost the fight in a sugar high."})
    return jsonify({"status": "success", "message": "You survived the salvia experience!"})


# ChupaChups Route
@lollipop_blueprint.route('/chupa', methods=['GET'])
def suck_chupa():
    from python_app.player_class import player
    black_money = random.randint(500, 1000)
    player.update_balance(-black_money)
    return jsonify({"status": "fail", "message": f"You lost {black_money}€", "balance": player.get_balance()})


# Lollipop Selector Route
@lollipop_blueprint.route('/select', methods=['POST'])
def lollipop_action():
    from python_app.player_class import player
    try:
        data = request.json
        lollipop_choice = data.get('lollipop', '').upper()

        actions = {
            "RINGPOP": ring_pop,
            "MOOMIN": suck_moomin,
            "JOLLY RANCHER": suck_jolly,
            "JOHN PLAYER SPECIAL": suck_john,
            "SALVIA POP": suck_salvia,
            "CHUPACHUPS": suck_chupa
        }

        if lollipop_choice in actions:
            response = actions[lollipop_choice]()
            return response

        return jsonify({"status": "error", "message": "Invalid lollipop choice."}), 400

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
