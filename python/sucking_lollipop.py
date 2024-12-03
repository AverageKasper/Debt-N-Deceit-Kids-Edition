from utilities import anim_print, clear_window
import time
import random
from player_class import player

# Turn based combat function
def start_fighting(salvia_mode=False):
    player_lost=False
    fighter = {
        "name": "Player",
        "health": 100,
        "attacks": {
            "Lollipop eye poke": (10, 20),
            "Lollipop throw": (15, 25),
            "Nut cracker": (20, 35)
        }
    }

    enemy = {
        "name": "Enemy",
        "health": 100,
        "attacks": {
            "Pop Bite": (8, 18),
            "Claw": (12, 25),
            "Crotch grab": (18, 30)
        }
    }

    if salvia_mode:
        anim_print("You're in a violent, sugar-induced state!\n")
        fighter["attacks"] = {
            "Moomin punch": (15, 30),
            "Chupa kick": (20, 40),
            "Sugar rage": (25, 50)
        }
        enemy["name"] = "Lollipop hater"
        enemy["health"] = 80

    # Attack function
    def attack(attacker, defender, attack_type):
        damage = random.randint(*attacker["attacks"][attack_type])
        defender["health"] -= damage
        if defender["health"] < 0:
            defender["health"] = 0  # Prevent negative health values
        print(f"{attacker['name']} uses {attack_type} and deals {damage} damage!")
        print(f"{defender['name']} has {defender['health']} health left.\n")
        time.sleep(1)

    # Players turn function
    def player_turn():
        print("It's your turn! Choose your attack:")
        for attack in fighter["attacks"]:
            print(f"- {attack}")
        choice = input("Enter your attack: ").capitalize()
        while choice not in fighter["attacks"]:
            print("Invalid choice. Please select a valid attack.")
            choice = input("Enter your attack: ").capitalize()
        return choice

    # Enemy's turn function (random attack)
    def enemy_turn():
        choice = random.choice(list(enemy["attacks"].keys()))
        return choice

    # Randomly decide who starts
    turn = random.choice(["player", "enemy"])  # Randomly choose who goes first
    print(f"The fight begins! {turn.capitalize()} throws the first punch!\n")

    # Main fight loop
    while fighter["health"] > 0 and enemy["health"] > 0:

        if turn == "player":
            # Player's turn
            player_attack = player_turn()
            attack(fighter, enemy, player_attack)

            # Check if enemy is dead after attack
            if enemy["health"] <= 0:
                if salvia_mode:
                    anim_print("You force a lollipop hater to suck your lollipop!\n")
                else:
                    anim_print("Enemy has been converted to lollipopism!\n")
                break  # Break the loop to stop the fight immediately if enemy is dead

            turn = "enemy"  # Switch to enemy's turn

        else:
            # Enemy's turn
            print("Enemy's turn...\n")
            enemy_attack = enemy_turn()
            attack(enemy, fighter, enemy_attack)

            # Check if player is dead after attack
            if fighter["health"] <= 0:
                anim_print("You have been forced to stop sucking!\n")
                player_lost = True
                return player_lost

            turn = "player"

    print("The fight is over!")

#Ring pop
def ring_pop():
    anim_print("You chose Ringpop, a classic choice\n")
    anim_print("While sucking you start talking to a Japanese businessman\n")
    random_bucks = random.randint(1, 1500)
    businessman = input(anim_print(f"The businessman offers you {random_bucks}€. Do you accept: \n")).upper()
    if businessman == "YES":
        player.update_balance(random_bucks)
        anim_print(f"You got {random_bucks}€")
        clear_window()
    elif businessman == "NO":
        anim_print(f"You didn't get money, stupid ah decision.")
    clear_window()

#Moomin pop
def suck_moomin():
    anim_print("You chose the Moomin lollipop\n")
    anim_print("You start sucking indoors and people around you start getting agitated\n")
    angry_person = input(anim_print(
        "An angry person asks you to stop and threatens to attack you, do you stop sucking (Yes or No): \n")).upper()
    if angry_person == "NO":
        clear_window()
        player_lost = start_fighting()
        if player_lost == True:
            player.death("Lost due to losing a fight over sucking a lollipop")
            clear_window()
        clear_window()
    if angry_person == "YES":
        anim_print("You stop sucking and the situation cools down\n")
        clear_window()

