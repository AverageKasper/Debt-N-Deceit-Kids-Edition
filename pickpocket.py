from utilities import anim_print
from utilities import clear_window
from utilities import int_check
import random as r

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
    clear_window()
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
    victim = int_check(victim) 
    while victim not in range(1,4):
        victim = input(anim_print("Invalid option, try again: "))
        victim = int_check(victim)

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
    
    if roll <= success_chance:
        anim_print(f"\nSuccess! You successfully pickpocketed {chosen_name} and earned {reward}€.")
        money_sum += reward
    else:
        anim_print(f"\nFailure! You got caught trying to pickpocket {chosen_name}. You got fined for {penalty}€.")
        money_sum -= penalty

    return money_sum
