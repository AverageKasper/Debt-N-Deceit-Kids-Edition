import random as r
from flask import Blueprint, jsonify
from python_app.player_class import player

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


































import time
import random as r

def int_check(player_input):
    pass

# This will be changed to Morphious pill selection
# Russian roulette function
def russian_roulette():
    bullet = 1
    player_death = False
    shark_death = False
    player_turn = False
    print("\nBonk\n")
    time.sleep(2)
    print(f"""You wake up in a dark cellar with 2 chairs and a table.          
You see a 6 chamber revolver on the table.
The loanshark is across the table from you.         
A rough voice speaks at you.            
"Its time to start the game now"            
"There is 1 bullet loaded into the revolver in front of you"            
"You will take turns firing the gun at your head"           
"Whoever survives gets to walk away"            
"Lets flip a coin for who goes first"           
""")
    coin_flip = input(print("Heads or tails: ")).upper()
    while coin_flip != "HEADS" and coin_flip != "TAILS":
        coin_flip = input(print("Invalid choice. type Heads or tails: ")).upper()
    coin_flip_result = r.randint(1,2)
    if (coin_flip_result == 1 and coin_flip == "HEADS") or (coin_flip_result == 2 and coin_flip == "TAILS"):
        print("""Player goes first.\n""")
        player_turn = True
    else:
        print("""Shark goes first\n""")
        player_turn = False
    time.sleep(1)
    while player_death == False and shark_death == False:
        if player_turn == True:
            print("""You spin the chamber\n""")
            time.sleep(1)
            chamber_spin = r.randint(1,6)
            if chamber_spin == bullet:
                print("""BANG!
""")
                player_death = True
                time.sleep(1)
                break
            else:
                print("""CLICK             
You live for a moment longer.
""")
                player_turn = False
        elif player_turn == False:
            print("""Shark spins the chamber\n""")
            time.sleep(1)
            chamber_spin = r.randint(1,6)
            if chamber_spin == bullet:
                print("""BANG!
""")
                time.sleep(1)
                shark_death = True
                break
            else:
                print("""CLICK             
Shark stares you in the eyes.
""")
                player_turn = True
    return player_death

#Event list
# event_list = ["Sausage",
#                 "9/11",
#                 "Mother",
#                 "organ seller",
#                 "Loanshark",
#                 "Celebrity",
#                 "Burning hand",
#                 "Poolparty",
#                 "PDiddy"]

# Random event function, picks one event to be played out from the above list and then removes it from the list
# Easy to add more events, To add more events add the name to the list above and make elif statement at the bottom of the script
# elif "name_of_event" == event_check:
def random_event():
    event_money = 0
    event_cp = 0
    player_death = False
    roulette_played = False
    pdiddy_ending = False
    kidney = 2
    shark = 1
    if len(event_list) == 0:
        return event_money, event_cp, kidney, player_death, roulette_played
    event_check = r.randint(0,len(event_list)-1)

    # Sausage event, just lore
    if "Sausage" == event_check :
        print("""You found a person digging through the trash for a sausage.
Strange people these days.
""")    
        event_list.remove("Sausage")
    # 9/11 event, needs content or to be changed to something else
    elif "9/11" == event_check:
        print("""You are chilling at the airport watching news as you wait for your next flight.
You see on the news that an airport you were earlier got hit with a terrorist attack.
The Shark is slowed down by this.
""")
        shark += 2
        event_list.remove("9/11")
    # Mother event, Mother calls and gives money
    elif "Mother" == event_check:
        print("""Your mother is calling you, do you wish to pick up?\n""")
        call_answer = input(print("Yes/No: ")).upper()
        while call_answer != "YES" and call_answer != "NO":
            call_answer = input(print("Invalid choice, type Yes/No: ")).upper()

        if call_answer == "YES":
            mother_money = r.randint(300,700)
            print(f"""You picked up the phone.
You hear your mothers voice.
"Hello my child, i hear you are in a bit of a tight spot."
"I will send you some money"
You got {mother_money}€ from your mother.
""")
            event_money = mother_money
        else: 
            print("You chose to not pick up.")
        event_list.remove("Mother")

    # Organ seller event, You can sell your kidney
    elif "organ seller" == event_check:
        print(f"""You meet an black market organ seller.
He offers to buy your kidney
Do you accept?
""")
        kidney_sold = input(print("Yes/No: ")).upper()
        while kidney_sold != "YES" and kidney_sold != "NO":
            kidney_sold = input(print("Invalid choice, type Yes/No: ")).upper()

        if kidney_sold == "YES":
            kidney_money = r.randint(1500,3500)
            kidney = 1
            print(f"You sold your kidney for {kidney_money}€")
            event_money = kidney_money
        else:
            print("You refused the organ sellers offer.")

        event_list.remove("organ seller")
    
    # Russian roulette, The Shark calls you and offers to play a game. Ends game if russian roulette is played
    elif "Loanshark" == event_check:
        print("The loanshark is calling you, do you wish to pick up?\n")
        call_answer = input(print("Yes/No: ")).upper()

        while call_answer != "YES" and call_answer != "NO":
            call_answer = input(print("Invalid choice, type Yes/No: ")).upper()
        if call_answer == "YES":
            print("""You chose to answer the phone.
He gives you a choice.
1. Play russain roulette with him to settle your debt.
2. Continue the chase.
""")
            choice = input(print("What is your choice: "))
            choice = int_check(choice)
            while choice not in range(1,3):
                choice = input(print("What is your choice: "))
                choice = int_check(choice)
            if choice == 1:
                print("You chose to play russian roulette.")
                player_death = russian_roulette()
                roulette_played = True
            elif choice == 2:
                print("You declined his offer. The chase continues.")
        else:
            print("You chose to not pick up.")
            
        event_list.remove("Loanshark")
    
    # Celebrity event, he throws money around and you pick up some
    elif "Celebrity" == event_check:
        celeb_money = r.randint(100, 1000)
        print(f"""You see a vaguely familiar looking celebrity.
All of a sudden he starts throwing cash around.
People rush in to gather as much as they can.
You manage to pick up {celeb_money}€.
""")
        event_money += celeb_money
        event_list.remove("Celebrity")
    elif "Burning hand" == event_check:
        burning_money = r.randint(200,700)
        print(f"""You burn your hand in an accident.
The medical bills cost {burning_money}€.
Tough luck.""")
        event_money -= burning_money
        event_list.remove("Burning hand")
    
    # Pool party event, loses money
    elif "Poolparty" == event_check:
        pool_money = r.randint(123,567)
        print(f"""You are in a good mood.
You decide to throw a pool party at the airports lounge.
It cost you {pool_money}€. """)
        event_money -= pool_money

    # P.Diddy offers you help
    elif "PDiddy" == event_check:
        print("""You meet P.Diddy at the airport.
He sees that you are troubled and offers to help you.
""")
        pdiddy_choice = input(print("Do you accept? (Yes/No): ")).upper()
        while pdiddy_choice != "YES" and pdiddy_choice != "NO":
            pdiddy_choice = input(print("Do you accept? (Yes/No): ")).upper()
        
        if pdiddy_choice == "YES":
            print("""You accepted P.Diddys offer and you join him for his party.
""")
            pdiddy_ending = True
        else:
            print("You declined his offer.")
        
        event_list.remove("PDiddy")
    # Insert new event above
    # end of random events
    else:
        event_check = r.randint(0,len(event_list)-1)
    time.sleep(2)
    return event_money, event_cp, kidney, player_death, roulette_played, pdiddy_ending, shark

