import random as r
from flask import Flask, Response
from flask_cors import CORS
import json
app = Flask(__name__)
CORS(app)
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



@app.route('/pickpocket/<name>/<difficulty>')
def calculate_pickpocket(name, difficulty):
    result = ""
    difficulties= {"★": 10,
                   "★★": 30,
                   "★★★": 50,
                   "★★★★": 70,
                   "★★★★★": 90}
    for key, value in difficulties.items():
        if difficulty == key:
            r.randint(1, 100)
            chance = value
            if chance >= r.randint(1, 100):
                result = f"Success! You successfully pickpocketed {name} and earned {r.randint(10,50) * chance}€."
            else:
                result = f"Failure! You got caught trying to pickpocket {name}. You got fined for {300}€."
    response = make_response(result, 200)
    return result

    # List





def pickpocket():
    penalty = 300
    money_sum = 0
    dif1 = "★"
    dif2 = "★★"
    dif3 = "★★★"
    dif4 = "★★★★"
    dif5 = "★★★★★"

    # List of possible targets and difficulty
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
    # Randomizes thieving targets
    name1 ,difficulty1 = r.choice(list(steal_list.items()))
    del steal_list[name1]
    name2 ,difficulty2 = r.choice(list(steal_list.items()))
    del steal_list[name2]
    name3 ,difficulty3 = r.choice(list(steal_list.items()))
    del steal_list[name3]
    anim_print(f"""You have chosen a life of crime, Choose your victim today:
1. {name1}, difficulty {difficulty1}.
2. {name2}, difficulty {difficulty2}.
3. {name3}, difficulty {difficulty3}.
""")
    victim = input(anim_print("Choose: "))
    victim = int_check(victim,3) 


   # Assign variables based on victim choice
    if victim == 1:
        chosen_name, chosen_difficulty = name1, difficulty1
    elif victim == 2:
        chosen_name, chosen_difficulty = name2, difficulty2
    elif victim == 3:
        chosen_name, chosen_difficulty = name3, difficulty3

    # Assign percentage chance and reward based on difficulty
    difficulty_mapping = {
        "★": (90, r.randint(10,200)),   # 90% chance, 10-200€ reward
        "★★": (70, r.randint(200,400)),  # 70% chance, 200-400€ reward
        "★★★": (50, r.randint(400,600)),  # 50% chance, 400-600€ reward
        "★★★★": (30, r.randint(600,800)),  # 30% chance, 600-800€ reward
        "★★★★★": (10, r.randint(1000,2000))  # 10% chance, 1000-2000€ reward
    }
    
    success_chance, reward = difficulty_mapping[chosen_difficulty]
    
    anim_print(f"You attempt to pickpocket {chosen_name}, difficulty {chosen_difficulty}.")
    
    # Random success check
    roll = r.randint(1, 100)
    
    # if roll <= success_chance:
    #     anim_print(f"\nSuccess! You successfully pickpocketed {chosen_name} and earned {reward}€.")
    #     money_sum += reward
    # else:
    #     anim_print(f"\nFailure! You got caught trying to pickpocket {chosen_name}. You got fined for {penalty}€.")
    #     money_sum -= penalty

    return money_sum

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=4000)