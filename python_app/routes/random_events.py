import random as r
from flask import Blueprint, jsonify


random_blueprint = Blueprint('random', __name__)


event_list = ["Sausage",
              "9/11",
              "Mother",
              "mysterious merchant",
              "morpheus",
              "Celebrity",
              "Burning hand",
              "Poolparty",
              "PDiddy",
              "lost_ticket"]

@random_blueprint.route('/event')
def random_event():
    from python_app.player_class import player
    money = 0
    carbon = 0
    shark = 0
    lore = 0
    result = {}
    text_result = ""
    if len(event_list) == 0:
        result = {"event": False} 
        return jsonify(result)
    event_check = r.choice(event_list)

    # Sausage event, just lore
    # Converted
    if "Sausage" == event_check:
        lore = 1
        text_result = "You found a person digging through the trash for a sausage. Strange people these days."
        event_list.remove("Sausage")
        
    # 9/11 event
    # Converted
    elif "9/11" == event_check:
        text_result = """You are chilling at the airport watching news as you wait for your next flight.
You see on the news that an airport you were earlier got hit with a terrorist attack.
The Shark is slowed down by this.
"""
        shark += 2
        event_list.remove("9/11")
        
    # Mother event, Mother calls and gives money
    # Converted
    elif "Mother" == event_check:
        money = r.randint(300,700)

        text_result = f"""Your mother is calling you.
        You pick up and she gives you some money
        You gain {money} """
        event_list.remove("Mother")

    # Organ seller event, You can sell your kidney
    # Needs to be completly changed
    # Converted to mysterious merchant
    elif "mysterious merchant" == event_check:
        text_result = """While wandering through the airport, you stumble upon a shadowy figure.
        <br>The figure speaks in hushed tones, offering a deal too tempting to ignore."""
        # Random chance for whether the player accepts or declines the deal
        outcome = r.choice(["accept", "decline"])
        
        if outcome == "accept":
            money = r.randint(500, 1500)  # Random monetary reward
            text_result += f"""<br>You instinctively agree, and the figure hands you an envelope containing {money}€.
            <br>Before you can ask any questions, they vanish into the crowd."""    
        else:
            lore = 1
            text_result +="""<br>Something about the figure feels off, and you walk away without a second glance."
            <br>It might have been wise to trust your instincts."""

        # Remove the "mysterious merchant" event from the list after interaction
        event_list.remove("mysterious merchant")
    
    # Russian roulette, The Shark calls you and offers to play a game. Ends game if russian roulette is played
    elif "morpheus" == event_check:
        text_result = """You receive a mysterious message from an unknown number.
        <br>The message reads: "I offer you a choice.<br>Take a pill to end your journey
        or continue to see how far you can run."
        <br>What do you do?"""
        event_list.remove("morpheus")
        result = {"event": True, "text": text_result, "input": "morpheus_pill"}
    
    # Celebrity event, he throws money around and you pick up some
    # Converted
    elif "Celebrity" == event_check:
        money = r.randint(100, 1000)
        text_result = f"""You see a vaguely familiar looking celebrity.
All of a sudden he starts throwing cash around.
People rush in to gather as much as they can.
You manage to pick up {money}€.
"""
        event_list.remove("Celebrity")
        
    # Burning hand event, loses money
    # Converted
    elif "Burning hand" == event_check:
        money = r.randint(-700,-200)
        text_result = f"""You burn your hand in an accident.
The medical bills cost {money}€.
Tough luck."""

        event_list.remove("Burning hand")
    
    # Pool party event, loses money
    # Converted
    elif "Poolparty" == event_check:
        money = r.randint(-567,-123)
        text_result = f"""You are in a good mood.
You decide to throw a pool party at the airports lounge.
It cost you {money}€. """
        event_list.remove("Poolparty")


    # P.Diddy offers you help
    # Converted
    elif "PDiddy" == event_check:
        money = r.randint(666, 1984)
        text_result = f"""You meet P.Diddy at the airport.
He sees that you are troubled and offers to help you.
You gain {money}.
"""
        event_list.remove("PDiddy")
    elif "lost_ticket" == event_check:
        carbon = r.randrange(100, 1000, 100)
        text_result = f"""You found a lost airplane ticket on the ground.
        <br>Out of the goodness of your heart, you decide to return it to the lost and found.
        <br>As a reward, the airport staff give you a small sum of carbon points.
        <br>You gain {carbon} carbon."""
        event_list.remove("lost_ticket")
    # Insert new event above
    # end of random events
    else:
        result = {"event": False, "text": "what the fuck", "event_choice": event_check}
    
    if money != 0:
        result = {"event": True, "reward": money, "text": text_result}
        #!#player.update_balance(money)
    elif carbon !=0:
        result = {"event": True, "reward": carbon, "text": text_result}
        #!#player.update_carbon(carbon)
    elif shark != 0:
        result = {"event": True, "reward": shark, "text": text_result}
        #!#player.update_shark(shark)
    elif lore != 0:
        result = {"event": True, "reward": "lore", "text": text_result}
    
    return jsonify(result)

# with russian roulette being changed to morpheus pill, it is kind of pointless to have in the python.
# might as well be in javascript but we'll see
@random_blueprint.route('/morpheus_pill')
def morpheus_pill():
    pill_list = ["red", "blue"]
    bad_pill = r.choice(pill_list)
    result = {"bad_pill": bad_pill}
    return jsonify(result)