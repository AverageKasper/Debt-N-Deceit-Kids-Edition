import random as r
import time
from utilities import anim_print, loading, clear_window, int_check
from python.player_class import player


def horse_race(player):
    horses = ["Diddy", "Kolovastaava", "Sakke", "Rinne", "Uusitalo"]
    odds = {horse: r.uniform(1.5, 5.0) for horse in horses}

    anim_print("Welcome to the Horse Racing track!\n")
    anim_print("Here are the competing horses and their odds:\n")
    for horse in horses:
        anim_print(f"{horse} (Odds: {odds[horse]:.2f})\n")

    while True:
        bet_horse = input(anim_print(f"Which horse do you want to bet on? ({', '.join(horses)}): ")).capitalize()
        if bet_horse not in horses:
            anim_print("Invalid horse. Please choose from the list.\n")
            continue
        break

    anim_print(f"Your total balance is {player.balance} euros\n")
    bet = input(anim_print("How much do you want to bet: "))
    bet = int_check(bet)
    while bet > player.balance:
        bet = input(anim_print("Broke ass, bet less: "))
        bet = int_check(bet)

    anim_print(f"You placed {bet} euros on {bet_horse}.\n")
    horse_speeds = {horse: r.randint(10, 20) for horse in horses}
    race_results = sorted(horse_speeds.items(), key=lambda x: x[1], reverse=True)

    anim_print("The race is starting!\n")
    time.sleep(2)
    for horse, speed in race_results:
        anim_print(f"{horse} finishes with a speed of {speed} km/h!\n")
        time.sleep(1)

    winner = race_results[0][0]
    anim_print(f"\nThe winner is {winner}!\n")

    if bet_horse == winner:
        winnings = bet * odds[bet_horse]
        anim_print(f"Congratulations! You won {winnings:.0f} euros!\n")
        player.update_balance(winnings)
    else:
        anim_print(f"You lost {bet} euros bozo.\n")
        player.update_balance(-bet)

    anim_print(f"Your total balance is now {player.balance:.0f} euros.\n")


def blackjack(player):
    def deal_card():
        cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
        return r.choice(cards)

    def calculate_hand(hand):
        card_values = {
            '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
            'J': 10, 'Q': 10, 'K': 10, 'A': 11
        }
        value, ace_count = 0, 0
        for card in hand:
            value += card_values[card]
            if card == 'A':
                ace_count += 1
        while value > 21 and ace_count:
            value -= 10
            ace_count -= 1
        return value

    def display_hand(player_name, hand, hide_dealer=False):
        if hide_dealer:
            anim_print(f"{player_name}'s hand: {hand[0]}, Hidden\n")
        else:
            anim_print(f"{player_name}'s hand: {', '.join(hand)} (Value: {calculate_hand(hand)})\n")

    anim_print("Welcome to Blackjack!")
    anim_print(f"Your total balance is {player.balance} euros\n")
    bet = input(anim_print("How much do you want to bet: "))
    bet = int_check(bet)
    while bet > player.balance:
        bet = input(anim_print("Broke ass, bet less: "))
        bet = int_check(bet)

    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]

    display_hand("Dealer", dealer_hand, hide_dealer=True)
    display_hand("Player", player_hand)

    while calculate_hand(player_hand) < 21:
        choice = input("Do you want to 'hit' or 'stand'? ").lower()
        if choice == 'hit':
            player_hand.append(deal_card())
            display_hand("Player", player_hand)
            if calculate_hand(player_hand) > 21:
                anim_print("Player busted! You lose!\n")
                player.update_balance(-bet)
                return
        elif choice == 'stand':
            break

    display_hand("Dealer", dealer_hand)
    while calculate_hand(dealer_hand) < 17:
        dealer_hand.append(deal_card())
        display_hand("Dealer", dealer_hand)

    player_value = calculate_hand(player_hand)
    dealer_value = calculate_hand(dealer_hand)

    if dealer_value > 21 or player_value > dealer_value:
        anim_print(f"Player wins! You won {bet} euros!\n")
        player.update_balance(bet)
    elif dealer_value > player_value:
        anim_print(f"Dealer wins! You lost {bet} euros!\n")
        player.update_balance(-bet)
    else:
        anim_print("It's a tie!\n")

    anim_print(f"Your total balance is {player.balance} euros\n")