#Jolly rancher
def suck_jolly():
        anim_print("You chose Jolly Rancher, broke choice\n")
        anim_print("Due to your low money choice a group of guys come up to you and mock you for choosing Jolly Rancher.\n")
        anim_print("They feel so bad for you that they give you money.\n")
        random_money=random.randint(100, 300)
        anim_print(f"You got {random_money}€")
        player.update_balance(random_money)
        clear_window()

#John Player function
def suck_john():
    anim_print("You chose the John Player Special, spicy choice\n")
    anim_print("You start enjoying your pack of lollipops\n")

    # Loop to handle the "YES or NO" question for the stranger
    while True:
        bum = input(anim_print(
            "A random stranger appears and is desperate for a lollipop, do you give her one or not? (Yes or No): \n")).upper()

        if bum == "YES":
            anim_print("She is extremely thankful and offers you a special lollipop service in a back alley\n")

            # Loop to handle the "YES or NO" question for the handjob
            while True:
                handjob = input("Do you accept: \n").upper()

                if handjob == "YES":
                    anim_print("You accepted and received a rough treatment in a back alley\n")
                    anim_print("While you're getting treated, a mysterious guy comes up behind you and stabs you\n")
                    player.death("Lost while sucking in a back alley")
                    clear_window()
                    return  # End function after death

                elif handjob == "NO":
                    anim_print("You denied the stranger's offer and continued sucking\n")
                    anim_print("You're done sucking and get ready for your next flight\n")
                    clear_window()
                    return  # End function after denial

                else:
                    anim_print("Invalid choice. Please enter 'Yes' or 'No'.\n")

        elif bum == "NO":
            anim_print("You denied to give a lollipop to the stranger\n")
            anim_print("You're done sucking and get ready for your next flight\n")
            clear_window()
            return  # End function after refusal

        else:
            anim_print("Invalid choice. Please enter 'Yes' or 'No'.\n")


#Salvia Function
def suck_salvia():
    anim_print("You chose the Salvia pop.\n")
    anim_print("You experience a whole other lifetime in your lollipop trip\n")
    anim_print("You wake up and feel extremely sugar rushed and confused \n")
    anim_print("You attack a random bystander while still sucking \n")
    player_lost = start_fighting(salvia_mode=True)
    if player_lost:
        player.death("Lost while being sugar high")
        return
    clear_window()

#Chupachups function
def suck_chupa():
    anim_print("You chose ChupaChups, strong choice\n")
    anim_print("You start sucking \n")
    anim_print("It's some strong ass stuff\n")
    anim_print("You start coughing and feeling terrible\n")
    anim_print("While you're out of it and suffering someone steals your wallet\n")
    black_money = random.randint(500, 1000)
    anim_print(f"You lost {black_money}€")
    player.update_balance(black_money)
    clear_window()



#List of lollipops
lollipop_brands = [
        "RINGPOP", "MOOMIN", "JOLLY RANCHER", "JOHN PLAYER SPECIAL",
        "SALVIA POP", "CHUPACHUPS"]


#Main Function
def lollipop_action():
    player_lost=False

# Prints the cigarette list and asks which one you want to choose
    print(lollipop_brands)
    cig=input(anim_print("You are at 7eleven, choose your delicacy: \n")).upper()
    clear_window()
    while cig not in lollipop_brands:
        print(lollipop_brands)
        cig=input(anim_print("Invalid choice. Please choose your delicacy:")).upper()

    if cig==lollipop_brands[0]:
        ring_pop()
    elif cig==lollipop_brands[1]:
        suck_moomin()
    elif cig==lollipop_brands[2]:
        suck_jolly()
    elif cig==lollipop_brands[3]:
        suck_john()
    elif cig==lollipop_brands[4]:
        suck_salvia()
    elif cig==lollipop_brands[5]:
        suck_chupa()


