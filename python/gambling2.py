import random as r
from player_class import player
from flask import jsonify, request, Flask, session
from flask_cors import CORS

app = Flask(__name__)
app.secret_key="secret"
CORS(app)

@app.route('/casino/horse_race', methods=['POST'])
def horse_race():
    try:
        data = request.json

        # Parse and validate bet
        bet_horse = data.get("horse")
        if not bet_horse:
            return jsonify({"error": "Horse not specified"}), 400

        horses = ["Diddy", "Kolovastaava", "Sakke", "Rinne", "Uusitalo"]
        if bet_horse.capitalize() not in horses:
            return jsonify({"error": "Invalid horse. Please choose from the list."}), 400

        bet = data.get("bet", 0)
        if not isinstance(bet, (int, float)) or bet <= 0:
            return jsonify({"error": "Invalid or missing bet amount"}), 400

        if bet > player.balance:
            return jsonify({"error": "Insufficient funds"}), 400

        # Calculate odds for each horse
        odds = {horse: r.uniform(1.5, 5.0) for horse in horses}

        # Race simulation
        horse_speeds = {horse: r.randint(10, 20) for horse in horses}
        race_results = sorted(horse_speeds.items(), key=lambda x: x[1], reverse=True)

        winner = race_results[0][0]
        result_message = f"The winner is {winner}!"

        if bet_horse.capitalize() == winner:
            winnings = bet * odds[bet_horse.capitalize()]
            result_message += f" Congratulations! You won {winnings:.0f} euros!"
            player.update_balance(winnings)
        else:
            result_message += f" You lost {bet} euros."
            player.update_balance(-bet)

        # Return race results and updated balance
        return jsonify({
            "result": result_message,
            "player_balance": player.balance,
            "race_results": {horse: speed for horse, speed in race_results},
            "odds": {horse: odds[horse] for horse in horses}
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/casino/blackjack/start', methods=['POST'])
def start_blackjack():
    try:
        data = request.json
        bet = data.get("bet")

        # Validate the bet
        if not isinstance(bet, (int, float)) or bet <= 0:
            return jsonify({"error": "Invalid bet amount"}), 400

        error = player.validate_bet(bet)
        if error:
            return jsonify({"error": error}), 400

        # Initialize the game
        game_id = str(r.randint(1000, 9999))  # Example game ID
        player_hand = [deal_card(), deal_card()]
        dealer_hand = [deal_card(), deal_card()]

        # Retrieve existing games from session (if any)
        blackjack_games = session.get('blackjack_games', {})

        # Save the new game state
        blackjack_games[game_id] = {
            "bet": bet,
            "player_hand": player_hand,
            "dealer_hand": dealer_hand,
            "player_value": calculate_hand(player_hand),
            "dealer_value": calculate_hand(dealer_hand),
            "finished": False
        }

        # Store the updated game state back into the session
        session['blackjack_games'] = blackjack_games

        return jsonify({
            "game_id": game_id,
            "player_hand": player_hand,
            "dealer_hand": [dealer_hand[0], "Hidden"],
            "player_value": blackjack_games[game_id]["player_value"],
            "message": "Game started! Your move: hit or stand."
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/casino/blackjack/play', methods=['POST'])
def play_blackjack():
    try:
        data = request.json
        game_id = data.get("game_id")
        action = data.get("action")

        # Retrieve the existing games from session
        blackjack_games = session.get('blackjack_games', {})

        if game_id not in blackjack_games:
            return jsonify({"error": "Game not found"}), 400

        game = blackjack_games[game_id]

        if game["finished"]:
            return jsonify({"error": "Game already finished"}), 400

        if action == "hit":
            game["player_hand"].append(deal_card())
            game["player_value"] = calculate_hand(game["player_hand"])

            if game["player_value"] > 21:
                game["finished"] = True
                player.update_balance(-game["bet"])
                session['blackjack_games'] = blackjack_games  # Update session
                return jsonify({
                    "result": "Busted! You lost.",
                    "player_hand": game["player_hand"],
                    "balance": player.balance
                }), 200

            session['blackjack_games'] = blackjack_games  # Update session
            return jsonify({
                "player_hand": game["player_hand"],
                "player_value": game["player_value"],
                "message": "Your move: hit or stand."
            }), 200

        elif action == "stand":
            dealer_value = game["dealer_value"]
            while dealer_value < 17:
                game["dealer_hand"].append(deal_card())
                dealer_value = calculate_hand(game["dealer_hand"])

            game["dealer_value"] = dealer_value
            game["finished"] = True

            # Determine outcome
            if dealer_value > 21 or game["player_value"] > dealer_value:
                result = "Player wins!"
                player.update_balance(game["bet"])
            elif dealer_value > game["player_value"]:
                result = "Dealer wins!"
                player.update_balance(-game["bet"])
            else:
                result = "It's a tie!"

            session['blackjack_games'] = blackjack_games  # Update session
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


# Helper functions for Blackjack game
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






@app.route('/casino/snake-eyes', methods=['POST'])
def snake_eyes():
    try:
        bet = request.json.get('bet', 0)
        error = player.validate_bet(bet)
        if error:
            return jsonify(error, 400)

        # Proceed with game logic
        dice_1, dice_2 = r.randint(1, 6), r.randint(1, 6)
        result = {"rolls": [dice_1, dice_2]}

        if dice_1 == dice_2 == 1:
            winnings = bet * 10
            result.update({"message": "Big win!", "winnings": winnings})
            player.update_balance(winnings)
        elif dice_1 == dice_2:
            winnings = bet
            result.update({"message": "Small win!", "winnings": winnings})
            player.update_balance(winnings)
        else:
            loss = -bet
            result.update({"message": "You lost!", "winnings": loss})
            player.update_balance(loss)

        result["balance"] = player.balance
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500



@app.route('/casino/dice', methods=['POST'])
def dice():
    try:
        # Parse the bet from the request body
        bet = request.json.get('bet', 0)
        if not isinstance(bet, (int, float)) or bet <= 0:
            return jsonify({"error": "Invalid or missing bet amount"}), 400

        # Validate the bet against player's balance
        error = player.validate_bet(bet)
        if error:
            return jsonify({"error": error}), 400

        # Roll the dice
        dealer_dice1, dealer_dice2 = r.randint(1, 6), r.randint(1, 6)
        player_dice1, player_dice2 = r.randint(1, 6), r.randint(1, 6)
        dealer_total = dealer_dice1 + dealer_dice2
        player_total = player_dice1 + player_dice2

        # Determine the result
        result = {
            "dealer_rolls": [dealer_dice1, dealer_dice2],
            "dealer_total": dealer_total,
            "player_rolls": [player_dice1, player_dice2],
            "player_total": player_total,
        }

        if dealer_total > player_total:
            result.update({"message": "You lost!", "winnings": -bet})
            player.update_balance(-bet)
        elif dealer_total < player_total:
            result.update({"message": "You won!", "winnings": bet})
            player.update_balance(bet)
        else:
            result.update({"message": "It's a tie!", "winnings": 0})

        # Include updated balance
        result["balance"] = player.balance

        # Return the result as JSON
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/casino/hilo', methods=['POST'])
def hilo():
    try:
        # Extract and validate input from the request
        data = request.json
        bet = data.get('bet', 0)
        guess = data.get('guess', '').upper()

        # Validate bet and guess
        if not isinstance(bet, (int, float)) or bet <= 0:
            return jsonify({"error": "Invalid or missing bet amount"}), 400
        if guess not in ["HI", "LO"]:
            return jsonify({"error": "Invalid guess. Please use 'HI' or 'LO'"}), 400

        error = player.validate_bet(bet)
        if error:
            return jsonify({"error": error}), 400

        # Generate cards
        first_card = r.randint(1, 13)
        second_card = r.randint(1, 13)

        # Determine outcome
        result = {"first_card": first_card, "second_card": second_card, "guess": guess}
        if (guess == "HI" and second_card > first_card) or (guess == "LO" and second_card < first_card):
            winnings = bet
            result.update({"message": "You won!", "winnings": winnings})
            player.update_balance(winnings)
        else:
            loss = -bet
            result.update({"message": "You lost!", "winnings": loss})
            player.update_balance(loss)

        # Add updated balance to the result
        result["balance"] = player.balance

        # Return the result as JSON
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/casino/menu', methods=['GET'])
def casino_menu():
    try:
        # Check player's balance
        if player.balance <= 0:
            return jsonify({
                "message": "You don’t have any money. Please add funds to play.",
                "balance": player.balance
            }), 400

        # List available games
        games = ["Snake Eyes", "HiLo", "Dice", "Blackjack", "Horse Racing"]

        return jsonify({
            "message": "Welcome to the casino! Choose a game to play.",
            "games": games,
            "balance": player.balance
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500