from utilities import anim_print
from utilities import clear_window
from utilities import int_check
from utilities import loading

def next_page():
    page_turn = input(anim_print("Type 1 to go to the next page or 2 to play the game: ",delay=0.01))
    page_turn = int_check(page_turn)
    while page_turn != 1 and page_turn != 2:
        page_turn = input(anim_print("Invalid option, try again: "))
        page_turn = int_check(page_turn)
    return page_turn

def rule_print():
    page_turn = 1
    while page_turn == 1:
        anim_print("""HOW TO PLAY
Your goal is to avoid the loanshark (aka The Shark), and gather money to pay back your debt to him.
You fly around to different airports using CP (Carbon Points) and do tasks at the airports to gain money.
Every flight puts the Shark 1 step behind and every task you do makes the Shark come 1 step closer.
""")
        page_turn = next_page()
        clear_window()
        if page_turn == 2:
            break
        anim_print("""DIFFICULTIES
On easy difficulty you are 10000€ in debt, start out with 2500€ and 10000CP. The Shark starts 7 steps behind.
On normal difficulty you are 10000€ in debt, start out with 1000€ and 7000CP. The Shark starts 4 steps behind.
On hard difficulty you are 20000€ in debt, start out with 0€ and 4000CP. The Shark starts 2 steps behind.
Choosing a difficulty doesnt affect the game otherwise.
""")
        page_turn = next_page()
        clear_window()
        if page_turn == 2:
            break
        anim_print("""MOVING AND GAMEPLAY PART 1
When you move you will choose between 3 different airports.

TYPE 1: Cheapest option to fly to, costing 100CP.
Tasks to do at Type 1 airports are: Dumpster diving, Pickpocketing.

TYPE 2: Medium airports, costing 200CP.
Tasks to do at Type 2 airports are: Trivia.

TYPE 3: Largest airports, costing 500CP.
Tasks to do at Type 3 airports are: Gambling, Smoking.
""")
        page_turn = next_page()
        clear_window()
        if page_turn == 2:
            break
        anim_print("""MOVING AND GAMEPLAY PART 2
You can do 2 task at an airport before you need to move to the next one.
Be careful, if the shark is 1 airport behind. doing a task at this point will make him catch up and might end the game.
""")
        page_turn = next_page()
        clear_window()
        if page_turn == 2:
            break
        anim_print("""TASKS
Dumpster diving: Take a look in the trash. You can find money, CP or even a strange object.
Pickpocketing: Steal from someone at the airport, people have different difficulties and rewards according to the challenge.
Trivia: Answer some interesting trivia questions and win money with correct answers.
Gambling: Go to the local casino and play various different games like blackjack or HI/LO.
Smoke break: Enjoy a small break and meet all kinds of people.
""")
    
    

    anim_print("Have fun playing the game\n")
    loading()
