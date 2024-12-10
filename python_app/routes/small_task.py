import random as r
from flask import Blueprint, jsonify



small_blueprint = Blueprint('small', __name__)

#When game is done remove the comments marked with #!#

# Handles the pickpocketing options
@small_blueprint.route('/pp/victims_list')
def pickpocket_victims():
    try:
        dif1 = "★"
        dif2 = "★★"
        dif3 = "★★★"
        dif4 = "★★★★"
        dif5 = "★★★★★"
        steal_list = {"Homeless man" : dif1,
                    "Elderly lady" : dif1,
                    "Random kid" : dif1,
                    "Frisbee golfer" : dif1,
                    "Flight attendant" : dif2,
                    "Airport drunk" : dif2,
                    "Student traveller": dif2,
                    "Tourist" : dif3,
                    "Chinese tourists" : dif3,
                    "Store clerk" : dif3,
                    "Carl Johnson" : dif4, 
                    "Airport police" : dif4,
                    "Pilot" : dif4,
                    "VIP escort" : dif4,
                    "Japanese man with an eyepatch" : dif5,
                    "Sausage man" : dif5,
                    "Juha" : dif5,
                    }
        name1 ,difficulty1 = r.choice(list(steal_list.items()))
        del steal_list[name1]
        name2 ,difficulty2 = r.choice(list(steal_list.items()))
        del steal_list[name2]
        name3 ,difficulty3 = r.choice(list(steal_list.items()))
        del steal_list[name3]
        status_code = 200
        result = [{"victim_1": {"name": name1, 
                            "difficulty": difficulty1},
                "victim_2": {"name": name2, 
                            "difficulty": difficulty2},
                "victim_3": {"name": name3,
                            "difficulty": difficulty3}}]
    except Exception as e:
        status_code = 500
        result = {"status_code": status_code,
                "error": str(e)}

    return jsonify(result)

# Handles the pickpocketing choice and chance
@small_blueprint.route('/pp/<name>/<difficulty>')
def calculate_pickpocket(name, difficulty):
    from python_app.player_class import player
    result = {}
    difficulties= {"★": 10,
                   "★★": 30,
                   "★★★": 50,
                   "★★★★": 70,
                   "★★★★★": 90}
    for key, value in difficulties.items():
        if difficulty == key:
            r.randint(1, 100)
            chance = value
            if chance <= r.randint(1, 100):
                win_money = r.randint(5,15) * difficulties[difficulty]
                result = {"message": f"Success! You successfully pickpocketed {name} and earned {win_money}€.",
                          "money": win_money}
                player.update_balance(win_money)
                
            else:
                lose_money = r.randint(1,5) * difficulties[difficulty]
                result = {"message": f"Failure! You got caught trying to pickpocket {name}. You got fined for {lose_money}€.",
                          "money": lose_money}
                player.update_balance(-lose_money)
    return jsonify(result)

# Function for dumpster diving at small airports, returns gained currencies
@small_blueprint.route('/diving')
def dumpster_dive():

    # Randomizes percentage 
    find =  r.randint(1,100)
    money = 0
    text_result = ""
    carbon = 0
    inventory = 0
    # Get stuff based on what the percentage
    if find < 30: ## A Little money
        money = r.randint(50, 150)
        text_result = f"You found a portable dvd player from the trash, you got {money}€ for it at the pawn shop!"
        
    elif find >= 30 and find <= 40: ## A Little bit more money
        money = r.randint(200, 400)
        text_result = f"You found a pair of earbuds from the trash, you got {money}€ for it at the pawn shop!"
        
    elif find > 40 and find <= 65: ## A lot of money
        money = r.randint(500, 700)
        text_result = f"You found an IPhone XS in the trash, you got {money}€ for it at the pawn shop!"
        
    elif find > 65 and find <= 85: ## You didnt find anything :(
        text_result = "You dig through the trash but you dont find anything worthwile."

    elif find > 85 and find <= 95: ## Get some CP for flying
        carbon = r.randrange(100, 700, 100)
        text_result = f"You found a voucher for CP from the trash! You got {carbon}CP!"
        
    elif find > 95 and find <= 100: ## Phallic object will save your ass
        text_result = f"\nYou found 1 phallic object from the trash! It smells wierd."
        inventory += 1
    
    # Check what reward was got and update class stats accordingly
    from python_app.player_class import player
    if money > 0:
        reward = f"{money} €"
        player.update_balance(money)
    elif carbon > 0:
        reward = f"{carbon} carbon"
        player.update_carbon(carbon)
    elif inventory > 0:
        reward = f"{inventory} items"
        player.update_inventory(inventory)
    else: 
        reward = "nothing"
    
    result = {"text": text_result,
              "reward": reward}
    
    return jsonify(result)
