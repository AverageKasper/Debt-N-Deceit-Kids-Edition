import random as r
from flask import Flask, Response
from flask_cors import CORS
import json
from player_class import player
app = Flask(__name__)
CORS(app)

# Handles the pickpocketing options
@app.route('/pickpocket')
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
    jsonvast = json.dumps(result)
    return Response(response=jsonvast, status=status_code, mimetype="application/json")


# Handles the pickpocketing choice and chance
@app.route('/pickpocket/<name>/<difficulty>')
def calculate_pickpocket(name, difficulty):
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
                # Uncomment the line below when player is done
                #player.update_balance(win_money)
                
            else:
                lose_money = r.randint(1,5) * difficulties[difficulty]
                result = {"message": f"Failure! You got caught trying to pickpocket {name}. You got fined for {lose_money}€.",
                          "money": lose_money}
                # Uncomment the line below when player is done
                #player.update_balance(-lose_money)
    response = json.dumps(result)
    return Response(response=response, status=200, mimetype="application/json")


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=4000)