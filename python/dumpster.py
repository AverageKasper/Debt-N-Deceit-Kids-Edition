from utilities import anim_print
import random as r

# Function for dumpster diving at small airports, returns gained currencies
def dumpster_dive():
    money = 0
    cp = 0
    phallic_object = 0
    
    # Randomizes percentage 
    find =  r.randint(1,100)

    # Get stuff based on what the percentage
    if find < 30: ## A Little money
        trash_money = r.randint(50, 150)
        anim_print(f"\nYou found a portable dvd player from the trash, you got {trash_money}€ for it at the pawn shop!")
        money += trash_money

    elif find >= 30 and find <=40: ## A Little bit more money
        trash_money = r.randint(200, 400)
        anim_print(f"\nYou found a pair of earbuds from the trash, you got {trash_money}€ for it at the pawn shop!")
        money += trash_money

    elif find > 40 and find <= 65: ## A lot of money
        trash_money = r.randint(500, 700)
        anim_print(f"\nYou found an IPhone XS in the trash, you got {trash_money}€ for it at the pawn shop!")
        money += trash_money

    elif find > 65 and find <=85: ## You didnt find anything :(
        anim_print("\nYou dig through the trash but you dont find anything worthwile.")

    elif find > 85 and find <=95: ## Get some CP for flying
        rand_cp = r.randrange(100, 700, 100)
        anim_print(f"\nYou found a voucher for CP from the trash! You got {rand_cp}CP!")
        cp += rand_cp

    elif find>95 and find <= 100: ## Phallic object will save your ass
        anim_print(f"\nYou found 1 phallic object from the trash! It smells wierd.")
        phallic_object += 1
    return money, cp, phallic_object