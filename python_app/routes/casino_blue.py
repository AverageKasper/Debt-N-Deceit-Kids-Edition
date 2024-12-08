import random as r
from flask import Blueprint, jsonify, request, session, Flask
from python_app.player_class import create_player_object

casino_blueprint=Blueprint('casino', __name__)


@casino_blueprint.route('/menu', methods=['GET'])
def casino_menu():


    create_player_object('test', 1000, 100, 0, 0, 'Helsinki-Vantaa', 'Finland', 'large_airport')
    from python_app.player_class import player
    
    try:
        if player.balance<=0:
            return jsonify ({
                "message":"You don't have any money. Please add funs to play",
                "balance": player.balance
            }), 400

        games=["SNAKE EYES", "HILO", "BLACKJACK", "HORSE RACING"]
        return jsonify({
            "message":"Welcome to the casino! Choose a game to play",
            "games":games,
            "balance": player.balance
        }), 200
    except Exception as e:
        return jsonify({"error":str(e)}), 500

@casino_blueprint.route('/horse_race', methods=['POST'])
def horse_race():
    from python_app.player_class import player
    try:
        data = request.json

        # Validate the selected horse
        bet_horse = data.get("horse")
        if not bet_horse:
            return jsonify({"error": "Horse not specified"}), 400

        horses = ["Diddy", "Kolovastaava", "Sakke", "Rinne", "Uusitalo"]
        if bet_horse.capitalize() not in horses:
            return jsonify({"error": "Invalid horse. Please choose from the list."}), 400

        # Retrieve and validate the bet using the `validate_bet` method
        bet = data.get("bet", 0)
        error = player.validate_bet(bet)  # Call the method
        if error:
            return jsonify(error), 400  # Respond with the validation error

        # Generate odds and simulate the race
        odds = {horse: r.uniform(1.5, 5.0) for horse in horses}
        horse_speeds = {horse: r.randint(10, 20) for horse in horses}
        race_results = sorted(horse_speeds.items(), key=lambda x: x[1], reverse=True)

        winner = race_results[0][0]
        result_message = f"The winner is {winner}!"

        # Check if the player won
        if bet_horse.capitalize() == winner:
            winnings = bet * odds[bet_horse.capitalize()]
            result_message += f" Congratulations! You won {winnings:.0f} euros!"
            player.update_balance(winnings)
        else:
            result_message += f" You lost {bet} euros."
            player.update_balance(-bet)

        # Return the race results and player's updated balance
        return jsonify({
            "result": result_message,
            "player_balance": player.balance,
            "race_results": {horse: speed for horse, speed in race_results},
            "odds": {horse: odds[horse] for horse in horses}
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


#Blackjack

def deal_card():
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return r.choice(cards)

def calculate_hand(hand):
    card_values = {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
        "J": 10, "Q": 10, "K": 10, "A": 11
    }
    value, ace_count = 0, 0
    for card in hand:
        value += card_values[card]
        if card == "A":
            ace_count += 1
    while value > 21 and ace_count:
        value -= 10
        ace_count -= 1
    return value


@casino_blueprint.route('/blackjack/start', methods=['POST'])
def start_blackjack():
    from python_app.player_class import player
    try:
        data = request.json
        bet = data.get("bet")

        # Validate the bet
        if not isinstance(bet, (int, float)) or bet <= 0:
            return jsonify({"error": "Invalid bet amount"}), 400

        error = player.validate_bet(bet)
        if error:
            return jsonify({"error": error}), 400

        # Initialize the game (assigning cards)
        game_id = str(r.randint(1000, 9999))  # Generate a random game ID
        player_hand = [deal_card(), deal_card()]  # Player starts with two cards
        dealer_hand = [deal_card(), deal_card()]  # Dealer starts with two cards

        # Create the game state
        blackjack_games = session.get('blackjack_games', {})
        blackjack_games[game_id] = {
            "bet": bet,
            "player_hand": player_hand,
            "dealer_hand": dealer_hand,
            "player_value": calculate_hand(player_hand),
            "dealer_value": calculate_hand(dealer_hand),
            "finished": False
        }

        # Store the updated game state
        session['blackjack_games'] = blackjack_games

        # Send response with game details
        return jsonify({
            "game_id": game_id,
            "player_hand": player_hand,
            "dealer_hand": [dealer_hand[0], "Hidden"],  # Hide dealer's second card
            "player_value": blackjack_games[game_id]["player_value"],
            "message": "Game started! Your move: hit or stand."
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

def play_blackjack():
    from python_app.player_class import player
    try:
        data = request.json
        game_id = data.get("game_id")
        action = data.get("action")

        # Retrieve the game from session
        blackjack_games = session.get('blackjack_games', {})

        if game_id not in blackjack_games:
            return jsonify({"error": "Game not found"}), 400

        game = blackjack_games[game_id]

        if game["finished"]:
            return jsonify({"error": "Game already finished"}), 400

        if action == "hit":
            # Player hits (draws a card)
            game["player_hand"].append(deal_card())
            game["player_value"] = calculate_hand(game["player_hand"])

            # Check if player has busted (value > 21)
            if game["player_value"] > 21:
                game["finished"] = True
                player.update_balance(-game["bet"])  # Player loses the bet
                session['blackjack_games'] = blackjack_games  # Update the session
                return jsonify({
                    "result": "Busted! You lost.",
                    "player_hand": game["player_hand"],
                    "balance": player.balance
                }), 200

            session['blackjack_games'] = blackjack_games  # Update the session
            return jsonify({
                "player_hand": game["player_hand"],
                "player_value": game["player_value"],
                "message": "Your move: hit or stand."
            }), 200

        elif action == "stand":
            # Dealer's turn
            dealer_value = game["dealer_value"]
            while dealer_value < 17:
                game["dealer_hand"].append(deal_card())
                dealer_value = calculate_hand(game["dealer_hand"])

            game["dealer_value"] = dealer_value
            game["finished"] = True

            # Determine outcome
            if dealer_value > 21 or game["player_value"] > dealer_value:
                result = "Player wins!"
                player.update_balance(game["bet"])  # Player wins the bet
            elif dealer_value > game["player_value"]:
                result = "Dealer wins!"
                player.update_balance(-game["bet"])  # Player loses the bet
            else:
                result = "It's a tie!"

            session['blackjack_games'] = blackjack_games  # Update the session
            return jsonify({
                "result": result,
                "player_hand": game["player_hand"],
                "dealer_hand": game["dealer_hand"],
                "player_value": game["player_value"],
                "dealer_value": game["dealer_value"],
                "balance": player.balance
            }), 200

        else:
            return jsonify({"error": "Invalid action"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@casino_blueprint.route('/snake-eyes', methods=['POST'])
def snake_eyes():
    from python_app.player_class import player
    try:
        data = request.json
        bet = data.get("bet", 0)

        # Validate the bet using the player's validate_bet method
        error = player.validate_bet(bet)
        if error:
            return jsonify({"error": error}), 400  # Return validation error if bet is invalid

        # Roll the dice (both dice are random between 1 and 6)
        dice_1, dice_2 = r.randint(1, 6), r.randint(1, 6)
        result = {"rolls": [dice_1, dice_2]}

        # Check the result of the dice roll
        if dice_1 == dice_2 == 1:
            # Big win case: double ones (Snake Eyes)
            winnings = bet * 10
            result.update({"message": "Big win!", "winnings": winnings})
            player.update_balance(winnings)
        elif dice_1 == dice_2:
            # Small win case: any other doubles
            winnings = bet
            result.update({"message": "Small win!", "winnings": winnings})
            player.update_balance(winnings)
        else:
            # Loss case: no doubles
            loss = -bet
            result.update({"message": "You lost!", "winnings": loss})
            player.update_balance(loss)

        # Include the player's updated balance in the response
        result["balance"] = player.balance
        return jsonify(result)  # Return the final result

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@casino_blueprint.route('/hilo', methods=['POST'])
def hilo():
    from python_app.player_class import player
    try:
        data = request.json

        # Extract and validate bet and guess from the request
        bet = data.get('bet', 0)
        guess = data.get('guess', '').upper()

        # Validate the bet and guess
        if not isinstance(bet, (int, float)) or bet <= 0:
            return jsonify({"error": "Invalid or missing bet amount"}), 400
        if guess not in ["HI", "LO"]:
            return jsonify({"error": "Invalid guess. Please use 'HI' or 'LO'"}), 400

        # Validate the bet using the player's method
        error = player.validate_bet(bet)
        if error:
            return jsonify({"error": error}), 400  # Return validation error if bet is invalid

        # Generate the two cards
        first_card = r.randint(1, 13)
        second_card = r.randint(1, 13)

        # Determine the outcome based on the guess
        result = {"first_card": first_card, "second_card": second_card, "guess": guess}
        if (guess == "HI" and second_card > first_card) or (guess == "LO" and second_card < first_card):
            winnings = bet
            result.update({"message": "You won!", "winnings": winnings})
            player.update_balance(winnings)
        else:
            loss = -bet
            result.update({"message": "You lost!", "winnings": loss})
            player.update_balance(loss)

        # Include the player's updated balance in the response
        result["balance"] = player.balance

        # Return the result as JSON
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

