from utilities import anim_print, clear_window
import time
import random

# Prints a nice box around the cigarette_brands
def print_boxed_list(items):

    max_len = max(len(str(item)) for item in items)
    box_width = max_len + 4


    print('+' + '-' * (box_width) + '+')


    for item in items:
        print(f'| {str(item).center(max_len)} |')


    print('+' + '-' * (box_width) + '+')

# Turn based combat function
def start_fighting(salvia_mode=False):
    player_death=False
    player = {
        "name": "Player",
        "health": 100,
        "attacks": {
            "Punch": (10, 20),
            "Kick": (15, 25),
            "Nut cracker": (20, 35)
        }
    }

    enemy = {
        "name": "Enemy",
        "health": 100,
        "attacks": {
            "Bite": (8, 18),
            "Claw": (12, 25),
            "Crotch grab": (18, 30)
        }
    }

    if salvia_mode:
        anim_print("You're in a violent, drug-induced state!\n")
        player["attacks"] = {
            "Frenzied punch": (15, 30),
            "Hallucination kick": (20, 40),
            "Salvia rage": (25, 50)
        }
        enemy["name"] = "Bystander"
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
        for attack in player["attacks"]:
            print(f"- {attack}")
        choice = input("Enter your attack: ").capitalize()
        while choice not in player["attacks"]:
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

    # Main game loop
    while player["health"] > 0 and enemy["health"] > 0:

        if turn == "player":
            # Player's turn
            player_attack = player_turn()
            attack(player, enemy, player_attack)

            # Check if enemy is dead after attack
            if enemy["health"] <= 0:
                if salvia_mode:
                    anim_print("You murdered an innocent bystander in cold blood!\n")
                else:
                    anim_print("Enemy has been killed!\n")
                break  # Break the loop to stop the fight immediately if enemy is dead

            turn = "enemy"  # Switch to enemy's turn

        else:
            # Enemy's turn
            print("Enemy's turn...\n")
            time.sleep(1)
            enemy_attack = enemy_turn()
            attack(enemy, player, enemy_attack)

            # Check if player is dead after attack
            if player["health"] <= 0:
                anim_print("You have been killed!\n")
                player_death = True
                return player_death

            turn = "player"

    print("The fight is over!")

# Cigarette list
cigarette_brands = [
        "MARLBORO RED", "MARLBORO GOLD", "WEST BLUE", "JOHN PLAYER SPECIAL",
        "SALVIA JOINT", "AMERICAN BLACK"]

# Main function for the smoking break
def smoking_action():
    money = 0
    player_death=False
    stabbed = False
    fighting_death=False
    salvia_death=False

# Prints the cigarette list and asks which one you want to choose
    print_boxed_list(cigarette_brands)
    cig=input(anim_print("You are at 7eleven, choose your delicacy: \n")).upper()
    clear_window()
    while cig not in cigarette_brands:
        print_boxed_list(cigarette_brands)
        cig=input(anim_print("Invalid choice. Please choose your delicacy:")).upper()



# John Player Special
    if cig==cigarette_brands[3]:
        anim_print("You chose the John Player Special, spicy choice\n")
        time.sleep(1)
        anim_print("You start enjoying your pack of cigarettes\n")
        time.sleep(1)
        bum=input(anim_print("A random strangers appears and is desperate for a cigarette, do you give her one or not? (Yes or No): \n")).upper()
        if bum=="YES":
            anim_print("She is extremely thankful and offers you a special service in a back alley\n")
            handjob=input("Do you accept: \n").upper()
            if handjob=="YES":
                anim_print("You accepted and received a rough treatment in a back alley\n")
                time.sleep(2)
                anim_print("While you're getting treated, a mysterious guy comes up behind you and stabs you\n")
                player_death = True
                stabbed = True
                time.sleep(3)
                clear_window()


            elif handjob=="NO":
                anim_print("You denied the strangers offer and continued smoking\n")
                time.sleep(2)
                anim_print("You're done smoking and get ready for your next flight\n")
                time.sleep(2)
                clear_window()

        elif bum=="NO":
            anim_print("You denied to give a cigarette to the stranger\n")
            time.sleep(2)
            anim_print("You're done smoking and get ready for your next flight\n")
            time.sleep(2)
            clear_window()

    # Marlboro Red
    elif cig==cigarette_brands[0]:
        anim_print("You chose Marlboro Red, a classic choice\n")
        time.sleep(1)
        anim_print("While smoking you start talking to a Japanese businessman\n")
        random_bucks=random.randint(1, 1500)
        businessman=input(anim_print(f"The businessman offers you {random_bucks}€. Do you accept: \n")).upper()
        if businessman=="YES":
            money+=random_bucks
            anim_print(f"You got {random_bucks}€")
            #Yakuza ending in ohjelmisto 2?????
            time.sleep(2)
            clear_window()
        elif businessman=="NO":
            anim_print(f"You didn't get money, stupid ah decision.")
        clear_window()


    # Marlboro Gold
    elif cig==cigarette_brands[1]:
        anim_print("You chose Marlboro Gold\n")
        time.sleep(1)
        anim_print("You start smoking indoors and people around you start getting agitated\n")
        time.sleep(1)
        angry_person=input(anim_print("An angry person asks you to stop and threatens to attack you, do you stop smoking (Yes or No): \n")).upper()
        if angry_person=="NO":
            clear_window()
            player_death=start_fighting()
            if player_death==True:
                fighting_death=True
                clear_window()
            clear_window()
        if angry_person=="YES":
            anim_print("You stop smoking and the situation cools down\n")
            time.sleep(3)
            clear_window()
            
    # West Blue
    elif cig==cigarette_brands[2]:
        anim_print("You chose West Blue, broke choice\n")
        time.sleep(1)
        anim_print("Due to your low money choice a group of guys come up to you and mock you for choosing West Blue.\n")
        time.sleep(1)
        anim_print("They feel so bad for you that they give you money.\n")
        random_money=random.randint(100, 300)
        time.sleep(0.5)
        anim_print(f"You got {random_money}€")
        time.sleep(3)
        money+=random_money
        clear_window()


    # Salvia Joint
    elif cig==cigarette_brands[4]:
        anim_print("You chose the Salvia Joint.\n")
        time.sleep(1)
        anim_print("You experience a whole other lifetime in your drug trip\n")
        time.sleep(1)
        anim_print("You wake up and feel extremely violent and confused \n")
        time.sleep(1)
        anim_print("You attack a random bystander while still being under the influence \n")
        time.sleep(1)
        player_death=start_fighting(salvia_mode=True)
        if player_death==True:
            salvia_death=True
        time.sleep(2)
        clear_window()


    # American Black
    elif cig==cigarette_brands[5]:
        anim_print("You chose American Black, strong choice\n")
        time.sleep(1)
        anim_print("You start smoking \n")
        time.sleep(1)
        anim_print("It's some strong ass stuff\n")
        time.sleep(1)
        anim_print("You start coughing and feeling terrible\n")
        time.sleep(1)
        anim_print("While you're out of it and suffering someone steals your wallet\n")
        time.sleep(0.5)
        black_money=random.randint(500, 1000)
        anim_print(f"You lost {black_money}€")
        money-=black_money
        time.sleep(2.5)
        clear_window()

    return money, player_death, stabbed, fighting_death, salvia_death



#Monke 6969