def snake_eyes():
    anim_print(f"Your total balance is {player.balance} euros\n")
    bet = input(anim_print("How much do you want to bet: "))
    bet = int_check(bet)
    while bet > player.balance:
        bet = input(anim_print("\nBroke ass, bet less: "))
        bet = int_check(bet)
    dice_1, dice_2 = r.randint(1, 6), r.randint(1, 6)
    anim_print(f"You rolled: {dice_1} and {dice_2}\n")
    if dice_1 == dice_2 == 1:
        anim_print(f"BIG WIN BOZO! You won {bet * 10} euros!\n")
        player.update_balance(+bet*10)
    elif dice_1 == dice_2:
        anim_print(f"Small win bozo! You won {bet} euros!\n")
        player.update_balance(+bet *2)
    else:
        anim_print(f"You lost {bet} euros bozo\n")
        player.update_balance(-bet)
    anim_print(f"Your total balance is {player.balance} euros\n")

def dice():
    anim_print(f"Your total balance is {player.balance} euros\n")
    bet = input(anim_print("How much do you want to bet: "))
    bet = int_check(bet)
    while bet > player.balance:
        bet = input(anim_print("Broke ass, bet less: "))
        bet = int_check(bet)
    dealer_dice1, dealer_dice2 = r.randint(1, 6), r.randint(1, 6)
    player_dice1, player_dice2 = r.randint(1, 6), r.randint(1, 6)
    dealer_total = dealer_dice1 + dealer_dice2
    player_total = player_dice1 + player_dice2
    anim_print(f"Dealer rolled: {dealer_dice1}, {dealer_dice2} (Total: {dealer_total})\n")
    anim_print(f"You rolled: {player_dice1}, {player_dice2} (Total: {player_total})\n")
    if dealer_total > player_total:
        anim_print(f"You lost {bet} euros\n")
        player.update_balance(-bet)
    elif dealer_total < player_total:
        anim_print(f"You won {bet} euros\n")
        player.update_balance(+bet*2)
    else:
        anim_print("It's a tie!\n")
    anim_print(f"Your total balance is {player.balance} euros\n")

def hilo():
    anim_print(f"Your total balance is {player.balance} euros\n")
    bet = input(anim_print("How much do you want to bet: "))
    bet = int_check(bet)
    while bet > player.balance:
        bet = input(anim_print("\nBroke ass, bet less: "))
        bet = int_check(bet)

    first_card = r.randint(1, 13)
    anim_print(f"First card: {first_card}\n")
    guess = input(anim_print("Will the next card be higher or lower (HI/LO): ")).upper()
    while guess != "HI" and guess != "LO":
        guess = input(anim_print("Invalid input, try again (HI/LO): ")).upper()
    second_card = r.randint(1, 13)
    anim_print(f"Second card: {second_card}\n")
    if (guess == 'HI' and second_card > first_card) or (guess == 'LO' and second_card < first_card):
        anim_print(f"You won {bet} euros\n")
        player.update_balance(+bet*2)
    else:
        anim_print(f"You lost {bet} euros\n")
        player.update_balance(-bet)
    anim_print(f"Your total balance is {player.balance} euros\n")


def casino(player):
    clear_window()
    game_select = ""
    gameoptions = ["SNAKE EYES", "HILO", "DICE", "BLACKJACK", "HORSE RACING", "RETURN"]

    anim_print("Welcome to the casino!")
    while game_select != gameoptions[5]:
        if player.balance <= 0:
            anim_print("\nYou don’t have any money, what are you doing at the casino?")
            loading()
            clear_window()
            break

        game_select = input(anim_print("\nChoose a game (dice, hilo, snake eyes, blackjack, horse racing) or return: ")).upper()
        if game_select not in gameoptions:
            anim_print("Invalid selection, try again.\n")
            continue

        if game_select == gameoptions[0]:
            snake_eyes()
        elif game_select ==gameoptions[1]:
            hilo()
        elif game_select== gameoptions[2]:
            dice()
        elif game_select ==gameoptions[3]:
            blackjack(player)
        elif game_select ==gameoptions[4]:
            horse_race(player)

        anim_print(f"Your balance is {player.balance} euros\n")

        continue_playing = input("Do you want to play another game? (yes to continue, no to exit): ").lower()
        if continue_playing != "yes":
            anim_print("Thanks for playing! See you next time!")
            break  #Exit the casino loop

    clear_window()


#monke69


