import time
import random as r
from utilities import int_check
from utilities import anim_print
from utilities import clear_window

# Russian roulette function
def russian_roulette():
    bullet = 1
    player_death = False
    shark_death = False
    player_turn = False
    anim_print("\nBonk\n")
    time.sleep(2)
    anim_print(f"""You wake up in a dark cellar with 2 chairs and a table.          
You see a 6 chamber revolver on the table.
The loanshark is across the table from you.         
A rough voice speaks at you.            
"Its time to start the game now"            
"There is 1 bullet loaded into the revolver in front of you"            
"You will take turns firing the gun at your head"           
"Whoever survives gets to walk away"            
"Lets flip a coin for who goes first"           
""")
    coin_flip = input(anim_print("Heads or tails: ")).upper()
    while coin_flip != "HEADS" and coin_flip != "TAILS":
        coin_flip = input(anim_print("Invalid choice. type Heads or tails: ")).upper()
    coin_flip_result = r.randint(1,2)
    if (coin_flip_result == 1 and coin_flip == "HEADS") or (coin_flip_result == 2 and coin_flip == "TAILS"):
        anim_print("""Player goes first.\n""")
        player_turn = True
    else:
        anim_print("""Shark goes first\n""")
        player_turn = False
    time.sleep(1)
    while player_death == False and shark_death == False:
        if player_turn == True:
            anim_print("""You spin the chamber\n""")
            time.sleep(1)
            chamber_spin = r.randint(1,6)
            if chamber_spin == bullet:
                anim_print("""BANG!
""")
                player_death = True
                time.sleep(1)
                break
            else:
                anim_print("""CLICK             
You live for a moment longer.
""")
                player_turn = False
        elif player_turn == False:
            anim_print("""Shark spins the chamber\n""")
            time.sleep(1)
            chamber_spin = r.randint(1,6)
            if chamber_spin == bullet:
                anim_print("""BANG!
""")
                time.sleep(1)
                shark_death = True
                break
            else:
                anim_print("""CLICK             
Shark stares you in the eyes.
""")
                player_turn = True
    return player_death

#Event list
event_list = ["Sausage",
                "9/11",
                "Mother",
                "organ seller",
                "Loanshark",
                "Celebrity",
                "Burning hand",
                "Poolparty",
                "PDiddy"]

# Random event function, picks one event to be played out from the above list and then removes it from the list
# Easy to add more events, To add more events add the name to the list above and make elif statement at the bottom of the script
# elif "name_of_event" == event_list[event_check]:
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
    if "Sausage" == event_list[event_check] :
        anim_print("""You found a person digging through the trash for a sausage.
Strange people these days.
""")    
        event_list.remove("Sausage")
    # 9/11 event, needs content or to be changed to something else
    elif "9/11" == event_list[event_check]:
        anim_print("""You are chilling at the airport watching news as you wait for your next flight.
You see on the news that an airport you were earlier got hit with a terrorist attack.
The Shark is slowed down by this.
""")
        shark += 2
        event_list.remove("9/11")
    # Mother event, Mother calls and gives money
    elif "Mother" == event_list[event_check]:
        anim_print("""Your mother is calling you, do you wish to pick up?\n""")
        call_answer = input(anim_print("Yes/No: ")).upper()
        while call_answer != "YES" and call_answer != "NO":
            call_answer = input(anim_print("Invalid choice, type Yes/No: ")).upper()

        if call_answer == "YES":
            mother_money = r.randint(300,700)
            anim_print(f"""You picked up the phone.
You hear your mothers voice.
"Hello my child, i hear you are in a bit of a tight spot."
"I will send you some money"
You got {mother_money}€ from your mother.
""")
            event_money = mother_money
        else: 
            anim_print("You chose to not pick up.")
        event_list.remove("Mother")

    # Organ seller event, You can sell your kidney
    elif "organ seller" == event_list[event_check]:
        anim_print(f"""You meet an black market organ seller.
He offers to buy your kidney
Do you accept?
""")
        kidney_sold = input(anim_print("Yes/No: ")).upper()
        while kidney_sold != "YES" and kidney_sold != "NO":
            kidney_sold = input(anim_print("Invalid choice, type Yes/No: ")).upper()

        if kidney_sold == "YES":
            kidney_money = r.randint(1500,3500)
            kidney = 1
            anim_print(f"You sold your kidney for {kidney_money}€")
            event_money = kidney_money
        else:
            anim_print("You refused the organ sellers offer.")

        event_list.remove("organ seller")
    
    # Russian roulette, The Shark calls you and offers to play a game. Ends game if russian roulette is played
    elif "Loanshark" == event_list[event_check]:
        anim_print("The loanshark is calling you, do you wish to pick up?\n")
        call_answer = input(anim_print("Yes/No: ")).upper()

        while call_answer != "YES" and call_answer != "NO":
            call_answer = input(anim_print("Invalid choice, type Yes/No: ")).upper()
        if call_answer == "YES":
            anim_print("""You chose to answer the phone.
He gives you a choice.
1. Play russain roulette with him to settle your debt.
2. Continue the chase.
""")
            choice = input(anim_print("What is your choice: "))
            choice = int_check(choice)
            while choice not in range(1,3):
                choice = input(anim_print("What is your choice: "))
                choice = int_check(choice)
            if choice == 1:
                anim_print("You chose to play russian roulette.")
                player_death = russian_roulette()
                roulette_played = True
            elif choice == 2:
                anim_print("You declined his offer. The chase continues.")
        else:
            anim_print("You chose to not pick up.")
            
        event_list.remove("Loanshark")
    
    # Celebrity event, he throws money around and you pick up some
    elif "Celebrity" == event_list[event_check]:
        celeb_money = r.randint(100, 1000)
        anim_print(f"""You see a vaguely familiar looking celebrity.
All of a sudden he starts throwing cash around.
People rush in to gather as much as they can.
You manage to pick up {celeb_money}€.
""")
        event_money += celeb_money
        event_list.remove("Celebrity")
    elif "Burning hand" == event_list[event_check]:
        burning_money = r.randint(200,700)
        anim_print(f"""You burn your hand in an accident.
The medical bills cost {burning_money}€.
Tough luck.""")
        event_money -= burning_money
        event_list.remove("Burning hand")
    
    # Pool party event, loses money
    elif "Poolparty" == event_list[event_check]:
        pool_money = r.randint(123,567)
        anim_print(f"""You are in a good mood.
You decide to throw a pool party at the airports lounge.
It cost you {pool_money}€. """)
        event_money -= pool_money

    # P.Diddy offers you help
    elif "PDiddy" == event_list[event_check]:
        anim_print("""You meet P.Diddy at the airport.
He sees that you are troubled and offers to help you.
""")
        pdiddy_choice = input(anim_print("Do you accept? (Yes/No): ")).upper()
        while pdiddy_choice != "YES" and pdiddy_choice != "NO":
            pdiddy_choice = input(anim_print("Do you accept? (Yes/No): ")).upper()
        
        if pdiddy_choice == "YES":
            anim_print("""You accepted P.Diddys offer and you join him for his party.
""")
            pdiddy_ending = True
        else:
            anim_print("You declined his offer.")
        
        event_list.remove("PDiddy")
    # Insert new event above
    # end of random events
    else:
        event_check = r.randint(0,len(event_list)-1)
    time.sleep(2)
    return event_money, event_cp, kidney, player_death, roulette_played, pdiddy_ending, shark

