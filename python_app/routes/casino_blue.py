import random as r
from flask import Blueprint, jsonify, request, session, Flask
from python_app.player_class import create_player_object

casino_blueprint = Blueprint('casino', __name__)


@casino_blueprint.route('/menu', methods=['GET'])
def casino_menu():
    create_player_object('test', 1000, 100, 0, 0, 'Helsinki-Vantaa', 'Finland', 'large_airport')
    from python_app.player_class import player

    try:
        if player.balance <= 0:
            return jsonify({
                "message": "You don't have any money. Please add funs to play",
                "balance": player.balance
            }), 400

        games = ["SNAKE EYES", "HILO", "BLACKJACK", "HORSE RACING"]
        return jsonify({
            "message": "Welcome to the casino! Choose a game to play",
            "games": games,
            "balance": player.balance
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@casino_blueprint.route('/horse_race/start', methods=['POST'])
def horse_race_start():
    from python_app.player_class import player
    try:
        data = request.json
        bet = data.get("bet", 0)

        # Validate the bet
        if not isinstance(bet, (int, float)) or bet <= 0:
            return jsonify({"error": "Invalid bet amount"}), 400

        error = player.validate_bet(bet)
        if error:
            return jsonify({"error": error}), 400

        # Define the horses
        horses = ["Diddy", "Kolovastaava", "Sakke", "Rinne", "Uusitalo"]

        # Generate odds for each horse
        odds = {horse: round(r.uniform(1.5, 5.0), 2) for horse in horses}

        return jsonify({
            "horses": horses,
            "odds": odds,
            "bet": bet,
            "message": "Place your bet by selecting a horse."
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


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

        # Retrieve and validate the bet
        bet = data.get("bet", 0)
        if not isinstance(bet, (int, float)) or bet <= 0:
            return jsonify({"error": "Invalid bet amount"}), 400

        error = player.validate_bet(bet)
        if error:
            return jsonify({"error": error}), 400

        # Generate race results and calculate odds
        odds = {horse: r.uniform(1.5, 5.0) for horse in horses}
        horse_speeds = {horse: r.randint(10, 20) for horse in horses}
        race_results = sorted(horse_speeds.items(), key=lambda x: x[1], reverse=True)

        winner = race_results[0][0]
        result_message = f"The winner is {winner}!"

        # Check if the player won
        winnings = 0
        if bet_horse.capitalize() == winner:
            winnings = bet * odds[bet_horse.capitalize()]
            result_message += f" Congratulations! You won {winnings:.2f}€."
            player.update_balance(winnings)
        else:
            result_message += f" You lost {bet:.2f}€."
            player.update_balance(-bet)

        # Return the race results and player's updated balance
        return jsonify({
            "message": result_message,
            "player_balance": player.balance,
            "race_results": {horse: speed for horse, speed in race_results},
            "odds": {horse: round(odds[horse], 2) for horse in horses}
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Blackjack

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
        bet = data.get("bet", 0)

        # Validate the bet
        if not isinstance(bet, (int, float)) or bet <= 0:
            return jsonify({"error": "Invalid bet amount"}), 400

        error = player.validate_bet(bet)
        if error:
            return jsonify({"error": error}), 400

        # Deal initial cards
        player_hand = [deal_card(), deal_card()]
        dealer_hand = [deal_card(), "Hidden"]

        return jsonify({
            "player_hand": player_hand,
            "dealer_hand": dealer_hand,
            "bet": bet,
            "message": "Game started. Your move: hit or stand."
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@casino_blueprint.route('/blackjack/play', methods=['POST'])
def play_blackjack():
    from python_app.player_class import player
    try:
        data = request.json
        player_hand = data.get("player_hand", [])
        dealer_hand = data.get("dealer_hand", [])
        bet = data.get("bet", 0)
        action = data.get("action", "").lower()

        if not player_hand or not dealer_hand or not isinstance(bet, (int, float)) or bet <= 0:
            return jsonify({"error": "Invalid game state"}), 400

        if action not in ["hit", "stand"]:
            return jsonify({"error": "Invalid action"}), 400

        # Handle "hit"
        if action == "hit":
            player_hand.append(deal_card())
            player_value = calculate_hand(player_hand)

            if player_value > 21:  # Player busts
                player.update_balance(-bet)
                return jsonify({
                    "player_hand": player_hand,
                    "dealer_hand": dealer_hand,
                    "result": "Busted! You lost.",
                    "balance": player.balance,
                    "amount": -bet,  # Amount lost
                    "finished": True
                })

            return jsonify({
                "player_hand": player_hand,
                "dealer_hand": dealer_hand,
                "message": "Your move: hit or stand.",
                "finished": False
            })

        # Handle "stand"
        if action == "stand":
            dealer_hand = [card for card in dealer_hand if card != "Hidden"]
            while calculate_hand(dealer_hand) < 17:  # Dealer must hit until 17
                dealer_hand.append(deal_card())

            player_value = calculate_hand(player_hand)
            dealer_value = calculate_hand(dealer_hand)
            result = ""
            amount = 0

            if dealer_value > 21 or player_value > dealer_value:  # Player wins
                result = "Player wins!"
                amount = bet
                player.update_balance(amount)
            elif dealer_value > player_value:  # Dealer wins
                result = "Dealer wins!"
                amount = -bet
                player.update_balance(amount)
            else:  # Tie
                result = "It's a tie!"

            return jsonify({
                "player_hand": player_hand,
                "dealer_hand": dealer_hand,
                "result": result,
                "balance": player.balance,
                "amount": amount,  # Amount won or lost
                "finished": True
            })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@casino_blueprint.route('/snake-eyes', methods=['POST'])
def snake_eyes():
    from python_app.player_class import player
    try:
        data = request.json
        bet = data.get("bet", 0)

        # Validate the bet
        if not isinstance(bet, (int, float)) or bet <= 0:
            return jsonify({"error": "Invalid bet amount"}), 400

        error = player.validate_bet(bet)
        if error:
            return jsonify({"error": "No money blud"}), 400

        # Roll the dice
        dice_1, dice_2 = r.randint(1, 6), r.randint(1, 6)
        result_message = f"You rolled {dice_1} and {dice_2}."
        winnings = 0

        # Determine the outcome
        if dice_1 == dice_2 == 1:  # Snake Eyes
            winnings = bet * 10
            result_message += f" Snake Eyes! You won {winnings:.2f}€."
        elif dice_1 == dice_2:  # Any other doubles
            winnings = bet
            result_message += f" Doubles! You won {winnings:.2f}€."
        else:  # No win
            winnings = -bet
            result_message += f" No doubles. You lost {bet:.2f}€."

        # Update the player's balance
        player.update_balance(winnings)

        # Return the result
        return jsonify({
            "message": result_message,
            "dice_rolls": [dice_1, dice_2],
            "winnings": winnings,
            "balance": player.balance
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@casino_blueprint.route('/hilo/start', methods=['POST'])
def hilo_start():
    from python_app.player_class import player
    try:
        data = request.json
        bet = data.get('bet', 0)

        if not isinstance(bet, (int, float)) or bet <= 0:
            return jsonify({"error": "Invalid or missing bet amount"}), 400

        error = player.validate_bet(bet)
        if error:
            return jsonify({"error": error}), 400

        first_card = r.randint(1, 13)

        return jsonify({
            "first_card": first_card,
            "bet": bet,
            "message": f"The first card is {first_card}. Make your guess: Hi or Lo."
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@casino_blueprint.route('/hilo/guess', methods=['POST'])
def hilo_guess():
    from python_app.player_class import player
    try:
        data = request.json
        first_card = data.get('first_card')
        bet = data.get('bet')
        guess = data.get('guess', '').upper()

        if not first_card or not isinstance(first_card, int):
            return jsonify({"error": "Missing or invalid first card."}), 400
        if not isinstance(bet, (int, float)) or bet <= 0:
            return jsonify({"error": "Invalid or missing bet amount"}), 400
        if guess not in ["HI", "LO"]:
            return jsonify({"error": "Invalid guess. Please use 'HI' or 'LO'."}), 400

        second_card = r.randint(1, 13)

        result_message = f"The first card was {first_card}, and the second card is {second_card}."
        winnings = 0

        if (guess == "HI" and second_card > first_card) or (guess == "LO" and second_card < first_card):
            winnings = bet
            result_message += f" You guessed correctly! You won {winnings:.2f}€."
        elif second_card == first_card:
            result_message += " It's a tie! No winnings or losses."
        else:
            winnings = -bet
            result_message += f" You guessed wrong. You lost {bet:.2f}€."

        player.update_balance(winnings)

        return jsonify({
            "first_card": first_card,
            "second_card": second_card,
            "bet": bet,
            "message": result_message,
            "balance": player.balance
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
